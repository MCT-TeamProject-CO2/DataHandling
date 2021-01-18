from __init__ import *
import datetime
import json
import colorama

# on message function to execute when a message
# comes in on the broker


def on_message(client, userdata, msg):
    data = json.loads((msg.payload).decode('utf-8'))

    if debug:
        now = datetime.datetime.now()

    # create a data point for the influx database from the received mqtt data
    point = Point(data["Room"])
    for key in data.keys():
        if (key.lower() != "room") and (key.lower() != "timestamp"):
            point = point.field(str(key).lower(), float(data[key]))
    point.time(data["Timestamp"], WritePrecision.NS)
    
    # write the data to the database
    try:
        write_api.write(bucket, organization, point)
        if debug:
            print(f"{colorama.Fore.BLUE}[STATUS]{colorama.Fore.RESET} written data on {now.strftime('%b %d %Y %H:%M:%S')}UTC: {str(data)}")

    except Exception as e:
        if debug:
            print(f"[{datetime.datetime.now()}UTC]: {colorama.Fore.YELLOW}[ALERT]{colorama.Fore.RESET} can't write to influxdb, reason:", (json.loads(e.body))["message"])

if __name__ == "__main__":
    try:
        print(f"\nDEBUG MODE [{colorama.Fore.GREEN}{'ON' if debug == 1 else 'OFF'}{colorama.Fore.RESET}]")
        client.on_message = on_message
        client.connect(host_address, topic, debug_mode=debug, keep_alive=5, disconnect_endpoint=disconnect_endpoint)
    except KeyboardInterrupt:
    # if manually stopped through a keyboardinterupt, give message
        print(f"\n[{datetime.datetime.now()}UTC]: {colorama.Fore.YELLOW}[ALERT]{colorama.Fore.RESET} Manually stopped")
    except Exception as e:
        # else show error
        print(f"[{datetime.datetime.now()}UTC]: {colorama.Fore.RED}[Error]{colorama.Fore.RESET} {e}")
