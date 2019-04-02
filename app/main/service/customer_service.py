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