# We need to read the CSV/Excel file
# Create a function create_token which can takes values from Excel/CSV file
# Verify the Expected Result
# Need to install openpyxl to work with Excel file


import requests
import pytest
import openpyxl

from src.constants.api_constants import APIConstants
from src.helpers.utils import common_headers_json


# Step-1 Read the file and put the content into a []

def read_the_credential_from_excel(file_path):
    # username and password
    credentials = []
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active

    for row in sheet.iter_rows(min_row=2, values_only=True):
        username, password = row
        credentials.append({"username": username, "password": password})
    return credentials


def make_request_auth(username, password):
    payload = {
        "username": username,
        "password": password
    }
    # headers = {
    #     "Content-Type": "application/json",
    # }
    response = requests.post(APIConstants.url_create_token(), headers=common_headers_json(), json=payload)
    assert response.status_code == 200
    return response


@pytest.mark.parametrize("user_cred", read_the_credential_from_excel("testdata_ddt.xlsx"))
def test_post_create_token(user_cred):
    # # make_request_auth -> run this function as many rows available in the excel file
    # file_path = "testdata_ddt.xlsx"
    # credentials = read_the_credential_from_excel(file_path)
    #
    # for user_cred in credentials:
    username = user_cred["username"]
    password = user_cred["password"]
    print(username, password)
    response = make_request_auth(username, password)
    #     print(response)
    #     # you can also write the logic for negative and positive
    assert response.status_code == 200
