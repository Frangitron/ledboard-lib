from dataclasses import dataclass

from pythonarduinoserial.types import *
from pythonhelpers.dataclass_annotate import DataclassAnnotateMixin

from ledboardlib.dmx_attribution.dmx_attribution import DmxAttribution


@dataclass
class DmxAttributionStruct(DmxAttribution, DataclassAnnotateMixin):
    """
    Data transfer object between Python and Arduino
    """
    dimmer: IntegerType() = 0

    mapping_mode: IntegerType() = 12

    noise_octaves: IntegerType() = 0
    noise_scale: IntegerType() = 0

    noise_scale_x: IntegerType() = 7
    noise_scale_y: IntegerType() = 8

    noise_speed_x: IntegerType() = 9
    noise_speed_y: IntegerType() = 10
    noise_speed_z: IntegerType() = 11

    noise_min: IntegerType() = 5
    noise_max: IntegerType() = 6

    color_mode: IntegerType() = 0

    noise_h: IntegerType() = 1
    noise_s: IntegerType() = 2
    noise_l: IntegerType() = 3

    noise_r: IntegerType() = 0
    noise_g: IntegerType() = 0
    noise_b: IntegerType() = 0

    runner_h: IntegerType() = 0
    runner_s: IntegerType() = 0
    runner_l: IntegerType() = 0

    runner_r: IntegerType() = 0
    runner_g: IntegerType() = 0
    runner_b: IntegerType() = 0

    runner_trigger: IntegerType() = 0
    are_colors_inverted: IntegerType() = 0
    is_noise_on: IntegerType() = 0

    mask_x1: IntegerType() = 0
    mask_x2: IntegerType() = 0
    mask_y1: IntegerType() = 0
    mask_y2: IntegerType() = 0

    shutter: IntegerType() = 4

    @staticmethod
    def from_base(base: DmxAttribution) -> "DmxAttributionStruct":
        return DmxAttributionStruct(**base.__dict__)

    def to_base(self) -> DmxAttribution:
        return DmxAttribution(**self.__dict__)
