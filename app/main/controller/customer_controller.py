from flask import request
from flask_restplus import Resource, fields
from app.main.util.decorator import customer_token_required

from ..util.dto import CustomerDto, ReturnDataDto
from ..service.customer_service import save_new_customer, get_all_customers, get_a_customer, update_customer

api = CustomerDto.api
_customer = CustomerDto.customer
_data = ReturnDataDto.returndata

@api.route('/')
class CustomerList(Resource):
    @customer_token_required
    @api.doc('list_of_registered_customers')
    @api.marshal_list_with(_data, envelope='Customers')
    def get(self):
        """List all registered customers"""
        return get_all_customers()

    @api.response(201, 'Customer successfully created.')
    @api.doc('create a new customer')
    @api.expect(_customer, validate=True)
    def post(self):
        """Creates a new Customer """
        data = request.json
        return save_new_customer(data=data)


@api.route('/<username>')
@api.param('username', 'The Customer identifier')
@api.response(404, 'Customer not found.')
class Customer(Resource):
    @customer_token_required
    @api.doc('get a customer')
    @api.response(404, 'Customer not found.')
    @api.marshal_with(_data, envelope='Customer')
    def get(self, username):
        """get a customer given its identifier"""
        customer = get_a_customer(username)
        if not customer:
            api.abort(404, 'Customer not found.')
        else:
            return customer
    
    @api.response(404, 'Customer not found.')
    @api.response(202, 'Customer updated successfully!')
    @api.doc('update a customer')
    @api.expect(_customer, validate=True)
    def put(self, username):
        """ update a customer """
        data = request.json
        return update_customer(data=data, username=username)
        
