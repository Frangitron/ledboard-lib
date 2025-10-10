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

    def set_options(self, options: DetectorOptions):
        self._options = options

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

        points = [self._detect() for _ in range(self._options.average_frame_count)]
        points = [point for point in points if point is not None]  # FIXME doesnt respect average frame count if None
        if points:
            x_coords, y_coords = zip(*points)
            brightest_point = (sum(x_coords) / len(x_coords), sum(y_coords) / len(y_coords))
        else:
            brightest_point = None

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
            radius = self._options.blur_radius * 2 + 1
            self._frame = cv2.GaussianBlur(self._frame, (radius, radius), 0)

    def _capture_frame(self):
        ret, self._frame = self._video_capture.read()
        if not ret:
            raise NoFrameCaptured("Failed to capture frame")

    def _find_brightest_point(self) -> tuple[int, int] | None:
        gray = cv2.cvtColor(self._frame, cv2.COLOR_BGR2GRAY)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(gray)
        return max_loc[0], max_loc[1]

    def _detect(self) -> tuple[int, int]:
        self._capture_frame()
        self._apply_blur()
        return self._find_brightest_point()
