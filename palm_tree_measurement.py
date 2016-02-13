#!/usr/bin/python3

from ABE_ADCPi import ADCPi
from ABE_helpers import ABEHelpers
import sqlite3
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

db_name = 'measurements.db'
i2c_helper = ABEHelpers()
bus = i2c_helper.get_smbus()
adc = ADCPi(bus, 0x68, 0x69, 18)

def writetodb(temperature, moisture):
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute("INSERT INTO measurements VALUES ('" + str(datetime.datetime.now()) + "','" + temperature + "','" + moisture + "')")
    conn.commit()
    conn.close()

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

    writetodb("%02f" % temp, "%02f" % moisture)
