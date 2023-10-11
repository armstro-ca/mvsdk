import os
from mvsdk.rest import Client


class Auth:
    def __init__(self):

        self.sdk_handle = Client()

        data = {
                'grant_type': 'password',
                'username': os.getenv('MVUSERNAME'),
                'password': os.getenv('MVPASSWORD'),
                'scope': 'openid api offline_access'
            }

        auth = {
                'client_id': os.getenv('MVCLIENTID'),
                'client_secret': os.getenv('MVCLIENTSECRET')
            }

        self.session = self.sdk_handle.connect.auth(
            data=data,
            auth=auth
            )
        
    def get_session(self):
        return self.session
