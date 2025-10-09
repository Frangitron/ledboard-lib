from ledboardlib.control_parameters.c_struct import ControlParametersStruct
from ledboardlib.dmx_attribution.c_struct import DmxAttributionStruct
from ledboardlib.hardware_configuration.c_struct import HardwareConfigurationStruct
from ledboardlib.hardware_info.c_struct import HardwareInfoStruct
from ledboardlib.sampling_point.c_struct.led_info import LedInfoStruct
from ledboardlib.sampling_point.c_struct.sample_point import SamplePointStruct
from ledboardlib.serial_communication.c_commands import *


def get():
    # Basic operations that all future serial protocol versions must handle
    protocol_foundation = [
        HardwareInfoStruct,
        RebootCommand,
        RebootInBootloaderModeCommand,
    ]

    # Version-specific operations
    return protocol_foundation + [
        BeginSamplePointsReceptionCommand,
        EndSamplePointsReceptionCommand,
        SaveControlParametersCommand,
        SaveSamplingPointsCommand,
    ] + [
        ControlParametersStruct,
        DmxAttributionStruct,
        HardwareConfigurationStruct,
        LedInfoStruct,
        SamplePointStruct,
    ]
