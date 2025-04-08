from urllib.request import urlopen
import json
import math
import numpy as np


def get_speed_extrusion():
    url = "http://192.168.1.14/rr_model?flags=d99fn"
    page = urlopen(url)
    html_bytes = page.read()
    html = html_bytes.decode("utf-8")
    html_json = json.loads(html)
    speed = html_json["result"]["move"]["currentMove"]["requestedSpeed"]
    Ex = html_json["result"]["move"]["extruders"][0]["position"]

    return speed, Ex
