# openapi_client.SDWANDeviceTemplateApi

All URIs are relative to *https://44.196.44.132*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dataservice_template_feature_get**](SDWANDeviceTemplateApi.md#dataservice_template_feature_get) | **GET** /dataservice/template/feature | Template Feature
[**dataservice_template_feature_types_get**](SDWANDeviceTemplateApi.md#dataservice_template_feature_types_get) | **GET** /dataservice/template/feature/types | Template Feature Type


# **dataservice_template_feature_get**
> str dataservice_template_feature_get()

Template Feature

### Example

* Api Key Authentication (cookieAuth):

```python
import time
import openapi_client
from openapi_client.api import sdwan_device_template_api
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
    api_instance = sdwan_device_template_api.SDWANDeviceTemplateApi(api_client)
    x_xsrf_token = "{{X-XSRF-TOKEN}}" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Template Feature
        api_response = api_instance.dataservice_template_feature_get(x_xsrf_token=x_xsrf_token)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SDWANDeviceTemplateApi->dataservice_template_feature_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_xsrf_token** | **str**|  | [optional]

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

# **dataservice_template_feature_types_get**
> str dataservice_template_feature_types_get()

Template Feature Type

### Example

* Api Key Authentication (cookieAuth):

```python
import time
import openapi_client
from openapi_client.api import sdwan_device_template_api
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
    api_instance = sdwan_device_template_api.SDWANDeviceTemplateApi(api_client)
    x_xsrf_token = "{{X-XSRF-TOKEN}}" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Template Feature Type
        api_response = api_instance.dataservice_template_feature_types_get(x_xsrf_token=x_xsrf_token)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SDWANDeviceTemplateApi->dataservice_template_feature_types_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_xsrf_token** | **str**|  | [optional]

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

