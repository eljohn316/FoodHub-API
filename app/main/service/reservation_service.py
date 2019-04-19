import datetime

from app.main import db
from app.main.model.models import *

def create_reservation(data):
    current_reservation = Reservation.query.filter_by().first()




def add_reservation(data):
    db.session.add(data)
    db.session.commit()

def all_reservations():
    return Reservation.query.all()