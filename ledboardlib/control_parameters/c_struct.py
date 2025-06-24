from dataclasses import dataclass

from pythonarduinoserial.base_c_struct import BaseCStruct
from pythonarduinoserial.types import *

from ledboardlib.control_parameters.control_parameters import ControlParameters


@dataclass
class ControlParametersStruct(BaseCStruct):
    """
    Data transfer object between Python and Arduino
    """

    noise_octaves: IntegerType() = 2
    noise_scale: IntegerType() = 3

    noise_scale_x: IntegerType() = 200
    noise_scale_y: IntegerType() = 200

    noise_speed_x: IntegerType() = 0
    noise_speed_y: IntegerType() = 0
    noise_speed_z: IntegerType() = 0

    noise_min: IntegerType() = 150
    noise_max: IntegerType() = 1024 - 200

    noise_r: IntegerType() = 0
    noise_g: IntegerType() = 200
    noise_b: IntegerType() = 200

    runner_r: IntegerType() = 255
    runner_g: IntegerType() = 0
    runner_b: IntegerType() = 0

    runner_trigger: IntegerType() = 0
    are_colors_inverted: IntegerType() = 0

    # > 0: additive, < 0: multiply
    mask_x1: IntegerType() = 0
    mask_x2: IntegerType() = 0
    mask_y1: IntegerType() = 0
    mask_y2: IntegerType() = 0

    bat_low: IntegerType() = 0
    bat_1_bar: IntegerType() = 0

    @staticmethod
    def from_base(base: ControlParameters) -> "ControlParametersStruct":
        return ControlParametersStruct(
            noise_octaves=base.noise_octaves,
            noise_scale=base.noise_scale,
            noise_scale_x=base.noise_scale_x,
            noise_scale_y=base.noise_scale_y,
            noise_speed_x=base.noise_speed_x,
            noise_speed_y=base.noise_speed_y,
            noise_speed_z=base.noise_speed_z,
            noise_min=base.noise_min,
            noise_max=base.noise_max,
            noise_r=base.noise_r,
            noise_g=base.noise_g,
            noise_b=base.noise_b,
            runner_r=base.runner_r,
            runner_g=base.runner_g,
            runner_b=base.runner_b,
            runner_trigger=int(base.runner_trigger),
            are_colors_inverted=int(base.are_colors_inverted),
            mask_x1=base.mask_x1,
            mask_x2=base.mask_x2,
            mask_y1=base.mask_y1,
            mask_y2=base.mask_y2,
            bat_low=int(base.bat_low),
            bat_1_bar=int(base.bat_1_bar)
        )

    def to_base(self) -> ControlParameters:
        return ControlParameters(
            noise_octaves=int(self.noise_octaves),
            noise_scale=int(self.noise_scale),
            noise_scale_x=int(self.noise_scale_x),
            noise_scale_y=int(self.noise_scale_y),
            noise_speed_x=int(self.noise_speed_x),
            noise_speed_y=int(self.noise_speed_y),
            noise_speed_z=int(self.noise_speed_z),
            noise_min=int(self.noise_min),
            noise_max=int(self.noise_max),
            noise_r=int(self.noise_r),
            noise_g=int(self.noise_g),
            noise_b=int(self.noise_b),
            runner_r=int(self.runner_r),
            runner_g=int(self.runner_g),
            runner_b=int(self.runner_b),
            runner_trigger=bool(self.runner_trigger),
            are_colors_inverted=bool(self.are_colors_inverted),
            mask_x1=int(self.mask_x1),
            mask_x2=int(self.mask_x2),
            mask_y1=int(self.mask_y1),
            mask_y2=int(self.mask_y2),
            bat_low=bool(self.bat_low),
            bat_1_bar=bool(self.bat_1_bar)
        )
