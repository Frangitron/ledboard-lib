from dataclasses import dataclass

from pythonarduinoserial.base_c_struct import BaseCStruct
from pythonarduinoserial.types import *


@dataclass
class LedInfoStruct(BaseCStruct):
    sampling_point_index: IntegerType() = 0
    led_index: IntegerType() = 0
