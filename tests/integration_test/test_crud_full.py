import pytest
from requests import auth

from src.helpers.api_requests_wrapper import post_requests, put_requests, delete_requests
from src.constants.api_constants import BASE_URL, APIConstants, base_url
from src.helpers.utils import common_headers_json, common_headers_for_put_delete_patch
from src.helpers.payload_manager import payload_create_booking, payload_create_token
from src.helpers.common_verifications import verify_responses_key_should_not_none, verify_http_status_code


class TestCreateBooking(object):

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
        response = post_requests(url=APIConstants.url_create_booking(), auth=None, headers=common_headers_json(),
                                 payload=payload_create_booking(), in_json=False)
        print(response)
        bookingid = response.json()["bookingid"]
        print(bookingid)
        verify_responses_key_should_not_none(response.json()["bookingid"])
        verify_http_status_code(response, 200)
        return bookingid

    @pytest.mark.positive
    def test_update_booking(self, create_token, create_booking):  # for update booking we need token/auth and bookingID from Create Token, Booking
        # token = "6e6773e458c281b"
        # after adding fixture,
        # print(test_create_token)
        # print(test_create_booking)
        bookingid = create_booking
        put_url = APIConstants.url_create_booking() + "/" + str(bookingid)
        # auth = ("admin", "password123")
        response = put_requests(url=put_url, headers=common_headers_for_put_delete_patch(),
                                payload=payload_create_booking(), in_json=False)
        print(response.json())
        # bookingid = response.json()["bookingid"]
        # print(bookingid)
        # verify_responses_key_should_not_none(response.json()["bookingid"])
        # verify_http_status_code(response, 200)

    def test_delete_booking(self,create_token, create_booking
                            ):  # # for delete booking we need token and bookingID from Create Token, Booking
        bookingid = create_booking
        delete_url = APIConstants.url_create_booking() + "/" + str(bookingid)
        response = delete_requests(url=delete_url, auth=auth, headers=common_headers_for_put_delete_patch(),
                                   payload={}, in_json=False)
        print(response.json())
