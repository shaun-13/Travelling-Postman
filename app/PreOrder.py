from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
 
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/preorder'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
 
db = SQLAlchemy(app)
 
class PreOrder(db.Model):
    __tablename__ = 'preorder_details'
 
    po_id = db.Column(db.String(10), primary_key=True)
    traveller_id = db.Column(db.String(32), unique=True, nullable=False)
    country = db.Column(db.String(30), nullable=False)
    end_date = db.Column(db.Date, nullable=False)
    item_name = db.Column(db.String(32), nullable=False)
    item_category = db.Column(db.String(32), nullable=False)
    price = db.Column(db.Float(precision=2), nullable=False)
 
    def __init__(self, po_id, traveller_id, country, end_date, item_name, item_category, price):
        self.po_id = po_id
        self.traveller_id = traveller_id
        self.country = country
        self.end_date = end_date
        self.item_name = item_name
        self.item_category = item_category
        self.price = price
 
    def json(self):
        return {"po_id": self.po_id, "traveller_id": self.traveller_id, "country": self.country, "end_date": self.end_date, "item_name": self.item_name, "item_category": self.item_category, "price": self.price}
 
class Registered(db.Model):
    __tablename__ = 'registered_users'
 
    po_id = db.Column(db.String(10), primary_key=True, nullable=False)
    requester_id = db.Column(db.String(32), primary_key=True, nullable=False)
 
    def __init__(self, po_id, requester_id):
        self.po_id = po_id
        self.requester_id = requester_id
 
    def json(self):
        return {"po_id": self.po_id, "traveller_id": self.traveller_id, "paid_status": self.paid_status}

# ALL GET/POST functions

# Get all preorders
@app.route("/preorders")
def get_all():
    return jsonify({"preorders": [preorder_details.json() for preorder_details in PreOrder.query.all()]})

# Create preorder
@app.route("/preorder/<string:po_id", methods=['POST'])
def create_preorder():
    data = request.get_json()
    preorder = PreOrder(po_id, **data)
 
    try:
        db.session.add(preorder)
        db.session.commit()
    except:
        return jsonify({"message": "An error occurred while creating the preorder."}), 500
 
    return jsonify(preorder.json()), 201

# Get all registered users
@app.route("/Registered_Users")
def get_all():
    return jsonify({"registered users": [registered_users.json() for registered_users in Registered.query.all()]})


#Function for POSTING preorder joined details to payment MS


#Function for traveller creating PreOrder [POST]

@app.route("/preOrder/<string:po_id>")
def find_by_poid(po_id):
    preorder = PreOrder.query.filter_by(po_id=po_id).first()
    if preorder:
        return jsonify(preorder.json())
    return jsonify({'message': 'Pre-Order not found'}), 404


if __name__=='__main__':
    app.run(port=5000, debug=True)