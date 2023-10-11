import os
from mvsdk.rest import Client


class Auth:
    def __init__(self):

        auth_url = os.getenv('MVAPIAUTHURL')
        base_url = os.getenv('MVAPIBASEURL')

        self.sdk_handle = Client(auth_url=auth_url, base_url=base_url)

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
