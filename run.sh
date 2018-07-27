#!/bin/sh
SETUP_FILE=/var/lightberry.setup

if [ -f "$1" ]; then
	. $1
fi

if [ ! -d "$DEVICE_CLASS" ] || [ ! -f "$DEVICE_CLASS/device.py" ]; then
	echo "Device class $DEVICE_CLASS not found! Exiting..."
	exit 1
fi

if [ ! -f "$SETUP_FILE" ]; then
	pip3 install -r requirements.txt -r $DEVICE_CLASS/requirements.txt
	touch $SETUP_FILE
fi

python3 ./main.py
