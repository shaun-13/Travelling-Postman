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

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/notification'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
CORS(app)

class Person(db.Model):
    __tablename__ = 'tele_details'

    userid = db.Column(db.String(10), primary_key=True)
    teleuserid = db.Column(db.String(20), nullable=False)
    telechatid = db.Column(db.String(80), nullable=False)

    def __init__(self, userid, teleuserid, telechatid):
        self.userid = userid
        self.teleuserid = teleuserid
        self.telechatid = telechatid

    def json(self):
        return {"userid": self.userid, "teleuserid": self.teleuserid, "telechatid": self.telechatid}

hostname = "localhost" 
port = 5672 
connection = pika.BlockingConnection(pika.ConnectionParameters(host=hostname, port=port))
channel = connection.channel()
exchangename="order_topic"
channel.exchange_declare(exchange=exchangename, exchange_type='topic')

def receiveRequest():
    # channelqueue = channel.queue_declare(queue="confirmed_orders", durable=True) #KIV THE QUEUE NAME
    # queue_name = channelqueue.method.queue
    # channel.queue_bind(exchange=exchangename, queue=queue_name, routing_key='orders.*') 
    # channel.basic_qos(prefetch_count=1) # The "Quality of Service" setting makes the broker distribute only one message to a consumer if the consumer is available (i.e., having finished processing and acknowledged all previous messages that it receives)
    # channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True) # 'auto_ack=True' acknowledges the reception of a message to the broker automatically, so that the broker can assume the message is received and processed and remove it from the queue
    # channel.start_consuming()

    channelqueue = channel.queue_declare(queue="notification", durable=True) # 'durable' makes the queue survive broker restarts so that the messages in it survive broker restarts too
    queue_name = channelqueue.method.queue
    channel.queue_bind(exchange=exchangename, queue=queue_name, routing_key='*.success') # bind the queue to the exchange via the key
        # any routing_key with two words and ending with '.success' will be matched

    # set up a consumer and start to wait for coming messages
    channel.basic_qos(prefetch_count=1) # The "Quality of Service" setting makes the broker distribute only one message to a consumer if the consumer is available (i.e., having finished processing and acknowledged all previous messages that it receives)
    channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True) # 'auto_ack=True' acknowledges the reception of a message to the broker automatically, so that the broker can assume the message is received and processed and remove it from the queue
    channel.start_consuming() # an implicit loop waiting to receive messages; it doesn't exit by default. Use Ctrl+C in the command window to terminate it.


def callback(channel, method, properties, body): 
    print("Received an request by " + __file__)
    processOrder(json.loads(body))
    # json.dump(result, sys.stdout, default=str) # convert the JSON object to a string and print out on screen
    print() # print a new line feed to the previous json dump
    print() # print another new line as a separator

def processOrder(order):
#
#     Order details:
# {'po_id': '90', 'requester_id': '10215444379333051', 'quantity': 5, 'item_name': 'Bananas', 'total': 55.23}



    print("Sending a message:")
    print('Order details:')
    print(order)
    print()
    userid = order['requester_id']

    quantity = order['quantity']
    item_name = order['item_name']
    total = order['total']

    cuser = Person.query.filter_by(userid=userid).first()
    chatid = str(cuser.telechatid)
    bot_token = '1076658459:AAHwvu83zFLd803XwCa6yBip6j0vwA1Ax5s'
    # chatid = '410414385'
    bot_message = "You have successfully registered for your preorder for " + str(quantity) + ' ' + item_name + ' at $' + str(total) + '. Thank you!' 
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + chatid + '&parse_mode=Markdown&text=' + bot_message
    response = requests.get(send_text)
    print(response.json())

# FLASK side
# @app.route('/<string:userid>/<string:teleid>')
# def insert_chatid(userid, teleid):
#     updates = "https://api.telegram.org/bot1076658459:AAHwvu83zFLd803XwCa6yBip6j0vwA1Ax5s/getUpdates"
#     response = requests.get(updates)
#     response = response.json()
#     # looping through messages to find chatid that matches the username
#     update_list = (list(response.values())[1])
#     for loopnum in range(1, len(update_list)):
#         update = update_list[loopnum]
#         for key,value in update.items():
#             if type(value) is dict:
#                 for key,value in value.items():
#                     if type(value) is dict:
#                         for key, value in value.items():
#                             if key == 'id': #id
#                                 chatid_holder = value
#                             if value == teleid: #username
#                                 chatid = chatid_holder
#     # check if duplicate
#     cuser = Person.query.filter_by(teleuserid=teleid).first()
#     if cuser:
#         return jsonify(cuser.json())

#     # inserting into DB
#     tele_details = Person(userid=userid,
#                             teleuserid=teleid,
#                             telechatid=chatid)
    
#     try:
#         db.session.add(tele_details)
#         db.session.commit()
#     except:
#         return jsonify({"message": "An error occurred creating the user."}), 500

#     return jsonify(tele_details.json()), 201


if __name__ == "__main__":  # execute this program only if it is run as a script (not by 'import')
    print("This is " + os.path.basename(__file__) + ": sending a notification...")
    receiveRequest()
    # print('is this running')
    # app.run(host="127.0.0.1", port=5005, debug=True)
    
