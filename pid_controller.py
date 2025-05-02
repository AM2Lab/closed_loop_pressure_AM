import numpy as np

"""
This code is developed by Mahsa Rabiei (mrabiei@princeton.edu) for a PID control system.
"""

def pid_control(pressure_first, pressure_next, deltaP, deltaP_sum, previous_extrusion):
    """
    A PID controller

    Returns:
        float, float: speed and extrusion factor
    """

    print("LOG: pid_control: pressure_1st={}, pressure_2={}, deltap={}, deltapsum={}, prev_ext={}".format(pressure_first, pressure_next, deltaP, deltaP_sum, previous_extrusion
                                                                                           ))
    kp = 0.5                           
    kd = 0.2
    ki = 0


    speed_factor = kp * ((pressure_next - pressure_first) - 0) + ki * \
        deltaP_sum + kd * (((pressure_next - pressure_first) - deltaP) / (1))

    if speed_factor == 1 or speed_factor > 1:
        speed_factor = 1 + speed_factor
        extrusion_factor = 1 
    else:
        speed_factor = 1
        extrusion_factor = 1

    print("LOG: control returns speed_factor={}, extrusion_factor={}".format(
        speed_factor, extrusion_factor))
    return speed_factor, extrusion_factor
