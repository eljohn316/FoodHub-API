# app/__init__.py

from flask_restplus import Api
from flask import Blueprint

from .main.controller.owner_controller import api as owner_ns
from .main.controller.auth_controller import api as auth_ns
from .main.controller.restaurant_controller import api as rest_ns
from .main.controller.customer_login import api as cust_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='FoodHub-API')

api.add_namespace(owner_ns, path='/owner')
api.add_namespace(auth_ns)
api.add_namespace(rest_ns)
api.add_namespace(cust_ns)