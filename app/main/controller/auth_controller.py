from flask import request
from flask_restplus import Resource

from app.main.service.auth_helper import OwnerAuth
from ..util.dto import AuthDto
from app.main.util.decorator import owner_token_required

api = AuthDto.api
owner_auth = AuthDto.owner_auth


@api.route('/login')
class OwnerLogin(Resource):
    """
        owner login Resource
    """
    @api.doc('owner login')
    @api.expect(owner_auth, validate=True)
    def post(self):
        # get the post data
        post_data = request.json
        return OwnerAuth.login_owner(data=post_data)

@owner_token_required
@api.route('/logout')
class LogoutAPI(Resource):
    """
    Logout Resource
    """
    @api.doc('logout a user')
    def post(self):
        # get auth token
        auth_header = request.headers.get('Authorization')
        return OwnerAuth.logout_owner(data=auth_header)