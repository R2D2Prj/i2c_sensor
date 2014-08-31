#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lib.Adafruit_I2C import Adafruit_I2C

# ==================================================
# =   INA226 Class                                 =
# =   I2C PowerMeasure Module from StrawberryLinux =
# ==================================================

class INA226(Adafruit_I2C):
    # Constructor
    def __init__(self, debug=False, adr=0x40, bus=1):
        Adafruit_I2C.__init__(self, adr, bus, debug)
        # シャント抵抗値をセット 0.002Ω
        Adafruit_I2C.writeList(self, 0x05, [0x0a, 0x00])

    def get_voltage(self):
        __raw_data = Adafruit_I2C.readU16(self, 0x02, False)
        return __raw_data * 1.25 / 1000.0

    def get_current(self):
        __raw_data = Adafruit_I2C.readU16(self, 0x04, False)
        return __raw_data / 1000.0

    def get_power(self):
        __raw_data = Adafruit_I2C.readU16(self, 0x03, False)
        return __raw_data * 0.025