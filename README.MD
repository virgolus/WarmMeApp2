# WarmMeApp2

# Dependencies
## RF24Libs
RF24 libraries installer by TMRh20 (install.sh)
```
script/install
```

## Mosquitto
APT -> mosquitto-clients

## Utils
APT -> moreutils

## Python
pymysql
paho-mqtt

## Local Test
### Mysql
https://dev.mysql.com/doc/mysql-installation-excerpt/5.5/en/docker-mysql-getting-started.html#docker-download-image
```
docker run --name=warmme-db -d -p 3306:3306 -e MYSQL_ROOT_HOST=% mysql/mysql-server:8.0
```
eseguire script "sql/initDb.sql"

### Mosquitto
https://github.com/toke/docker-mosquitto
```
docker run --name=warmme-mqtt -d -p 1883:1883 -p 9001:9001 toke/mosquitto
```

### Mqtt
```
scripts/mosquitto/publish.sh
```