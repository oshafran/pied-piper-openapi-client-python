# openapi_client.UtilityConfigurationDBApi

All URIs are relative to *https://1.1.1.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_db_size_on_file**](UtilityConfigurationDBApi.md#get_db_size_on_file) | **GET** /util/configdb/size | 


# **get_db_size_on_file**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_db_size_on_file()



Fetches the disk usage by configuration-db

### Example


```python
import time
import openapi_client
from openapi_client.api import utility_configuration_db_api
from pprint import pprint
# Defining the host is optional and defaults to https://1.1.1.1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://1.1.1.1"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = utility_configuration_db_api.UtilityConfigurationDBApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_db_size_on_file()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling UtilityConfigurationDBApi->get_db_size_on_file: %s\n" % e)
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

