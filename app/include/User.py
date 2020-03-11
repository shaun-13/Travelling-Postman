from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
 
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/book'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
 
db = SQLAlchemy(app)
 
class User(db.Model):
    __tablename__ = 'user'
 
    userid = db.Column(db.String(30), primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    travellerid = db.Column(db.String(10), nullable=False)
    requesterid = db.Column(db.String(10), nullable=False)
    password = db.Column(db.String(10), nullable=False)
    email = db.Column(db.String(30), nullable=False)
 
    def __init__(self, userid, name, travellerid, requesterid, password, email):
        self.userid = userid
        self.name = name
        self.travellerid = travellerid
        self.requesterid = requesterid
        self.password = password
        self.email = email
 
    def json(self):
        return {"userid": self.userid, "name": self.name, "travellerid": self.travellerid, "requesterid": self.requesterid, "password": self.password, "email": self.email}
 
 
@app.route("/bookURLHERE")
def get_all():
    return jsonify({"users": [user.json() for user in User.query.all()]})