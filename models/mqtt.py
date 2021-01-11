import paho.mqtt.client as paho
import datetime
import requests
import json

# this class extends the basic mqtt Client class from the paho module
class MyClient(paho.Client):
    # initialize the paho mqtt client on intantiating this class
    def __init__(self):
        super().__init__()

    # check a given parameter against the expected type, and return an error if not the expected type
    @staticmethod
    def __check_type(given, expected):
        return given if isinstance(given, expected) else AttributeError(f'AttributeError: Expected type {expected}, given type {type(given)}')  

    # custom on connect with basic info display
    # also subscribes to the topic, so it does not need to be done in the main.py file
    def on_connect(self, client, flags, userdata, rc):
        if rc == 0:
            print(f'''
client connected:
    result code > {rc}
    flags > {flags}
    userdata > {userdata}''')
            self.subscribe(self.__topic)
        else:
            return ConnectionError("Error: Bad connection, result code [{}]".format(rc))

    def on_disconnect(self, client, userdata, rc):
        msg = "client disconnected, result code [{}]".format(rc)
        print(msg)
        data = json.dumps({
            "message": msg,
            "date": str(datetime.datetime.now())
        })

        try:
            req = requests.post(self.__disc_end, data)
        except:
            if self.__debug:
                print(self.__disc_end, "not available")

    def check_connection(self):
        print("waiting for connection")
        while not self.is_connected():
            pass
        while self.is_connected():
            pass

    # general connect method to initialize an mqtt connection
    def connect(self, hostaddr:str, topic:str, port:int=1883, keep_alive:int=60, disconnect_endpoint:str="", debug:int=0):
        self.__debug = debug
        self.__topic = MyClient.__check_type(topic, str)
        MyClient.__check_type(hostaddr, str)
        
        try:
            MyClient.__check_type(disconnect_endpoint, str)
        except:
            disconnect_endpoint = ""
        finally:
            self.__disc_end = disconnect_endpoint    
    
        self.loop_start()
        try:
            self.connect_async(host=hostaddr, port=port, keepalive=keep_alive)
        except:
            return ConnectionError("Error: Bad connection")
        self.check_connection()
