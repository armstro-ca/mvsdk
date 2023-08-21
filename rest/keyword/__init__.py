class Keyword:

    def __init__(self, mv_sdk, base_url, domain,**kwargs):
        """
        Initialize the Keyword Domain
        """
        super(Keyword, self)
        self.mv_sdk = mv_sdk
        self.base_url = base_url
        self.domain = domain

    def get(self, params=None, data=None, headers=None, auth=None, profile_id=None, domain_id=None, domain_action=None):
        """
        url = "https://api.mediavalet.com/assets/urn:uuid:bb93be4f-89d6-0086-e619-8d52e3ee08ce/keywords?includeSoftDeleted=<boolean>"

        payload={}
        headers = {
        'Ocp-Apim-Subscription-Key': '<uuid>',
        'Authorization': '<bG9sIHlvdSB0aGluayB0aGlzIHdhcyBhIHJlYWwgdG9rZW4/>'
        }

        response = requests.request("GET", url, headers=headers, data=payload)

        print(response.text)
        """
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

    def delete(self, params=None, data=None, headers=None, auth=None, profile_id=None, domain_id=None, domain_action=None):
        """
        url = "https://api.mediavalet.com/assets/urn:uuid:bb93be4f-89d6-0086-e619-8d52e3ee08ce/keywords/esse consequat"

        payload={}
        headers = {
        'Ocp-Apim-Subscription-Key': '<uuid>',
        'Authorization': '<bG9sIHlvdSB0aGluayB0aGlzIHdhcyBhIHJlYWwgdG9rZW4/>'
        }

        response = requests.request("DELETE", url, headers=headers, data=payload)

        print(response.text)
        """
        return self.mv_sdk.request(
            'delete',
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