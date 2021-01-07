import paho.mqtt.client as paho
import threading

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
            raise ConnectionError("Error: Bad connection, result code [{}]".format(rc))
    
    def on_disconnect(self, client, userdata, rc):
        print("client disconnected, result code [{}]".format(rc))
    
    def check_connection(self):
        i = 0
        while not self.is_connected():
            if i == 0:
                print("waiting for connection")
                i = 1

        while self.is_connected():
            pass
    
    # general connect method to initialize an mqtt connection
    def connect(self, hostaddr:str, topic:str, port:int=1883, keep_alive:int=60):
        self.__topic = MyClient.__check_type(topic, str)
        MyClient.__check_type(hostaddr, str)
        self.loop_start()
        try:
            self.connect_async(host=hostaddr, port=port, keepalive=keep_alive)
        except:
            raise ConnectionError("Error: Bad connection")
        self.check_connection()