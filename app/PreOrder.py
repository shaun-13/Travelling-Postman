from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
 
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/preorder'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
 
db = SQLAlchemy(app)
 
class PreOrder(db.Model):
    __tablename__ = 'preorder_details'
 
    po_id = db.Column(db.String(10), primary_key=True)
    traveller_id = db.Column(db.String(10), unique=True, nullable=False)
    country = db.Column(db.String(30), nullable=False)
    end_date = db.Column(db.Date, nullable=False)
    item_name = db.Column(db.String(30), nullable=False)
    item_catagory = db.Column(db.String(30), nullable=False)
    price = db.Column(db.Float(precision=2), nullable=False)
 
    def __init__(self, po_id, traveller_id, country, end_date, item_name, item_catagory, price):
        self.po_id = po_id
        self.traveller_id = traveller_id
        self.country = country
        self.end_date = end_date
        self.item_name = item_name
        self.item_catagory = item_catagory
        self.price = price
 
    def json(self):
        return {"po_id": self.po_id, "traveller_id": self.traveller_id, "country": self.country, "end_date": self.end_date, "item_name": self.item_name, "item_catagory": self.item_catagory, "price": self.price}
 
class Registered(db.Model):
    __tablename__ = 'registered_users'
 
    po_id = db.Column(db.String(10), nullable=False)
    traveller_id = db.Column(db.String(10), nullable=False)
    paid_status = db.Column(db.Boolean, default=False, nullable=False)
 
    def __init__(self, po_id, traveller_id, paid_status):
        self.po_id = po_id
        self.traveller_id = traveller_id
        self.paid_status = paid_status
 
    def json(self):
        return {"po_id": self.po_id, "traveller_id": self.traveller_id, "paid_status": self.paid_status}

@app.route("/preorders")
def get_all():
    return jsonify({"preorders": [preorder_details.json() for preorder_details in PreOrder.query.all()]})

@app.route("/Registered_Users")
def get_all():
    return jsonify({"registered users": [registered_users.json() for registered_users in Registered.query.all()]})


#Function for POSTING preorder joined details to payment MS


#Function for traveller creating PreOrder [POST]
@