from flask import request
from flask_restplus import Resource

from ..util.dto import OwnerDto
from ..service.owner_service import save_new_owner, get_all_owners, get_a_owner

api = OwnerDto.api
_owner = OwnerDto.owner


@api.route('/')
class OwnerList(Resource):
    @api.doc('list_of_registered_owners')
    @api.marshal_list_with(_owner, envelope='data')
    def get(self):
        """List all registered owners"""
        return get_all_owners()

    @api.response(201, 'Owner successfully created.')
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
    @api.doc('get a owner')
    @api.marshal_with(_owner)
    def get(self, username):
        """get a owner given its identifier"""
        owner = get_a_owner(username)
        if not owner:
            api.abort(404)
        else:
            return owner