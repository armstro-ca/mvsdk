import unittest
import os

from mvsdk.rest import Client


class TestAuth(unittest.TestCase):

    def setUp(self):
        self.client_id = os.getenv('MVCLIENTID')
        self.client_secret = os.getenv('MVCLIENTSECRET')
        self.username = os.getenv('MVUSERNAME')
        self.password = os.getenv('MVPASSWORD')

        self.sdk_handle = Client()

    def test_password(self):
        data = {
                'grant_type': 'password',
                'username': self.username,
                'password': self.password,
                'scope': 'openid api offline_access'
            }

        auth = {
                'client_id': self.client_id,
                'client_secret': self.client_secret
            }
        
        response = self.sdk_handle.connect.auth(
                data=data,
                auth=auth
                )
                
        self.assertEqual(response['status'], 200)
