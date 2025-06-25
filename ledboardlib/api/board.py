import time

from pythonarduinoserial.communicator import SerialCommunicator

from ledboardlib.control_parameters.c_struct import ControlParametersStruct
from ledboardlib.control_parameters.control_parameters import ControlParameters
from ledboardlib.hardware_configuration.c_struct import HardwareConfigurationStruct
from ledboardlib.hardware_configuration.hardware_configuration import HardwareConfiguration
from ledboardlib.hardware_info.c_struct import HardwareInfoStruct
from ledboardlib.hardware_info.hardware_info import HardwareInfo
from ledboardlib.sampling_point.c_struct.led_info import LedInfoStruct
from ledboardlib.sampling_point.c_struct.sample_point import SamplePointStruct
from ledboardlib.sampling_point.sampling_point import SamplingPoint
from ledboardlib.serial_communication import all_structs, c_commands


class BoardApi:
    """
    Manages communication and interaction with hardware using a serial interface.

    This class provides an interface to communicate with a connected device via a
    serial port. It facilitates sending and receiving structured data, as well as
    configuring hardware settings, retrieving hardware information, and managing
    specific sampling points and control parameters. It ensures proper connection
    setup and disconnection when needed.

    :ivar serial_port: The name of the serial port used for communication.
    :type serial_port: Str
    """
    def __init__(self, serial_port):
        self.serial_port = serial_port

        self.serial_communicator = SerialCommunicator(structs=all_structs.get())
        self.serial_communicator.set_port_name(self.serial_port)

    def get_hardware_info(self) -> HardwareInfo:
        return self.serial_communicator.receive(HardwareInfoStruct).to_base()

    def set_configuration(self, configuration: HardwareConfiguration):
        self.serial_communicator.send(HardwareConfigurationStruct.from_base(configuration))

    def get_configuration(self) -> HardwareConfiguration:
        return self.serial_communicator.receive(HardwareConfigurationStruct).to_base()

    def set_sampling_points(self, sampling_points: list[SamplingPoint]):
        if not sampling_points:
            return

        self.serial_communicator.send(c_commands.BeginSamplePointsReceptionCommand(len(sampling_points)))
        for sampling_point in sampling_points:
            self.serial_communicator.send(SamplePointStruct.from_base(sampling_point))
            for led_index in sampling_point.led_indices:
                self.serial_communicator.send(LedInfoStruct(sampling_point.index, led_index))

        time.sleep(0.6)
        self.serial_communicator.send(c_commands.SaveSamplingPointsCommand())
        time.sleep(0.6)
        self.serial_communicator.send(c_commands.EndSamplePointsReceptionCommand())

    def get_control_parameters(self) -> ControlParameters | None:
        c_struct = self.serial_communicator.receive(ControlParametersStruct)
        if c_struct is None:
            raise

        return c_struct.to_base()

    def set_control_parameters(self, parameters: ControlParameters):
        self.serial_communicator.send(ControlParametersStruct.from_base(parameters))

    def save_control_parameters(self):
        self.serial_communicator.send(c_commands.SaveControlParametersCommand())

    def reboot(self):
        self.serial_communicator.send(c_commands.RebootCommand())

    def reboot_in_bootloader_mode(self):
        self.serial_communicator.send(c_commands.RebootInBootloaderModeCommand())
