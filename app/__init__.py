# app/__init__.py

from flask_restplus import Api
from flask import Blueprint

from .main.controller.owner_controller import api as owner_ns
from .main.controller.customer_controller import api as customer_ns
from .main.controller.auth_controller import api as auth_ns
from .main.controller.restaurant_controller import api as rest_ns
from .main.controller.customer_login import api as cust_ns
from .main.controller.menu_controller import api as menu_ns
from .main.controller.menu_controller import item_api as item_ns


blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='FOODHUB-API',
          version='1.0',
          description='API for FoodHub App'
          )

api.add_namespace(owner_ns, path='/owner')
api.add_namespace(customer_ns, path='/customer')
api.add_namespace(auth_ns)
api.add_namespace(rest_ns)
api.add_namespace(cust_ns)
api.add_namespace(menu_ns)
api.add_namespace(item_ns, path='/menu')

