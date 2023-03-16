from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy import REAL

db = SQLAlchemy()

class Plant(db.Model, SerializerMixin):
    __tablename__ = 'plants'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    image = db.Column(db.String)
    price = db.Column(db.REAL)

    def to_dict(self):
        plant_dict = {
            "id": self.id,
            "name": self.name,
            "image": self.image,
            "price": self.price,
        }
        
        return plant_dict
