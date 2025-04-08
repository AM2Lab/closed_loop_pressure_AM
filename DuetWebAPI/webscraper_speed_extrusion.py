from urllib.request import urlopen
import json

"""
This code is an API reader that retrieves speed and extrusion data from a web interface.
"""

def get_speed_extrusion():
    """
    Reading speed and extrusion from a web interface.

    Returns:
        Tuple[float, float]: speed and extrusion values.
    """
    
    url = "http://192.168.1.14/rr_model?flags=d99fn"
    page = urlopen(url)
    html_bytes = page.read()
    html = html_bytes.decode("utf-8")
    html_json = json.loads(html)
    speed = html_json["result"]["move"]["currentMove"]["requestedSpeed"]
    Ex = html_json["result"]["move"]["extruders"][0]["position"]

    return speed, Ex
