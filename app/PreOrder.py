from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/preorder'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
 
db = SQLAlchemy(app)
CORS(app)
 
class PreOrder(db.Model):
    __tablename__ = 'preorder_details'
 
    po_id = db.Column(db.Integer(), primary_key=True)
    traveller_id = db.Column(db.String(32), unique=True, nullable=False)
    country = db.Column(db.String(30), nullable=False)
    end_date = db.Column(db.Date, nullable=False)
    item_name = db.Column(db.String(32), nullable=False)
    item_category = db.Column(db.String(32), nullable=False)
    price = db.Column(db.Float(precision=2), nullable=False)

    # img_id = db.Column(db.Integer, nullable=False)
    # img_name = db.Column(db.String(300))
    # img_data =  db.Column(db.LargeBinary)
 
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

# POST preorder to database
@app.route("/preorders/<string:po_id>", methods=['POST'])
def create_preorder(po_id):
    
    data = request.get_json()
    preorder_details = PreOrder(po_id, **data)
 
    try:
        db.session.add(preorder_details)
        db.session.commit()
    except:
        return jsonify({"message": "An error occurred while creating the preorder."}), 500
 
    return jsonify(preorder_details.json()), 201

# GET all preorder based on traveller id
@app.route("/preorders/<string:traveller_id>")
def get_all_by_traveller(traveller_id):
    return jsonify({"preorders": [preorder_details.json() for preorder_details in PreOrder.query.filter_by(traveller_id=traveller_id).all()]})


# Get all registered users
@app.route("/Registered_Users")
def getRegisteredUsers():
    pass

@app.route("/preorders/<string:po_id>")
def find_by_poid(po_id):
    pass

if __name__=='__main__':
    app.run(port=5000, debug=True)