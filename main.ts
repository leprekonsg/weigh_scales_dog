input.onButtonPressed(Button.A, function () {
    basic.clearScreen()
})
input.onButtonPressed(Button.B, function () {
    basic.clearScreen()
    SGBotic.cali_UserLoad(90)
})
let motion = 0
let _var = 0
basic.clearScreen()
radio.setGroup(1)
radio.setFrequencyBand(7)
radio.setTransmitPower(7)
SGBotic.init_loadcell(
DigitalPin.P1,
DigitalPin.P2
)
SGBotic.loadCell_noLoad(
)
basic.forever(function () {
    _var = SGBotic.read_grams(
    )
    motion = pins.digitalReadPin(DigitalPin.P0)
    if (motion == 1) {
        basic.showNumber(_var)
        radio.sendValue("W0", _var)
        for (let index = 0; index < 50; index++) {
            basic.pause(1000)
            _var = SGBotic.read_grams(
            )
            radio.sendValue("W0", _var)
        }
    } else {
        basic.showIcon(IconNames.No)
    }
    basic.pause(1000)
})
