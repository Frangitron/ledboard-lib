from dataclasses import dataclass

from pythonarduinoserial.base_c_struct import BaseCStruct
from pythonarduinoserial.python_extension import without_terminator, bytes_to_string
from pythonarduinoserial.types import *

from ledboardlib.hardware_info.hardware_info import HardwareInfo


@dataclass
class HardwareInfoStruct(BaseCStruct):

    name: StringType(8) = "Board"  # 7 char max (includes null terminator, length 8 to avoid manual bytes padding)

    hardware_id: BytesType(8) = BytesDefault(8)
    hardware_revision: IntegerType() = 0

    firmware_revision: IntegerType() = 0

    @staticmethod
    def from_base(base: HardwareInfo) -> "HardwareInfoStruct":
        return HardwareInfoStruct(
            name=base.name,
            hardware_id=bytes(base.hardware_id, "utf-8"),
            hardware_revision=base.hardware_revision,
            firmware_revision=base.firmware_revision
        )

    def to_base(self) -> HardwareInfo:
        return HardwareInfo(
            name=without_terminator(self.name),
            hardware_id=bytes_to_string(self.hardware_id),
            hardware_revision=int(self.hardware_revision),
            firmware_revision=int(self.firmware_revision)
        )
