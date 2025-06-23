from dataclasses import dataclass

from ledboardlib.serial_communication.c_structs import HardwareInfoStruct


@dataclass
class ListedBoard:
    serial_port_name: str
    available: bool
    hardware_info: HardwareInfoStruct | None = None
