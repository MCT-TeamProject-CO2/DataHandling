from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
import models.mqtt as mqtt
import configparser
import os

# this init file will load necessary global variables on startup
#region CONFIG
# load in the configuration file
config = configparser.ConfigParser()
config.read("./config/config.ini")
#endregion

#region ARGS
# general arguments
debug = os.environ.get('DEBUG', 0)
try:
    debug = 1 if debug.lower() == "true" else 0
except:
    debug = debug if isinstance(debug, int) else 0

disconnect_endpoint = config.read("endpoints", "disconnected")
#endregion 

#region MQTT
# set mqtt variables
client = mqtt.MyClient()
host_address = config.get("mqtt", "host")
topic = config.get("mqtt", "topic")
#endregion

#region INFLUXDB
# set influx database variables
token = config.get("influxdb", "token")
url = config.get("influxdb", "url")
organization = config.get("influxdb", "org")
bucket = config.get("influxdb", "bucket")
influx_client = InfluxDBClient(url=url, token=token)
write_api = influx_client.write_api(write_options=SYNCHRONOUS)
#endregion