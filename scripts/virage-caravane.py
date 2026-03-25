from ledboardlib import BoardApi, ColorFormat, GpioEnum, SamplingPoint


def main(port:str, update_board_config:bool, update_board_points: bool):
    strand_led_count = 75
    strand_count = 2
    sampling_points = list()
    for index in range(strand_led_count * strand_count):
        new = SamplingPoint(
            index=index,
            x=int(index),
            y=0,
            universe_number=0,
            universe_channel=index * 3,
            color_format=ColorFormat.RGB,
            led_indices=[index]
        )
        sampling_points.append(new)

    print(f"Sampling points: {len(sampling_points)}")

    board = BoardApi(serial_port_name=port)
    if update_board_config:
        configuration = board.get_configuration()
        configuration.name = "Caravan"
        configuration.led_color_format = ColorFormat.RGB
        configuration.led_count = strand_led_count
        configuration.gpio_led_first = GpioEnum.Ledboard2GpioD.value
        configuration.gpio_buttons_enable = True
        configuration.gpio_button_a = GpioEnum.Ledboard2GpioB.value
        configuration.gpio_button_b = GpioEnum.Ledboard2GpioC.value
        configuration.dmx_address = 1
        board.set_configuration(configuration)

        print(configuration)

    if update_board_points:
        board.set_sampling_points(sampling_points)


if __name__ == "__main__":
    main(
        port="COM4",
        update_board_config=True,
        update_board_points=False
    )
