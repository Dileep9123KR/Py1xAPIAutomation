# Common Headers

def common_headers_json():
    headers = {
        "ContentType": "application/json"
    }
    return headers

def common_headers_for_put_delete_patch():
    headers = {
        "Content-Type":"application/json",
        "Authorization":"Basic YWRtaW46cGFzc3dvcmQxMjM="
    }
    return headers

def common_headers_xml():
    headers = {
        "ContentType": "application/xml"
    }
    return headers

# If we want to read data from excel, csv, json, yaml can be added here