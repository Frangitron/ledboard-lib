from dataclasses import dataclass

from pythonhelpers.dataclass_annotate import DataclassToFromBaseMixin
from pythonarduinoserial.types import *

from ledboardlib.sampling_point.sampling_point import SamplingPoint


@dataclass
class SamplePointStruct(DataclassToFromBaseMixin):
    index: IntegerType() = 0
    x: IntegerType() = 0
    y: IntegerType() = 0
    universe_number: IntegerType() = 0
    universe_channel: IntegerType() = 0
    color_format: IntegerType() = 0

    @staticmethod
    def from_base(sampling_point: SamplingPoint) -> "SamplePointStruct":
        return SamplePointStruct(
            index=sampling_point.index,
            x=sampling_point.x,
            y=sampling_point.y,
            universe_number=sampling_point.universe_number,
            universe_channel=sampling_point.universe_channel,
            color_format=sampling_point.color_format.value
        )
