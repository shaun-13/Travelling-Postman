from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
 
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/users'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
 
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

# @app.route("/book/<string:isbn13>")
# def find_by_isbn13(isbn13):
#     # book = Book.query.filter_by(isbn13=isbn13).first()
#     # if book:
#     #     return jsonify(book.json())
#     return jsonify({"message": "Filtering coming soon!"}), 404

if __name__ == '__main__':
    app.run(port=5000, debug=True)