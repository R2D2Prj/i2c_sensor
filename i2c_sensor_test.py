#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from ina226 import INA226

class TestSequenceFunctions(unittest.TestCase):
    def setUp(self):
        self.tester = INA226(False)

    # 電圧値取得チェック
    def test_ina226_get_voltage(self):
        __v = self.tester.get_voltage()
        print "Voltage:%2.2f" % __v
        self.assertTrue(4.0 <= __v <= 13.0)

    # 電流値取得チェック
    def test_ina226_get_current(self):
        __i = self.tester.get_current()
        print "Current:%2.2f" % __i
        self.assertTrue(0.1 <= __i <= 0.5)

    # 電力値の取得チェック
    def test_ina226_get_power(self):
        __w = self.tester.get_power()
        print "Power:%2.2f" % __w
        self.assertTrue(0.3 <= __w <= 5)

if __name__ == '__main__':
    unittest.main()