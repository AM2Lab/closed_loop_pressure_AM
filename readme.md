# Pressure-based Closed-Loop Control for Extrusion-based Additive Manufacturing 
This code is developed to run a pressure-based PID controller on the SCARA 3D potter. Please note that only the main parts of the code are provided.

## PID Controller
Under specific pressure change conditions (more than 0.3 kPa), PID controller is triggered. Pressure change is the input of the controller and speed factor (change in speed) is the output of the controller. 

## Load cell Script via Python
### Connection to the Load cell
```setup()``` function in ```loadcell_python.py``` is developed to read and save data from an OMEGA LC103B-1K loadcell. The data is received through serial port.<br>
More information about the loadcell and its interface can be found here: <br>
[Loadcell](https://www.farnell.com/datasheets/2849896.pdf)<br>
[Interface](https://www.sparkfun.com/products/13261)<br>

To read from the serial port: <br>
```Python
def main():
    serialPort = 'COM3'
```
The correct port can be found in the device manager of the PC. The format of the port's name is different in Windows and Mac.<br>
Besides using this code, the received data can be read on a terminal. There are multiple software for this, but [PuTTY](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html) is one of them.<br>

### Initial Calibration to Zero
```set_to_zero()``` function in ```loadcell_python.py``` sends a interface-specific command to set the measurement in the beginning of the process to zero.

### Reading, Parsing and Saving Data
```read_and_parse()```, ```save_data()```, and ```save_data_FE``` reads the data, parses the data with comma, and saves the data.

### Connecting to the SCARA Web Interface to Read the Speed and Extrusion Values
Speed and extrusion values are retrieved from web interface by API reading as developed in  ```webscraper_speed_extrusion.py```.

### Commanding the Robot using DuetWebAPI
[DuetWebAPI](https://github.com/AndyEveritt/DuetWebAPI?tab=MIT-1-ov-file) is used to communicate with the duet board to send the speed and extrusion commands. All added files including main operating codes should be located in this folder along with main DuetWebAPI files. 

## Data Acquisition with LJX8200 Keyence Laser Profiler and LJX8002 Controller through Ethernet (TCP/IP) in Python
A Python code is developed to receive and save data from Keyence [LJX8200](https://www.keyence.com/products/measure/laser-2d/lj-x8000/models/lj-x8200/) Laser Profiler with [LJX8002](https://www.keyence.com/products/measure/laser-2d/lj-x8000/models/lj-x8002/) controller. The communication is through TCP/IP (Ethernet). ```laser_reading.py``` is the main code to run the laser profiler to get the data of geometry (width and height of the filaments) after the process (offline). <br>

## How to set up the system?
### Hardware
The laser head is connected to the controller and the controller is connected to the power supply. An ethernet cable and a USB cable should be connected to the PC/laptop and the controller at the same time. <br>
### Software
USB should be selected as the main connection type in the Keyence terminal software (available to download on the [Keyence website](https://www.keyence.com/)). Then, connect and then launch remote desktop buttons should be selected.<br> First, specifications of the laser head and its sensitivity should be set. In this project, sensitivity level is selected to be middle level. Then, measurement tools (the specifications that we would like to measure) should be selected. Width and height difference tools are utilized in this project. The position adjustment should also be activated to track the filament in case of deviations from a straight line. This can be applied by selecting the edge as x-adjustment (selecting the option of bidirectional) and the peak as z-adjustment (selecting the option of peak). It should be noted that registering the current profile in position adjustment should be done before setting up x and z. <br>
### IP Setting
IP should be set in both Keyence terminal software and PC. <br>
In the software, IP can be set in Global/Communication I/O/Network. In network, the IP can be set as 192.168.10.11. Then, the IP of the PC should be set in control panel/network and sharing center/change adapter setting. After right clicking on Ethernet, and selecting properties/Internet protocol version 4/properties, IP should be entered as 192.168.10.1.<br>
### Output Setting
In the Keyence terminal software and in the setup mode on top right, the output option should be selected as Ethernet (non-procedural). Then, the output variables can be selected to be shown. <br>
After entering the run mode on the Keyence terminal software, laser_reading.py should run to see the received data on the Python IDE's terminal. <br>
If any ethernet connection error on the software is shown, the reason can be the Python code not running (missing one part of the communication). <br>
[TeraTerm](https://teratermproject.github.io/index-en.html) can also be used to monitor the data through IP and port number.<br>
### TCP/IP
Reading through TCP/IP needs [socket_programming](https://www.datacamp.com/tutorial/a-complete-guide-to-socket-programming-in-python), and an IP and a port number. The IP number is the IP set on the Terminal software. The port number should be 8500 (given in the controller's available documentation). <br>
Through these lines of code, the socket can be setup to read the data:<br>
```client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)``` <br>
```client.connect((server_ip, port))``` <br>
```msg = "T1"```<br>
```client.send(msg.encode("utf-8")[:1024])```<br>
```response = client.recv(1024)```<br>
```response = response.decode("utf-8")```<br>
The message that is sent to the server to get data is set to T1 as T1 command in the controller requests the output data (based on the available documentation).<br>

## Main codes
```main_loadcell_woPID.py``` is developed for the tests without PID controller running (reading data from the Load cell only), and ```main_loadcell_wPID.py``` is developed for the tests with the PID controller. 


  

