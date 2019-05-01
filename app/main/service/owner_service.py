import datetime

from app.main import db
from app.main.model.models import *

 
def save_new_owner(data):
    owner = Owner.query.filter_by(username=data['username']).first()
    if not owner:
        new_owner = Owner(
            username=data['username'],
            password=data['password'],
            firstname = data['firstname'],
            lastname = data['lastname'],
            email = data['email'],
            contact_number = data['contact_number'],
            gender = data['gender']
        )
        save_changes(new_owner)
        response_object = {
            'status': 'Success',
            'message': 'Owner successfully created.'
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'Owner already exists.'
        }
        return response_object, 409

def response(data):
    response = Response.query.filter_by(owner_username=data['owner_username']).first()
    if not response:
        new_response = Response(
            owner_username = data['owner_username'],
            response = data['response'],
            message = data['message'],
            owner = data['owner'],
            reservation = data['reservation']
        )
        save_changes(new_response)
        response_object = {
            'status':'success',
            'message':'Response successful.'
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'Response already exists.'
        }
        return response_object, 409


def current_owner(auth_header):
    print(auth_header+'auth_header')
    if auth_header == None:
        response_object = {
            'status': 'fail',
            'message': 'Data not found'
        }
        return response_object, 404
    else:
        identifier = Owner.decode_auth_token(auth_header)
        return identifier

def reservation_list():
    return Reservation.query.all()

# def get_reservation_list():
#     result = db.session.query(Reservation, Response).outerjoin(Response, Reservation.reservation_id == Response.response_id).all()
#     return result

def get_all_responses():
    return Response.query.all()

def get_owner_id(own_id):
    cur_own = Owner.query.filter_by(owner_id=own_id).first()
    print(own_id)
    print(cur_own)
    return cur_own

def get_all_owners():
    return Owner.query.all()


def get_a_owner(username):
    return Owner.query.filter_by(username=username).first()


def save_changes(data):
    db.session.add(data)
    db.session.commit()


# def generate_token(owner):
#     try:
#         # generate the auth token
#         auth_token = owner.encode_auth_token(owner.owner_id)
#         response_object = {
#             'status': 'Success',
#             'message': 'Owner successfully created.',
#             'Authorization': auth_token.decode()
#         }
#         return response_object, 201
#     except Exception as e:
#         response_object = {
#             'status': 'fail',
#             'message': 'Some error occurred. Please try again.'
#         }
#         return response_object, 401
