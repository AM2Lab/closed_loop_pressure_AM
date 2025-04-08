from duetwebapi import DuetWebAPI as DWA
import webscraper_speed_extrusion as wse

"""
To  test how to send extrusion and speed command to SCARA through duet board
"""
print("initial:", wse.get_speed_extrusion())
print("initial:", wse.get_speed_extrusion())
print("initial:", wse.get_speed_extrusion())

printer = DWA('http://Scara')
speed_factor = 2
printer.send_code("M220 S{}".format(speed_factor * 100.0))  # speed
print("after changing factor to 2", wse.get_speed_extrusion())

printer = DWA('http://Scara')
speed_factor = 2
printer.send_code("M220 S{}".format(speed_factor * 100.0))  # speed
print("after changing factor to 2", wse.get_speed_extrusion())

speed_factor = 2
printer.send_code("M220 S{}".format(speed_factor * 100.0))  # speed
print("after changing factor to 2", wse.get_speed_extrusion())

speed_factor = 4
printer.send_code("M220 S{}".format(speed_factor * 100.0))  # speed
print("after changing factor to 4", wse.get_speed_extrusion())

speed_factor = 4
printer.send_code("M220 S{}".format(speed_factor * 100.0))  # speed
print("after changing factor to 4", wse.get_speed_extrusion())

speed_factor = 5
printer.send_code("M220 S{}".format(speed_factor * 100.0))  # speed
print("after changing factor to 5", wse.get_speed_extrusion())

speed_factor = 5
printer.send_code("M220 S{}".format(speed_factor * 100.0))  # speed
print("after changing factor to 5", wse.get_speed_extrusion())

speed_factor = 1
printer.send_code("M220 S{}".format(speed_factor * 100.0))  # speed
print("after changing factor to 1", wse.get_speed_extrusion())

