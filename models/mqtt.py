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
        return given if isinstance(given, expected) else AttributeError(f'AttributeError: Excpected type {expected}, given type {type(given)}')  
    
    # custom on connect with basic info display
    # also subscribes to the topic, so it does not need to be done in the main.py file
    def __on_connect(self, client, flags, userdata, rc):
        print(f'''
            client connected:
                result code > {rc}
                flags > {flags}
                userdata > {userdata}''')
        client.subscribe(self.__topic)
    
    # general connect method to initialize an mqtt connection
    def connect(self, hostaddr:str, topic:str, port:int=1883, keep_alive:int=0):
        self.__topic = MyClient.__check_type(topic, str)
        MyClient.__check_type(hostaddr, str)
        super().connect_async(host=hostaddr, port=port, keepalive=keep_alive)
        self.on_connect = self.__on_connect