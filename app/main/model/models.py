from .. import db, flask_bcrypt
import datetime
import jwt
from app.main.model.blacklist import BlacklistToken
from ..config import key
# from app.main.model.restaurant import Restaurant
# from app.main.model.owner import Owner


class Restaurant(db.Model):
    """ Restaurant Model for storing restaurant related details """
    __tablename__= 'restaurant'
	
    restaurant_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    restaurant_name = db.Column(db.String(30), nullable=False, unique=True)
    restaurant_type = db.Column(db.String(30), nullable=False)
    bio = db.Column(db.String(200), nullable=False)
    locations = db.Column(db.String(200), nullable=False)
    owner = db.Column(db.Integer, db.ForeignKey('owner.owner_id'))
    restaurant_reservations = db.relationship('Reservation', backref='restaurant_reservations')
    restaurant_response = db.relationship('Response', backref='restaurant_response')
    
    def __repr__(self):
        return "<Restaurant '{}'>".format(self.restaurant_name)

        
class Owner(db.Model):
    """ Owner Model for storing owner related details """
    __tablename__ = "owner"

    owner_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(100), nullable=False, unique=True)
    email = db.Column(db.String(155),nullable=False)
    firstname = db.Column(db.String(50), nullable=False)
    lastname = db.Column(db.String(50), nullable=False)
    contact_number = db.Column(db.String(11))
    gender = db.Column(db.String(6), nullable=False)
    password_hash = db.Column(db.String(80))
    restaurants = db.relationship('Restaurant', backref='restaurant_owner')
    respondee = db.relationship('Response', backref='owner_reponse')

    @property
    def password(self):
        raise AttributeError('password: write-only field')

    @password.setter
    def password(self, password):
        self.password_hash = flask_bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return flask_bcrypt.check_password_hash(self.password_hash, password)

    def __repr__(self):
        return "<Owner '{}'>".format(self.username)
    
    def encode_auth_token(self, owner_id):
        """
        Generates the Auth Token
        :return: string
        """
        try:
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1, seconds=60),
                'iat': datetime.datetime.utcnow(),
                'sub': owner_id
            }
            return jwt.encode(
                payload,
                key,
                algorithm='HS256'
            )
        except Exception as e:
            return e
    
    @staticmethod  
    def decode_auth_token(auth_token):
        """
        Decodes the auth token
        :param auth_token:
        :return: integer|string
        """ 
        try:
            payload = jwt.decode(auth_token, key)
            is_blacklisted_token = BlacklistToken.check_blacklist(auth_token)
            if is_blacklisted_token:
                return 'Token blacklisted. Please log in again.'
            else:
                return payload['sub']
        except jwt.ExpiredSignatureError:
            return 'Signature expired. Please log in again.'
        except jwt.InvalidTokenError:
            return 'Invalid token. Please log in again.'

class Customer(db.Model):
    """ Customer Model for storing customer related details """
    __tablename__ = "customer"

    customer_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(100), nullable=False, unique=True)
    email = db.Column(db.String(155),nullable=False)
    firstname = db.Column(db.String(50), nullable=False)
    lastname = db.Column(db.String(50), nullable=False)
    contact_number = db.Column(db.String(11), nullable=False)
    gender = db.Column(db.String(6), nullable=False)
    password_hash = db.Column(db.String(80))
    customer_reservation = db.relationship('Reservation', backref='reservation_customers')
    
    @property
    def password(self):
        raise AttributeError('password: write-only field')

    @password.setter
    def password(self, password):
        self.password_hash = flask_bcrypt.generate_password_hash(password).decode('utf-8')


    def check_password(self, password):
        return flask_bcrypt.check_password_hash(self.password_hash, password)

    def __repr__(self):
        return "<Customer '{}'>".format(self.username)

    def encode_auth_token(self, customer_id):
        """
        Generates the Auth Token
        :return: string
        """
        try:
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1, seconds=60),
                'iat': datetime.datetime.utcnow(),
                'sub': customer_id
            }
            return jwt.encode(
                payload,
                key,
                algorithm='HS256'
            )
        except Exception as e:
            return e
            
    @staticmethod  
    def decode_auth_token(auth_token):
        """
        Decodes the auth token
        :param auth_token:
        :return: integer|string
        """
        try:
            payload = jwt.decode(auth_token, key)
            is_blacklisted_token = BlacklistToken.check_blacklist(auth_token)
            if is_blacklisted_token:
                return 'Token blacklisted. Please log in again.'
            else:
                return payload['sub']
        except jwt.ExpiredSignatureError:
            return 'Signature expired. Please log in again.'
        except jwt.InvalidTokenError:
            return 'Invalid token. Please log in again.'

class Reservation(db.Model):
    """ Reservation Model for storing reservation related details """
    __tablename__ = "reservation"

    reservation_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    reservee = db.Column(db.String(155), nullable=False, unique=True)
    number_of_persons = db.Column(db.String(155), nullable=False)
    booking_date = db.Column(db.DateTime, nullable=False)
    # response = db.Column(db.String(255), nullable=False)
    customer_account = db.Column(db.Integer, db.ForeignKey('customer.customer_id'))
    restaurant = db.Column(db.Integer, db.ForeignKey('restaurant.restaurant_id'))
    status = db.relationship('Response', backref='reservation_status')

    def __repr__(self):
        return "<Reservation '{}'>".format(self.reservee)

class Response(db.Model):
    """ Response Model for storing response related details """
    __tablename__ = "response"
    response_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    owner_username = db.Column(db.String(155), nullable=False, unique=True)  
    response = db.Column(db.Boolean, nullable=False)
    message = db.Column(db.String(300))
    owner = db.Column(db.Integer, db.ForeignKey('owner.owner_id'))
    reservation = db.Column(db.Integer, db.ForeignKey('reservation.reservation_id'))
    restaurant = db.Column(db.Integer, db.ForeignKey('restaurant.restaurant_id'))

    def __repr__(self):
        return "<Response '{}'>".format(self.owner_username)