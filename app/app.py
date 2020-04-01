from flask import Flask, request, jsonify, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from os import environ
import requests
import json
import pika


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/notifications'
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

def OrderCreation():
    hostname = "localhost" # default host
    port = 5672 # default port
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=hostname, port=port))
    channel = connection.channel()
    exchangename="order_topic"
    channel.exchange_declare(exchange=exchangename, exchange_type='topic')
    channelqueue = channel.queue_declare(queue='', exclusive=True) 
   
    queue_name = channelqueue.method.queue
    channel.queue_bind(exchange=exchangename, queue=queue_name, routing_key='orders.*') # bind the queue to the exchange via the key

    # set up a consumer and start to wait for coming messages
    channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
    channel.start_consuming() # an implicit loop waiting to receive messages; it doesn't exit by default. Use Ctrl+C in the command window to terminate it.


    # queue_name = channelqueue.method.queue
    # channel.queue_bind(exchange=exchangename, queue=queue_name, routing_key='#') 
    # channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
    # channel.start_consuming() 

def callback(channel, method, properties, body): # required signature for the callback; no return
    print("Received an order log by " + __file__)
    processOrderLog(json.loads(body))
    # print() # print a new line feed

def processOrderLog(order):
    # userid = order['requester_id']

    print('######## I AM ALIVE!!!!!! ####################')
    print(order)

    bot_token = '1076658459:AAHwvu83zFLd803XwCa6yBip6j0vwA1Ax5s'
    chatid = '223450427' #223450427 -shaun 410414385-wushen
    bot_message = "You have successfully registered for your preorder."
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + chatid + '&parse_mode=Markdown&text=' + bot_message
    print(send_text)
    response = requests.get(send_text)
    print(response)
    return response #jsonify(response.json()), 200

@app.route('/<string:userid>/<string:teleid>')
def insert_chatid(userid, teleid):
    updates = "https://api.telegram.org/bot1076658459:AAHwvu83zFLd803XwCa6yBip6j0vwA1Ax5s/getUpdates"
    response = requests.get(updates)
    response = response.json()
    # looping through messages to find chatid that matches the username
    update_list = (list(response.values())[1])
    for loopnum in range(1, len(update_list)):
        update = update_list[loopnum]
        for key,value in update.items():
            if type(value) is dict:
                for key,value in value.items():
                    if type(value) is dict:
                        for key, value in value.items():
                            if key == 'id': #id
                                chatid_holder = value
                            if value == teleid: #username
                                chatid = chatid_holder
    # check if duplicate
    cuser = Person.query.filter_by(teleuserid=teleid).first()
    if cuser:
        return jsonify(cuser.json())

    # inserting into DB
    tele_details = Person(userid=userid,
                            teleuserid=teleid,
                            telechatid=chatid)
    
    try:
        db.session.add(tele_details)
        db.session.commit()
    except:
        return jsonify({"message": "An error occurred creating the user."}), 500

    return jsonify(tele_details.json()), 201


# @app.route('/<string:userid>')
# def send_message(userid):
#     bot_token = '1076658459:AAHwvu83zFLd803XwCa6yBip6j0vwA1Ax5s'
#     cuser = Person.query.filter_by(userid=userid).first()
#     # chatid = '410414385'
#     chatid = str(cuser.telechatid)
#     bot_message = "You have successfully registered for your preorder."
#     send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + chatid + '&parse_mode=Markdown&text=' + bot_message
#     response = requests.get(send_text)
#     return response.json()


if __name__=='__main__':
    app.run(host="127.0.0.1", port=5005, debug=True)
    OrderCreation()