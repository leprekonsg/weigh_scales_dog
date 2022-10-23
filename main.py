def on_button_pressed_a():
    basic.clear_screen()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    basic.clear_screen()
    SGBotic.cali_UserLoad(90)
input.on_button_pressed(Button.B, on_button_pressed_b)

motion = 0
_var = 0
basic.clear_screen()
radio.set_group(1)
radio.set_frequency_band(7)
radio.set_transmit_power(7)
SGBotic.init_loadcell(DigitalPin.P1, DigitalPin.P2)
SGBotic.loadCell_noLoad()

def on_forever():
    global _var, motion
    _var = SGBotic.read_grams()
    motion = pins.digital_read_pin(DigitalPin.P0)
    if motion == 1:
        basic.show_number(_var)
        radio.send_value("W0", _var)
        for index in range(51):
            basic.pause(1000)
            radio.send_value("\"W0\"", _var)
    else:
        basic.show_icon(IconNames.NO)
    basic.pause(1000)
basic.forever(on_forever)
