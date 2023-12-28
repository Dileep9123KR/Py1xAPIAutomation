import json

from src.helpers.api_requests_wrapper import post_requests
from src.constants.api_constants import BASE_URL, APIConstants, base_url
from src.helpers.utils import common_headers_json
from src.helpers.payload_manager import payload_create_booking
from src.helpers.common_verifications import verify_responses_key_should_not_none, verify_http_status_code
from jsonschema import validate
from jsonschema.exceptions import ValidationError

import requests
import pytest


class TestCreateBooking(object):

    def load_schema(self, schema_file):
        with open(schema_file, 'r') as file:
                return json.load(file)

    def test_create_booking_jsonschema(self):
        payload = payload_create_booking()
        print(payload)
        # payload.update({"key", "value"}) it can take multiple updates
        payload["firstname"] = "Amber"
        print(payload)

        response = post_requests(url=APIConstants.url_create_booking(), auth=None, headers=common_headers_json(),
                                 payload=payload, in_json=False)
        print(response)
        bookingid = response.json()["bookingid"]
        print(bookingid)
        verify_responses_key_should_not_none(response.json()["bookingid"])
        verify_http_status_code(response, 200)
        respose_json = response.json()

        schema = self.load_schema("C:\Users\Dr.Computers\PycharmProjects\Py1xAPIAutomation\tests\json_schema\schema.json")
        print(schema)
        try:
            validate(instance=respose_json, schema=schema)
        except ValidationError as e:
            print(e.message)
