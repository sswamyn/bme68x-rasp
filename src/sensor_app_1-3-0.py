from bme68x import BME68X
import bme68xConstants as cst
import bsecConstants as bsec
from time import sleep
from pathlib import Path

# https://github.com/mcalisterkm/p-sensors/blob/master/src/1.3.0/sensor_app_1-3-0.py 

temp_prof = [320, 100, 100, 100, 200, 200, 200, 320, 320, 320]
dur_prof =[5, 2, 10, 30, 5, 5, 5, 5, 5, 5]

state_file_name = "state_data1644485092616.txt"

