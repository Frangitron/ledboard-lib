from dataclasses import dataclass


@dataclass
class ControlParameters:
    noise_octaves: int
    noise_scale: int

    noise_scale_x: int
    noise_scale_y: int

    noise_speed_x: int
    noise_speed_y: int
    noise_speed_z: int

    noise_min: int
    noise_max: int

    noise_r: int
    noise_g: int
    noise_b: int

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

    bat_low: bool
    bat_1_bar: bool
