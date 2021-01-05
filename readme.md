# Setup

## step 1

download or clone the repository to your system. And make sure docker is installed.

## step 2

in the `config` folder there is a file named `config.ini.example`. remove the `.example` extension and edit the file in your text editor of choice.

the config file will have some placholder text, this need to be filled in as followed:

for `[influxdb]`

- `token` = the access token to the influxdb database
- `url` = the hostname or ip needed to connect to influxdb
- `org` = the organization on influx that the bucket belongs to
- `bucket` = the bucket(table) that will hold the data

for `[mqtt]`

- `topic` = the topic to subscribe to on the mqtt broker
- `host`= host ip/address of the mqtt broker