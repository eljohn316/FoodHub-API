from flask_restplus import Namespace, fields


class OwnerDto:
    api = Namespace('owner', description='owner related operations')
    owner = api.model('owner', {
        'username': fields.String(required=True, description='owner username'),
        'password': fields.String(required=True, description='owner password'),
        'firstname': fields.String(required=True, description='owner firstname'),
        'lastname': fields.String(required=True, description='owner lastname'),
        'contact_number': fields.String(required=True, description='owner contact number'),
        'gender': fields.String(required=True, description='owner gender')
    })

class CustomerDto:
    api = Namespace('customer', description='customer related operations')
    customer = api.model('customer', {
        'username': fields.String(required=True, description='customer username'),
        'password': fields.String(required=True, description='customer password'),
        'firstname': fields.String(required=True, description='customer firstname'),
        'lastname': fields.String(required=True, description='customer lastname'),
        'contact_number': fields.String(required=True, description='customer contact number'),
        'gender': fields.String(required=True, description='customer gender')
    })

class AuthDto:
    api = Namespace('auth', description='authentication related operations')
    owner_auth = api.model('auth_details', {
        'username': fields.String(required=True, description='owner username '),
        'password': fields.String(required=True, description='owner password '),
    })