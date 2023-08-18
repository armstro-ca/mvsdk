class Asset:

    def __init__(self, mv_sdk, base_url, domain,**kwargs):
        """
        Initialize the Asset Domain
        """
        super(Asset, self)
        self.mv_sdk = mv_sdk
        self.base_url = base_url
        self.domain = domain

    def get(self, params=None, data=None, headers=None, auth=None, profile_id=None, domain_id=None, domain_action=None):
        return self.mv_sdk.request(
            'get',
            self.base_url,
            self.domain,
            params=params,
            data=data,
            headers=headers,
            auth=auth,
            profile_id=profile_id,
            domain_id=domain_id,
            domain_action=domain_action
        )
