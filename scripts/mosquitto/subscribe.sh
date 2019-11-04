#!/bin/sh

mosquitto_sub -v -t 'sensors' | ts
