from .. import db
from ..config import key
# from app.main.model.owner import Owner


class Restaurant(db.Model):
    """ Restaurant Model for storing restaurant related details """
    __tablename__= 'restaurant'
	
    restaurant_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    restaurant_name = db.Column(db.String(30), nullable=False, unique=True)
    restaurant_type = db.Column(db.String(30), nullable=False)
    bio = db.Column(db.String(200), nullable=False)
    locations = db.Column(db.String(200), nullable=False)
    restaurant_owner_id = db.Column(db.Integer, db.ForeignKey('owner.owner_id'))

    def __repr__(self):
        return "<Restaurant '{}'>".format(self.restaurant_name)