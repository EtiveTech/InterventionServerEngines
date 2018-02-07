#!/usr/bin/python
# -*- coding: utf-8 -*-

from json import dumps

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

    params = {"user": '"' + getDeliveryUser() + '"',
              "pass": '"' + getDeliveryPassword() + '"',
              "mode": "relay",
              "msg": message.message_text,
              "sendTime": message.date + ' ' + message.time}  # DD/MM/YYYY HH:mm

    if message.channel == "SMS":
        params['channel'] = "sms"
        params['to'] = aged.mobile_phone_number
        params.msg = params.msg.replace("'"," ").encode('utf8')

    elif message.channel == 'Email':
        params['channel'] = "email"
        params['to'] = aged.email

    elif message.channel == 'Telegram':
        params['channel'] = "telegram"
        params['to'] = aged.telegram

    elif message.channel == 'Facebook':
        params['channel'] = "fbm"
        params['to'] = aged.facebook

    elif message.channel == 'Whatsapp':
        params['channel'] = "whatsapp"
        params['to'] = aged.mobile_phone_number

    print(params)
    return requests.post(getDeliveryPath() + "sendIntervention/", data=dumps(params)).json()
