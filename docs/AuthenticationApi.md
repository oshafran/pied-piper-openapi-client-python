# openapi_client.AuthenticationApi

All URIs are relative to *https://44.196.44.132*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dataservice_client_token_get**](AuthenticationApi.md#dataservice_client_token_get) | **GET** /dataservice/client/token | Token
[**j_security_check_post**](AuthenticationApi.md#j_security_check_post) | **POST** /j_security_check | Authentication


# **dataservice_client_token_get**
> str dataservice_client_token_get()

Token

### Example

* Api Key Authentication (Cookie):

```python
import time
import openapi_client
from openapi_client.api import authentication_api
from pprint import pprint
# Defining the host is optional and defaults to https://44.196.44.132
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://44.196.44.132"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Cookie
configuration.api_key['Cookie'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Cookie'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentication_api.AuthenticationApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Token
        api_response = api_instance.dataservice_client_token_get()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AuthenticationApi->dataservice_client_token_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

[Cookie](../README.md#Cookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **j_security_check_post**
> str j_security_check_post()

Authentication

### Example

* Api Key Authentication (Cookie):

```python
import time
import openapi_client
from openapi_client.api import authentication_api
from pprint import pprint
# Defining the host is optional and defaults to https://44.196.44.132
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://44.196.44.132"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Cookie
configuration.api_key['Cookie'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Cookie'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentication_api.AuthenticationApi(api_client)
    content_type = "application/x-www-form-urlencoded" # str |  (optional)
    j_username = "{{j_username}}" # str |  (optional)
    j_password = "{{j_password}}" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Authentication
        api_response = api_instance.j_security_check_post(content_type=content_type, j_username=j_username, j_password=j_password)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AuthenticationApi->j_security_check_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**|  | [optional]
 **j_username** | **str**|  | [optional]
 **j_password** | **str**|  | [optional]

### Return type

**str**

### Authorization

[Cookie](../README.md#Cookie)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: text/plain


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  * Set-Cookie -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

