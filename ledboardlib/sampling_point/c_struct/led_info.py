from dataclasses import dataclass

from pythonhelpers.dataclass_annotate import DataclassToFromBaseMixin

from pythonarduinoserial.types import *


@dataclass
class LedInfoStruct(DataclassToFromBaseMixin):
    sampling_point_index: IntegerType() = 0
    led_index: IntegerType() = 0
