from dataclasses import dataclass


@dataclass
class FrameDetectionResult:
    frame_as_bytes: bytes
    frame_height: int
    frame_width: int
    point: tuple[int, int] | None
    timestamp: float
