#!/usr/bin/python
# -*- coding: utf-8 -*-

from json import dumps

# import logging
import requests
import os
import re
from controller.utilities import getDeliveryPath, getDeliveryUser, getDeliveryPassword


def sendIntervention(message, aged):
    '''
    Send to the delivery system the information to send the messages to the aged, 
    this one respondes with sent or scheduled
    :param message: the message to send
    :param aged: the aged that receives the message
    :return: the response of the delivery system
    '''

    msg = message.message_text

    if message.channel == "SMS":
        channel = "sms"
        to = aged.mobile_phone_number
        # encode('utf8') changes the string to an array of bytes which stops the JSON encode from working
        msg = msg.replace("'"," ") #.encode('utf8')

    elif message.channel == 'Email':
        channel = "email"
        to = aged.email

    elif message.channel == 'Telegram':
        channel = "telegram"
        to = aged.telegram

    elif message.channel == 'Facebook':
        channel = "fbm"
        to = aged.facebook

    elif message.channel == 'Whatsapp':
        channel = "whatsapp"
        to = aged.mobile_phone_number

    params = {
        "user": getDeliveryUser(),
        "pass": getDeliveryPassword(),
        "channel": channel,
        "mode": "relay",
        "to": to,
        "msg": msg,
        "sendTime": message.date + ' ' + message.time # DD/MM/YYYY HH:mm
    }

    jsonParams = dumps(params)
    # logging.debug("Intervention params: " + jsonParams)
    result = requests.post(getDeliveryPath() + "sendIntervention/", data = jsonParams).json()
    # logging.debug("Intervention response: " + result['response'])

    return result
