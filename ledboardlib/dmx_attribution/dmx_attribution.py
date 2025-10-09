from dataclasses import dataclass


@dataclass
class DmxAttribution:
    """
    DMX channels attribution
    -1 : unused
    0 - 255 : DMX channel
    """
    noise_octaves: int
    noise_scale: int

    noise_scale_x: int
    noise_scale_y: int

    noise_speed_x: int
    noise_speed_y: int
    noise_speed_z: int

    noise_min: int
    noise_max: int

    color_mode: int

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

    runner_trigger: int
    are_colors_inverted: int
    is_noise_on: int

    mask_x1: int
    mask_x2: int
    mask_y1: int
    mask_y2: int

    shutter: int
