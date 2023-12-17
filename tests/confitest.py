import pytest
import requests

from src.helpers.api_requests_wrapper import post_requests, put_requests, delete_requests
from src.constants.api_constants import BASE_URL, APIConstants, base_url
from src.helpers.utils import common_headers_json, common_headers_for_put_delete_patch
from src.helpers.payload_manager import payload_create_booking, payload_create_token
from src.helpers.common_verifications import verify_responses_key_should_not_none, verify_http_status_code


@pytest.fixture()
def create_token(self):
    response = post_requests(
        url=APIConstants.url_create_token(),
        headers=common_headers_json(),
        auth=None,
        payload=payload_create_token(), in_json=False
    )
    verify_http_status_code(response, 200)
    token = response.json()["token"]
    print(token)
    verify_responses_key_should_not_none(token)
    return token


@pytest.fixture()
def create_booking(self):
    response = post_requests(url=APIConstants.base_url(), auth=None, headers=common_headers_json(),
                             payload=payload_create_booking(), in_json=False)
    print(response)
    bookingid = response.json()["bookingid"]
    print(bookingid)
    verify_responses_key_should_not_none(response.json()["bookingid"])
    verify_http_status_code(response, 200)
    return bookingid