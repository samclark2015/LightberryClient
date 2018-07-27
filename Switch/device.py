import os
from gpiozero import DigitalOutputDevice
from enum import IntEnum
from json import dumps as jsonify
from .config import DEVICE

class Status(IntEnum):
    OFF = 0
    ON = 1

class Controller:
    def __init__(self, pin):
        self.__status = Status.OFF
        self.__device = DigitalOutputDevice(pin)

    def setStatus(self, status):
        if status == Status.OFF:
            self.__device.off()
        elif status == Status.ON :
            self.__device.on()
        self.__status = status
        return self.__status

    def getStatus(self):
        return self.__status

class Device:
    def __init__(self):
        self.__config = DEVICE
        self.__controller = Controller(int(os.getenv('GPIO_PIN')))

    def getId(self):
        return self.__config.get('deviceId')

    def getStatus(self):
        return self.__controller.getStatus()

    def publishStatus(self, mqtt):
        payload = jsonify({
            'state': self.getStatus()
        })
        mqtt.publish("{}/status".format(self.getId()), payload)

    def registerMqtt(self, mqtt):
        # Register callbacks
        deviceId = self.__config.get('deviceId')
        payload = jsonify({
            'metadata': DEVICE,
            'state': self.getStatus()
        })
        mqtt.message_callback_add('{}/on'.format(deviceId), self.handleOnMessage)
        mqtt.message_callback_add('{}/off'.format(deviceId), self.handleOffMessage)
        mqtt.publish("{}/online".format(deviceId), payload)

        pairingCode = self.__config.get('pairingCode')
        print("Connected. Pairing code: {}".format(pairingCode))

    def handleOnMessage(self, mosq, obj, msg):
        self.__controller.setStatus(Status.ON)
        self.publishStatus(mosq)

    def handleOffMessage(self, mosq, obj, msg):
        self.__controller.setStatus(Status.OFF)
        self.publishStatus(mosq)
