import re
import parse

class Bulk:

    def __init__(self, mv_sdk, base_url: str, domain: str):
        """
        Initialize the Bulk Domain
        """
        super(Bulk, self)
        self.mv_sdk = mv_sdk
        self.base_url = base_url
        self.domain = domain

    def post(self, params=None, data=None, headers=None, auth=None, object_id=None,
             domain_id=None, domain_action=None):
        """

        """
        headers = headers or {}

        return self.mv_sdk.request(
            'post',
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


class BulkRequest:
    def __init__(self):
        self.bulk_requests = []

    def add_request(self, request):
        self.bulk_requests.append(request)

    def get_all_requests(self):
        return self.bulk_requests

    def get_payload(self):
        bulk_request_dict = {}

        boundary_string = 'c6c2ed020aadd284efd61a7c9d4dfe94'
        bulk_request_dict['headers'] = {
            'Content-Type': f'multipart/mixed; boundary={boundary_string}'
            }

        bulk_request_payloads = []

        for request in self.bulk_requests:
            bulk_request = ''.join(f'--{boundary_string}\r\n'
                                   'Content-Type: application/http; msgtype=request\r\n\r\n'
                                   f'{request["method"]} {request["uri"]} HTTP/1.1\r\n'
                                   f'host: {request["headers"]["Host"]}\r\n'
                                   f'Authorization: {request["headers"]["Authorization"]}\r\n'
                                   f'content-type: {request["headers"]["Content-Type"]}\r\n\r\n'
                                   )

            if request['data']:
                bulk_request += f'{request["data"]}\r\n'

            bulk_request_payloads.append(bulk_request)

        bulk_request_payloads.append(f'\r\n\r\n--{boundary_string}--\r\n')
        bulk_request_payload = '\r\n'.join(bulk_request_payloads)
        bulk_request_dict['payload'] = bulk_request_payload.encode(encoding='UTF-8', errors='strict')

        payload_length = str(len(bulk_request_dict['payload']))
        bulk_request_dict['headers']['Content-Length'] = payload_length

        return bulk_request_dict


class BulkResponse:
    def __init__(self, response):
        self.bulk_response = []

        json_payload = response['json'].pop()
        boundary_string = json_payload[:38]

        print(f'Boundary String: {boundary_string}')

        # Split the string into individual sections using the boundary string
        sections = re.split(boundary_string, json_payload)

        # Iterate over the sections
        for section in sections[1:-1]:
            # Extract HTTP response information
            parsed_headers = parse.search('HTTP/1.1 {status_code} {status_message}\r\nContent-Type: {content_type};', section)

            # Extract payload response information
            parsed_body = parse.search('{"apiVersion":"{api_version}","warnings":{warnings},"errors":{errors},"payload":{payload},"meta":{"metaInformation":{"ElapsedTimeInMS":{elapsed_time}},"createdAt":"{created_at}"}}', section)

            section_dict = {
                "status_code": parsed_headers['status_code'],
                "status_message": parsed_headers['status_message'],
                "content_type": parsed_headers['content_type'],
                "api_version": parsed_body['api_version'],
                "warnings": parsed_body['warnings'],
                "errors": parsed_body['errors'],
                "payload": parsed_body['payload']
            }

            self.add_section(section_dict)

    def add_section(self, section: dict):
        self.bulk_response.append(section)

    def get_response_dict(self):
        return self.bulk_response
    
  def get_post_response(self):

    def get_get_response(self):
