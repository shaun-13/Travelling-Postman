from flask import Flask, request, jsonify
from flask_cors import CORS
import pika
import json

app = Flask(__name__)

CORS(app)







def process_payment(order):
    print('!!!!!!**************HI!!!!!!**************')
    hostname = "localhost" # default broker hostname. Web management interface default at http://localhost:15672
    port = 5672 # default messaging port.
    # connect to the broker and set up a communication channel in the connection
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=hostname, port=port))
        # Note: various network firewalls, filters, gateways (e.g., SMU VPN on wifi), may hinder the connections;
        # If "pika.exceptions.AMQPConnectionError" happens, may try again after disconnecting the wifi and/or disabling firewalls
    channel = connection.channel()

    # set up the exchange if the exchange doesn't exist
    exchangename="order_direct"
    channel.exchange_declare(exchange=exchangename, exchange_type='direct')

    # prepare the message body content
    message = json.dumps(order, default=str) # convert a JSON object to a string

    # send the message to confirmed_orders
    channel.queue_declare(queue='confirmed_orders', durable=True) # make sure the queue used by the confirmed_orders exist and durable
    channel.queue_bind(exchange=exchangename, queue='confirmed_orders', routing_key='orders.add') # make sure the queue is bound to the exchange
    channel.basic_publish(exchange=exchangename, routing_key="orders.add", body=message)
    

@app.route("/paymentConfirmed/", methods=['POST'])
def receive_order():
    status = 201
    order = request.json
    for key in order:
        print(key, order[key])
    process_payment(order)
    return jsonify(order), status

    
#     return jsonify({"books": [book.json() for book in Book.query.all()]})

# @app.route("/book/<string:isbn13>")
# def find_by_isbn13(isbn13):
#     book = Book.query.filter_by(isbn13=isbn13).first()
#     if book:
#         return jsonify(book.json())
#     return jsonify({"message": "Book not found."}), 404


# @app.route("/book/<string:isbn13>", methods=['POST'])
# def create_book(isbn13):
#     if (Book.query.filter_by(isbn13=isbn13).first()):
#         return jsonify({"message": "A book with isbn13 '{}' already exists.".format(isbn13)}), 400

#     data = request.get_json()
#     book = Book(isbn13, **data)

#     try:
#         db.session.add(book)
#         db.session.commit()
#     except:
#         return jsonify({"message": "An error occurred creating the book."}), 500

#     return jsonify(book.json()), 201


if __name__=='__main__':
    app.run(port=5000, debug=True)