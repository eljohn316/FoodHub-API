import unittest
import datetime

from app.main import db
from app.main.model.customer import Customer
from app.test.base import BaseTestCase


class TestUserModel(BaseTestCase):

    def test_encode_auth_token(self):
        customer = Customer(
            customer_id = '1',
            username = 'john',
            password = 'password',
            firstname = 'johnny',
            lastname = 'solomon',
            contact_number = '09123456789',
            gender = 'gay'
        )
        db.session.add(customer)
        db.session.commit()
        auth_token = customer.encode_auth_token(customer.customer_id)
        self.assertTrue(isinstance(auth_token, bytes))

    def test_decode_auth_token(self):
        customer = Customer(
            customer_id = '1',
            username = 'john',
            password = 'password',
            firstname = 'johnny',
            lastname = 'solomon',
            contact_number = '09123456789',
            gender = 'gay'
        )
        db.session.add(customer)
        db.session.commit()
        auth_token = customer.encode_auth_token(customer.customer_id)
        self.assertTrue(isinstance(auth_token, bytes))
        self.assertTrue(Customer.decode_auth_token(auth_token.decode("utf-8") ) == 1)


if __name__ == '__main__':
    unittest.main()