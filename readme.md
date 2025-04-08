# Pressure-based Feedback Control System (PID) for SCARA 3D Potter 
The developed code runs a pressure-based PID controller on SCARA 3D potter, instrumented with [OMEGA LC103B-1K loadcell](https://www.farnell.com/datasheets/2849896.pdf).

## PID Controller
Under specific pressure change conditions (more than 0.3 kPa), PID controller will be triggered. The PID controller gets pressure change as the input and speed factor (change in speed) is the output. The PID coefficients and pressure change conditions for trigggering the controller are defined based on a parametric study which is available in ```pid_scara_pressure_offline_case_study``` project. The extrusion factor will be commanded to 100% in every speed command by the controller.

## Load cell Script via Python
### Connection to the load cell
```setup()``` function in ```loadcell_python.py``` is developed to get data and save data from OMEGA LC103B-1K load cell. The data is received through serial port, so the loadcell and its interface are connected through USB port.<br>
More information about the loadcell and its interface can be found here: <br>
[Loadcell](https://www.farnell.com/datasheets/2849896.pdf)<br>
[Interface](https://www.sparkfun.com/products/13261)<br>

To read from the correct serial port in this part of the code: <br>
```Python
def main():
    serialPort = 'COM3'
```
You should find the correct port from your own PC or laptop. The format of its name is different in Windows and Mac. You can find its correct value on device manager or through ports of Arduino IDE after conencting the interface to the PC or laptop.<br>
Besides using this code, you can see the data received from the interface on a terminal. There are multiple software for this, but [PuTTY](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html) is one of them.<br>

### Initial Calibration to zero
```set_to_zero()``` function in ```loadcell_python.py``` sends a interface-specific command to set the measurement in the beginning of the process to zero.

### Calibration
It has been observed that the load cell has an error in reading the data. This amount of error has been calculated by experimental testing with MTS machine and using interpolation. ```calibrate()``` function calibrates the data based on calculations in ```code_500``` and ```code_2000```.

### Reading, Parsing and Saving Data
```read_and_parse()```, ```save_data()```, and ```save_data_FE``` reads the data, parses the data with comma, and saves the data.

### Connecting to the SCARA web interface to read speed and extrusion
Speed and extrusion will be retrieved from web interface by API reading with ```webscraper_speed_extrusion.py```.

### Commanding the robot using DuetWebAPI
[DuetWebAPI](https://github.com/AndyEveritt/DuetWebAPI?tab=MIT-1-ov-file) is used to communicate with the duet board to send the speed and extrusion commands. All added files including running codes should be located in this folder along with DuetWebAPI files. 

## Main codes
```main_loadcell_woPID.py``` should run for the tests without PID as it doesn't include the PID controller and ```main_loadcell_wPID.py``` should run for the tests with PID. 


  

