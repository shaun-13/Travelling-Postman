#!/usr/bin/env python3
# The above shebang (#!) operator tells Unix-like environments
# to run this file as a python3 script

from flask import Flask, request, jsonify, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from os import environ
import json
import sys
import os
import random
import requests
import pika

hostname = "localhost" 
port = 5672 
connection = pika.BlockingConnection(pika.ConnectionParameters(host=hostname, port=port))
channel = connection.channel()
exchangename="order_topic"
channel.exchange_declare(exchange=exchangename, exchange_type='topic')

def receiveRequest():
    channelqueue = channel.queue_declare(queue="confirmed_orders", durable=True) #KIV THE QUEUE NAME
    queue_name = channelqueue.method.queue
    channel.queue_bind(exchange=exchangename, queue=queue_name, routing_key='orders.*') 
    channel.basic_qos(prefetch_count=1) # The "Quality of Service" setting makes the broker distribute only one message to a consumer if the consumer is available (i.e., having finished processing and acknowledged all previous messages that it receives)
    channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True) # 'auto_ack=True' acknowledges the reception of a message to the broker automatically, so that the broker can assume the message is received and processed and remove it from the queue
    channel.start_consuming() 

def callback(channel, method, properties, body): 
    print("Received an request by " + __file__)
    result = processOrder(json.loads(body))
    # json.dump(result, sys.stdout, default=str) # convert the JSON object to a string and print out on screen
    print() # print a new line feed to the previous json dump
    print() # print another new line as a separator

def processOrder(order):
    print("Sending a message:")
    bot_token = '1076658459:AAHwvu83zFLd803XwCa6yBip6j0vwA1Ax5s'
    chatid = '410414385'
    bot_message = "You have successfully registered for your preorder"
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + chatid + '&parse_mode=Markdown&text=' + bot_message
    response = requests.get(send_text)
    print(response.json())


if __name__ == "__main__":  # execute this program only if it is run as a script (not by 'import')
    print("This is " + os.path.basename(__file__) + ": sending a notification...")
    receiveRequest()
