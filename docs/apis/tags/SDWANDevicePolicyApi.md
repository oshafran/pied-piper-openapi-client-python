<a name="__pageTop"></a>
# openapi_client.apis.tags.sdwan_device_policy_api.SDWANDevicePolicyApi

All URIs are relative to *https://44.196.44.132*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dataservice_template_policy_list_get**](#dataservice_template_policy_list_get) | **get** /dataservice/template/policy/list | Policy List
[**dataservice_template_policy_vedge_devices_get**](#dataservice_template_policy_vedge_devices_get) | **get** /dataservice/template/policy/vedge/devices | vEdge Template Policy

# **dataservice_template_policy_list_get**
<a name="dataservice_template_policy_list_get"></a>
> dataservice_template_policy_list_get()

Policy List

### Example

```python
import openapi_client
from openapi_client.apis.tags import sdwan_device_policy_api
from pprint import pprint
# Defining the host is optional and defaults to https://44.196.44.132
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://44.196.44.132"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sdwan_device_policy_api.SDWANDevicePolicyApi(api_client)

    # example passing only optional values
    header_params = {
        'X-XSRF-TOKEN': "{{X-XSRF-TOKEN}}",
    }
    try:
        # Policy List
        api_response = api_instance.dataservice_template_policy_list_get(
            header_params=header_params,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling SDWANDevicePolicyApi->dataservice_template_policy_list_get: %s\n" % e)
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
200 | [ApiResponseFor200](#dataservice_template_policy_list_get.ApiResponseFor200) | Successful response

#### dataservice_template_policy_list_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, ] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **dataservice_template_policy_vedge_devices_get**
<a name="dataservice_template_policy_vedge_devices_get"></a>
> dataservice_template_policy_vedge_devices_get()

vEdge Template Policy

### Example

```python
import openapi_client
from openapi_client.apis.tags import sdwan_device_policy_api
from pprint import pprint
# Defining the host is optional and defaults to https://44.196.44.132
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://44.196.44.132"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sdwan_device_policy_api.SDWANDevicePolicyApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # vEdge Template Policy
        api_response = api_instance.dataservice_template_policy_vedge_devices_get()
    except openapi_client.ApiException as e:
        print("Exception when calling SDWANDevicePolicyApi->dataservice_template_policy_vedge_devices_get: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#dataservice_template_policy_vedge_devices_get.ApiResponseFor200) | Successful response

#### dataservice_template_policy_vedge_devices_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, ] |  |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

