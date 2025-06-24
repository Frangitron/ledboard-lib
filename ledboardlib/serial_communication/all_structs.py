from ledboardlib.control_parameters.c_struct import ControlParametersStruct
from ledboardlib.hardware_configuration.c_struct import HardwareConfigurationStruct
from ledboardlib.hardware_info.c_struct import HardwareInfoStruct
from ledboardlib.sampling_point.c_struct.led_info import LedInfoStruct
from ledboardlib.sampling_point.c_struct.sample_point import SamplePointStruct
from ledboardlib.serial_communication.c_commands import *



def get():
    return [
        BeginSamplePointsReceptionCommand,
        EndSamplePointsReceptionCommand,
        RebootInBootloaderModeCommand,
        SaveControlParametersCommand,
        SaveSamplingPointsCommand,
    ] + [
        ControlParametersStruct,
        HardwareConfigurationStruct,
        HardwareInfoStruct,
        LedInfoStruct,
        SamplePointStruct,
    ]
