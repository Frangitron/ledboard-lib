from dataclasses import dataclass

from dataclasses_json import dataclass_json

from ledboardlib.color_mode import ColorMode
from ledboardlib.mapping_mode import MappingMode


@dataclass_json
@dataclass
class ControlParameters:
    dimmer: int

    mapping_mode: MappingMode

    noise_octaves: int
    noise_scale: int

    noise_scale_x: int
    noise_scale_y: int

    noise_speed_x: int
    noise_speed_y: int
    noise_speed_z: int

    noise_min: int
    noise_max: int

    color_mode: ColorMode

    noise_h: int
    noise_s: int
    noise_l: int

    noise_r: int
    noise_g: int
    noise_b: int

    runner_h: int
    runner_s: int
    runner_l: int

    runner_r: int
    runner_g: int
    runner_b: int

    runner_trigger: bool
    are_colors_inverted: bool
    is_noise_on: bool

    # > 0: additive, < 0: multiply
    mask_x1: int
    mask_x2: int
    mask_y1: int
    mask_y2: int

    shutter: int

    single_led: int
    single_led_brightness: int

    dmx_enabled: bool

