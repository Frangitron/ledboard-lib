from dataclasses import dataclass

from dataclasses_json import dataclass_json

from ledboardlib.color_format import ColorFormat


@dataclass_json
@dataclass
class SamplingPoint:
    index: int
    x: int
    y: int
    universe_number: int
    universe_channel: int
    color_format: ColorFormat
    led_indices: list[int]
