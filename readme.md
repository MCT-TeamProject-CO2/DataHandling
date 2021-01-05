# Setup

## step 1

download or clone the repository to your system. And **make sure docker is installed**.

you might also need to connect to the howest network through the recommended proxy/vpn to access the mqtt broker, unless you are directly connected on the network of course.

## step 2

in the `config` folder there is a file called `config.ini.example`. remove the `.example` extension and edit the file in your text editor of choice.

the config file will have some placholder text, this needs to be filled in as following:

for `[influxdb]`

- `token` = the access token to the influxdb database
- `url` = the hostname or ip needed to connect to influxdb
- `org` = the organization on influx that the bucket belongs to
- `bucket` = the bucket(table) that will hold the data

for `[mqtt]`

- `topic` = the topic to subscribe to on the mqtt broker
- `host`= host ip/address of the mqtt broker

## step 3

in the repository there are some docker files include. In a command terminal navigate to the cloned/downloaded folder and type the following 

>docker-compose up

to execute the docker container. Additionally you can add the `-d` parameter to the docker compose command to run it in the background.

>docker compose up -d

to see all running containers you can type

>docker ps

and to stop the service simply type (whilst in the directory)

>docker-compose stop