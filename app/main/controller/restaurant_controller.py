from flask import request
from flask_restplus import Resource

from ..util.dto import RestaurantDto
from ..service.restaurant_service import add_restaurant, update_restaurant, delete_restaurant, get_restaurant, all_restaurants, restaurant_owned, get_restaurant_id

api = RestaurantDto.api
_restaurant = RestaurantDto.restaurant

@api.route('/')
class RestaurantList(Resource):
    @api.doc('list_of_all_restaurants')
    @api.marshal_list_with(_restaurant, envelope='Restaurants')
    def get(self):
        """List all restaurants"""
        return all_restaurants()

    @api.response(201,'Restaurant successfully created.')
    @api.doc('Create a restaurant')
    @api.expect(_restaurant, validate=True)
    def post(self):
        """Creates a new restaurant"""
        data = request.json
        return add_restaurant(data=data)
    

@api.route('/<restaurant_name>')
@api.param('restaurant_name','Restaurant identifier')
@api.response(404,'Restaurant not found.')
class Restaurant(Resource):
    @api.doc('get a restaurant')
    @api.marshal_with(_restaurant)
    @api.response(404,'Restaurant not found.')
    def get(self, restaurant_name):
        """Get restaurant"""
        restaurant = get_restaurant(restaurant_name)
        if not restaurant:
            api.abort(404,'Restaurant not found.')
        else:
            return restaurant

    @api.response(203,'Restaurant successfully deleted.')
    @api.doc('delete a restaurant')
    @api.response(404,'Restaurant not found.')
    def delete(self, restaurant_name):
        """Delete an existing restaurant"""
        restaurant = get_restaurant(restaurant_name)
        if not restaurant:
            api.abort(404,'Restaurant not found.')
        else:
            return delete_restaurant(restaurant)
    
    @api.response(202,'Restaurant successfully updated.')        
    @api.doc('update a restaurant')
    @api.expect(_restaurant, validate=True)
    def put(self, restaurant_name):
        """Update an existing restaurant"""
        data = request.json
        return update_restaurant(data=data, restaurant_name=restaurant_name)

@api.route('/<int:owner>/owner')
@api.param('owner','Owner identifier')
@api.response(404,'Owner does not exist.')
class RestaurantOwned(Resource):
    """Get restaurant by owner"""
    @api.doc('get restaurant by owner')
    @api.marshal_with(_restaurant)
    @api.response(404,'Owner does not exist.')
    def get(self, owner):
        result = restaurant_owned(owner)
        if not result:
            api.abort(404,'Owner does not exist.')
        return result


@api.route('/<restaurant_id>')
@api.param('restaurant_id', 'Restaurant finder')
@api.response(404, 'Restaurant not found.')
class Restaurant(Resource):
    @api.doc('get a restaurant through ID')
    @api.marshal_with(_restaurant)
    @api.response(404, 'Restaurant not found.')
    def get(self, restaurant_id):
        """Get restaurant"""
        restaurant = get_restaurant_id(restaurant_id)
        if not restaurant:
            api.abort(404, 'Restaurant not found.')
        else:
            return restaurant
