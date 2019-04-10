from functools import wraps
from flask import request
from app.main.service.auth_helper import OwnerAuth
from app.main.service.customer_login_helper import Auth

def owner_token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):

        data, status = OwnerAuth.get_logged_in_owner(request)
        token = data.get('data')

        if not token:
            return data, status 

        return f(*args, **kwargs)
 
    return decorated

def customer_token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):

        data, status = Auth.get_logged_in_customer(request)
        token = data.get('data')

        if not token:
            return data, status 

        return f(*args, **kwargs)
 
    return decorated

def admin_token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):

            token = None

            if 'X-Fields' in request.headers:
                token = request.headers['X-Fields']
            
            if not token:
                return {'message': 'Token is missing.'}, 401

            if token != 'admintoken':
                return {'message': 'Invalid Token'}
            else:
                print('TOKEN: {}'.format(token))
                return f(*args, **kwargs)
        
    return decorated
    #     data, status = Auth.get_logged_in_customer(request)
    #     token = data.get('data')

    #     if not token:
    #         return data, status

    #     admin = token.get('admin')
    #     if not admin:
    #         response_object = {
    #             'status': 'fail',
    #             'message': 'admin token required'
    #         }
    #         return response_object, 401

    #     return f(*args, **kwargs)

    # return decorated