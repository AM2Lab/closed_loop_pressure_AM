import socket
from datetime import date
import time

"""
This code is developed by Mahsa Rabiei (mrabiei@princeton.edu) to read the geometry data from a LJX8200 laser profiler.
"""

# Ethernet Setup
server_ip = '192.168.10.11'
port = 8500
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((server_ip, port))

# Path to the saved file
today = date.today()
now = time.localtime()
path = 'laserProfiler_data_' + str(
    today) + '_' + str(time.strftime("%H-%M-%S", now)) + '.txt'
file = open(path, 'w')

# Setting up a timer 
t_start = time.time()

# Checking if we are receiving float values, not error or set up strings
def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False


while True:

    # Sending T1 message to receive data
    msg = "T1"
    client.send(msg.encode("utf-8")[:1024])

    # Receiving data
    response = client.recv(1024)
    response = response.decode("utf-8")
    if response.lower() == "closed":
        break
    response = str(response)
    response_str = response.split(',')

    # Time lapse (end of timer)
    t_end = time.time() - t_start

    # Parsing data
    if response_str[0] == 'ER' or 'T1' in response_str[1] or isfloat(response_str[1]) == False:
        continue
    width = float(response_str[0])
    height = float(response_str[1])

    # Storing the data in a file
    file.write("width:{}, height: {}, t: {}".format(width, height, t_end))
    file.write("width:{}, height:{}, time:{}".format(width, height, t_end))
    file.write('\n')

    print(width, height, t_end)


client.close()
print("Connection to server closed")



