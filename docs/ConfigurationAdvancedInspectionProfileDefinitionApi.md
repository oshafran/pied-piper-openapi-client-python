# openapi_client.ConfigurationAdvancedInspectionProfileDefinitionApi

All URIs are relative to *https://1.1.1.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_policy_definition10**](ConfigurationAdvancedInspectionProfileDefinitionApi.md#create_policy_definition10) | **POST** /template/policy/definition/advancedinspectionprofile | 
[**delete_policy_definition10**](ConfigurationAdvancedInspectionProfileDefinitionApi.md#delete_policy_definition10) | **DELETE** /template/policy/definition/advancedinspectionprofile/{id} | 
[**edit_multiple_policy_definition10**](ConfigurationAdvancedInspectionProfileDefinitionApi.md#edit_multiple_policy_definition10) | **PUT** /template/policy/definition/advancedinspectionprofile/multiple/{id} | 
[**edit_policy_definition10**](ConfigurationAdvancedInspectionProfileDefinitionApi.md#edit_policy_definition10) | **PUT** /template/policy/definition/advancedinspectionprofile/{id} | 
[**get_definitions10**](ConfigurationAdvancedInspectionProfileDefinitionApi.md#get_definitions10) | **GET** /template/policy/definition/advancedinspectionprofile | 
[**get_policy_definition10**](ConfigurationAdvancedInspectionProfileDefinitionApi.md#get_policy_definition10) | **GET** /template/policy/definition/advancedinspectionprofile/{id} | 
[**preview_policy_definition10**](ConfigurationAdvancedInspectionProfileDefinitionApi.md#preview_policy_definition10) | **POST** /template/policy/definition/advancedinspectionprofile/preview | 
[**preview_policy_definition_by_id10**](ConfigurationAdvancedInspectionProfileDefinitionApi.md#preview_policy_definition_by_id10) | **GET** /template/policy/definition/advancedinspectionprofile/preview/{id} | 
[**save_policy_definition_in_bulk10**](ConfigurationAdvancedInspectionProfileDefinitionApi.md#save_policy_definition_in_bulk10) | **PUT** /template/policy/definition/advancedinspectionprofile/bulk | 


# **create_policy_definition10**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} create_policy_definition10()



Create policy definition

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_advanced_inspection_profile_definition_api
from pprint import pprint
# Defining the host is optional and defaults to https://1.1.1.1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://1.1.1.1"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_advanced_inspection_profile_definition_api.ConfigurationAdvancedInspectionProfileDefinitionApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Policy definition (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_policy_definition10(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationAdvancedInspectionProfileDefinitionApi->create_policy_definition10: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Policy definition | [optional]

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_policy_definition10**
> delete_policy_definition10(id)



Delete policy definition

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_advanced_inspection_profile_definition_api
from pprint import pprint
# Defining the host is optional and defaults to https://1.1.1.1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://1.1.1.1"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_advanced_inspection_profile_definition_api.ConfigurationAdvancedInspectionProfileDefinitionApi(api_client)
    id = "id_example" # str | Policy Id

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_policy_definition10(id)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationAdvancedInspectionProfileDefinitionApi->delete_policy_definition10: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Policy Id |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_multiple_policy_definition10**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} edit_multiple_policy_definition10(id)



Edit multiple policy definitions

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_advanced_inspection_profile_definition_api
from pprint import pprint
# Defining the host is optional and defaults to https://1.1.1.1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://1.1.1.1"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_advanced_inspection_profile_definition_api.ConfigurationAdvancedInspectionProfileDefinitionApi(api_client)
    id = "id_example" # str | Policy Id
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Policy definition (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.edit_multiple_policy_definition10(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationAdvancedInspectionProfileDefinitionApi->edit_multiple_policy_definition10: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.edit_multiple_policy_definition10(id, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationAdvancedInspectionProfileDefinitionApi->edit_multiple_policy_definition10: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Policy Id |
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Policy definition | [optional]

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_policy_definition10**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} edit_policy_definition10(id)



Edit a policy definitions

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_advanced_inspection_profile_definition_api
from pprint import pprint
# Defining the host is optional and defaults to https://1.1.1.1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://1.1.1.1"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_advanced_inspection_profile_definition_api.ConfigurationAdvancedInspectionProfileDefinitionApi(api_client)
    id = "id_example" # str | Policy Id
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Policy definition (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.edit_policy_definition10(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationAdvancedInspectionProfileDefinitionApi->edit_policy_definition10: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.edit_policy_definition10(id, body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationAdvancedInspectionProfileDefinitionApi->edit_policy_definition10: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Policy Id |
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Policy definition | [optional]

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_definitions10**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_definitions10()



Get policy definitions

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_advanced_inspection_profile_definition_api
from pprint import pprint
# Defining the host is optional and defaults to https://1.1.1.1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://1.1.1.1"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_advanced_inspection_profile_definition_api.ConfigurationAdvancedInspectionProfileDefinitionApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_definitions10()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationAdvancedInspectionProfileDefinitionApi->get_definitions10: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

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

# **get_policy_definition10**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_policy_definition10(id)



Get a specific policy definitions

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_advanced_inspection_profile_definition_api
from pprint import pprint
# Defining the host is optional and defaults to https://1.1.1.1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://1.1.1.1"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_advanced_inspection_profile_definition_api.ConfigurationAdvancedInspectionProfileDefinitionApi(api_client)
    id = "id_example" # str | Policy Id

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_policy_definition10(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationAdvancedInspectionProfileDefinitionApi->get_policy_definition10: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Policy Id |

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

# **preview_policy_definition10**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} preview_policy_definition10()



Preview policy definition

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_advanced_inspection_profile_definition_api
from pprint import pprint
# Defining the host is optional and defaults to https://1.1.1.1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://1.1.1.1"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_advanced_inspection_profile_definition_api.ConfigurationAdvancedInspectionProfileDefinitionApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Policy definition (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.preview_policy_definition10(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationAdvancedInspectionProfileDefinitionApi->preview_policy_definition10: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Policy definition | [optional]

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **preview_policy_definition_by_id10**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} preview_policy_definition_by_id10(id)



Preview policy definition

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_advanced_inspection_profile_definition_api
from pprint import pprint
# Defining the host is optional and defaults to https://1.1.1.1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://1.1.1.1"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_advanced_inspection_profile_definition_api.ConfigurationAdvancedInspectionProfileDefinitionApi(api_client)
    id = "id_example" # str | Policy Id

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.preview_policy_definition_by_id10(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationAdvancedInspectionProfileDefinitionApi->preview_policy_definition_by_id10: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Policy Id |

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

# **save_policy_definition_in_bulk10**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} save_policy_definition_in_bulk10()



Create/Edit policy definitions in bulk

### Example


```python
import time
import openapi_client
from openapi_client.api import configuration_advanced_inspection_profile_definition_api
from pprint import pprint
# Defining the host is optional and defaults to https://1.1.1.1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://1.1.1.1"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = configuration_advanced_inspection_profile_definition_api.ConfigurationAdvancedInspectionProfileDefinitionApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | Policy definition (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.save_policy_definition_in_bulk10(body=body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConfigurationAdvancedInspectionProfileDefinitionApi->save_policy_definition_in_bulk10: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| Policy definition | [optional]

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

