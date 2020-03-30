from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from os import environ
import requests
import json

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


@app.route('/<string:userid>')
def send_message(userid):
    bot_token = '1076658459:AAHwvu83zFLd803XwCa6yBip6j0vwA1Ax5s'
    cuser = Person.query.filter_by(userid=userid).first()
    chatid = str(cuser.telechatid)
    
    # get chatid from database
    bot_message = "You have successfully registered for your preorder."
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + chatid + '&parse_mode=Markdown&text=' + bot_message
    response = requests.get(send_text)
    return response.json()

if __name__=='__main__':
    app.run(port=5005, debug=True)