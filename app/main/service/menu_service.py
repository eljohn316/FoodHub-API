from app.main import db
from app.main.model.models import *

def add_menu(data):
    menu = Menu.query.filter_by(menu_name=data['menu_name']).first()
    if not menu:
        new_menu = Menu(
            menu_name = data['menu_name']
        )
        add(new_menu)
        response_object = {
            'status': 'success',
            'message': 'Menu successfully created.'
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'Menu already exists.'
        }
        return response_object, 409

def add_item(data):
    current_item = Item.query.filter_by(item_name=data['item_name']).first()
    if not current_item:
        new_item = Item(
            price = data['price'],
            item_name = data['item_name'],
            category = data['category'],
            menu = data['menu']
            )
        add(new_item)
        response_object = {
            'status':'success',
            'message':'Item added successfully'
        }
        return response_object, 201
    else:
        response_object = {
            'status':'fail',
            'message':'Item already exists'
        }
        return response_object, 409

def update_menu(data, menu_name):
    update_menu = Menu.query.filter_by(menu_name=menu_name).first()
    if update_menu == None:
        response_object = {
            'status': 'fail',
            'message': 'Menu not found'
        }
        return response_object, 404
    else:
        update_menu.menu_name = data['menu_name']
        db.session.commit()
        response_object = {
            'status': 'success',
            'message': 'Menu successfully updated.'
        }
        return response_object, 202


def delete_menu(data):
    db.session.delete(data)
    db.session.commit()
    response_object = {
        'status': 'success',
        'message': 'Menu deleted.'
    }
    return response_object, 203

def menu_owned(owner):
    return Menu.query.filter_by(owner=owner).all()
    
def add(data):
    db.session.add(data)
    db.session.commit()

def all_menu():
    return Menu.query.all()

def get_menu(menu_name):
    return Menu.query.filter_by(menu_name=menu_name).first()
