__all__ = [
    "BeginSamplePointsReceptionCommand",
    "EndSamplePointsReceptionCommand",
    "RebootInBootloaderModeCommand",
    "SaveControlParametersCommand",
    "SaveSamplingPointsCommand",
]
from dataclasses import dataclass

from pythonarduinoserial.base_c_struct import BaseCStruct
from pythonarduinoserial.types import IntegerType


@dataclass
class BeginSamplePointsReceptionCommand(BaseCStruct):
    count: IntegerType() = 0


@dataclass
class EndSamplePointsReceptionCommand(BaseCStruct):
    unused: IntegerType() = 0


@dataclass
class RebootInBootloaderModeCommand(BaseCStruct):
    unused: IntegerType() = 0


@dataclass
class SaveControlParametersCommand(BaseCStruct):
    unused: IntegerType() = 0  # FIXME


@dataclass
class SaveSamplingPointsCommand(BaseCStruct):
    unused: IntegerType() = 0  # FIXME
