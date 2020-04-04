from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from os import environ
 
app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/user'
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
CORS(app)
 
class User(db.Model):
    __tablename__ = 'user_details'
 
    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
 
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
 
    def json(self):
        return {"user_id": self.user_id, "name": self.name}
 
 
@app.route("/users")
def get_all():
    return jsonify({"users": [user_details.json() for user_details in User.query.all()]})

@app.route("/users/<string:user_id>", methods=["POST"])
def add_user(user_id):
    if (User.query.filter_by(user_id=user_id).first()):
        return jsonify({"message": "A user with user_id '{}' already exists.".format(user_id)}), 400

    data = request.get_json()
    print(data)
    user = User(user_id, **data)

    try:
        db.session.add(user)
        db.session.commit()
    except:
        return jsonify({"message": "An error occurred creating the user."}), 500

    return jsonify(user.json()), 201


# @app.route("/book/<string:isbn13>")
# def find_by_isbn13(isbn13):
#     # book = Book.query.filter_by(isbn13=isbn13).first()
#     # if book:
#     #     return jsonify(book.json())
#     return jsonify({"message": "Filtering coming soon!"}), 404

if __name__ == '__main__':
    # app.run(port=5002, debug=True)
    app.run(host = '0.0.0.0', port = 5002, debug = True)