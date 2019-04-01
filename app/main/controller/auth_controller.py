from flask import request
from flask_restplus import Resource

from app.main.service.auth_helper import Auth
from ..util.dto import AuthDto

api = AuthDto.api
owner_auth = AuthDto.owner_auth


@api.route('/login')
class OwnerLogin(Resource):
    """
        Owner Login Resource
    """
    @api.doc('owner login')
    @api.expect(owner_auth, validate=True)
    def post(self):
        # get the post data
        post_data = request.json
        return Auth.login_owner(data=post_data)


@api.route('/logout')
class LogoutAPI(Resource):
    """
    Logout Resource
    """
    @api.doc('logout a user')
    def post(self):
        # get auth token
        auth_header = request.headers.get('Authorization')
        return Auth.logout_owner(data=auth_header)