from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    favorites = db.relationship('Favorites')

    def __init__ (self, id, email, username, password):
        self.id = id,
        self.username = username,
        self.email = email,
        self.password = password

    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "password": self.password,
        }

class Characters(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    planet_id = db.Column(db.Integer, db.ForeignKey('planet.id'))
    planet = db.relationship('Planet')
    

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name 
        }

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    characters = db.relationship('Characters')
    favorites = db.relationship('Favorites')

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name 
        }

class Favorites(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User')
    
    planet_id = db.Column(db.Integer, db.ForeignKey('planet.id'))
    planet = db.relationship('Planet')

    def serialize(self):
        return {
            "id": self.id,   
        }