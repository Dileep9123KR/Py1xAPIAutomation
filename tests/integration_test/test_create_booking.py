from src.helpers.api_requests_wrapper import post_requests
from src.constants.api_constants import BASE_URL, APIConstants, base_url
from src.helpers.utils import common_headers_json
from src.helpers.payload_manager import payload_create_booking
from src.helpers.common_verifications import verify_responses_key_should_not_none, verify_http_status_code

import requests
import pytest


# to make a create booing ->URL, Headers, Payload

class TestCreateBooking(object):

    @pytest.mark.positive
    def test_create_booking_tc1(self):

        payload = payload_create_booking()
        print(payload)
        #payload.update({"key", "value"}) it can take multiple updates
        payload["firstname"] = "Amber"
        print(payload)

        # response = post_requests(url=APIConstants.base_url(), auth=None, headers=common_headers_json(),
        #                          payload=payload_create_booking(), in_json=False)
        # print(response)
        # bookingid = response.json()["bookingid"]
        # print(bookingid)
        # verify_responses_key_should_not_none(response.json()["bookingid"])
        # verify_http_status_code(response, 200)

    @pytest.mark.negative
    def test_create_booking_tc2(self):
        response = post_requests(url=APIConstants.base_url(), auth=None, headers=common_headers_json(),
                                 payload={}, in_json=False)
        # print(response)
        # bookingid = response.json()["bookingid"]
        # print(bookingid)
        # verify_responses_key_should_not_none(response.json()["bookingid"])
        verify_http_status_code(response, 404)

    def test_create_booking_tc3(self):
        response = post_requests(url=APIConstants.url_create_booking(), auth=None, headers=common_headers_json(),
                                 payload=None, in_json=False)

        verify_http_status_code(response, 500)

    def test_create_booking_tc4(self):
        response = post_requests(url=APIConstants.url_create_booking(), auth=None, headers=common_headers_json(),
                                 payload="None-text", in_json=False)
        verify_http_status_code(response, 500) # but in postman its showing 400