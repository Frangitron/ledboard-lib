from dataclasses import dataclass


@dataclass
class DetectorOptions:
    average_frame_count: int
    blur_radius: int
    camera_height: int
    camera_index: int
    camera_width: int

    def __post_init__(self):
        if self.camera_index < 0:
            raise ValueError("Camera index must be non-negative")
        if self.camera_width <= 0:
            raise ValueError("Camera width must be positive")
        if self.camera_height <= 0:
            raise ValueError("Camera height must be positive")
        if self.blur_radius < 0:
            raise ValueError("Blur radius must be non-negative")
        if self.average_frame_count < 1:
            raise ValueError("Average frame count must be at least 1")
