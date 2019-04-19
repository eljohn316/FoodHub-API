from flask_restplus import Resource

from ..service.reservation_service import *
from ..util.dto import ReservationDto
from ..service.reservation_service import *

api = ReservationDto.api
_reservation = ReservationDto.reservation

@api.route('/')
@api.response(404, 'No reservation found.')
class ReservationList(Resource):
    @api.doc('list_of_all_reservations')
    @api.marshal_with(_reservation, envelope='Reservations')
    def get(self):
        """List of all reservations"""
        return all_reservations()
    