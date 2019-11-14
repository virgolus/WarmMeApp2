#!/usr/bin/python3
import time
import DB
import paho.mqtt.client as mqtt
import json

global sensors
sensors = []

def start():
    # get
    init()
    # subscribe to mqtt
    subscribe()
    
def init():
    try:
        con = DB.getDBConnection()
        cur = con.cursor()

        # All Zones
        cur.execute("SELECT * from sensor")
        sensors.append(cur.fetchall())
        
        # Create a map of zone - related sensor
        #for zone in allZones:
        #    zoneModel = Zone(zone[0], zone[1])
        #    cur.execute('SELECT * from sensor where zone_id=' + str(zone[0]))
        #    zoneModel.addSensors(cur.fetchall())
        #    zones.append(zoneModel)

    finally:
        if con:
            con.close()

def subscribe():
    client = mqtt.Client('warmMeHarvester')
    client.on_message = on_message
    client.connect('localhost')
    client.subscribe('sensors')
    print("Harvester connected to mqtt")
    #client.loop_start()
    client.loop_forever()

def on_message(client, userdata, message):
    # Log
    msgAsStr = str(message.payload.decode("utf-8"))
    print("message topic=",message.topic)
    print("message received ",msgAsStr)

    write(msgAsStr)

def write(msgAsStr):
    # get sensor id
    msg = json.loads(msgAsStr)
    # sensorId = next((x for x in sensors[0] if x[5] == msg["id"]), None)

    for sensor in sensors[0]:
        if sensor[4] == str(msg["id"]):
            sensorId = sensor[4]
            # write
            query = "Insert into sensor_monitor (sensor_id, temperature, humidity) VALUES (" + str(int(sensorId)) + "," + str(float(msg["temperature"])) + "," + str(float(msg["humidity"])) + ")"
            print(query)
            try:
                con = DB.getDBConnection()
                cur = con.cursor()
                cur.execute(query)
                con.commit()
            finally:
                if con:
                    con.close()
            break