from dataclasses import dataclass

from pythonhelpers.dataclass_annotate import DataclassAnnotateMixin

from pythonarduinoserial.python_extension import stripped_without_terminator, bytes_to_string
from pythonarduinoserial.types import *

from ledboardlib.hardware_info.hardware_info import HardwareInfo


@dataclass
class HardwareInfoStruct(HardwareInfo, DataclassAnnotateMixin):

    name: StringType(8) = "Board"  # 7 char max (includes null terminator, length 8 to avoid manual bytes padding)

    firmware_id: IntegerType() = 0

    hardware_id: IntegerType() = 0
    hardware_serial_number: BytesType(8) = BytesDefault(8)

    serial_protocol_version: IntegerType(raw_value="protocolVersion") = 0

    def to_base(self) -> HardwareInfo:
        return HardwareInfo(
            name=stripped_without_terminator(self.name),
            firmware_id=int(self.firmware_id),
            hardware_id=int(self.hardware_id),
            hardware_serial_number=bytes_to_string(self.hardware_serial_number),
            serial_protocol_version=int(self.serial_protocol_version),
        )
