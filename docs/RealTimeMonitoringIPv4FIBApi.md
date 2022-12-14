# openapi_client.RealTimeMonitoringIPv4FIBApi

All URIs are relative to *https://1.1.1.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_ipv4_fib_list**](RealTimeMonitoringIPv4FIBApi.md#create_ipv4_fib_list) | **GET** /device/ip/v4fib | 


# **create_ipv4_fib_list**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} create_ipv4_fib_list(device_id)



Get IPv4 FIB list from device (Real Time)

### Example


```python
import time
import openapi_client
from openapi_client.api import real_time_monitoring_ipv4_fib_api
from pprint import pprint
# Defining the host is optional and defaults to https://1.1.1.1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://1.1.1.1"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = real_time_monitoring_ipv4_fib_api.RealTimeMonitoringIPv4FIBApi(api_client)
    device_id = "00r252U250?250" # str | Device Id
    vpn_id = "0" # str | VPN Id (optional)
    prefix = "prefix_example" # str | IP prefix (optional)
    tloc = "tloc_example" # str | tloc IP (optional)
    color = "default" # str | tloc color (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_ipv4_fib_list(device_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringIPv4FIBApi->create_ipv4_fib_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_ipv4_fib_list(device_id, vpn_id=vpn_id, prefix=prefix, tloc=tloc, color=color)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RealTimeMonitoringIPv4FIBApi->create_ipv4_fib_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Device Id |
 **vpn_id** | **str**| VPN Id | [optional]
 **prefix** | **str**| IP prefix | [optional]
 **tloc** | **str**| tloc IP | [optional]
 **color** | **str**| tloc color | [optional]

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

