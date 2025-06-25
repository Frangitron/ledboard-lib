from dataclasses import dataclass


@dataclass
class HardwareInfo:
    """
    This class provides details about the hardware, such as its name, firmware and
    hardware identifiers, and the serial number. The serial protocol version is
    used to track changes in the associated communication structure.

    Make sure to update the serial protocol version when making changes to the C structs.

    :ivar name: The name of the hardware.
    :type name: Str
    :ivar firmware_id: The identifier of the firmware associated with the hardware.
    :type firmware_id: Int
    :ivar hardware_id: The identifier of the hardware.
    :type hardware_id: Int
    :ivar hardware_serial_number: The serial number of the hardware.
    :type hardware_serial_number: Str
    :ivar serial_protocol_version: The version of the protocol structure used
        for serial communication.
    :type serial_protocol_version: Int
    """
    name: str

    firmware_id: int

    hardware_id: int
    hardware_serial_number: str

    # Increment this on C struct changes
    serial_protocol_version: int = 0
