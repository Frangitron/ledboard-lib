from dataclasses import dataclass

from ledboardlib.hardware_info.hardware_info import HardwareInfo


@dataclass
class ListedBoard:
    serial_port_name: str
    available: bool
    hardware_info: HardwareInfo | None = None
