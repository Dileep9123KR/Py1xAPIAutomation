from src.constants.api_constants import BASE_URL, APIConstants, base_url
#                                       direct   class_function   normal function



def test_curd():
    print(BASE_URL)

    url_class = APIConstants.base_url()
    print(url_class)

    url_direct_func = base_url()
    print(url_direct_func)
