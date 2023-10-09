import unittest
import os
import json

from mvsdk.rest import Client


class TestAsset(unittest.TestCase):

    def setUp(self):
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

        self.sdk_handle = Client()

        self.asset_id = '151b33b1-4c30-4968-bbd1-525ad812e357'

        self.session = self.sdk_handle.connect.auth(
                data=data,
                auth=auth
                )

    def test_add_keywords(self):

        keywords = 'clouds,mountains,snow'

        response = self.sdk_handle.asset.create_keywords(
            data=json.dumps(keywords.split(',')),
            object_id=self.asset_id,
            auth=self.session.json()["access_token"]
            )

        self.assertEqual(response.status_code, 202)

    def test_delete_keyword(self):

        keyword = 'snow'
        existing_keywords = get_existing_keywords(self.sdk_handle, self.session)

        response = self.sdk_handle.asset.delete_keyword(
            object_action=f'keywords/{existing_keywords[keyword]}',
            object_id=self.asset_id,
            auth=self.session.json()["access_token"]
            )

        self.assertEqual(response['status'], 202)

    def test_get_keywords(self):

        response = self.sdk_handle.asset.get_keywords(
            object_id=self.asset_id,
            auth=self.session.json()["access_token"]
            )

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json()['payload'], list)


def get_existing_keywords(sdk_handle, session):

    response = sdk_handle.keyword.get(
        auth=session.json()["access_token"]
        )

    existing_keywords = {}
    for existing_keyword in response.json()['payload']:
        existing_keywords[existing_keyword['keywordName']] = existing_keyword['id']

    return existing_keywords
