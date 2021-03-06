from flask import request
from flask_restplus import Resource
from app.main.util.decorator import owner_token_required

from ..util.dto import *
from ..service.owner_service import *

api = OwnerDto.api
response_api = ResponseDto.api
reservation_api = ReservationDto

_owner = OwnerDto.owner
_response = ResponseDto.response
_reservation = ReservationDto.reservation


@api.route('/reservation')
class ReservationList(Resource):
    
    @owner_token_required
    @api.doc('list_of_all_owner_reservations')
    @api.marshal_list_with(_reservation, envelope='Reservations')
    def get(self):
         """ List of all owner responses. """
         return reservation_list()

@api.route('/')
class OwnerList(Resource):
    @owner_token_required
    @api.doc('list_of_registered_owners')
    @api.marshal_list_with(_owner, envelope='Owners')
    def get(self):
        """List all registered owners"""
        return get_all_owners()

    @api.response(201, 'Owner successfully created.')
    @api.response(409, 'Owner already exists.')
    @api.doc('create a new owner')
    @api.expect(_owner, validate=True)
    def post(self):
        """Creates a new Owner """
        data = request.json
        return save_new_owner(data=data)


@api.route('/<username>')
@api.param('username', 'The Owner identifier')
@api.response(404, 'Owner not found.')
class Owner(Resource):
    @owner_token_required
    @api.doc('get a owner')
    @api.marshal_with(_owner, envelope='Owner')
    def get(self, username):
        """get a owner given its identifier"""
        owner = get_a_owner(username)
        if not owner:
            api.abort(404,'Owner not found.')
        return owner

@api.route('/current')
class CurrentOwner(Resource):
    """
    Current User Resouorce
    """
    @api.marshal_with(_owner, envelope='Owner')
    @api.doc('get current user')
    def get(self):
        auth_header = request.headers.get('Authorization')
        print('------------')
        print(auth_header)
        own_id = current_owner(auth_header)
        print('................')
        print(own_id)
        print('own_id   ')
        
        return get_owner_id(own_id)

@api.route('/response')
class OwnerResponse(Resource):
    """
    Owner Response
    """
    @owner_token_required
    @api.doc('Owner response')
    @api.response(201, 'Response successful.')
    @api.response(409, 'Response already exists.')
    @api.expect(_response, validate=True)
    def post(self):
        """ Owner Response """
        data = request.json
        return response(data=data)

