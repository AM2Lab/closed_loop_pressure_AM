import serial
from datetime import date
import time
import code_500 as s_500
import code_2000 as s_2000
import numpy as np

"""
Required functions for reading pressure from the load cell and data calibration
"""

def setup():
    serialPort = 'COM3'
    baudRate = 9600
    data_handle = serial.Serial(serialPort, baudRate)
    today = date.today()
    now = time.localtime()
    path = 'C:/Users/LabUser/Desktop/loadcell_data_' + str(
        today) + '_' + str(time.strftime("%H-%M-%S", now)) + '.txt'
    file = open(path, 'w')
    path_t = 'C:/Users/LabUser/Desktop/loadcell_time_' + str(
        today) + '_' + str(time.strftime("%H-%M-%S", now)) + '.txt'
    file_t = open(path_t, 'w')
    path_FE = 'C:/Users/LabUser/Desktop/speed_extrusion_' + str(
        today) + '_' + str(time.strftime("%H-%M-%S", now)) + '.txt'
    file_FE = open(path_FE, 'w')
    return data_handle, file, file_t, file_FE


def set_to_zero(data_handle):
    # data_handle = setup()
    data_handle.write('x'.encode())
    data_handle.write('1'.encode())
    data_handle.write('x'.encode())


def calibrate(data):
    d = 92 / 1000
    slope_500 = s_500.slope_reader()
    slope_2000 = s_2000.slope_reader()
    slope_average = (slope_500[0] + slope_500[1] + slope_500[2] +
                     slope_2000[0] + slope_2000[1] + slope_2000[2]) / 6

    intercept_500 = s_500.intercept_reader()
    intercept_2000 = s_2000.intercept_reader()
    intercept_average = (intercept_500[0] + intercept_500[1] + intercept_500[2] +
                         intercept_2000[0] + intercept_2000[1] + intercept_2000[2]) / 6
    error_test = slope_average * data + intercept_average
    lc_corrected = data - error_test
    lc_data_final = (lc_corrected / (np.pi * (d ** 2) / 4)) / 1000
    return lc_data_final


def read_and_parse(data_handle):
    # data_handle = setup()
    while True:
        line = data_handle.readline()
        line_sec = line.strip().split(b',')
        if len(line_sec) > 1:
            try:
                pressure = float(line_sec[1])
                time = float(line_sec[0])
                return pressure, time
            except:
                pass


def save_data(file, file_t, pressure, time):
    # data_handle = setup()

    # while True:
    # line = data_handle.readline()
    # line_sec = line.strip().split(b',')
    # data_loadcell = float(line_sec[1])
    file.write(str(pressure))
    file.write('\n')
    file_t.write(str(time))
    file_t.write('\n')


def save_data_FE(file_FE, F, E, t):
    # data_handle = setup()

    # while True:
    # line = data_handle.readline()
    # line_sec = line.strip().split(b',')
    # data_loadcell = float(line_sec[1])
    file_FE.write('speed: {}, extrusion factor: {}, time: {}'.format(F, E, t))
    file_FE.write('\n')


# def loadcell_main():
#     handle, file, file_t = setup()
#     set_to_zero(handle)
#     while True:
#         pressure, time = read_and_parse(handle)
#         save_data(file, file_t, pressure, time)


# def save_data_pid(file, pressure, state):
#     file.write(str(pressure))
#     file.write('\n')
#     state[0] = state[1]
#     state[1] = pressure


# def loadcell_main_pid(state, q):
#     handle, file = setup()
#     set_to_zero(handle)
#     while True:
#         pressure = read_and_parse()
#         save_data_pid(file, pressure, state)
