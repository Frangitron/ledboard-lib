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


def strip_5m(port: str, led_count: int = 300):

    board = BoardApi(serial_port_name=port)
    configuration = board.get_configuration()
    configuration.name = "Strip"
    configuration.gpio_button_a = 2
    configuration.gpio_button_b = 3
    configuration.gpio_led_first = GpioEnum.LedsWaveshareHat.value
    configuration.led_color_format = ColorFormat.GRB
    configuration.led_count = led_count
    board.set_configuration(configuration)

    print(configuration)

    sampling_points = list()
    for s in range(led_count):
        new = SamplingPoint(
            index=s,
            x=s,
            y=0,
            universe_number=0,
            universe_channel=s * 3,
            color_format=ColorFormat.RGB,
            led_indices=[s]
        )
        sampling_points.append(new)

    board.set_sampling_points(sampling_points)


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


def rect_256(port: str):
    board = BoardApi(serial_port_name=port)
    configuration = board.get_configuration()
    configuration.led_count = 256
    configuration.gpio_button_a = 2
    configuration.gpio_button_b = 3
    configuration.gpio_led_first = GpioEnum.LedsWaveshareHat.value
    configuration.led_color_format = ColorFormat.GRB
    board.set_configuration(configuration)

    index = 0
    led_offset = 0
    sampling_points = list()
    point_offset = len(sampling_points)

    for y in range(16):
        x_ = (lambda X: X) if y % 2 else (lambda X: 15 - X)
        for x in range(16):
            new = SamplingPoint(
                index=point_offset + index,
                x=x_(x),
                y=y,
                universe_number=0,
                universe_channel=index * 3,
                color_format=ColorFormat.RGB,
                led_indices=[led_offset + index]
            )
            sampling_points.append(new)
            index += 1

    print(f"Sampling points: {len(sampling_points)}")
    board.set_sampling_points(sampling_points)


def set_speed_z(port: str, speed: int):
    board = BoardApi(serial_port_name=port)
    parameters = board.get_control_parameters()
    if parameters is None:
        print("No parameters received !")
        return
    parameters.noise_speed_z = speed
    board.save_control_parameters()


def blue_pipes(port: str):
    strand_led_count = 150
    strand_count = 6
    pixel_doubling = 1

    board = BoardApi(serial_port_name=port)
    configuration = board.get_configuration()
    configuration.name = "BluPipe"
    configuration.gpio_button_a = GpioEnum.ButtonBluePipesA.value
    configuration.gpio_button_b = GpioEnum.ButtonBluePipesB.value
    configuration.gpio_led_first = GpioEnum.LedsNoonBoard.value
    configuration.led_color_format = ColorFormat.GRB
    configuration.led_count = strand_led_count
    board.set_configuration(configuration)

    print(configuration)

    sampling_points = list()
    for r in range(strand_count):
        for s in range(int(strand_led_count / pixel_doubling)):
            index = (r * int(strand_led_count / pixel_doubling)) + s
            new = SamplingPoint(
                index=index,
                x=s * pixel_doubling,
                y=r,
                universe_number=0,
                universe_channel=index * 3,
                color_format=ColorFormat.GRB,
                led_indices=[index * pixel_doubling + i for i in range(pixel_doubling)]
            )
            sampling_points.append(new)

    print(f"Sampling points: {len(sampling_points)}")
    board.set_sampling_points(sampling_points)


def melinerion(port: str):
    strand_led_count = 150

    strand_count = 1
    pixel_doubling = 1

    board = BoardApi(serial_port_name=port)
    configuration = board.get_configuration()
    configuration.name = "Meliner"
    configuration.led_color_format = ColorFormat.GRBW
    configuration.led_count = strand_led_count
    board.set_configuration(configuration)

    print(configuration)

    sampling_points = list()
    for r in range(strand_count):
        for s in range(int(strand_led_count / pixel_doubling)):
            index = (r * int(strand_led_count / pixel_doubling)) + s
            new = SamplingPoint(
                index=index,
                x=s * pixel_doubling,
                y=r,
                universe_number=0,
                universe_channel=index * 3,
                color_format=ColorFormat.GRB,
                led_indices=[index * pixel_doubling + i for i in range(pixel_doubling)]
            )
            sampling_points.append(new)

    print(f"Sampling points: {len(sampling_points)}")
    board.set_sampling_points(sampling_points)


if __name__ == '__main__':
    com = "COM4"
    print_info(com)
    # waveshare_10x16(com)
    # strip_5m(com, 40)
    # rect_256(com)
    # set_speed_z(com, 1)
    # blue_pipes(com)
    melinerion(com)
    print("Done.")
