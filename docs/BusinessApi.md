# openapi_client.BusinessApi

All URIs are relative to *https://44.196.44.132*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dataservice_system_device_vedges_get**](BusinessApi.md#dataservice_system_device_vedges_get) | **GET** /dataservice/system/device/vedges | Get  Device VEdges
[**dataservice_template_policy_list_site_get**](BusinessApi.md#dataservice_template_policy_list_site_get) | **GET** /dataservice/template/policy/list/site | Get  Prefix Template List


# **dataservice_system_device_vedges_get**
> str dataservice_system_device_vedges_get()

Get  Device VEdges

### Example

* Api Key Authentication (cookieAuth):

```python
import time
import openapi_client
from openapi_client.api import business_api
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

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = business_api.BusinessApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get  Device VEdges
        api_response = api_instance.dataservice_system_device_vedges_get()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling BusinessApi->dataservice_system_device_vedges_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

[cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dataservice_template_policy_list_site_get**
> str dataservice_template_policy_list_site_get()

Get  Prefix Template List

### Example

* Api Key Authentication (cookieAuth):

```python
import time
import openapi_client
from openapi_client.api import business_api
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

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = business_api.BusinessApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get  Prefix Template List
        api_response = api_instance.dataservice_template_policy_list_site_get()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling BusinessApi->dataservice_template_policy_list_site_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

[cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

