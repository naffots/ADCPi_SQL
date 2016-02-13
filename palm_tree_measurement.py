#!/usr/bin/python3

from ABE_ADCPi import ADCPi
from ABE_helpers import ABEHelpers
import datetime
import time

"""
================================================
ABElectronics ADC Pi 8-Channel ADC data-logger demo
Version 1.0 Created 29/02/2015

Requires python 3 smbus to be installed
run with: python3 demo-read_voltage.py
================================================

Initialise the ADC device using the default addresses and sample rate, change
this value if you have changed the address selection jumpers

Sample rate can be 12,14, 16 or 18
"""


i2c_helper = ABEHelpers()
bus = i2c_helper.get_smbus()
adc = ADCPi(bus, 0x68, 0x69, 18)


def writetofile(filename, texttowrtite):
    f = open(filename, 'a')
    f.write(str(datetime.datetime.now()) + ";" + texttowrtite)
    f.closed

while (True):
    temp = 0
    moisture = 0

    for x in range(0, 60):
        # read from adc channels and write to the log file
        temp = temp + (adc.read_voltage(1) - 0.5) * 100
        moisture = moisture + adc.read_voltage(2)
        time.sleep(1)

    temp = temp / 60
    moisture =  moisture / 60

    writetofile('temp.csv', "%02f\n" % temp)
    writetofile('moisture.csv', "%02f\n" % moisture)
