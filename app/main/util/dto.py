from flask_restplus import Namespace, fields

class RestaurantDto:
    api = Namespace('restaurant', description='restaurant related operations')
    restaurant = api.model('restaurant', {
        'restaurant_name': fields.String(required=True, description='restaurant name'),
        'restaurant_type': fields.String(required=True, description='restaurant type'),
        'bio': fields.String(required=True, description='restaurant bio'),
        'locations': fields.String(required=True, description='restaurant location/locations')
    })

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

class AuthDto:
    api = Namespace('owner', description='owner login')
    owner_auth = api.model('login details', {
        'username': fields.String(required=True, description='owner username '),
        'password': fields.String(required=True, description='owner password ')
    })

class CustomerLoginDto:
    api = Namespace('customer', description='customer login')
    customer_auth = api.model('login details', {
        'username': fields.String(required=True, description='customer username '),
        'password': fields.String(required=True, description='customer password ')
    })
