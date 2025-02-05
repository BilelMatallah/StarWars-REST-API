"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, Characters, Planet, Favorites
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)


@app.route('/user', methods=['GET'])
def get_users():
    all_user = User.query.all()
    serialize_all_user = list(map(lambda user: user.serialize(), all_user))
    response_body = {
        "msg": "Hello, this is your GET /user response "
    }

    return jsonify(serialize_all_user), 200

@app.route('/user/<int:id>', methods=['GET'])
def get_one_user(id):
    
    user = User.query.get(id)
    
    return jsonify(user.serialize()), 200
    

@app.route('/user', methods=['POST'])
def create_user():
    data = request.get_json()
    new_user = User(data['username'], data['email'], data['password'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify("NUEVO USER"), 200


@app.route('/planet', methods=['GET'])
def get_planets():
    all_planets = Planet.query.all()
    serialize_all_planets = [planet.serialize() for planet in all_planets]
    return jsonify(serialize_all_planets), 200

@app.route('/planets/<int:planet_id>', methods=['GET'])
def get_one_planet(id)
    planet = Planet.query.get(id)
    return jsonify(planet.serialize()), 200



 
    




# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
