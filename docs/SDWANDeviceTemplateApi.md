# openapi_client.SDWANDeviceTemplateApi

All URIs are relative to *https://https*

Method | HTTP request | Description
------------- | ------------- | -------------
[**example_comport_dataservice_template_feature_get**](SDWANDeviceTemplateApi.md#example_comport_dataservice_template_feature_get) | **GET** //example.com:{port}/dataservice/template/feature | Template Feature
[**example_comport_dataservice_template_feature_types_get**](SDWANDeviceTemplateApi.md#example_comport_dataservice_template_feature_types_get) | **GET** //example.com:{port}/dataservice/template/feature/types | Template Feature Type


# **example_comport_dataservice_template_feature_get**
> str example_comport_dataservice_template_feature_get(port)

Template Feature

### Example


```python
import time
import openapi_client
from openapi_client.api import sdwan_device_template_api
from pprint import pprint
# Defining the host is optional and defaults to https://https
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://https"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = sdwan_device_template_api.SDWANDeviceTemplateApi(api_client)
    port = "port_example" # str | 
    x_xsrf_token = "{{X-XSRF-TOKEN}}" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Template Feature
        api_response = api_instance.example_comport_dataservice_template_feature_get(port)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SDWANDeviceTemplateApi->example_comport_dataservice_template_feature_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Template Feature
        api_response = api_instance.example_comport_dataservice_template_feature_get(port, x_xsrf_token=x_xsrf_token)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SDWANDeviceTemplateApi->example_comport_dataservice_template_feature_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **port** | **str**|  |
 **x_xsrf_token** | **str**|  | [optional]

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

# **example_comport_dataservice_template_feature_types_get**
> str example_comport_dataservice_template_feature_types_get(port)

Template Feature Type

### Example


```python
import time
import openapi_client
from openapi_client.api import sdwan_device_template_api
from pprint import pprint
# Defining the host is optional and defaults to https://https
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://https"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = sdwan_device_template_api.SDWANDeviceTemplateApi(api_client)
    port = "port_example" # str | 
    x_xsrf_token = "{{X-XSRF-TOKEN}}" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Template Feature Type
        api_response = api_instance.example_comport_dataservice_template_feature_types_get(port)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SDWANDeviceTemplateApi->example_comport_dataservice_template_feature_types_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Template Feature Type
        api_response = api_instance.example_comport_dataservice_template_feature_types_get(port, x_xsrf_token=x_xsrf_token)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SDWANDeviceTemplateApi->example_comport_dataservice_template_feature_types_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **port** | **str**|  |
 **x_xsrf_token** | **str**|  | [optional]

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

