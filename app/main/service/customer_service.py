import datetime
import jwt

from app.main import db
from app.main.model.models import *

from ..config import key
from .. import db, flask_bcrypt

from flask import jsonify

def save_new_customer(data):
    customer = Customer.query.filter_by(username=data['username']).first()
    if not customer:
        new_customer = Customer(
            username = data['username'],
            password = data['password'],
            firstname = data['firstname'],
            lastname = data['lastname'],
            email = data['email'],
            contact_number = data['contact_number'],
            gender = data['gender']
        )
        save_changes(new_customer)
        response_object = {
            'status':'success',
            'message':'Customer created successfully'
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'customer already exists. Please Log in.'
        }
        return response_object, 409

def update_customer(data,username):
    update_customer = Customer.query.filter_by(username=username).first()
    if update_customer == None:
        response_object = {
            'status':'fail',
            'message': 'Customer not found'
        }
        return response_object, 404
    else:
        update_customer.username = data['username'],
        update_customer.firstname = data['firstname'],
        update_customer.lastname = data['lastname'],
        update_customer.email = data['email'],
        update_customer.contact_number = data['contact_number'],
        update_customer.gender = data['gender'],
        update_customer.password = data['password']
        db.session.commit()
        response_object = {
            'status':'success',
            'message':'Customer updated successfully!'
        }
        return response_object, 202


# def generate_token(customer):
#     try:
#         # generate the auth token
#         auth_token = customer.encode_auth_token(customer.customer_id)
#         response_object = {
#             'status': 'success',
#             'message': 'Successfully logged in.',
#             'Authorization': auth_token.decode()
#         }
#         return response_object, 201
#     except Exception as e:
#         response_object = {
#             'status': 'fail',
#             'message': 'Some error occurred. Please try again.'
#         }
#         return response_object, 401

# def current_customer(auth_token):
#     data = jwt.decode(auth_token, key)
#     if not data:
#         response_object = {
#             'status': 'fail',
#             'message': 'Customer not Found'
#         } 
#         return response_object, 404
#     else:
#         print(data['sub'])
#         # customer = int(data)
#         # print(customer)
#         return Customer.query.filter_by(customer_id = data['sub']).first()

def current_customer(auth_header):
    if auth_header == None:
        response_object = {
            'status':'fail',
            'message':'Data not found.'
        }
        return response_object, 400
    else:
        # strdata = str(auth_header)
        # auth_token = strdata.split(".")[1]
        identifier = Customer.decode_auth_token(auth_header)
        return identifier    
   
    #     response_object = {
    #         'status':'fail',
    #         'message':'token not passed'
    #     }
    #     return response_object, 401
    # else:
    #     return Customer.query.filter_by(customer_id=result).first()

def book_a_reservation(data):
    current_reservation = Reservation.query.filter_by(reservee=data['reservee']).first()
    if not current_reservation:
        new_reservation = Reservation(
            reservee = data['reservee'],
            number_of_persons = data['number_of_persons'],
            booking_date = datetime.datetime.now(),
            customer_account = data['customer_account'],
            restaurant = data['restaurant']
        )
        save_changes(new_reservation)
        response_object = {
            'status':'success',
            'message':'Reservation created.'
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'Reservation already exists.'
        }
        return response_object, 409

def cancel_reservation(data):
    db.session.delete(data)
    db.session.commit()
    response_object = {
        'status': 'success',
        'message': 'Reservation canceled.'
    }
    return response_object, 203


def get_all_customers():
    return Customer.query.all()


def get_a_customer(username):
    return Customer.query.filter_by(username=username).first()

def get_customer_id(cust_id):
    print(cust_id)
    cur_cus = Customer.query.filter_by(customer_id=cust_id).first()
    # print(cur_cus.firstname)
    # print(cur_cus.gender)
    # print(cur_cus.customer_id)
    # print(cur_cus)
    # result = cur_cus.customer_id
    return cur_cus 

def get_customer_reservation(reservee):
    return Reservation.query.filter_by(reservee=reservee).first()

def get_reservation(reservation_id):
    return Reservation.query.filter_by(reservation_id=reservation_id).first()

def save_changes(data):
    db.session.add(data)
    db.session.commit()