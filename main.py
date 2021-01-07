from __init__ import *
from sys import stdout
from time import sleep
import threading
import datetime
import json

# on message function to execute when a message
# comes in on the broker


def on_message(client, userdata, msg):
    data = json.loads((msg.payload).decode('utf-8'))

# region DEBUG
# some code only for debugging, as it slows down the service a big chunk
    # now = datetime.datetime.now()
    # print(f"written data on {now.strftime('%b %d %Y %H:%M:%S')}: {str(data)}")
# endregion

    # create a data point for the influx database from the received mqtt data
    point = Point(data["Room"])\
        .field("humidity", float(data["Humidity"]))\
        .field("tvoc_ppb", float(data["tvoc_ppb"]))\
        .field("temperature", float(data["Temperature"]))\
        .field("co2eq_ppm", float(data["co2eq_ppm"]))\
        .time(data["Timestamp"], WritePrecision.NS)
    # write the data to the database
    write_api.write(bucket, organization, point)

if __name__ == "__main__":
    try:
        client.on_message = on_message
        client.connect(host_address, topic, keep_alive=5)
    except KeyboardInterrupt:
    # if manually stopped through a keyboardinterupt, give message
        print("\nManually stopped")
    except Exception as e:
        # else show error
        print(f"Error: {e}")