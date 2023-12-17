# To make the POST, PUT, PATCH, DELETE
import json

import requests


# HTTP methods are writing here - Generic Functions

def get_requests(url, auth, in_json):
    response = requests.get(url=url, auth=auth)
    if in_json in True:
        return response.json()

    return response


# data = get_request("https://restfullbooker.com/booking/1", in_json=True/False)
# here we are not using auth because its a POST request
# date -> in return json format if the in_json is True and if its = False returns in normal format

def post_requests(url, auth, headers, payload, in_json):
    post_response = requests.post(url=url, headers=headers, auth=auth, data=json.dumps(payload))
    if in_json is True:
        return post_response.json()
    return post_response


def patch_requests(url, auth, headers, payload, in_json):
    patch_response = requests.patch(url=url, headers=headers, auth=auth, data=json.dumps(payload))
    if in_json is True:
        return patch_response.json()
    return patch_response


def put_requests(url, auth, headers, payload, in_json):
    put_response = requests.put(url=url, headers=headers, auth=auth, data=json.dumps(payload))
    if in_json is True:
        return put_response.json()
    return put_response


def delete_requests(url, auth, headers, payload, in_json):
    delete_response = requests.delete(url=url, headers=headers, auth=auth, data=json.dumps(payload))
    if in_json is True:
        return delete_response.json()
    return delete_response
