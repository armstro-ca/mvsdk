import os
import json
from urllib.parse import urlencode
import requests
from mvsdk.api import PathBuilder, APIRequester

class Client(object):
    """ 
    A client for accessing the MVAPI. 
    """
    def __init__(self):

        self.base_url = os.getenv('MVAPIPATH') or 'https://api.mediavalet.com'
        
        # Domains
        self._asset = None
        self._keyword = None



    def request(self, method, base_url, domain, profile_id=None, 
        domain_id=None, domain_action=None, params=None, data=None, headers=None, auth=None):

        headers = headers or {}
        params = params or {}
        method = method.upper()

        path, url = PathBuilder(base_url=base_url, domain=domain, profile_id=profile_id,
            domain_id=domain_id, domain_action=domain_action, params=params).build()

        print(f'Endpoint (url): \n{url}\n\n')
        api = APIRequester(url = url)
        response = api.get()

        print(
            f'Response:\nStatus:\n{response.status_code}\nJson Response:\n{response.json()}'
        )
        json_response = response.json()
        return {
            "status": response.status_code,
            "json": json_response
        }
         
    @property
    def asset(self):
        """
        Access the MVAPI Asset API
        """
        if self._asset is None:
            from mvsdk.rest.asset import Asset
            self._asset = Asset(self, self.base_url, 'asset')
        return self._asset
    
    @property
    def keyword(self):
        """
        Access the MVAPI Keyword API
        """
        if self._keyword is None:
            from mvsdk.rest.keyword import Keyword
            self._keyword = Keyword(self, self.base_url, 'keyword')
        return self._asset