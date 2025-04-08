from datetime import date
import time
import loadcell_python as lc
import webscraper_speed_extrusion as FE
import pid_controller as pid
from duetwebapi import DuetWebAPI as DWA
import numpy as np

"""
Main test without PID
"""

def loadcell_main():
    # Initial setup
    printer = DWA('http://Scara')
    handle, file, file_t, file_FE = lc.setup()
    lc.set_to_zero(handle)
    i = 0
    pressure_list = []
    time_list = []
    deltaP_list = []
    print("LOG INFO: INITIAL SETUP DONE")
    # Main loop that executes PID control
    while True:

        if i == 0:
            # Getting pressure data
            pressure, t = lc.read_and_parse(handle)
            # Saving pressure data
            t = t / 1000  # ms to s
            pressure = lc.calibrate(pressure * 4.4482216153)  # kpa
            lc.save_data(file, file_t, pressure, t)
            pressure_list.append(pressure)
            time_list.append(t)
            deltaP_list.append(0)
            i = i + 1
            print("LOG INFO: FIRST PRESSURE DATA READING")
            continue
        # Getting pressure data
        pressure, t = lc.read_and_parse(handle)
        # Saving pressure data
        t = t / 1000
        pressure = lc.calibrate(pressure * 4.4482216153)  # to newtons
        lc.save_data(file, file_t, pressure, t)
        pressure_list.append(pressure)
        time_list.append(t)
        deltaP_list.append(pressure_list[i] - pressure_list[i-1])
        deltaP_sum = np.sum(deltaP_list)
        print("LOG INFO: ANOTHER PRESSURE READING")
        

        # Get the speed and extrusion rate to plot
        speed, extrusion = FE.get_speed_extrusion()
        # Time may change considerably between loadcell measurement and PID, so we measure the time again
        _, t = lc.read_and_parse(handle)
        # Saving the speed and extrusion data
        lc.save_data_FE(file_FE, speed, extrusion, t)      

        i = i + 1


loadcell_main()  # uncomment it and run this code when you don't have a laser on board
