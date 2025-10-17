from dataclasses import dataclass, field

from dataclasses_json import dataclass_json

from ledboardlib.control_parameters.control_parameters import ControlParameters
from ledboardlib.fixture import Fixture
from ledboardlib.sampling_point.sampling_point import SamplingPoint


@dataclass_json
@dataclass
class InteropData:
    artnet_target_ip: str = "127.0.0.1"
    default_control_parameters: ControlParameters | None = None
    emulator_ignores_dimmer: bool = True
    enttec_output_enabled: bool = False
    enttec_port_name: str = "COM18"
    fixtures: list[Fixture] = field(default_factory=list)
    midi_port_name: str = "OSC Artnet"
    sampling_points: list[SamplingPoint] = field(default_factory=list)
