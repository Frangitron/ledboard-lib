from dataclasses import dataclass

from pythonarduinoserial.types import *
from pythonhelpers.dataclass_annotate import DataclassAnnotateMixin

from ledboardlib.dmx_attribution.dmx_attribution import DmxAttribution


@dataclass
class DmxAttributionStruct(DmxAttribution, DataclassAnnotateMixin):
    """
    Data transfer object between Python and Arduino
    """
    noise_octaves: IntegerType() = -1
    noise_scale: IntegerType() = -1

    noise_scale_x: IntegerType() = -1
    noise_scale_y: IntegerType() = -1

    noise_speed_x: IntegerType() = -1
    noise_speed_y: IntegerType() = -1
    noise_speed_z: IntegerType() = -1

    noise_min: IntegerType() = -1
    noise_max: IntegerType() = -1

    color_mode: IntegerType() = -1

    noise_h: IntegerType() = -1
    noise_s: IntegerType() = -1
    noise_l: IntegerType() = -1

    noise_r: IntegerType() = -1
    noise_g: IntegerType() = -1
    noise_b: IntegerType() = -1

    runner_h: IntegerType() = -1
    runner_s: IntegerType() = -1
    runner_l: IntegerType() = -1

    runner_r: IntegerType() = -1
    runner_g: IntegerType() = -1
    runner_b: IntegerType() = -1

    runner_trigger: IntegerType() = -1
    are_colors_inverted: IntegerType() = -1
    is_noise_on: IntegerType() = -1

    mask_x1: IntegerType() = -1
    mask_x2: IntegerType() = -1
    mask_y1: IntegerType() = -1
    mask_y2: IntegerType() = -1

    shutter: IntegerType() = -1

    @staticmethod
    def from_base(base: DmxAttribution) -> "DmxAttributionStruct":
        return DmxAttributionStruct(**base.__dict__)

    def to_base(self) -> DmxAttribution:
        return DmxAttribution(**self.__dict__)
