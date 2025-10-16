from dataclasses import dataclass
from ipaddress import IPv4Address

from ledboardlib.color_format import ColorFormat


@dataclass
class HardwareConfiguration:
    name: str

    gpio_admin_mode: int
    gpio_dmx_input: int
    gpio_led_first: int
    gpio_button_a: int
    gpio_button_b: int

    wifi_password: str
    wifi_ip_address: IPv4Address
    wifi_gateway: IPv4Address
    wifi_subnet: IPv4Address

    led_count: int
    led_color_format: ColorFormat

    gamma_correction: float

    osc_receive_port: int

    dmx_address: int
