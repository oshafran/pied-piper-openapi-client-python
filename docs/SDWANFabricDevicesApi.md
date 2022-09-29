# openapi_client.SDWANFabricDevicesApi

All URIs are relative to *https://https*

Method | HTTP request | Description
------------- | ------------- | -------------
[**example_comport_dataservice_device_counters_get**](SDWANFabricDevicesApi.md#example_comport_dataservice_device_counters_get) | **GET** //example.com:{port}/dataservice/device/counters | Device Counters
[**example_comport_dataservice_device_get**](SDWANFabricDevicesApi.md#example_comport_dataservice_device_get) | **GET** //example.com:{port}/dataservice/device | Fabric Devices
[**example_comport_dataservice_device_monitor_get**](SDWANFabricDevicesApi.md#example_comport_dataservice_device_monitor_get) | **GET** //example.com:{port}/dataservice/device/monitor | Devices Status
[**example_comport_dataservice_statistics_interface_get**](SDWANFabricDevicesApi.md#example_comport_dataservice_statistics_interface_get) | **GET** //example.com:{port}/dataservice/statistics/interface | Interface statistics


# **example_comport_dataservice_device_counters_get**
> str example_comport_dataservice_device_counters_get(port)

Device Counters

### Example


```python
import time
import openapi_client
from openapi_client.api import sdwan_fabric_devices_api
from pprint import pprint
# Defining the host is optional and defaults to https://https
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://https"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = sdwan_fabric_devices_api.SDWANFabricDevicesApi(api_client)
    port = "port_example" # str | 
    x_xsrf_token = "{{X-XSRF-TOKEN}}" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Device Counters
        api_response = api_instance.example_comport_dataservice_device_counters_get(port)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SDWANFabricDevicesApi->example_comport_dataservice_device_counters_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Device Counters
        api_response = api_instance.example_comport_dataservice_device_counters_get(port, x_xsrf_token=x_xsrf_token)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SDWANFabricDevicesApi->example_comport_dataservice_device_counters_get: %s\n" % e)
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

# **example_comport_dataservice_device_get**
> str example_comport_dataservice_device_get(port)

Fabric Devices

### Example


```python
import time
import openapi_client
from openapi_client.api import sdwan_fabric_devices_api
from pprint import pprint
# Defining the host is optional and defaults to https://https
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://https"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = sdwan_fabric_devices_api.SDWANFabricDevicesApi(api_client)
    port = "port_example" # str | 
    x_xsrf_token = "{{X-XSRF-TOKEN}}" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Fabric Devices
        api_response = api_instance.example_comport_dataservice_device_get(port)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SDWANFabricDevicesApi->example_comport_dataservice_device_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Fabric Devices
        api_response = api_instance.example_comport_dataservice_device_get(port, x_xsrf_token=x_xsrf_token)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SDWANFabricDevicesApi->example_comport_dataservice_device_get: %s\n" % e)
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

# **example_comport_dataservice_device_monitor_get**
> str example_comport_dataservice_device_monitor_get(port)

Devices Status

### Example


```python
import time
import openapi_client
from openapi_client.api import sdwan_fabric_devices_api
from pprint import pprint
# Defining the host is optional and defaults to https://https
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://https"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = sdwan_fabric_devices_api.SDWANFabricDevicesApi(api_client)
    port = "port_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Devices Status
        api_response = api_instance.example_comport_dataservice_device_monitor_get(port)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SDWANFabricDevicesApi->example_comport_dataservice_device_monitor_get: %s\n" % e)
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

# **example_comport_dataservice_statistics_interface_get**
> str example_comport_dataservice_statistics_interface_get(port)

Interface statistics

### Example


```python
import time
import openapi_client
from openapi_client.api import sdwan_fabric_devices_api
from pprint import pprint
# Defining the host is optional and defaults to https://https
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://https"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = sdwan_fabric_devices_api.SDWANFabricDevicesApi(api_client)
    port = "port_example" # str | 
    x_xsrf_token = "{{X-XSRF-TOKEN}}" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Interface statistics
        api_response = api_instance.example_comport_dataservice_statistics_interface_get(port)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SDWANFabricDevicesApi->example_comport_dataservice_statistics_interface_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Interface statistics
        api_response = api_instance.example_comport_dataservice_statistics_interface_get(port, x_xsrf_token=x_xsrf_token)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SDWANFabricDevicesApi->example_comport_dataservice_statistics_interface_get: %s\n" % e)
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

