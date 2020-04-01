from flask import Flask, request, jsonify, redirect, url_for
from flask_cors import CORS
import pika
import json

app = Flask(__name__)

CORS(app)

@app.route('/')
def redirectToPayment():
    return

@app.route("/passToPayment")
def passToPayment():

    quantity = request.args.get('quantity')
    po_id = request.args.get('poid')
    item_name = request.args.get('item_name')
    requester_id = request.args.get('requester')
    price = request.args.get('price')

    PARAMS = jsonify({
        'quantity':quantity,
        'po_id': po_id,
        'item_name': item_name,
        'requester_id':requester_id,
        'price':price
        })


    redirectURL = url_for('redirectToPayment', quantity=quantity, po_id=po_id, item_name=item_name, requester_id=requester_id, price=price) 

    redirectURL = redirectURL[1:]
    
    serviceURL = 'http://localhost/ESD/app/order_details.html' + redirectURL
    
    r = redirect(serviceURL)
   
    print('Sent to order_details.html')

    return PARAMS, 201




    # for key in order:
    #     print(key, order[key])
    
    # print(po_id)
    # serviceURL = 'order_details.html?po_id='
    
    # return redirect(serviceURL + po_id)
    # r = request.get(url = serviceURL, param = po_id)
    # if 201 in r:
    #     print('Passed order:', po_id, 'to Payment Microservice successfully!')
    # else:
    #     print('Something is wrong!!!!')
    


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
    exchangename="order_topic"
    channel.exchange_declare(exchange=exchangename, exchange_type='topic')

    # prepare the message body content
    message = json.dumps(order, default=str) # convert a JSON object to a string

    # send the message to confirmed_orders
    channel.queue_declare(queue='confirmed_orders', durable=True) # make sure the queue used by the confirmed_orders exist and durable
    channel.queue_bind(exchange=exchangename, queue='confirmed_orders', routing_key='orders.success') # make sure the queue is bound to the exchange
    channel.basic_publish(exchange=exchangename, routing_key="orders.success", body=message)
    

@app.route("/paymentConfirmed/", methods=['POST'])
def receive_order():
    status = 201
    order = request.json
    # for key in order:
    #     print(key, order[key])

    # quantity = request.form['quantity']
    # po_id = request.form['poid']
    # item_name = request.form['item_name']
    # requester_id = request.form['requester']
    # price = request.form['price']

    # PARAMS = jsonify({
    #     'quantity':quantity,
    #     'po_id': po_id,
    #     'item_name': item_name,
    #     'requester_id':requester_id,
    #     'price':price
    #     })

    # print(PARAMS)

    # redirectURL = url_for('redirectToPayment', quantity=quantity, po_id=po_id, item_name=item_name, requester_id=requester_id, price=price) 

    # redirectURL = redirectURL[1:]
    
    # serviceURL = 'http://localhost/ESD/app/successful_payment.html' + redirectURL
    
    # r = redirect(serviceURL)
   
    # print('Sent to sucessful_payment.html')



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
    app.run(port=5001, debug=True)