from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
 
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/book'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
 
db = SQLAlchemy(app)
 
class Registered(db.Model):
    __tablename__ = 'registered'
 
    poid = db.Column(db.String(10), nullable=False)
    travellerid = db.Column(db.String(10), nullable=False)
    paidStatus = db.Column(db.Boolean, default=False, nullable=False)
 
    def __init__(self, poid, requesterid, paidStatus):
        self.poid = poid
        self.travellerid = travellerid
        self.paidStatus = paidStatus
 
    def json(self):
        return {"poid": self.poid, "travellerid": self.travellerid, "paidStatus": self.paidStatus}

@app.route("/registetredURLHERE")
def get_all():
    return jsonify({"registered": [registered.json() for registered in Registered.query.all()]})