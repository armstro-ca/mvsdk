from mvsdk.api import PathBuilder, APIRequester


class Client(object):
    """
    A client for accessing the MVAPI.
    """
    def __init__(self, auth_url: str = None, base_url: str = None):

        self.auth_url = auth_url or 'login.mediavalet.com'
        self.base_url = base_url or 'mv-api-usva.mediavalet.net'

        # Domains
        self._asset = None
        self._attribute = None
        self._bulk = None
        self._category = None
        self._connect = None
        self._direct_link = None
        self._keyword = None
        self._keyword_group = None
        self._org_unit = None
        self._user = None
        self._user_group = None

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

        return response

    @property
    def asset(self):
        """
        Access the MVAPI Asset API
        """
        if self._asset is None:
            from mvsdk.rest.asset import Asset
            self._asset = Asset(self, base_url=self.base_url, domain='asset')
        return self._asset

    @property
    def attribute(self):
        """
        Access the MVAPI Attribute API
        """
        if self._attribute is None:
            from mvsdk.rest.attribute import Attribute
            self._attribute = Attribute(self, base_url=self.base_url, domain='attribute')
        return self._attribute

    @property
    def bulk(self):
        """
        Access the MVAPI Bulk API
        """
        if self._bulk is None:
            from mvsdk.rest.bulk import Bulk
            self._bulk = Bulk(self, base_url=self.base_url, domain='bulk')
        return self._bulk

    @property
    def category(self):
        """
        Access the MVAPI Category API
        """
        if self._category is None:
            from mvsdk.rest.category import Category
            self._category = Category(self, base_url=self.base_url, domain='category')
        return self._category

    @property
    def connect(self):
        """
        Access the MVAPI Connect API
        """
        if self._connect is None:
            from mvsdk.rest.connect import Connect
            self._connect = Connect(self, base_url=self.auth_url, domain='connect')
        return self._connect
    
    @property
    def direct_link(self):
        """
        Access the MVAPI DirectLink API
        """
        if self._direct_link is None:
            from mvsdk.rest.direct_link import DirectLink
            self._direct_link = DirectLink(self, base_url=self.base_url, domain='direct_link')
        return self._direct_link

    @property
    def keyword(self):
        """
        Access the MVAPI Keyword API
        """
        if self._keyword is None:
            from mvsdk.rest.keyword import Keyword
            self._keyword = Keyword(self, base_url=self.base_url, domain='keyword')
        return self._keyword

    @property
    def keyword_group(self):
        """
        Access the MVAPI KeywordGroup API
        """
        if self._keyword_group is None:
            from mvsdk.rest.keyword_group import KeywordGroup
            self._keyword_group = KeywordGroup(self, base_url=self.base_url, domain='keyword_group')
        return self._keyword_group

    @property
    def org_unit(self):
        """
        Access the MVAPI OrgUnit API
        """
        if self._org_unit is None:
            from mvsdk.rest.org_unit import OrgUnit
            self._org_unit = OrgUnit(self, base_url=self.base_url, domain='org_unit')
        return self._org_unit

    @property
    def user(self):
        """
        Access the MVAPI User API
        """
        if self._user is None:
            from mvsdk.rest.user import User
            self._user = User(self, base_url=self.base_url, domain='user')
        return self._user

    @property
    def user_group(self):
        """
        Access the MVAPI UserGroup API
        """
        if self._user_group is None:
            from mvsdk.rest.user_group import UserGroup
            self._user_group = UserGroup(self, base_url=self.base_url, domain='user_group')
        return self._user_group
