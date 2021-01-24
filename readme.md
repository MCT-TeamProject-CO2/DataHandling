# Setup

## step 1

Download or clone the repository to your system. **`Also, make sure docker and docker-compose are installed and functional`**.

Note that you might also need to use a VPN proxy to connect to the network where the MQTT-broker is located. If so, make sure the VPN is installed and functional.

## step 2

Within the [config](https://github.com/MCT-TeamProject-CO2/DataHandling/tree/master/config) folder there is a file named [config.ini.example](https://github.com/MCT-TeamProject-CO2/DataHandling/blob/master/config/config.ini.example). remove the `.example` extension and edit the file in your text editor of choice.

The config file will have some placholder text. These parameters need to be configured as following:

**`[influxdb]`**

- `token` = the access token to the influxdb database
- `url` = the hostname or ip needed to connect to influxdb
- `org` = the organization on influx that the bucket belongs to
- `bucket` = the bucket (= database table) that will hold the datmeasurements

**`[mqtt]`**

- `topic` = the topic to subscribe to on the mqtt broker
- `host`= host- or ip-address of the mqtt broker on the network

**`[endpoints]`**

- `disconnected` = [the API endpoint](https://github.com/MCT-TeamProject-CO2/Node-Server/blob/main/api/v1/mqtt_disconnect.js) to send a message to when the client gets disconnected which should be supplied with the [Node server](https://github.com/MCT-TeamProject-CO2/Node-Server)

## step 3

Within the repository there are some docker files included. In a command terminal navigate to the repository folder and type the following command:

```
docker-compose up
```

Additionally you can add the `-d` parameter to the `docker-compose` command to run it in the background.

```
docker compose up -d
```

You can check if the container is running with 
```
docker ps
```
Or to see all existing containers:
```
docker ps -a
```

to stop the container, you can use 
```
docker stop <container name/ID>
```

Or whilst in the [Datahandling](https://github.com/MCT-TeamProject-CO2/DataHandling/tree/master/) folder
```
docker-compose stop
```