from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
import models.mqtt as mqtt
import configparser


#region CONFIG
config = configparser.ConfigParser()
config.read("./config/config.ini")
#endregion

#region MQTT
client = mqtt.MyClient()
host_address = config.get("mqtt", "host")
topic = config.get("mqtt", "topic")
#endregion

#region INFLUXDB
token = config.get("influxdb", "token")
url = config.get("influxdb", "url")
organization = config.get("influxdb", "org")
bucket = config.get("influxdb", "bucket")
influx_client = InfluxDBClient(url=url, token=token)
write_api = influx_client.write_api(write_options=SYNCHRONOUS)
#endregion