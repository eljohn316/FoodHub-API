from app.main import db
from app.main.model.restaurant import Restaurant

def add_restaurant(data):
    restaurant = Restaurant.query.filter_by(restaurant_name=data['restaurant_name']).first()
    if not restaurant:
        new_restaurant = Restaurant(
            restaurant_name = data['restaurant_name'],
            restaurant_type = data['restaurant_type'],
            bio = data['bio'],
            locations = data['locations']
        )
        add(new_restaurant)
        response_object = {
            'status': 'success',
            'message': 'Successfully added.'
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'Restaurant already exists.',
        }
        return response_object, 409

def add(data):
    db.session.add(data)
    db.session.commit()

def all_restaurants():
    return Restaurant.query.all()

def get_restaurant(restaurant_name):
    return Restaurant.query.filter_by(restaurant_name=restaurant_name).first()