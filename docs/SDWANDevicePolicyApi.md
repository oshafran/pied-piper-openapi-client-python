# openapi_client.SDWANDevicePolicyApi

All URIs are relative to *https://https*

Method | HTTP request | Description
------------- | ------------- | -------------
[**example_comport_dataservice_template_policy_list_get**](SDWANDevicePolicyApi.md#example_comport_dataservice_template_policy_list_get) | **GET** //example.com:{port}/dataservice/template/policy/list | Policy List
[**example_comport_dataservice_template_policy_vedge_devices_get**](SDWANDevicePolicyApi.md#example_comport_dataservice_template_policy_vedge_devices_get) | **GET** //example.com:{port}/dataservice/template/policy/vedge/devices | vEdge Template Policy


# **example_comport_dataservice_template_policy_list_get**
> str example_comport_dataservice_template_policy_list_get(port)

Policy List

### Example


```python
import time
import openapi_client
from openapi_client.api import sdwan_device_policy_api
from pprint import pprint
# Defining the host is optional and defaults to https://https
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://https"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = sdwan_device_policy_api.SDWANDevicePolicyApi(api_client)
    port = "port_example" # str | 
    x_xsrf_token = "{{X-XSRF-TOKEN}}" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Policy List
        api_response = api_instance.example_comport_dataservice_template_policy_list_get(port)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SDWANDevicePolicyApi->example_comport_dataservice_template_policy_list_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Policy List
        api_response = api_instance.example_comport_dataservice_template_policy_list_get(port, x_xsrf_token=x_xsrf_token)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SDWANDevicePolicyApi->example_comport_dataservice_template_policy_list_get: %s\n" % e)
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

# **example_comport_dataservice_template_policy_vedge_devices_get**
> str example_comport_dataservice_template_policy_vedge_devices_get(port)

vEdge Template Policy

### Example


```python
import time
import openapi_client
from openapi_client.api import sdwan_device_policy_api
from pprint import pprint
# Defining the host is optional and defaults to https://https
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://https"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = sdwan_device_policy_api.SDWANDevicePolicyApi(api_client)
    port = "port_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # vEdge Template Policy
        api_response = api_instance.example_comport_dataservice_template_policy_vedge_devices_get(port)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SDWANDevicePolicyApi->example_comport_dataservice_template_policy_vedge_devices_get: %s\n" % e)
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

