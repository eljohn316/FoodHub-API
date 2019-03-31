import uuid
import datetime

from app.main import db
from app.main.model.owner import Owner


def save_new_owner(data):
    owner = Owner.query.filter_by(username=data['username']).first()
    if not owner:
        new_owner = Owner(
            username=data['username'],
            password=data['password'],
            firstname = data['firstname'],
            lastname = data['lastname'],
            contact_number = data['contact_number'],
            gender = data['gender']
        )
        save_changes(new_owner)
        response_object = {
            'status': 'success',
            'message': 'Successfully created.'
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'Owner already exists. Please Log in.',
        }
        return response_object, 409


def get_all_owners():
    return Owner.query.all()


def get_a_owner(username):
    return Owner.query.filter_by(username=username).first()


def save_changes(data):
    db.session.add(data)
    db.session.commit()
