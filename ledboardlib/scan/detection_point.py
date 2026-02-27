from dataclasses import dataclass

from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class DetectionPoint:
    x: float
    y: float
    led_index: int
