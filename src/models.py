from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email 
        }

class Characters(db.models):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    planet_id = db.Column(db.integer, db.ForeignKey('planet_id'))
    planet = relationship(Planet)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name 
        }

class Planet(db.models):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name 
        }

class Favorites(db.models):
    id = db.Column(db.Integer, primary_key=True)
    
    user_id = db.Column(db.Integer, ForeignKey('user.id'))
    user = db.relationship(User)
    
    planet_id = Column(Integer, ForeignKey('planet.id'))
    planet = relationship(Planet)

    def serialize(self):
        return {
            "id": self.id,   
        }