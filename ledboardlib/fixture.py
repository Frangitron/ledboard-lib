from dataclasses import dataclass

from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class Fixture:
    name: str
    midi_channel: int
    dmx_address: int
    dmx_channel_count: int
