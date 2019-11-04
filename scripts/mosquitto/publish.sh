#!/bin/sh

mosquitto_pub -d -t sensors -m '{"id":11, "temperature":22, "umidità":77}'
