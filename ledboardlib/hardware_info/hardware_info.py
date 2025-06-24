from dataclasses import dataclass


@dataclass
class HardwareInfo:
    name: str

    hardware_id: str
    hardware_revision: int

    firmware_revision: int
