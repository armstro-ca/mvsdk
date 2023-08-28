class Asset:

    def __init__(self, mv_sdk, base_url: str, domain: str, **kwargs: dict):
        """
        Initialize the Asset Domain
        """
        super(Asset, self)
        self.mv_sdk = mv_sdk
        self.base_url = base_url
        self.domain = domain

    def delete_keywords(self, params=None, data=None, headers=None, auth=None, object_id=None, object_action='keyword',
                         domain_id=None, domain_action=None):
        """
        Pass the required parameters to delete asset keywords
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
            object_id=object_id,
            object_action=object_action,
            domain_id=domain_id,
            domain_action=domain_action
        )
    
    def get(self, params=None, data=None, headers=None, auth=None, object_id=None,
            domain_id=None, domain_action=None):
        """
        Pass the required parameters to 
        https://docs.mediavalet.com/#22e41739-3b8b-40e6-ade7-b70406a318e4
        
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
            object_id=object_id,
            domain_id=domain_id,
            domain_action=domain_action
        )
    
    def get_keywords(self, params=None, data=None, headers=None, auth=None, object_id=None, object_action='keywords',
                     domain_id=None, domain_action=None):
        """
        Pass the required parameters to 
        url = "https://api.mediavalet.com/assets/urn:uuid:bb93be4f-89d6-0086-e619-8d52e3ee08ce/keywords?includeSoftDeleted=<boolean>"

        payload={}
        headers = {
        'Ocp-Apim-Subscription-Key': '<uuid>',
        'Authorization': '<bG9sIHlvdSB0aGluayB0aGlzIHdhcyBhIHJlYWwgdG9rZW4/>'
        }

        response = requests.request("GET", url, headers=headers, data=payload)

        print(response.text)
        """
        headers['Host'] = self.base_url

        return self.mv_sdk.request(
            'get',
            self.base_url,
            self.domain,
            params=params,
            data=data,
            headers=headers,
            auth=auth,
            object_id=object_id,
            object_action=object_action,
            domain_id=domain_id,
            domain_action=domain_action
        )

    def put(self, params=None, data=None, headers=None, auth=None, profile_id=None, domain_id=None, domain_action=None):
        """
        https://docs.mediavalet.com/#62f7d9bd-793a-4eb4-928c-f5d216d09de8

        url = "https://api.mediavalet.com/assets/urn:uuid:bb93be4f-89d6-0086-e619-8d52e3ee08ce"

        payload = "{\n  \"id\": \"<uuid>\",\n  \"filename\": \"<string>\",\n  \"title\": \"<string>\",\n  \"description\": \"<string>\",\n  \"fileSizeInBytes\": \"<long>\"\n}"
        headers = {
        'Ocp-Apim-Subscription-Key': '<uuid>',
        'Authorization': '<bG9sIHlvdSB0aGluayB0aGlzIHdhcyBhIHJlYWwgdG9rZW4/>'
        }

        response = requests.request("PUT", url, headers=headers, data=payload)

        print(response.text)
        """