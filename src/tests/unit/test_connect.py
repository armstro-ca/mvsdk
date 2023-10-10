import unittest
import os

from mvsdk.rest import Client
from auth import Auth


class TestAuth(unittest.TestCase):

    def setUp(self):
        self.client_id = os.getenv('MVCLIENTID')
        self.client_secret = os.getenv('MVCLIENTSECRET')
        self.username = os.getenv('MVUSERNAME')
        self.password = os.getenv('MVPASSWORD')

        self.sdk_handle = Client()

    def test_password(self):
        self.session = Auth().get_session()
                
        self.assertEqual(self.session.status_code, 200)
