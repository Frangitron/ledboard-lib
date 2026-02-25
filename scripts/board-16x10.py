"""
LEGACY code waiting for JSON files
"""

from ledboardlib import BoardApi, SamplingPoint, GpioEnum, ColorFormat


def make_wave_share_points():
    index = 0
    sampling_points = list()

    for y in range(10):
        for x in range(16):
            new = SamplingPoint(
                index=index,
                x=x,
                y=y,
                universe_number=0,
                universe_channel=index * 3,
                color_format=ColorFormat.RGB,
                led_indices=[index]
            )
            sampling_points.append(new)
            index += 1
    return sampling_points


def waveshare_10x16(port: str):
    board = BoardApi(serial_port_name=port)
    configuration = board.get_configuration()
    configuration.name = "10x16"
    configuration.gpio_button_a = 2
    configuration.gpio_button_b = 3
    configuration.gpio_led_first = GpioEnum.LedsWaveshareHat.value
    configuration.led_color_format = ColorFormat.RGB
    configuration.led_count = 160
    board.set_configuration(configuration)

    print(configuration)

    board.set_sampling_points(make_wave_share_points())


def print_info(port: str):
    board = BoardApi(serial_port_name=port)

    print("-- Hardware:")
    info = board.get_hardware_info()
    for key, value in vars(info).items():
        print(f"{key} = {value}")

    print("-- Current configuration:")
    configuration = board.get_configuration()
    for key, value in vars(configuration).items():
        print(f"{key} = {value}")

    print('-' * 20)


if __name__ == '__main__':
    com = "COM4"
    print_info(com)
    waveshare_10x16(com)
    print("Done.")
