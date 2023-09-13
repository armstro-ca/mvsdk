import logging
from json import JSONDecodeError

from mvsdk.api import PathBuilder, APIRequester


class Client(object):
    """
    A client for accessing the MVAPI.
    """
    def __init__(self):

        self.base_url = 'mv-api-whistler.mediavalet.com'
        self.auth_url = 'iam-qa.mediavalet.com'

        # Domains
        self._asset = None
        self._bulk = None
        self._connect = None
        self._keyword = None

    def request(self, method, base_url, domain, object_id=None,
                object_action=None, domain_id=None, domain_action=None,
                params=None, data=None, headers=None, auth=None, bulk=None, **kwargs):

        headers = headers or {}
        params = params or {}
        data = data or {}
        method = method.upper()
        bulk = bulk or False

        headers['User-Agent'] = 'MediaValetSDK/0.0.4'
        headers['Host'] = base_url or self.base_url
        if auth:
            headers['Authorization'] = f'Bearer {auth}'

        uri, url = PathBuilder(base_url=base_url, domain=domain, object_id=object_id,
                               object_action=object_action, domain_id=domain_id,
                               domain_action=domain_action, params=params).build()

        if bulk:
            return {
                'method': method,
                'uri': uri,
                'headers': headers,
                'data': data
            }

        api = APIRequester(url=url, headers=headers, data=data, **kwargs)

        if method == 'GET':
            response = api.get()
        elif method == 'POST':
            response = api.post()
        elif method == 'DELETE':
            response = api.delete()
        else:
            response = {'status_code': "405", 'json': "Verb not allowed"}

        logging.debug(response.headers)
        logging.debug(response.text)

        try:
            response_status_code = response.status_code
            response_json = response.json()

            return {
                "status": response_status_code,
                "json": response_json
            }
        except (JSONDecodeError, KeyError) as ex:
            logging.debug('%s exception thrown while handling response:\n%s',
                          type(ex).__name__, ex.args)
            return {
                "status": response.status_code,
                "json": {response.text}
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
    def bulk(self):
        """
        Access the MVAPI Bulk API
        """
        if self._bulk is None:
            from mvsdk.rest.bulk import Bulk
            self._bulk = Bulk(self, self.base_url, 'bulk')
        return self._bulk

    @property
    def connect(self):
        """
        Access the MVAPI Connect API
        """
        if self._connect is None:
            from mvsdk.rest.connect import Connect
            self._connect = Connect(self, self.auth_url, 'connect')
        return self._connect

    @property
    def keyword(self):
        """
        Access the MVAPI Keyword API
        """
        if self._keyword is None:
            from mvsdk.rest.keyword import Keyword
            self._keyword = Keyword(self, self.base_url, 'keyword')
        return self._keyword
