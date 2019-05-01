from flask import request
from flask_restplus import Resource, fields
from app.main.util.decorator import customer_token_required
from ..util.dto import *
from ..service.customer_service import *

customer_api = CustomerDto.api
reservation_api = ReservationDto.api

_customer = CustomerDto.customer
_reservation = ReservationDto.reservation

@customer_api.route('/')
class CustomerList(Resource):
    @customer_token_required
    @customer_api.doc('list_of_registered_customers')
    @customer_api.marshal_list_with(_customer, envelope='Customers')
    def get(self):
        """List all registered customers"""
        return get_all_customers()

    @customer_api.response(201, 'Customer successfully created.')
    @customer_api.doc('create a new customer')
    @customer_api.expect(_customer, validate=True)
    def post(self):
        """Creates a new Customer """
        data = request.json
        return save_new_customer(data=data)


@customer_api.route('/<username>')
@customer_api.param('username', 'The Customer identifier')
@customer_api.response(404, 'Customer not found.')
class Customer(Resource):  
    @customer_token_required
    @customer_api.doc('get a customer')
    @customer_api.response(404, 'Customer not found.')
    @customer_api.marshal_with(_customer, envelope='Customer')
    def get(self, username):
        """get a customer given its identifier"""
        customer = get_a_customer(username)
        if not customer:
            customer_api.abort(404, 'Customer not found.')
        else:
            return customer
    
    @customer_api.response(404, 'Customer not found.')
    @customer_api.response(202, 'Customer updated successfully!')
    @customer_api.doc('update a customer')
    @customer_api.expect(_customer, validate=True)
    def put(self, username):
        """ update a customer """
        data = request.json
        return update_customer(data=data, username=username)

@customer_api.route('/current')
class CurrentCustomer(Resource):
    """
    Current User Resouorce
    """
    @customer_api.marshal_with(_customer, envelope='Customer')
    @customer_api.doc('get current user')
    def get(self):
        """ current customer """
        auth_header = request.headers.get('Authorization')
        print("---------------")
        print(auth_header)
        cust_id = current_customer(auth_header)
        print('................')
        print(cust_id)
        
        return get_customer_id(cust_id)

@customer_api.route('/reservation')
class CreateReservation(Resource):
    """
    Customer Reservation
    """
    @customer_api.doc('book_a_reservation')
    @customer_api.response(201, 'Reservation created.')
    @customer_api.expect(_reservation, validate=True)
    def post(self):
        """ book a reservation """
        data = request.json
        return book_a_reservation(data=data)
    
@customer_api.route('/reservation/<reservee>')
@customer_api.param('reservee', 'The Customer identifier')
@customer_api.response(404,'Reservation not found.')
class CustomerReservation(Resource):
    """
    List of reservations by customer.
    """
    @customer_api.doc('get_reservation_by_customer')
    @customer_api.marshal_with(_reservation)
    def get(self, reservee):
        """ view reservation by customer """
        customer = get_customer_reservation(reservee)
        if not customer:
            customer_api.abort(404, 'Reservation not found.') 
        else:
            return customer

@customer_api.response(203,'Reservation canceled.')
@customer_api.response(404,'Reservation not found.')
@customer_api.route('/reservation/<reservation_id>')
@customer_api.param('reservation_id', 'Reservation identifier')
class Reservation(Resource):
    """
    Cancel a reservation.
    """
    @customer_api.doc('cancel a reservation')
    def delete(self, reservation_id):
        """Cancel a reservation"""
        reservation = get_reservation(reservation_id)
        if not reservation:
            customer_api.abort(404,'Reservation not found.')
        else:
            return cancel_reservation(reservation)