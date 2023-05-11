function car_UTurn (num: number, num2: number) {
    pins.analogWritePin(AnalogPin.P8, num)
    pins.digitalWritePin(DigitalPin.P12, 1)
    pins.analogWritePin(AnalogPin.P13, num2)
    pins.digitalWritePin(DigitalPin.P14, 1)
}
bluetooth.onUartDataReceived(serial.delimiters(Delimiters.NewLine), function () {
    cmd = bluetooth.uartReadUntil(serial.delimiters(Delimiters.NewLine))
    if (cmd.charAt(0).compare("A") == 0) {
        L_speed = parseFloat(cmd.substr(1, cmd.length - 1))
        MotorL_CW(L_speed)
        MotorL_status = 1
        basic.showString("A")
    } else if (cmd.charAt(0).compare("B") == 0) {
        L_speed = parseFloat(cmd.substr(1, cmd.length - 1))
        MotorL_CCW(L_speed)
        MotorL_status = 1
        basic.showString("B")
    } else if (cmd.charAt(0).compare("C") == 0) {
        R_speed = parseFloat(cmd.substr(1, cmd.length - 1))
        MotorR_CW(R_speed)
        MotorR_status = 1
        basic.showString("C")
    } else if (cmd.charAt(0).compare("D") == 0) {
        R_speed = parseFloat(cmd.substr(1, cmd.length - 1))
        MotorR_CCW(R_speed)
        MotorR_status = 1
        basic.showString("D")
    } else if (cmd.compare("E") == 0) {
        pins.analogWritePin(AnalogPin.P13, 0)
        MotorL_status = 0
        basic.showString("E")
    } else if (cmd.charAt(0).compare("L") == 0) {
        L_speed = parseFloat(cmd.substr(1, cmd.length - 1))
        if (MotorL_status == 1) {
            pins.analogWritePin(AnalogPin.P13, L_speed)
        }
    } else if (cmd.charAt(0).compare("R") == 0) {
        R_speed = parseFloat(cmd.substr(1, cmd.length - 1))
        if (MotorR_status == 1) {
            pins.analogWritePin(AnalogPin.P8, R_speed)
        }
    } else if (cmd.compare("F") == 0) {
        pins.analogWritePin(AnalogPin.P8, 0)
        MotorR_status = 0
        basic.showString("F")
    }
    bluetooth.uartWriteString("L-" + ("" + L_speed) + "R-" + ("" + R_speed))
})
function MotorL_CW (num3: number) {
    pins.analogWritePin(AnalogPin.P13, num3)
    pins.analogSetPeriod(AnalogPin.P13, 500)
    pins.digitalWritePin(DigitalPin.P14, 1)
}
bluetooth.onBluetoothConnected(function () {
    basic.showIcon(IconNames.Happy)
    bluetooth.startUartService()
    bluetooth.setTransmitPower(7)
    serial.redirect(
    SerialPin.P0,
    SerialPin.P1,
    BaudRate.BaudRate115200
    )
    cuteBot.turnleft()
})
bluetooth.onBluetoothDisconnected(function () {
    basic.showIcon(IconNames.Sad)
})
function MotorR_CW (num4: number) {
    pins.analogWritePin(AnalogPin.P8, num4)
    pins.analogSetPeriod(AnalogPin.P8, 500)
    pins.digitalWritePin(DigitalPin.P12, 1)
}
function MotorR_CCW (num5: number) {
    pins.analogWritePin(AnalogPin.P8, num5)
    pins.analogSetPeriod(AnalogPin.P8, 500)
    pins.digitalWritePin(DigitalPin.P12, 0)
}
function MotorL_CCW (num6: number) {
    pins.analogWritePin(AnalogPin.P13, num6)
    pins.analogSetPeriod(AnalogPin.P13, 500)
    pins.digitalWritePin(DigitalPin.P14, 0)
}
function car_Forward (num7: number, num22: number) {
    pins.analogWritePin(AnalogPin.P8, num7)
    pins.digitalWritePin(DigitalPin.P12, 1)
    pins.analogWritePin(AnalogPin.P13, num22)
    pins.digitalWritePin(DigitalPin.P14, 1)
}
function car_TurnRight (num8: number, num23: number) {
    pins.analogWritePin(AnalogPin.P8, num8)
    pins.digitalWritePin(DigitalPin.P12, 1)
    pins.analogWritePin(AnalogPin.P13, num23)
    pins.digitalWritePin(DigitalPin.P14, 1)
}
function car_TurnLeft (num9: number, num24: number) {
    pins.analogWritePin(AnalogPin.P8, num9)
    pins.digitalWritePin(DigitalPin.P12, 1)
    pins.analogWritePin(AnalogPin.P13, num24)
    pins.digitalWritePin(DigitalPin.P14, 1)
}
function car_stop () {
    pins.digitalWritePin(DigitalPin.P8, 1)
    pins.digitalWritePin(DigitalPin.P12, 1)
}
let cmd = ""
let R_speed = 0
let L_speed = 0
let MotorR_status = 0
let MotorL_status = 0
let F_status = 0
basic.showIcon(IconNames.Asleep)
MotorL_status = 0
MotorR_status = 0
L_speed = 700
R_speed = 700
