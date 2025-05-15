# Pressure-based Closed-Loop Control for Extrusion-based Additive Manufacturing 
The developed code runs a pressure-based PID controller on SCARA 3D potter. Please note that only the main parts of the code are provided.

## PID Controller
Under specific pressure change conditions (more than 0.3 kPa), PID controller will be triggered. The PID controller gets pressure change as the input and speed factor (change in speed) is the output. 

## Load cell Script via Python
### Connection to the load cell
```setup()``` function in ```loadcell_python.py``` is developed to get data and save data from an OMEGA LC103B-1K loadcell. The data is received through serial port, so the loadcell and its interface are connected through USB port.<br>
More information about the loadcell and its interface can be found here: <br>
[Loadcell](https://www.farnell.com/datasheets/2849896.pdf)<br>
[Interface](https://www.sparkfun.com/products/13261)<br>

To read from the serial port: <br>
```Python
def main():
    serialPort = 'COM3'
```
You should find the correct port from your own PC or laptop. The format of its name is different in Windows and Mac. You can find its correct name in device manager.<br>
Besides using this code, you can see the data received from the interface on a terminal. There are multiple software for this, but [PuTTY](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html) is one of them.<br>

### Initial Calibration to zero
```set_to_zero()``` function in ```loadcell_python.py``` sends a interface-specific command to set the measurement in the beginning of the process to zero.

### Reading, Parsing and Saving Data
```read_and_parse()```, ```save_data()```, and ```save_data_FE``` reads the data, parses the data with comma, and saves the data.

### Connecting to the SCARA web interface to read speed and extrusion
Speed and extrusion will be retrieved from web interface by API reading with ```webscraper_speed_extrusion.py```.

### Commanding the robot using DuetWebAPI
[DuetWebAPI](https://github.com/AndyEveritt/DuetWebAPI?tab=MIT-1-ov-file) is used to communicate with the duet board to send the speed and extrusion commands. All added files including running codes should be located in this folder along with DuetWebAPI files. 

## Data Acquisition with LJX8200 Keyence Laser Profiler with LJX8002 Controller through Ethernet (TCP/IP) in Python
The following Python code is developed to receive and save data from Keyence [LJX8200](https://www.keyence.com/products/measure/laser-2d/lj-x8000/models/lj-x8200/) Laser Profiler with [LJX8002](https://www.keyence.com/products/measure/laser-2d/lj-x8000/models/lj-x8002/) controller. The communication is through TCP/IP (Ethernet). ```laser_reading.py``` is the main code to run the laser profiler to get the data of geometry after the process (offline). <br>

## How to set up the system?
### Hardware
The laser head is connected to the controller and the controller is connected to the power supply. An ethernet cable and a USB cable should be connected to the PC/laptop and the controller at the same time. <br>
### Software
Then, we can start working in the Keyence Terminal software. We select USB as the connection, we press connect and then launch remote desktop.<br> We should first set the head and its sensitivity to middle level. Then, we set the measurement tools. We have used width and height difference in this project. Then, we set the position adjustment by selecting the edge as x-adjustment (selecting the option of bidirectional) and the peak as z-adjustment (selecting the option of peak). Remember to register the current profile in position adjustment before setting up x and z. <br>
### IP Setting
You should set IP in both Terminal software and your PC. <br>
In the software, go to Global, Communication I/O, Network. In network, set the IP as 192.168.10.11. Then, go to control panel, network and sharing center, change adapter setting. Click right on Ethernet, click on properties, Internet protocol version 4, and click on properties. Enter the IP as 192.168.10.1 (If you already see an IP, write it down, just in case). Click on OK.
### Output Setting
In the setup mode, on top right, you can see the output option. In Ethernet (non-procedural), select the variables you want to see, and go to run mode. <br>
Now, you should run the laser_reading.py to see the received data. <br>
If you get ethernet connection error on the software, don't worry! The reason is you haven't run the code yet and one part of the communication is missing. Run the code in Python, close the error on the software, and it would be resolved.<br>
If you go to Utility on top right of the software, you can see the data through Ethernet monitor as well. <br>
You can also use [TeraTerm](https://teratermproject.github.io/index-en.html) to monitor the data through IP and port number.<br>
### TCP/IP
Reading through TCP/IP needs [socket_programming](https://www.datacamp.com/tutorial/a-complete-guide-to-socket-programming-in-python), and an IP and a port number. The IP number is the IP that you have set on the Terminal software. The port number should be 8500 (given in the controller manual). <br>
Through these lines of code, we can set up the socket and we request to get data:<br>
```client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)``` <br>
```client.connect((server_ip, port))``` <br>
```msg = "T1"```<br>
```client.send(msg.encode("utf-8")[:1024])```<br>
```response = client.recv(1024)```<br>
```response = response.decode("utf-8")```<br>
The message that is sent to the server to get data is set to T1 as T1 command in the controller requests the output data that was set in the software.<br>

## Main codes
```main_loadcell_woPID.py``` is developed for the tests without PID, as it doesn't include the PID controller, and ```main_loadcell_wPID.py``` is developed for the tests with PID. 


  

