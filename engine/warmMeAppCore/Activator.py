#!/usr/bin/python3
import time
import DB
import paho.mqtt.client as mqtt

def start():
    # get
    init()
    # subscribe to mqtt
    subscribe()
    
def init():
	print('init')

def subscribe():
    client = mqtt.Client('warmMeActivator')
    client.on_message = on_message
    client.connect('localhost')
    client.subscribe('activate/')

    client.loop_start()

def on_message(client, userdata, message):
    print("message received " ,str(message.payload.decode("utf-8")))
    print("message topic=",message.topic)
    print("message qos=",message.qos)
    print("message retain flag=",message.retain)
