from dataclasses import dataclass, field

from dataclasses_json import dataclass_json

from ledboardlib.control_parameters.control_parameters import ControlParameters
from ledboardlib.fixture import Fixture
from ledboardlib.sampling_point.sampling_point import SamplingPoint


@dataclass_json
@dataclass
class InteropData:
    sampling_points: list[SamplingPoint] = field(default_factory=list)
    default_control_parameters: ControlParameters | None = None
    fixtures: list[Fixture] = field(default_factory=list)
