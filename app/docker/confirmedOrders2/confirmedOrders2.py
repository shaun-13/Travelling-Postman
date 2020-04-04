from flask import Flask, request, jsonify, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from os import environ
from datetime import datetime
import json
import sys
import os
import random
import requests
import pika

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/confirmed_order'
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
CORS(app)

class Confirmed_order(db.Model):
    __tablename__ = 'pre_orders'
 
    po_id = db.Column(db.Integer(), primary_key=True)
    requester_id = db.Column(db.Integer(), primary_key=True)
    quantity = db.Column(db.Integer(), nullable=False)

    def __init__(self, po_id, requester_id, quantity):
        self.po_id = po_id
        self.requester_id = requester_id
        self.quantity = quantity

    def json(self):
        return {'po_id': self.po_id, 'requester_id': self.requester_id, 'quantity': self.quantity}

hostname = "localhost" 
port = 5672 
connection = pika.BlockingConnection(pika.ConnectionParameters(host=hostname, port=port))
channel = connection.channel()
exchangename="order_topic"
channel.exchange_declare(exchange=exchangename, exchange_type='topic')

def orderCreation(): #!!!!!!!!!!!!!!!!KIV FUNCTION NAME!!!!!!!!!!!!!!!!!!!!!!
    # channelqueue = channel.queue_declare(queue="confirmed_order", durable=True) 
    # queue_name = channelqueue.method.queue
    # channel.queue_bind(exchange=exchangename, queue=queue_name, routing_key='orders.*') 
    # channel.basic_qos(prefetch_count=1) # The "Quality of Service" setting makes the broker distribute only one message to a consumer if the consumer is available (i.e., having finished processing and acknowledged all previous messages that it receives)
    # channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True) # 'auto_ack=True' acknowledges the reception of a message to the broker automatically, so that the broker can assume the message is received and processed and remove it from the queue
    # channel.start_consuming()

    channelqueue = channel.queue_declare(queue="confirmed_order", durable=True) # 'durable' makes the queue survive broker restarts so that the messages in it survive broker restarts too
    queue_name = channelqueue.method.queue
    channel.queue_bind(exchange=exchangename, queue=queue_name, routing_key='*.success') # bind the queue to the exchange via the key
        # any routing_key with two words and ending with '.success' will be matched

    # set up a consumer and start to wait for coming messages
    channel.basic_qos(prefetch_count=1) # The "Quality of Service" setting makes the broker distribute only one message to a consumer if the consumer is available (i.e., having finished processing and acknowledged all previous messages that it receives)
    channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True) # 'auto_ack=True' acknowledges the reception of a message to the broker automatically, so that the broker can assume the message is received and processed and remove it from the queue
    channel.start_consuming() # an implicit loop waiting to receive messages; it doesn't exit by default. Use Ctrl+C in the command window to terminate it.


def callback(channel, method, properties, body): 
    print("Received an request by " + __file__)
    processOrderLog(json.loads(body))
    
def processOrderLog(order):
    print("Recording an order creation log:")
    print(order)
    print()
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Current Time =", current_time)

    po_id = order['po_id']
    requester_id = order['requester_id']
    quantity = order['quantity']
    order = Confirmed_order(po_id= po_id, requester_id= requester_id, quantity= quantity)
    
    print()
    print('Order details:')
    print(order.__dict__)
    print()

    status = 201
    result = {'status': status, 'message':'Successfully created order!'}

    try:
        db.session.add(order)
        db.session.commit()
        print('******Successfully added order into database!******')
    except Exception as e:
        status = 500
        result = {'status': status, 'message':'An error occured when confirming order.', 'error:': str(e)}
        print(str(e))
        return str(result), status

    return str(result), status

if __name__ == "__main__":  # execute this program only if it is run as a script (not by 'import')
    print("This is " + os.path.basename(__file__) + ": running...")
    orderCreation()
    # app.run(host="127.0.0.1", port=5003, debug=True)
    app.run(host = '0.0.0.0', port = 5003, debug = True)
    
