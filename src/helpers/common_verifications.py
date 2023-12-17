# HTTP Status verification
# Common verifications are:
# HTTP Status Code
# Headers
# Data Verifications
# Json Schema
def verify_http_status_code(response_data, expect_data):
    print(response_data.status_code)
    print(expect_data)
    assert response_data.status_code == expect_data, "Expected HTTP Status Code" + str(expect_data)


def verify_json_key_for_not_null(key):
    assert key != 0, "Key is not Empty" + key
    assert key > 0, "Key is greater than 0" + key


def verify_responses_key_should_not_none(key):
    assert key is not None

# def verify_responses_time():
