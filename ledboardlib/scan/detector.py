import time

import cv2
import numpy as np

from ledboardlib.scan.detector_options import DetectorOptions
from ledboardlib.scan.exceptions import CameraOpenError, NoFrameCaptured
from ledboardlib.scan.frame_detection_result import FrameDetectionResult


class Detector:
    def __init__(self, options: DetectorOptions):
        self._options = options
        self._video_capture: cv2.VideoCapture | None = None
        self._frame: np.ndarray | None = None

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

        self._capture_frame()
        self._apply_blur()
        brightest_point = self._find_brightest_point()

        return FrameDetectionResult(
            frame_as_bytes=cv2.imencode('.jpg', self._frame, [cv2.IMWRITE_JPEG_QUALITY, 85])[1].tobytes(),
            frame_height=self._options.camera_height,
            frame_width=self._options.camera_width,
            point=brightest_point,
            timestamp=time.time(),
        )

    def end(self):
        print("Closing camera...")
        if self._video_capture is not None:
            self._video_capture.release()
            self._video_capture = None
            print("Camera closed successfully")

    def _apply_blur(self):
        if self._options.blur_radius > 0:
            self._frame = cv2.GaussianBlur(self._frame, (self._options.blur_radius, self._options.blur_radius), 0)

    def _capture_frame(self):
        ret, self._frame = self._video_capture.read()
        if not ret:
            raise NoFrameCaptured("Failed to capture frame")

    def _find_brightest_point(self) -> tuple[int, int] | None:
        gray = cv2.cvtColor(self._frame, cv2.COLOR_BGR2GRAY)
        bright_mask = gray >= self._options.brightness_threshold

        if not np.any(bright_mask):
            return None

        y_coords, x_coords = np.where(bright_mask)
        bright_values = gray[bright_mask]
        top_index = np.argsort(bright_values)[::-1][1]

        return int(x_coords[top_index]), int(y_coords[top_index])
