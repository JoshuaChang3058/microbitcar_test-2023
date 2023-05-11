def car_UTurn(num: number, num2: number):
    pins.analog_write_pin(AnalogPin.P8, num)
    pins.digital_write_pin(DigitalPin.P12, 1)
    pins.analog_write_pin(AnalogPin.P13, num2)
    pins.digital_write_pin(DigitalPin.P14, 1)

def on_uart_data_received():
    global cmd, L_speed, MotorL_status, R_speed, MotorR_status
    cmd = bluetooth.uart_read_until(serial.delimiters(Delimiters.NEW_LINE))
    if cmd.char_at(0).compare("A") == 0:
        L_speed = parse_float(cmd.substr(1, len(cmd) - 1))
        MotorL_CW(L_speed)
        MotorL_status = 1
        basic.show_string("A")
    elif cmd.char_at(0).compare("B") == 0:
        L_speed = parse_float(cmd.substr(1, len(cmd) - 1))
        MotorL_CCW(L_speed)
        MotorL_status = 1
        basic.show_string("B")
    elif cmd.char_at(0).compare("C") == 0:
        R_speed = parse_float(cmd.substr(1, len(cmd) - 1))
        MotorR_CW(R_speed)
        MotorR_status = 1
        basic.show_string("C")
    elif cmd.char_at(0).compare("D") == 0:
        R_speed = parse_float(cmd.substr(1, len(cmd) - 1))
        MotorR_CCW(R_speed)
        MotorR_status = 1
        basic.show_string("D")
    elif cmd.compare("E") == 0:
        pins.analog_write_pin(AnalogPin.P13, 0)
        MotorL_status = 0
        basic.show_string("E")
    elif cmd.char_at(0).compare("L") == 0:
        L_speed = parse_float(cmd.substr(1, len(cmd) - 1))
        if MotorL_status == 1:
            pins.analog_write_pin(AnalogPin.P13, L_speed)
    elif cmd.char_at(0).compare("R") == 0:
        R_speed = parse_float(cmd.substr(1, len(cmd) - 1))
        if MotorR_status == 1:
            pins.analog_write_pin(AnalogPin.P8, R_speed)
    elif cmd.compare("F") == 0:
        pins.analog_write_pin(AnalogPin.P8, 0)
        MotorR_status = 0
        basic.show_string("F")
    bluetooth.uart_write_string("L-" + ("" + str(L_speed)) + "R-" + ("" + str(R_speed)))
bluetooth.on_uart_data_received(serial.delimiters(Delimiters.NEW_LINE),
    on_uart_data_received)

def MotorL_CW(num3: number):
    pins.analog_write_pin(AnalogPin.P13, num3)
    pins.analog_set_period(AnalogPin.P13, 500)
    pins.digital_write_pin(DigitalPin.P14, 1)

def on_bluetooth_connected():
    basic.show_icon(IconNames.HAPPY)
    bluetooth.start_uart_service()
    bluetooth.set_transmit_power(7)
    serial.redirect(SerialPin.P0, SerialPin.P1, BaudRate.BAUD_RATE115200)
    cuteBot.turnleft()
bluetooth.on_bluetooth_connected(on_bluetooth_connected)

def on_bluetooth_disconnected():
    basic.show_icon(IconNames.SAD)
bluetooth.on_bluetooth_disconnected(on_bluetooth_disconnected)

def MotorR_CW(num4: number):
    pins.analog_write_pin(AnalogPin.P8, num4)
    pins.analog_set_period(AnalogPin.P8, 500)
    pins.digital_write_pin(DigitalPin.P12, 1)
def MotorR_CCW(num5: number):
    pins.analog_write_pin(AnalogPin.P8, num5)
    pins.analog_set_period(AnalogPin.P8, 500)
    pins.digital_write_pin(DigitalPin.P12, 0)
def MotorL_CCW(num6: number):
    pins.analog_write_pin(AnalogPin.P13, num6)
    pins.analog_set_period(AnalogPin.P13, 500)
    pins.digital_write_pin(DigitalPin.P14, 0)
def car_Forward(num7: number, num22: number):
    pins.analog_write_pin(AnalogPin.P8, num7)
    pins.digital_write_pin(DigitalPin.P12, 1)
    pins.analog_write_pin(AnalogPin.P13, num22)
    pins.digital_write_pin(DigitalPin.P14, 1)
def car_TurnRight(num8: number, num23: number):
    pins.analog_write_pin(AnalogPin.P8, num8)
    pins.digital_write_pin(DigitalPin.P12, 1)
    pins.analog_write_pin(AnalogPin.P13, num23)
    pins.digital_write_pin(DigitalPin.P14, 1)
def car_TurnLeft(num9: number, num24: number):
    pins.analog_write_pin(AnalogPin.P8, num9)
    pins.digital_write_pin(DigitalPin.P12, 1)
    pins.analog_write_pin(AnalogPin.P13, num24)
    pins.digital_write_pin(DigitalPin.P14, 1)
def car_stop():
    pins.digital_write_pin(DigitalPin.P8, 1)
    pins.digital_write_pin(DigitalPin.P12, 1)
cmd = ""
R_speed = 0
L_speed = 0
MotorR_status = 0
MotorL_status = 0
F_status = 0
basic.show_icon(IconNames.ASLEEP)
MotorL_status = 0
MotorR_status = 0
L_speed = 700
R_speed = 700