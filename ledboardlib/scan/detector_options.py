from dataclasses import dataclass


@dataclass
class DetectorOptions:
    blur_radius: int
    brightness_threshold: int
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
        if self.brightness_threshold < 0 or self.brightness_threshold > 255:
            raise ValueError("Brightness threshold must be within 0-255 range")
        if self.blur_radius < 0:
            raise ValueError("Blur radius must be non-negative")
