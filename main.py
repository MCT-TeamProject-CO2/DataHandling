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
    point = Point(data["Room"])\
        .field("humidity", float(data["Humidity"]))\
        .field("tvoc_ppb", float(data["tvoc_ppb"]))\
        .field("temperature", float(data["Temperature"]))\
        .field("co2eq_ppm", float(data["co2eq_ppm"]))\
        .time(data["Timestamp"], WritePrecision.NS)
    # write the data to the database

    try:
        write_api.write(bucket, organization, point)
        if debug:
            print(f"{colorama.Fore.BLUE}[STATUS]{colorama.Fore.RESET} written data on {now.strftime('%b %d %Y %H:%M:%S')}: {str(data)}")

    except Exception as e:
        if debug:
            print(f"{colorama.Fore.YELLOW}[ALERT]{colorama.Fore.RESET} can't write to influxdb, reason:", (json.loads(e.body))["message"])

if __name__ == "__main__":
    try:
        print(f"DEBUG MODE [{colorama.Fore.GREEN}{'ON' if debug == 1 else 'OFF'}{colorama.Fore.RESET}]")
        client.on_message = on_message
        client.connect(host_address, topic, debug=debug, keep_alive=5, disconnect_endpoint=disconnect_endpoint)
    except KeyboardInterrupt:
    # if manually stopped through a keyboardinterupt, give message
        print(f"\n{colorama.Fore.YELLOW}[ALERT]{colorama.Fore.RESET} Manually stopped")
    except Exception as e:
        # else show error
        print(f"{colorama.Fore.RED}[Error]{colorama.Fore.RESET} {e}")
