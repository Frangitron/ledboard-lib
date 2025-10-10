from dataclasses import dataclass


@dataclass
class FrameDetectionResult:
    timestamp: float
    frame_width: int
    frame_height: int
    frame_as_bytes: bytes
    points: list[tuple[int, int]]
