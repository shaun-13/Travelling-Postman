from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
 
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/book'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
 
db = SQLAlchemy(app)
 
class PreOrder(db.Model):
    __tablename__ = 'preorder'
 
    poid = db.Column(db.String(10), primary_key=True)
    travellerid = db.Column(db.String(10), unique=True nullable=False)
    country = db.Column(db.String(30), nullable=False)
    endDate = db.Column(db.Date, nullable=False)
    status = db.Column(db.Boolean, default=True, nullable=False)
    itemName = db.Column(db.String(30), nullable=False)
    itemCatagory = db.Column(db.String(30), nullable=False)
    price = db.Column(db.Float(precision=2), nullable=False)
 
    def __init__(self, poid, travellerid, country, endDate, status, itemName, itemCatagory, price):
        self.poid = poid
        self.travellerid = travellerid
        self.country = country
        self.endDate = endDate
        self.status = status
        self.itemName = itemName
        self.itemCatagory = itemCatagory
        self.price = price
 
    def json(self):
        return {"poid": self.poid, "travellerid": self.travellerid, "country": self.country, "endDate": self.endDate, "status": self.status, "itemName": self.itemName, "itemCatagory": self.itemCatagory, "price": self.price}

@app.route("/PREORDERURL HERE")
def get_all():
    return jsonify({"preorder": [preorder.json() for preorder in PreOrder.query.all()]})