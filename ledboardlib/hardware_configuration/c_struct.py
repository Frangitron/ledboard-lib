from dataclasses import dataclass
from ipaddress import IPv4Address

from pythonarduinoserial.python_extension import stripped_without_terminator
from pythonarduinoserial.types import *
from pythonhelpers.dataclass_annotate import DataclassAnnotateMixin

from ledboardlib.color_format import ColorFormat
from ledboardlib.hardware_configuration.hardware_configuration import HardwareConfiguration


@dataclass
class HardwareConfigurationStruct(HardwareConfiguration, DataclassAnnotateMixin):
    """
    Data transfer object between Python and Arduino
    """

    name: StringType(8) = "Board"  # 7 char max (includes null terminator, length 8 to avoid manual bytes padding)

    gpio_admin_mode: IntegerType() = 1  # absent in Jan 2024 LedBoard
    gpio_dmx_input: IntegerType() = 5  # absent in Jan 2024 LedBoard
    gpio_led_first: IntegerType() = 6  # default for Jan 2024 LedBoard
    gpio_button_a: IntegerType() = 9
    gpio_button_b: IntegerType() = 9

    wifi_password: StringType(16) = "0123456789ABCDE"  # includes null terminator, length 16 to avoid manual bytes padding
    wifi_ip_address: BytesType(4) = bytes([192, 168, 0, 201])
    wifi_gateway: BytesType(4) = bytes([192, 168, 0, 1])
    wifi_subnet: BytesType(4) = bytes([255, 255, 0, 0])

    led_count: IntegerType() = 160  # value for 16x10 Led matrix
    led_color_format: IntegerType() = 0  # RGB: 0, GRB: 1

    gamma_correction: FloatType() = 2.6

    osc_receive_port: IntegerType() = 54321

    dmx_address: IntegerType() = 1

    @staticmethod
    def from_base(base: HardwareConfiguration) -> "HardwareConfigurationStruct":
        return HardwareConfigurationStruct(
            name=base.name,
            gpio_admin_mode=base.gpio_admin_mode,
            gpio_dmx_input=base.gpio_dmx_input,
            gpio_led_first=base.gpio_led_first,
            gpio_button_a=base.gpio_button_a,
            gpio_button_b=base.gpio_button_b,
            wifi_password=base.wifi_password,
            wifi_ip_address=base.wifi_ip_address.packed,
            wifi_gateway=base.wifi_gateway.packed,
            wifi_subnet=base.wifi_subnet.packed,
            led_count=base.led_count,
            led_color_format=base.led_color_format.value,
            gamma_correction=base.gamma_correction,
            osc_receive_port=base.osc_receive_port,
            dmx_address=base.dmx_address
        )

    def to_base(self) -> HardwareConfiguration:
        return HardwareConfiguration(
            name=stripped_without_terminator(self.name),
            gpio_admin_mode=int(self.gpio_admin_mode),
            gpio_dmx_input=int(self.gpio_dmx_input),
            gpio_led_first=int(self.gpio_led_first),
            gpio_button_a=int(self.gpio_button_a),
            gpio_button_b=int(self.gpio_button_b),
            wifi_password=stripped_without_terminator(self.wifi_password),
            wifi_ip_address=IPv4Address(self.wifi_ip_address),
            wifi_gateway=IPv4Address(self.wifi_gateway),
            wifi_subnet=IPv4Address(self.wifi_subnet),
            led_count=int(self.led_count),
            led_color_format=ColorFormat(self.led_color_format),
            gamma_correction=float(self.gamma_correction),
            osc_receive_port=int(self.osc_receive_port),
            dmx_address=int(self.dmx_address)
        )
