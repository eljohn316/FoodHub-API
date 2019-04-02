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
            'message': 'Restaurant successfully created.'
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'Restaurant already exists.'
        }
        return response_object, 409

def update_restaurant(data):
    update_restaurant = Restaurant.query.filter_by(restaurant_name=data['restaurant_name']).first()
    if not update_restaurant:
        response_object = {
            'status': 'fail',
            'message': 'Restaurant not found'
        }
        return response_object, 409
    else:
        update_restaurant.restaurant_name = data['restaurant_name']
        update_restaurant.restaurant_type = data['restaurant_type']
        update_restaurant.bio = data['bio']
        update_restaurant.locations = data['locations']
        db.session.commit()
        response_object = {
            'status': 'success',
            'message': 'Restaurant successfully updated.'
        }
        return response_object, 202

# def delete_restaurant(data):
#     restaurant = Restaurant.query.filter_by(restaurant_name=data['restaurant_name']).first()
#     if not restaurant:
#         response_object = {
#             'status': 'fail',
#             'message': 'Restaurant not found.'
#         } 
#         return response_object, 409
#     else:    
#         db.session.delete(restaurant)
#         db.session.commit()
#         response_object = {
#             'status':'success',
#             'message':'Restaurant deleted.'
#         }
#         return response_object, 203

def delete_restaurant(data):
    db.session.delete(data)
    db.session.commit()
    response_object = {
        'status': 'success',
        'message': 'Restaurant deleted.'
    }
    return response_object, 203

def add(data):
    db.session.add(data)
    db.session.commit()

def all_restaurants():
    return Restaurant.query.all()

def get_restaurant(restaurant_name):
    return Restaurant.query.filter_by(restaurant_name=restaurant_name).first()