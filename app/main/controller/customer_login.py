from flask import request
from flask_restplus import Resource

from app.main.service.customer_login_helper import Auth
from ..util.dto import CustomerLoginDto

api = CustomerLoginDto.api
customer_auth = CustomerLoginDto.customer_auth


@api.route('/login')
class CustomerLogin(Resource):
    """
        Customer Login Resource
    """
    @api.doc('customer login')
    @api.expect(customer_auth, validate=True)
    def post(self):
        # get the post data
        """ customer login """
        post_data = request.json
        return Auth.login_customer(post_data)


@api.route('/logout')
class LogoutAPI(Resource):
    """
    Logout Resource
    """
    @api.doc('logout a customer')
    def post(self):
        # get auth token
        """ customer logout """
        auth_header = request.headers.get('Authorization')
        return Auth.logout_customer(data=auth_header)