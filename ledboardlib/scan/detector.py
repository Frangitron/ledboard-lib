import time
from typing import Tuple

import cv2
import numpy as np

from ledboardlib.scan.detector_options import DetectorOptions
from ledboardlib.scan.exceptions import CameraOpenError, NoFrameCaptured
from ledboardlib.scan.frame_detection_result import FrameDetectionResult


class Detector:
    def __init__(self, options: DetectorOptions):
        self._options = options
        self._video_capture: cv2.VideoCapture | None = None

    def begin(self):
        print("Opening camera...")

        self._video_capture = cv2.VideoCapture(self._options.camera_index)
        if not self._video_capture.isOpened():
            raise CameraOpenError(f"Could not open camera {self._options.camera_index}")

        self._video_capture.set(cv2.CAP_PROP_FRAME_WIDTH, self._options.camera_width)
        self._video_capture.set(cv2.CAP_PROP_FRAME_HEIGHT, self._options.camera_height)

        print("Camera opened successfully")

    def step(self) -> FrameDetectionResult:
        if self._video_capture is None:
            raise RuntimeError("Detector not started (use begin() first)")


        # Capture frame
        ret, frame = self._video_capture.read()
        if not ret:
            raise NoFrameCaptured("Failed to capture frame")

        # Find brightest pixels
        brightest_points = self._find_brightest_points(
            frame, 1, self._options.brightness_threshold
        )

        # Prepare result data
        return FrameDetectionResult(
            timestamp=time.time(),
            frame_width=self._options.camera_width,
            frame_height=self._options.camera_height,
            frame_as_bytes=cv2.imencode('.jpg', frame, [cv2.IMWRITE_JPEG_QUALITY, 85])[1].tobytes(),
            points=brightest_points
        )

    def end(self):
        print("Closing camera...")
        if self._video_capture is not None:
            self._video_capture.release()
            self._video_capture = None
            print("Camera closed successfully")

    def _find_brightest_points(self, image: np.ndarray, num_pixels: int = 10, threshold: int = 200) -> list[Tuple[int, int]]:
        """
        Find the brightest pixels in the image.

        Args:
            image: Input image (BGR format)
            num_pixels: Number of brightest pixels to return
            threshold: Minimum brightness threshold

        Returns:
            List of (x, y) coordinates of brightest pixels
        """
        # Convert to grayscale for brightness calculation
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Find pixels above the given threshold
        bright_mask = gray >= threshold

        if not np.any(bright_mask):
            return []

        # Get coordinates of bright pixels
        y_coords, x_coords = np.where(bright_mask)
        bright_values = gray[bright_mask]

        # Sort by brightness and get top N pixels
        sorted_indices = np.argsort(bright_values)[::-1]
        top_indices = sorted_indices[:min(num_pixels, len(sorted_indices))]

        # Return as a list of (x, y) tuples
        brightest_points = [(int(x_coords[i]), int(y_coords[i])) for i in top_indices]
        return brightest_points
