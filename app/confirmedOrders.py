from flask import Flask, request, jsonify
# Use of jsonify is not necessary if the response message generated from the python code is already valid JSON
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

from datetime import datetime
import json
import pika

# This version of order.py uses a mysql DB via flask-sqlalchemy, instead of JSON files, as the data store.
#
# In comparison with topicmsg\order.py, this version
# (1) add appropriate flask routes to the respective functions in the file, so that
# - It allows HTTP GET or POST methods for retrieving all orders, one order, or creating a new order.
# (2): reuse, with some modification, the AMQP code in the topicmsg\order.py, so that
# - It fulfils the communication requirements for the "Place an order" user scenario for the Zoko/Amazing bookstore.
# TODO (after UI lab): follow the HTML and Javascript code samples for invoking the book microservice using Javascript, create a UI for this order microservice, so that
# - an order for a book can be placed through a HTML link or button click.

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/confirmed_order'
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
    
def OrderCreation():
    hostname = "localhost" # default host
    port = 5672 # default port
    # connect to the broker and set up a communication channel in the connection
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=hostname, port=port))
    channel = connection.channel()

    # set up the exchange if the exchange doesn't exist
    exchangename="order_direct"
    channel.exchange_declare(exchange=exchangename, exchange_type='direct')

    # prepare a queue for receiving messages
    channelqueue = channel.queue_declare(queue='confirmed_orders', durable=True) # '' indicates a random unique queue name; 'exclusive' indicates the queue is used only by this receiver and will be deleted if the receiver disconnects.
        # If no need durability of the messages, no need durable queues, and can use such temp random queues.
    queue_name = channelqueue.method.queue
    channel.queue_bind(exchange=exchangename, queue=queue_name, routing_key='orders.add') # bind the queue to the exchange via the key

    # set up a consumer and start to wait for coming messages
    channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
    channel.start_consuming() # an implicit loop waiting to receive messages; it doesn't exit by default. Use Ctrl+C in the command window to terminate it.

def callback(channel, method, properties, body): # required signature for the callback; no return
    print("Received an order creation order by " + __file__)
    processOrderLog(json.loads(body))
    print() # print a new line feed

def processOrderLog(order):
    print("Recording an order creation log:")
    print(order)
    print()

    now = datetime.now()

    current_time = now.strftime("%H:%M:%S")
    print("Current Time =", current_time)


    po_id = order['poid']
    requester_id = order['requesterID']
    quantity = order['quantity']

    order = Confirmed_order(po_id= po_id, requester_id= requester_id, quantity= quantity)

    print(order.__dict__)

    status = 201
    result = {'status': status, 'message':'Successfully created order!'}

    print("!!!!!!!!!!!!SANITY CHECK!!!!!!!!!!!!")

    try:
        db.session.add(order)
        db.session.commit()
        print('****OKAY!****')
    except Exception as e:
        status = 500
        result = {'status': status, 'message':'An error occured when confirming order.', 'error:': str(e)}
        print(str(e))
        return str(result), status

    return str(result), status



# @app.route("/order")
# def get_all():
#     return jsonify({'orders': [order.json() for order in Order.query.all()]})
 
# @app.route("/order/<int:order_id>")
# def find_by_order_id(order_id):
#     order = Order.query.filter_by(order_id=order_id).first()
#     if order:
#         return order.json()
#     return jsonify({'message': 'Order not found for id ' + str(order_id)}), 404
 
# @app.route("/order", methods=['POST'])
# def create_order():
#     # status in 2xx indicates success
#     status = 201
#     result = {}

#     # retrieve information about order and order items from the request
#     customer_id = request.json.get('customer_id', None)
#     order = Order(customer_id = customer_id)
#     cart_item = request.json.get('cart_item')
#     for index, ci in enumerate(cart_item):
#         if 'book_id' in cart_item[index] and 'quantity' in cart_item[index]:
#             order.order_item.append(Order_Item(book_id = cart_item[index]['book_id'], quantity = cart_item[index]['quantity']))
#         else:
#             status = 400
#             result = {"status": status, "message": "Invalid 'book_id' or 'quantity'."}
#             break

#     if status==201 and len(order.order_item)<1:
#         status = 404
#         result = {"status": status, "message": "Empty order."}

#     if status==201:
#         try:
#             db.session.add(order)
#             db.session.commit()
#         except Exception as e:
#             status = 500
#             result = {"status": status, "message": "An error occurred when creating the order in DB.", "error": str(e)}
         
#     if status==201:
#         result = order.json()

#     # FIXME: add a call to "send_order" copied from another appropriate file
#     send_order(result)
#     return jsonify(result), status


# def send_order(order):
#     """inform Shipping/Monitoring/Error as needed"""
#     # default username / password to the borker are both 'guest'
#     hostname = "localhost" # default broker hostname. Web management interface default at http://localhost:15672
#     port = 5672 # default messaging port.
#     # connect to the broker and set up a communication channel in the connection
#     connection = pika.BlockingConnection(pika.ConnectionParameters(host=hostname, port=port))
#         # Note: various network firewalls, filters, gateways (e.g., SMU VPN on wifi), may hinder the connections;
#         # If "pika.exceptions.AMQPConnectionError" happens, may try again after disconnecting the wifi and/or disabling firewalls
#     channel = connection.channel()

#     # set up the exchange if the exchange doesn't exist
#     exchangename="order_topic"
#     channel.exchange_declare(exchange=exchangename, exchange_type='topic')

#     # prepare the message body content
#     message = json.dumps(order, default=str) # convert a JSON object to a string

#     # send the message
#     # always inform Monitoring for logging no matter if successful or not
#     # FIXME: is this line of code needed according to the binding key used in Monitoring?
#     # No need of this line of code, because the monitoring uses '#' for its queue binding, and
#     # we don't need 'durable' monitoring records: channel.basic_publish(exchange=exchangename, routing_key="shipping.info", body=message)

#     if "status" in order: # if some error happened in order creation
#         # inform Error handler
#         channel.queue_declare(queue='errorhandler', durable=True) # make sure the queue used by the error handler exist and durable
#         channel.queue_bind(exchange=exchangename, queue='errorhandler', routing_key='*.error') # make sure the queue is bound to the exchange
#         channel.basic_publish(exchange=exchangename, routing_key="shipping.error", body=message,
#             properties=pika.BasicProperties(delivery_mode = 2) # make message persistent within the matching queues until it is received by some receiver (the matching queues have to exist and be durable and bound to the exchange)
#         )
#         print("Order status ({:d}) sent to error handler.".format(order["status"]))
#     else: # inform Shipping and exit
#         # prepare the channel and send a message to Shipping
#         channel.queue_declare(queue='shipping', durable=True) # make sure the queue used by Shipping exist and durable
#         channel.queue_bind(exchange=exchangename, queue='shipping', routing_key='*.order') # make sure the queue is bound to the exchange
#         channel.basic_publish(exchange=exchangename, routing_key="shipping.order", body=message,
#             properties=pika.BasicProperties(delivery_mode = 2, # make message persistent within the matching queues until it is received by some receiver (the matching queues have to exist and be durable and bound to the exchange, which are ensured by the previous two api calls)
#             )
#         )
#         print("Order sent to shipping.")
#     # close the connection to the broker
#     connection.close()


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5003, debug=True)
    OrderCreation()
    