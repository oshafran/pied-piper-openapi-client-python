# openapi_client.AuthenticationApi

All URIs are relative to *https://https*

Method | HTTP request | Description
------------- | ------------- | -------------
[**example_comport_dataservice_client_token_get**](AuthenticationApi.md#example_comport_dataservice_client_token_get) | **GET** //example.com:{port}/dataservice/client/token | Token
[**example_comport_j_security_check_post**](AuthenticationApi.md#example_comport_j_security_check_post) | **POST** //example.com:{port}/j_security_check | Authentication


# **example_comport_dataservice_client_token_get**
> str example_comport_dataservice_client_token_get(port)

Token

### Example


```python
import time
import openapi_client
from openapi_client.api import authentication_api
from pprint import pprint
# Defining the host is optional and defaults to https://https
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://https"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = authentication_api.AuthenticationApi(api_client)
    port = "port_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Token
        api_response = api_instance.example_comport_dataservice_client_token_get(port)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AuthenticationApi->example_comport_dataservice_client_token_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **port** | **str**|  |

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **example_comport_j_security_check_post**
> str example_comport_j_security_check_post(port)

Authentication

### Example


```python
import time
import openapi_client
from openapi_client.api import authentication_api
from pprint import pprint
# Defining the host is optional and defaults to https://https
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://https"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = authentication_api.AuthenticationApi(api_client)
    port = "port_example" # str | 
    content_type = "application/x-www-form-urlencoded" # str |  (optional)
    j_username = "{{j_username}}" # str |  (optional)
    j_password = "{{j_password}}" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Authentication
        api_response = api_instance.example_comport_j_security_check_post(port)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AuthenticationApi->example_comport_j_security_check_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Authentication
        api_response = api_instance.example_comport_j_security_check_post(port, content_type=content_type, j_username=j_username, j_password=j_password)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AuthenticationApi->example_comport_j_security_check_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **port** | **str**|  |
 **content_type** | **str**|  | [optional]
 **j_username** | **str**|  | [optional]
 **j_password** | **str**|  | [optional]

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: text/plain


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

