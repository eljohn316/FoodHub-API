from app.main.model.models import *
from ..service.blacklist_service import save_token


class Auth:

    @staticmethod
    def login_owner(data):
        try:
            # fetch the user data
            owner = Owner.query.filter_by(username=data.get('username')).first()
            owner_id = Owner.query.filter_by(owner_id=data.get('owner_id')).first()
            if owner and owner.check_password(data.get('password')):
                auth_token = owner.encode_auth_token(owner_id)
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
    def logout_owner(data):
        if data:
            auth_token = data.split(" ")[1]
        else:
            auth_token = ''
        if auth_token:
            resp = Owner.decode_auth_token(auth_token)
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
                'message': 'Provide a valid auth token.'
            }
            return response_object, 403
    
    @staticmethod
    def get_logged_in_owner(new_request):
            # get the auth token
            auth_token = new_request.headers.get('Authorization')
            if auth_token:
                resp = Owner.decode_auth_token(auth_token)
                if not isinstance(resp, str):
                    owner = Owner.query.filter_by(owner_id=resp).first()
                    response_object = {
                        'status': 'success',
                        'data': {
                            'username': owner.username,
                            'password': owner.password
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
                    'message': 'Provide a valid auth token.'
                }
                return response_object, 401
