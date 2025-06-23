from dataclasses import dataclass

from pythonarduinoserial.types import *


@dataclass
class HardwareInfoStruct:

    name: StringType(8) = "Board"  # 7 char max (includes null terminator, length 8 to avoid manual bytes padding)

    hardware_id: BytesType(8) = BytesDefault(8)
    hardware_revision: IntegerType() = 0

    firmware_revision: IntegerType() = 0
