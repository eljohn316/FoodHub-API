from app.main.model.models import *
from ..service.blacklist_service import save_token

class Auth:

    @staticmethod
    def login_customer(data):
        try:
            # fetch the user data
            customer = Customer.query.filter_by(username=data.get('username')).first()
            customer_id = Customer.query.filter_by(customer_id=data.get('customer_id')).first()
            if customer and customer.check_password(data.get('password')):
                auth_token = customer.encode_auth_token(customer_id)
                if auth_token:
                    response_object = {
                        'status': 'success',
                        'message': 'Successfully logged in.',
                        'Authorization': auth_token.decode()
                    }
                    return response_object, 200
            else:
                response_object = {
                    'status': 'fail',
                    'message': 'username or password does not match.'
                }
                return response_object, 401

        except Exception as e:
            print(e)
            response_object = {
                'status': 'fail',
                'message': 'Try again'
            }
            return response_object, 500

    @staticmethod
    def logout_customer(data):
        auth_token = data
        # if data:
        #     auth_token = data.split(".")[1]
        # else:
        #     auth_token = ''
        if auth_token:
            resp = Customer.decode_auth_token(auth_token)
            if not isinstance(resp, str):
                # mark the token as blacklisted
                return save_token(token=auth_token)
            else:
                response_object = {
                    'status': 'fail',
                    'message': resp
                }
                return response_object, 401
        else:
            response_object = {
                'status': 'fail',
                'message': 'Token is missing. Provide a valid token.'
            }
            return response_object, 403
    
    @staticmethod
    def get_logged_in_customer(new_request):
            # get the auth token
            auth_token = new_request.headers.get('Authorization')
            if auth_token:
                resp = Customer.decode_auth_token(auth_token)
                if not isinstance(resp, str):
                    customer = Customer.query.filter_by(customer_id=resp).first()
                    username = Customer.query.filter_by(username=resp).first()
                    password = Customer.query.filter_by(password=resp).first()
                    response_object = {
                        'status': 'success',
                        'data': {
                            'username': username,
                            'password': password
                        }
                    }
                    return response_object, 200
                response_object = {
                    'status': 'fail',
                    'message': resp
                }
                return response_object, 401
            else:
                response_object = {
                    'status': 'fail',
                    'message': 'Token is missing. Provide a valid token.'
                }
                return response_object, 401