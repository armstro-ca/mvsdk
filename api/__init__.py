import requests
import json
import unittest
from unittest import mock
from urllib.parse import urlencode


def create_params(**kwargs):
    '''
    Used to create url parameters for API call
    '''
    url = kwargs.get("url")
    params = kwargs.get("params")
    if params:
        query_string = urlencode(eval(params))
    return f'{url}?{query_string}'

def mocked_requests_get(url, headers, data):
    class MockResponse:
        def __init__(self, url, headers, status_code):
            self.verb = "GET"
            self.url = url
            self.headers = headers
            self.data = data
            self.status_code = status_code

        def json(self):
            return {
                "verb": self.verb,
                "url": self.url,
                "headers": self.headers,
                "data": self.data
            }

    return MockResponse(url, headers, 200)

class APIRequester:
    '''
    Used to make the request
    '''
    def __init__(self, **kwargs):

        self.method = kwargs.get("method")
        self.url = kwargs.get("url")
        self.headers = kwargs.get("headers")
        self.data = kwargs.get("data")
    
    #@mock.patch('requests.get', side_effect=mocked_requests_get)
    #def get(self, mock_get):
    def get(self):
        response = requests.get(
                self.url,
                headers=self.headers,
                data=self.data
            )
        return response
    
    #@mock.patch('requests.post', side_effect=mocked_requests_get)
    #def post(self, mock_get):
    def post(self):
        response = requests.post(
                self.url,
                headers=self.headers,
                data=self.data
            )
        return response

class PathBuilder:
    '''
    Used to build the correct API path that includes
    parameters & filters
    '''
    def __init__(self, **kwargs):
        self.base_url = kwargs.get('base_url')
        self.domain = kwargs.get('domain')
        self.version = kwargs.get('version')
        self.object_id = kwargs.get("object_id")
        self.domain_id = kwargs.get("domain_id")
        self.domain_action = kwargs.get("domain_action")
        self.params = kwargs.get('params')
        
    def build(self):
        paths = {
            "domains":{
                "asset": {
                    "path": 'assets'
                },
                "attribute": {
                    "path": f'{self.version}/attributes',
                    "name": None
                },
                "branded_portal": {
                    "path": f'{self.version}/brandedportals',
                    "name": None
                },
                "category": {
                    "path": f'{self.version}/categories',
                    "name": None
                },
                "config": {
                    "path": f'{self.version}/config',
                    "name": None
                },
                "connect": {
                    "path": 'connect'
                },
                "crop": {
                    "path": f'{self.version}/crop',
                    "name": None
                },
                "direct_link": {
                    "path": f'{self.version}/directlinks',
                    "name": None
                },
                "download": {
                    "path": f'{self.version}/downloads',
                    "name": None
                },
                "home": {
                    "path": f'{self.version}/',
                    "name": None
                },
                "introduction_and_help": {
                    "path": f'{self.version}/introductionAndHelp',
                    "name": None
                },
                "keyword_group": {
                    "path": f'{self.version}/keywordGroups',
                    "name": None
                },
                "keyword": {
                    "path": f'{self.version}/keywords',
                    "name": None
                },
                "notification": {
                    "path": f'{self.version}/notification',
                    "name": None
                },
                "org_unit": {
                    "path": f'{self.version}/organizationalUnits',
                    "name": None
                },
                "reports": {
                    "path": f'{self.version}/reports',
                    "name": None
                },
                "saved_searche": {
                    "path": f'{self.version}/savedsearches',
                    "name": None
                },
                "search": {
                    "path": f'{self.version}/search',
                    "name": None
                },
                "share": {
                    "path": f'{self.version}/share',
                    "name": None
                },
                "public": {
                    "path": f'{self.version}/public',
                    "name": None
                },
                "upload": {
                    "path": f'{self.version}/uploads',
                    "name": None
                },
                "user_group": {
                    "path": f'{self.version}/groups',
                    "name": None
                },
                "user": {
                    "path": f'{self.version}/users',
                    "name": None
                }
            }
        }
        domain_info = paths['domains'][self.domain]
        sections = [domain_info['path']]
        if self.domain_action:
            sections.append(self.domain_action)
        if self.object_id:
            sections.append(self.object_id)
        
        
        path = f'/{"/".join(sections)}'
        url = f'{self.base_url}{path}'
        
        #manage params and filtering
        params = {}
        operators = ["e", "lt", "lte", "gt", "gte"]
        for param in self.params.keys():
            if param in operators:
                params['account.id'] = f'{param}:{self.params[param]}'
            else:
                params[param] = self.params[param]
        if params:
            url = create_params(params=json.dumps(params), url=url)

        return [path, url]