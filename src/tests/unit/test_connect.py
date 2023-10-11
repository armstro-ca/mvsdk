import unittest
import os

from tests.auth import Auth
from mvsdk.rest import Client


class TestAuth(unittest.TestCase):

    def setUp(self):
        self.client_id = os.getenv('MVCLIENTID')
        self.client_secret = os.getenv('MVCLIENTSECRET')
        self.username = os.getenv('MVUSERNAME')
        self.password = os.getenv('MVPASSWORD')

        auth_url = os.getenv('MVAPIAUTHURL')
        base_url = os.getenv('MVAPIBASEURL')

        self.sdk_handle = Client(auth_url=auth_url, base_url=base_url)

    def test_password(self):
        self.session = Auth().get_session()
                
        self.assertEqual(self.session.status_code, 200)
