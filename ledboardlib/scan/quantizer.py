import logging
import math

from scipy.signal import savgol_filter
import numpy as np

from ledboardlib.scan.detection_point import DetectionPoint


_logger = logging.getLogger(__name__)


class DetectionPointsQuantizer:
    def __init__(self, selection_as_detection_points: list[DetectionPoint]):
        self._detection_points = selection_as_detection_points
        self._output = list()
        self._pitch: float | None = None

    def quantize(self) -> list[DetectionPoint]:
        if not self._detection_points:
            _logger.warning("No detection points to quantize")
            return list()

        self._detect_pitch()
        _logger.info(f"Detected pitch: {self._pitch}")
        smoothed = self.smooth_detection_points(
            led_pitch=self._pitch
        )
        return [
            DetectionPoint(
                x=round(point.x / self._pitch),
                y=round(point.y / self._pitch),
                led_index=point.led_index
            ) for point in smoothed
        ]

    def pitch(self) -> float:
        return self._pitch

    def _detect_pitch(self):
        distances = self._compute_distances()
        distances.sort()
        self._pitch = distances[len(distances) // 2]

    def _compute_distances(self):
        distances_ = []
        for i in range(len(self._detection_points) - 1):
            a = self._detection_points[i]
            b = self._detection_points[i + 1]
            distances_.append(math.sqrt((b.x - a.x) ** 2 + (b.y - a.y) ** 2))
        return distances_

    def smooth_detection_points(self, led_pitch: float, break_threshold=3.0, window_length=5) -> list[DetectionPoint]:
        # Identify break points
        break_indices = set([0, len(self._detection_points) - 1])  # Always include endpoints
        for i in range(len(self._detection_points) - 1):
            distance = math.sqrt((self._detection_points[i + 1].x - self._detection_points[i].x) ** 2 +
                                 (self._detection_points[i + 1].y - self._detection_points[i].y) ** 2)
            if distance > led_pitch * break_threshold:
                break_indices.add(i + 1)

        # Smooth each segment separately
        segments = []
        start = 0
        for break_idx in sorted(break_indices):
            if break_idx > start:
                segments.append((start, break_idx))
            start = break_idx

        smoothed_points: list[DetectionPoint] = [None] * len(self._detection_points)

        for seg_start, seg_end in segments:
            if seg_end - seg_start < window_length:
                # Segment too short, just copy
                for i in range(seg_start, seg_end):
                    smoothed_points[i] = self._detection_points[i]
            else:
                # Apply Savitzky-Golay filter
                x_coords = np.array([p.x for p in self._detection_points[seg_start:seg_end]])
                y_coords = np.array([p.y for p in self._detection_points[seg_start:seg_end]])

                smooth_x = savgol_filter(x_coords, window_length, polyorder=3)
                smooth_y = savgol_filter(y_coords, window_length, polyorder=3)

                for i, (sx, sy) in enumerate(zip(smooth_x, smooth_y)):
                    # Update coordinates while preserving LED index
                    smoothed_points[seg_start + i] = DetectionPoint(
                        led_index=self._detection_points[seg_start + i].led_index,
                        x=float(sx),
                        y=float(sy)
                    )

        return [point for point in smoothed_points if point is not None]
