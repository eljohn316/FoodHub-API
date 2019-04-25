import datetime

from app.main import db
from app.main.model.models import *

def create_reservation(data):
    current_reservation = Reservation.query.filter_by(reservee=data['reservee']).first()
    if not current_reservation:
        new_reservation = Reservation(
            reservee = data['reservee'],
            pax_number = data['pax_number'],
            booking_date = datetime.datetime.utcnow(),
            customer_account = data['customer_account'],
            restaurant = data['restaurant']
        )
        add_reservation(new_reservation)
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


def add_reservation(data):
    db.session.add(data)
    db.session.commit()

def all_reservations():
    return Reservation.query.all()

    