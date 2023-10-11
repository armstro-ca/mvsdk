import os
from mvsdk.rest import Client

from icecream import ic


class Auth:
    def __init__(self):

        auth_url = ic(os.getenv('MVAPIAUTHURL'))
        base_url = ic(os.getenv('MVAPIBASEURL'))

        self.sdk_handle = Client(auth_url=auth_url, base_url=base_url)

        data = ic({
                'grant_type': 'password',
                'username': os.getenv('MVUSERNAME'),
                'password': os.getenv('MVPASSWORD'),
                'scope': 'openid api offline_access'
            })

        auth = ic({
                'client_id': os.getenv('MVCLIENTID'),
                'client_secret': os.getenv('MVCLIENTSECRET')
            })

        self.session = self.sdk_handle.connect.auth(
            data=data,
            auth=auth
            )
        
    def get_session(self):
        return self.session
