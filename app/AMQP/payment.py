# from flask import Flask, request, jsonify
# from flask_sqlalchemy import SQLAlchemy
# from flask_cors import CORS
# import json
# import sys
# import os
# import random
# import datetime
# import pika

# app = Flask(__name__)
# db = SQLAlchemy(app)
# CORS(app)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/book'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
 
# db = SQLAlchemy(app)

# @app.route('INSERTURL', methods = ['POST'])
# #Receive order, save as json then call sendPaymentStatus(status)
# def receivePODetails():
#     data = request.get_json()
#     print(data)
#     sendPaymentStatus(data)

# #PAYMENT AMQP TO NOTIFICATION MS 
# def sendPaymentStatus(data):
#     hostname = "localhost" # default broker hostname. Web management interface default at http://localhost:15672
#     port = 5672 # default messaging port.
#     # connect to the broker and set up a communication channel in the connection
#     connection = pika.BlockingConnection(pika.ConnectionParameters(host=hostname, port=port))
#         # Note: various network firewalls, filters, gateways (e.g., SMU VPN on wifi), may hinder the connections;
#         # If "pika.exceptions.AMQPConnectionError" happens, may try again after disconnecting the wifi and/or disabling firewalls
#     channel = connection.channel()

#     # set up the exchange if the exchange doesn't exist
#     exchangename="payment "
#     channel.exchange_declare(exchange=exchangename, exchange_type='direct')

#     # prepare the message body content
#     message = json.dumps(data, default=str) # convert a JSON object to a string

#     # send the message
#     # always inform Monitoring for logging no matter if successful or not
#     channel.basic_publish(exchange=exchangename, routing_key="shipping.info", body=message)

#     if "status" in order: # if some error happened in order creation
#         # inform Error handler
#         channel.queue_declare(queue='errorhandler', durable=True) # make sure the queue used by the error handler exist and durable
#         channel.queue_bind(exchange=exchangename, queue='errorhandler', routing_key='shipping.error') # make sure the queue is bound to the exchange
#         channel.basic_publish(exchange=exchangename, routing_key="shipping.error", body=message,
#             properties=pika.BasicProperties(delivery_mode = 2) # make message persistent within the matching queues until it is received by some receiver (the matching queues have to exist and be durable and bound to the exchange)
#         )
#         print("Order status ({:d}) sent to error handler.".format(order["status"]))
#     else: # inform Shipping and exit
#         # prepare the channel and send a message to Shipping
#         channel.queue_declare(queue='shipping', durable=True) # make sure the queue used by Shipping exist and durable
#         channel.queue_bind(exchange=exchangename, queue='shipping', routing_key='shipping.order') # make sure the queue is bound to the exchange
#         channel.basic_publish(exchange=exchangename, routing_key="shipping.order", body=message,
#             properties=pika.BasicProperties(delivery_mode = 2, # make message persistent within the matching queues until it is received by some receiver (the matching queues have to exist and be durable and bound to the exchange, which are ensured by the previous two api calls)
#             )
#         )
#         print("Order sent to shipping.")
#     # close the connection to the broker
#     connection.close()
