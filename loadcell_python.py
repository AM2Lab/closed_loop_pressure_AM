import serial
from datetime import date
import time

"""
This code is developed by Mahsa Rabiei (mrabiei@princeton.edu) to read and parse data from an OMEGA LC103B-1K loadcell.
"""

def setup():
    """
    Setting up the serial connection between the load cell and PC, and setting up file paths.

    Returns:
        data_handle: Serial connection instance
        file, file_t, file_FE: Files to save data
    """

    serialPort = 'COM3'
    baudRate = 9600
    data_handle = serial.Serial(serialPort, baudRate)
    today = date.today()
    now = time.localtime()
    path = 'loadcell_data_' + str(
        today) + '_' + str(time.strftime("%H-%M-%S", now)) + '.txt'
    file = open(path, 'w')
    path_t = 'loadcell_time_' + str(
        today) + '_' + str(time.strftime("%H-%M-%S", now)) + '.txt'
    file_t = open(path_t, 'w')
    path_FE = 'speed_extrusion_' + str(
        today) + '_' + str(time.strftime("%H-%M-%S", now)) + '.txt'
    file_FE = open(path_FE, 'w')
    return data_handle, file, file_t, file_FE


def set_to_zero(data_handle):
    """
    Sending interface-specific commands to set the initial measurement to zero.
    """

    data_handle.write('x'.encode())
    data_handle.write('1'.encode())
    data_handle.write('x'.encode())

def read_and_parse(data_handle):
    """
    Reading and parsing pressure and time data.
    """

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
    """
    Saving the pressure and time data.
    """

    file.write(str(pressure))
    file.write('\n')
    file_t.write(str(time))
    file_t.write('\n')


def save_data_FE(file_FE, F, E, t):
    """
    Saving the speed, extrusion, and time data.
    """

    file_FE.write('speed: {}, extrusion factor: {}, time: {}'.format(F, E, t))
    file_FE.write('\n')

