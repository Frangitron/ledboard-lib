__all__ = [
    "BeginSamplePointsReceptionCommand",
    "EndSamplePointsReceptionCommand",
    "RebootCommand",
    "RebootInBootloaderModeCommand",
    "SaveControlParametersCommand",
    "SaveSamplingPointsCommand",
]
from dataclasses import dataclass

from pythonhelpers.dataclass_annotate import DataclassToFromBaseMixin
from pythonarduinoserial.types import IntegerType


@dataclass
class BeginSamplePointsReceptionCommand(DataclassToFromBaseMixin):
    count: IntegerType() = 0


@dataclass
class EndSamplePointsReceptionCommand(DataclassToFromBaseMixin):
    unused: IntegerType() = 0


@dataclass
class RebootCommand(DataclassToFromBaseMixin):
    unused: IntegerType() = 0


@dataclass
class RebootInBootloaderModeCommand(DataclassToFromBaseMixin):
    unused: IntegerType() = 0


@dataclass
class SaveControlParametersCommand(DataclassToFromBaseMixin):
    unused: IntegerType() = 0  # FIXME


@dataclass
class SaveSamplingPointsCommand(DataclassToFromBaseMixin):
    unused: IntegerType() = 0  # FIXME
