from flask import request
from flask_restplus import Resource

from ..util.dto import *
from ..service.menu_service import *

api = MenuDto.api
item_api = ItemDto.api

_menu = MenuDto.menu
_item = ItemDto.menu_item

@api.route('/')
class MenuList(Resource):
    @api.doc('list_of_all_menu')
    @api.marshal_list_with(_menu, envelope='Menu')
    def get(self):
        """List of all menu"""
        return all_menu()

    @api.response(201,'Menu successfully created.')
    @api.doc('Create a menu')
    @api.expect(_menu, validate=True)
    def post(self):
        """Creates a new menu"""
        data = request.json
        return add_menu(data=data)
    
@api.route('/<menu_name>')
@api.param('menu_name','Menu identifier')
@api.response(404,'Menu not found.')
class Menu(Resource):
    @api.doc('get a menu')
    @api.marshal_with(_menu)
    @api.response(404,'Menu not found.')
    def get(self, menu_name):
        """Get menu"""
        menu = get_menu(menu_name)
        if not menu:
            api.abort(404,'Menu not found.')
        else:
            return menu

    @api.response(203,'Menu successfully deleted.')
    @api.doc('delete a Menu')
    @api.response(404,'Menu not found.')
    def delete(self, menu_name):
        """Delete an existing menu"""
        menu = get_menu(menu_name)
        if not menu:
            api.abort(404,'Menu not found.')
        else:
            return delete_menu(menu)
    
    @api.response(202,'Menu successfully updated.')        
    @api.doc('update a menu')
    @api.expect(_menu, validate=True)
    def put(self, menu_name):
        """Update an existing menu"""
        data = request.json
        return update_menu(data=data, menu_name=menu_name)

@api.route('/<int:owner>')
@api.param('owner','Owner identifier')
@api.response(404,'Owner does not exist.')
class MenuOwned(Resource):
    """Get menu by owner"""
    @api.doc('get menu by owner')
    @api.marshal_with(_menu)
    @api.response(404,'Owner does not exist.')
    def get(self, owner):
        result = menu_owned(owner)
        if not result:
            api.abort(404,'Owner does not exist.')
        return result

@api.route('/item')
class Item(Resource):
    @api.response(201,'Item added successfully')
    @api.response(409,'Item already exists')
    @api.doc('Create an item')
    @api.expect(_item, validate=True)
    def post(self):
        """Add an item"""
        data = request.json
        return add_item(data=data)
        