from dataclasses import dataclass, field

from dataclasses_json import dataclass_json

from ledboardlib.control_parameters.control_parameters import ControlParameters
from ledboardlib.fixture import Fixture
from ledboardlib.sampling_point.sampling_point import SamplingPoint


@dataclass_json
@dataclass
class InteropData:
    artnet_target_ip: str | None = None
    default_control_parameters: ControlParameters | None = None
    emulator_ignores_dimmer: bool = True
    enttec_output_enabled: bool = False
    enttec_port_name: str | None = None
    fixtures: list[Fixture] = field(default_factory=list)
    midi_port_name: str |None = None
    sampling_points: list[SamplingPoint] = field(default_factory=list)
