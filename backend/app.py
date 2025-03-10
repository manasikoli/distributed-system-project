from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# Database configuration for MySQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://user:password@db:3306/userdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Define the User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    age = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<User {self.name}>'

@app.route('/api/user', methods=['POST'])
def add_user():
    data = request.form
    new_user = User(name=data['name'], email=data['email'], age=int(data['age']))
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User added successfully"}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
