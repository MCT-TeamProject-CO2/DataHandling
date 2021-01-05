from __init__ import *
from sys import stdout
from time import sleep
import threading
import datetime
import json

def on_message(client, userdata, msg):
    data = json.loads((msg.payload).decode('utf-8'))

#region DEBUG
    # now = datetime.datetime.now()
    # print(f"written data on {now.strftime('%b %d %Y %H:%M:%S')}: {str(data)}")
#endregion

    point = Point(data["Room"])\
        .field("humidity", float(data["Humidity"]))\
        .field("tvoc_ppb", float(data["tvoc_ppb"]))\
        .field("temperature", float(data["Temperature"]))\
        .field("co2eq_ppm", float(data["co2eq_ppm"]))\
        .time(data["Timestamp"], WritePrecision.NS)
    write_api.write(bucket, organization, point)

if __name__ == "__main__":
    try:
        client.on_message = on_message
        client.connect(host_address, topic, keep_alive=60)
        client.loop_forever(timeout=0.5)
    except KeyboardInterrupt:
        print("\nManually stopped")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        client.disconnect()