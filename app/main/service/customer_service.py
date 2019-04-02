import datetime

from app.main import db
from app.main.model.customer import Customer

def save_new_customer(data):
    customer = Customer.query.filter_by(username=data['username']).first()
    if not customer:
        new_customer = Customer(
            username=data['username'],
            password=data['password'],
            firstname = data['firstname'],
            lastname = data['lastname'],
            contact_number = data['contact_number'],
            gender = data['gender']
        )
        save_changes(new_customer)
        return generate_token(new_customer)
    else:
        response_object = {
            'status': 'fail',
            'message': 'customer already exists. Please Log in.',
        }
        return response_object, 409

def update_customer(data, username):
    update_customer = Customer.query.filter_by(username=username).first()
    if not update_customer:
        response_object = {
            'status': 'fail',
            'message': 'Customer not found'
        }
        return response_object, 409
    else:
        update_customer.username = data['username']
        update_customer.firstname = data['firstname']
        update_customer.lastname = data['lastname']
        update_customer.gender = data['gender']
        update_customer.contact_number = data['contact_number']
        update_customer.password = data['password']
        db.session.commit()
        response_object = {
            'status': 'success',
            'message': 'Successfully updated'
        }
        return response_object, 202

def generate_token(customer):
    try:
        # generate the auth token
        print('Hi')
        auth_token = customer.encode_auth_token(customer.customer_id)
        print('Hello')
        response_object = {
            'status': 'success',
            'message': 'Successfully logged in.',
            'Authorization': auth_token.decode()
        }
        return response_object, 201
    except Exception as e:
        response_object = {
            'status': 'fail',
            'message': 'Some error occurred. Please try again.'
        }
        return response_object, 401

def get_all_customers():
    return Customer.query.all()


def get_a_customer(username):
    return Customer.query.filter_by(username=username).first()


def save_changes(data):
    db.session.add(data)
    db.session.commit()