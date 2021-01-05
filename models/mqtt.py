import paho.mqtt.client as paho
import threading

class MyClient(paho.Client):
    def __init__(self):
        super().__init__()
    
    @staticmethod
    def __check_type(given, expected):
        return given if isinstance(given, expected) else AttributeError(f'AttributeError: Excpected type {expected}, given type {type(given)}')  
    
    def __on_connect(self, client, flags, userdata, rc):
        print(f'''
client connected:
    result code > {rc}
    flags > {flags}
    userdata > {userdata}''')
        client.subscribe(self.__topic)
    
    def connect(self, hostaddr:str, topic:str, port:int=1883, keep_alive:int=0):
        self.__topic = MyClient.__check_type(topic, str)
        MyClient.__check_type(hostaddr, str)
        super().connect_async(host=hostaddr, port=port, keepalive=keep_alive)
        self.on_connect = self.__on_connect