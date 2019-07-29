# Air quality monitoring with environmental sensors - testing the sensors
# Using the following libraries
#  - Adafruit_Python_BME280 by Adafruit - https://github.com/adafruit/Adafruit_Python_BME280
#  - HPMA115S0 library in Python by ThingType - https://github.com/ThingType/HPMA115S0_Python_library
# Tamas Halbrucker, 2018

from HPMA115S0_Python.HPMA115S0 import *
import time
import csv
import os.path
from datetime import datetime

try:
    print("Aachen Air Quality Monitor v02 starting up...")

    #sensor = BME280(t_mode=BME280_OSAMPLE_8, p_mode=BME280_OSAMPLE_8, h_mode=BME280_OSAMPLE_8)

    hpma115S0 = HPMA115S0("/dev/ttyS0")
    file_exists = os.path.isfile('results.csv')
    with open('results.csv', mode='a') as results:
        headers = ['Date', 'Time', 'PM2.5 (ug/m3)', 'PM10 (ug/m3)']
        result_writer = csv.DictWriter(results, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL, fieldnames=headers)
        if not file_exists:
            result_writer.write_header()
            
        hpma115S0.init() # Initialize HPMA
        hpma115S0.startParticleMeasurement() # Starts measurement

        while 1:
            two = [] # PM 2.5 Array
            ten = [] # PM 10 Array
            i = 0
            while i < 60: # One every 60 seconds
                if (hpma115S0.readParticleMeasurement()):
                    #print(hpma115S0._pm2_5)
                    two.append(hpma115S0._pm2_5) # PM 2.5 Measurement
                    ten.append(hpma115S0._pm10) # PM 10 Measurement
                    print(i)
                    i += 1
                    time.sleep(1) # Sleep 1 second
            val1 = sum(two)/len(two) # Take the average PM 2.5 over that minute
            val2 = sum(ten)/len(ten) # Take the average PM 10 over that minute
            print(val1, val2)
            result_writer.writerow([{'Date': datetime.now().date(), 'Time' : datetime.now().time().replace(microsecond=0), 
                                     'PM2.5 (ug/m3)': val1, 'PM10 (ug/m3)' : val2])
            # Write to csv
            print('Wrote to csv')
except KeyboardInterrupt:
    print(" Interrupt detected - Exiting.") 
