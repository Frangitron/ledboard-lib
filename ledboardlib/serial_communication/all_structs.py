from ledboardlib.control_parameters.c_struct import ControlParametersStruct
from ledboardlib.hardware_configuration.c_struct import HardwareConfigurationStruct
from ledboardlib.hardware_info.c_struct import HardwareInfoStruct
from ledboardlib.sampling_point.c_struct.led_info import LedInfoStruct
from ledboardlib.sampling_point.c_struct.sample_point import SamplePointStruct
from ledboardlib.serial_communication.c_commands import *



def get():
    return [
        HardwareInfoStruct,  # Always first to ensure all protocol versions can read it
    ] + [
        BeginSamplePointsReceptionCommand,
        EndSamplePointsReceptionCommand,
        RebootCommand,
        RebootInBootloaderModeCommand,
        SaveControlParametersCommand,
        SaveSamplingPointsCommand,
    ] + [
        ControlParametersStruct,
        HardwareConfigurationStruct,
        LedInfoStruct,
        SamplePointStruct,
    ]
