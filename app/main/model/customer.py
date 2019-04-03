# from .. import db, flask_bcrypt
# import datetime
# import jwt
# from app.main.model.blacklist import BlacklistToken
# from ..config import key

# class Customer(db.Model):
#     """ Customer Model for storing customer related details """
#     __tablename__ = "customer"

#     customer_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     username = db.Column(db.String(100), nullable=False, unique=True)
#     firstname = db.Column(db.String(50), nullable=False)
#     lastname = db.Column(db.String(50), nullable=False)
#     contact_number = db.Column(db.String(11))
#     gender = db.Column(db.String(6), nullable=False)
#     password_hash = db.Column(db.String(80))
    
#     @property
#     def password(self):
#         raise AttributeError('password: write-only field')

#     @password.setter
#     def password(self, password):
#         self.password_hash = flask_bcrypt.generate_password_hash(password).decode('utf-8')


#     def check_password(self, password):
#         return flask_bcrypt.check_password_hash(self.password_hash, password)

#     def __repr__(self):
#         return "<Customer '{}'>".format(self.username)

#     def encode_auth_token(self, customer_id):
#         """
#         Generates the Auth Token
#         :return: string
#         """
#         try:
#             payload = {
#                 'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1, seconds=60),
#                 'iat': datetime.datetime.utcnow(),
#                 'sub': customer_id
#             }
#             return jwt.encode(
#                 payload,
#                 key,
#                 algorithm='HS256'
#             )
#         except Exception as e:
#             return e
            
#     @staticmethod  
#     def decode_auth_token(auth_token):
#         """
#         Decodes the auth token
#         :param auth_token:
#         :return: integer|string
#         """
#         try:
#             payload = jwt.decode(auth_token, key)
#             is_blacklisted_token = BlacklistToken.check_blacklist(auth_token)
#             if is_blacklisted_token:
#                 return 'Token blacklisted. Please log in again.'
#             else:
#                 return payload['sub']
#         except jwt.ExpiredSignatureError:
#             return 'Signature expired. Please log in again.'
#         except jwt.InvalidTokenError:
#             return 'Invalid token. Please log in again.'