import os
from mvsdk.api import PathBuilder, APIRequester

#import json
#from urllib.parse import urlencode
#import requests

class Client(object):
    """ 
    A client for accessing the MVAPI. 
    """
    def __init__(self):

        self.base_url = os.getenv('MVAPIPATH') or 'https://api.mediavalet.com'
        
        # Domains
        self._asset = None
        self._connect = None
        self._keyword = None



    def request(self, method, base_url, domain, object_id=None, 
        domain_id=None, domain_action=None, params=None, data=None, headers=None, auth=None):

        headers = headers or {}
        params = params or {}
        data = data or {}
        method = method.upper()

        path, url = PathBuilder(base_url=base_url, domain=domain, object_id=object_id,
            domain_id=domain_id, domain_action=domain_action, params=params).build()

        print(f'Endpoint (url): \n{url}\n\n')
        api = APIRequester(url = url, headers = headers, data = data)
        
        if method == 'GET':
            response = api.get()
        elif method == 'POST':
            response = api.post()
        else:
            response = {'status_code': "900", 'json': "Verb did not match"}

        #print(f'Response:\nStatus:\n{response.status_code}')
        #print(f'Json Response:\n{response.json()}')
        
        if response.status_code is 200:
            return {
                "status": response.status_code,
                "json": response.json()
            }
        else:
            return {
                "status": response.status_code,
                "json": {}
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
    def connect(self):
        """
        Access the MVAPI Connect API
        """
        if self._connect is None:
            from mvsdk.rest.connect import Connect
            self._connect = Connect(self, self.base_url, 'connect')
        return self._connect
    
    @property
    def keyword(self):
        """
        Access the MVAPI Keyword API
        """
        if self._keyword is None:
            from mvsdk.rest.keyword import Keyword
            self._keyword = Keyword(self, self.base_url, 'keyword')
        return self._asset