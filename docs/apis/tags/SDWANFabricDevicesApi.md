<a name="__pageTop"></a>
# openapi_client.apis.tags.sdwan_fabric_devices_api.SDWANFabricDevicesApi

All URIs are relative to *https://44.196.44.132*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dataservice_device_counters_get**](#dataservice_device_counters_get) | **get** /dataservice/device/counters | Device Counters
[**dataservice_device_get**](#dataservice_device_get) | **get** /dataservice/device | Fabric Devices
[**dataservice_device_monitor_get**](#dataservice_device_monitor_get) | **get** /dataservice/device/monitor | Devices Status
[**dataservice_statistics_interface_get**](#dataservice_statistics_interface_get) | **get** /dataservice/statistics/interface | Interface statistics

# **dataservice_device_counters_get**
<a name="dataservice_device_counters_get"></a>
> dataservice_device_counters_get()

Device Counters

### Example

```python
import openapi_client
from openapi_client.apis.tags import sdwan_fabric_devices_api
from pprint import pprint
# Defining the host is optional and defaults to https://44.196.44.132
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://44.196.44.132"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sdwan_fabric_devices_api.SDWANFabricDevicesApi(api_client)

    # example passing only optional values
    header_params = {
        'X-XSRF-TOKEN': "{{X-XSRF-TOKEN}}",
    }
    try:
        # Device Counters
        api_response = api_instance.dataservice_device_counters_get(
            header_params=header_params,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling SDWANFabricDevicesApi->dataservice_device_counters_get: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
header_params | RequestHeaderParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
X-XSRF-TOKEN | XXSRFTOKENSchema | | optional

# XXSRFTOKENSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#dataservice_device_counters_get.ApiResponseFor200) | Successful response

#### dataservice_device_counters_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, ] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **dataservice_device_get**
<a name="dataservice_device_get"></a>
> dataservice_device_get()

Fabric Devices

### Example

```python
import openapi_client
from openapi_client.apis.tags import sdwan_fabric_devices_api
from pprint import pprint
# Defining the host is optional and defaults to https://44.196.44.132
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://44.196.44.132"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sdwan_fabric_devices_api.SDWANFabricDevicesApi(api_client)

    # example passing only optional values
    header_params = {
        'X-XSRF-TOKEN': "{{X-XSRF-TOKEN}}",
    }
    try:
        # Fabric Devices
        api_response = api_instance.dataservice_device_get(
            header_params=header_params,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling SDWANFabricDevicesApi->dataservice_device_get: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
header_params | RequestHeaderParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
X-XSRF-TOKEN | XXSRFTOKENSchema | | optional

# XXSRFTOKENSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#dataservice_device_get.ApiResponseFor200) | Successful response

#### dataservice_device_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, ] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **dataservice_device_monitor_get**
<a name="dataservice_device_monitor_get"></a>
> dataservice_device_monitor_get()

Devices Status

### Example

```python
import openapi_client
from openapi_client.apis.tags import sdwan_fabric_devices_api
from pprint import pprint
# Defining the host is optional and defaults to https://44.196.44.132
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://44.196.44.132"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sdwan_fabric_devices_api.SDWANFabricDevicesApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Devices Status
        api_response = api_instance.dataservice_device_monitor_get()
    except openapi_client.ApiException as e:
        print("Exception when calling SDWANFabricDevicesApi->dataservice_device_monitor_get: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#dataservice_device_monitor_get.ApiResponseFor200) | Successful response

#### dataservice_device_monitor_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, ] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **dataservice_statistics_interface_get**
<a name="dataservice_statistics_interface_get"></a>
> dataservice_statistics_interface_get()

Interface statistics

### Example

```python
import openapi_client
from openapi_client.apis.tags import sdwan_fabric_devices_api
from pprint import pprint
# Defining the host is optional and defaults to https://44.196.44.132
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://44.196.44.132"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sdwan_fabric_devices_api.SDWANFabricDevicesApi(api_client)

    # example passing only optional values
    header_params = {
        'X-XSRF-TOKEN': "{{X-XSRF-TOKEN}}",
    }
    try:
        # Interface statistics
        api_response = api_instance.dataservice_statistics_interface_get(
            header_params=header_params,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling SDWANFabricDevicesApi->dataservice_statistics_interface_get: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
header_params | RequestHeaderParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
X-XSRF-TOKEN | XXSRFTOKENSchema | | optional

# XXSRFTOKENSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#dataservice_statistics_interface_get.ApiResponseFor200) | Successful response

#### dataservice_statistics_interface_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, ] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

