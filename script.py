# Air quality monitoring with environmental sensors - testing the sensors
# Using the following libraries
#  - Adafruit_Python_BME280 by Adafruit - https://github.com/adafruit/Adafruit_Python_BME280
#  - HPMA115S0 library in Python by ThingType - https://github.com/ThingType/HPMA115S0_Python_library
# Tamas Halbrucker, 2018

from HPMA115S0_Python.HPMA115S0 import *
#from Adafruit_Python_BME280.Adafruit_BME280 import *
import time
import csv
from datetime import datetime

try:
    print("Aachen Air Quality Monitor v02 starting up...")

    #sensor = BME280(t_mode=BME280_OSAMPLE_8, p_mode=BME280_OSAMPLE_8, h_mode=BME280_OSAMPLE_8)

    hpma115S0 = HPMA115S0("/dev/ttyS0")
    with open('results.csv', mode='w') as results:
        result_writer = csv.writer(results, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        result_writer.writerow(['Date', 'Time', 'PM2.5 (ug/m3)', 'PM10 (ug/m3)'])

        hpma115S0.init()
        hpma115S0.startParticleMeasurement()

        while 1:
            two = []
            ten = []

            if (hpma115S0.readParticleMeasurement()):
                for i in range(10):
                    two.append(hpma115S0._pm2_5)
                    ten.append(hpma115S0._pm10)
                    time.sleep(0.1)
            val1 = sum(two)/len(two)
            val2 = sum(ten)/len(ten)
            result_writer.writerow([datetime.now().date(), datetime.now().time().replace(microsecond=0), val1, val2])
            print('PM2.5:{val1}')
            print('PM10:{val2}')

except KeyboardInterrupt:
    print(" Interrupt detected - Exiting.") 