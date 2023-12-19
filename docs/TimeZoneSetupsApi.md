# connectwise_psa.TimeZoneSetupsApi

All URIs are relative to *https://api-aus.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_system_time_zone_setups_by_id**](TimeZoneSetupsApi.md#delete_system_time_zone_setups_by_id) | **DELETE** /system/timeZoneSetups/{id} | Delete TimeZoneSetup
[**get_system_time_zone_setups**](TimeZoneSetupsApi.md#get_system_time_zone_setups) | **GET** /system/timeZoneSetups | Get List of TimeZoneSetup
[**get_system_time_zone_setups_by_id**](TimeZoneSetupsApi.md#get_system_time_zone_setups_by_id) | **GET** /system/timeZoneSetups/{id} | Get TimeZoneSetup
[**get_system_time_zone_setups_count**](TimeZoneSetupsApi.md#get_system_time_zone_setups_count) | **GET** /system/timeZoneSetups/count | Get Count of TimeZoneSetup
[**patch_system_time_zone_setups_by_id**](TimeZoneSetupsApi.md#patch_system_time_zone_setups_by_id) | **PATCH** /system/timeZoneSetups/{id} | Patch TimeZoneSetup
[**post_system_time_zone_setups**](TimeZoneSetupsApi.md#post_system_time_zone_setups) | **POST** /system/timeZoneSetups | Post TimeZoneSetup
[**put_system_time_zone_setups_by_id**](TimeZoneSetupsApi.md#put_system_time_zone_setups_by_id) | **PUT** /system/timeZoneSetups/{id} | Put TimeZoneSetup


# **delete_system_time_zone_setups_by_id**
> delete_system_time_zone_setups_by_id(id, client_id)

Delete TimeZoneSetup

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api-aus.myconnectwise.net/v4_6_release/apis/3.0
# See configuration.py for a list of all supported configuration parameters.
configuration = connectwise_psa.Configuration(
    host = "https://api-aus.myconnectwise.net/v4_6_release/apis/3.0"
)


# Enter a context with an instance of the API client
with connectwise_psa.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = connectwise_psa.TimeZoneSetupsApi(api_client)
    id = 56 # int | timeZoneSetupId
    client_id = 'client_id_example' # str | 

    try:
        # Delete TimeZoneSetup
        api_instance.delete_system_time_zone_setups_by_id(id, client_id)
    except Exception as e:
        print("Exception when calling TimeZoneSetupsApi->delete_system_time_zone_setups_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| timeZoneSetupId | 
 **client_id** | **str**|  | 

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
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_system_time_zone_setups**
> List[TimeZoneSetup] get_system_time_zone_setups(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of TimeZoneSetup

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.time_zone_setup import TimeZoneSetup
from connectwise_psa.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api-aus.myconnectwise.net/v4_6_release/apis/3.0
# See configuration.py for a list of all supported configuration parameters.
configuration = connectwise_psa.Configuration(
    host = "https://api-aus.myconnectwise.net/v4_6_release/apis/3.0"
)


# Enter a context with an instance of the API client
with connectwise_psa.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = connectwise_psa.TimeZoneSetupsApi(api_client)
    client_id = 'client_id_example' # str | 
    conditions = 'conditions_example' # str |  (optional)
    child_conditions = 'child_conditions_example' # str |  (optional)
    custom_field_conditions = 'custom_field_conditions_example' # str |  (optional)
    order_by = 'order_by_example' # str |  (optional)
    fields = 'fields_example' # str |  (optional)
    page = 56 # int |  (optional)
    page_size = 56 # int |  (optional)
    page_id = 56 # int |  (optional)

    try:
        # Get List of TimeZoneSetup
        api_response = api_instance.get_system_time_zone_setups(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of TimeZoneSetupsApi->get_system_time_zone_setups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TimeZoneSetupsApi->get_system_time_zone_setups: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**|  | 
 **conditions** | **str**|  | [optional] 
 **child_conditions** | **str**|  | [optional] 
 **custom_field_conditions** | **str**|  | [optional] 
 **order_by** | **str**|  | [optional] 
 **fields** | **str**|  | [optional] 
 **page** | **int**|  | [optional] 
 **page_size** | **int**|  | [optional] 
 **page_id** | **int**|  | [optional] 

### Return type

[**List[TimeZoneSetup]**](TimeZoneSetup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of TimeZoneSetup |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_system_time_zone_setups_by_id**
> TimeZoneSetup get_system_time_zone_setups_by_id(id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get TimeZoneSetup

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.time_zone_setup import TimeZoneSetup
from connectwise_psa.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api-aus.myconnectwise.net/v4_6_release/apis/3.0
# See configuration.py for a list of all supported configuration parameters.
configuration = connectwise_psa.Configuration(
    host = "https://api-aus.myconnectwise.net/v4_6_release/apis/3.0"
)


# Enter a context with an instance of the API client
with connectwise_psa.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = connectwise_psa.TimeZoneSetupsApi(api_client)
    id = 56 # int | timeZoneSetupId
    client_id = 'client_id_example' # str | 
    conditions = 'conditions_example' # str |  (optional)
    child_conditions = 'child_conditions_example' # str |  (optional)
    custom_field_conditions = 'custom_field_conditions_example' # str |  (optional)
    order_by = 'order_by_example' # str |  (optional)
    fields = 'fields_example' # str |  (optional)
    page = 56 # int |  (optional)
    page_size = 56 # int |  (optional)
    page_id = 56 # int |  (optional)

    try:
        # Get TimeZoneSetup
        api_response = api_instance.get_system_time_zone_setups_by_id(id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of TimeZoneSetupsApi->get_system_time_zone_setups_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TimeZoneSetupsApi->get_system_time_zone_setups_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| timeZoneSetupId | 
 **client_id** | **str**|  | 
 **conditions** | **str**|  | [optional] 
 **child_conditions** | **str**|  | [optional] 
 **custom_field_conditions** | **str**|  | [optional] 
 **order_by** | **str**|  | [optional] 
 **fields** | **str**|  | [optional] 
 **page** | **int**|  | [optional] 
 **page_size** | **int**|  | [optional] 
 **page_id** | **int**|  | [optional] 

### Return type

[**TimeZoneSetup**](TimeZoneSetup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | TimeZoneSetup |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_system_time_zone_setups_count**
> Count get_system_time_zone_setups_count(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Count of TimeZoneSetup

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.count import Count
from connectwise_psa.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api-aus.myconnectwise.net/v4_6_release/apis/3.0
# See configuration.py for a list of all supported configuration parameters.
configuration = connectwise_psa.Configuration(
    host = "https://api-aus.myconnectwise.net/v4_6_release/apis/3.0"
)


# Enter a context with an instance of the API client
with connectwise_psa.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = connectwise_psa.TimeZoneSetupsApi(api_client)
    client_id = 'client_id_example' # str | 
    conditions = 'conditions_example' # str |  (optional)
    child_conditions = 'child_conditions_example' # str |  (optional)
    custom_field_conditions = 'custom_field_conditions_example' # str |  (optional)
    order_by = 'order_by_example' # str |  (optional)
    fields = 'fields_example' # str |  (optional)
    page = 56 # int |  (optional)
    page_size = 56 # int |  (optional)
    page_id = 56 # int |  (optional)

    try:
        # Get Count of TimeZoneSetup
        api_response = api_instance.get_system_time_zone_setups_count(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of TimeZoneSetupsApi->get_system_time_zone_setups_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TimeZoneSetupsApi->get_system_time_zone_setups_count: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**|  | 
 **conditions** | **str**|  | [optional] 
 **child_conditions** | **str**|  | [optional] 
 **custom_field_conditions** | **str**|  | [optional] 
 **order_by** | **str**|  | [optional] 
 **fields** | **str**|  | [optional] 
 **page** | **int**|  | [optional] 
 **page_size** | **int**|  | [optional] 
 **page_id** | **int**|  | [optional] 

### Return type

[**Count**](Count.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Count |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_system_time_zone_setups_by_id**
> TimeZoneSetup patch_system_time_zone_setups_by_id(id, client_id, patch_operation)

Patch TimeZoneSetup

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.patch_operation import PatchOperation
from connectwise_psa.models.time_zone_setup import TimeZoneSetup
from connectwise_psa.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api-aus.myconnectwise.net/v4_6_release/apis/3.0
# See configuration.py for a list of all supported configuration parameters.
configuration = connectwise_psa.Configuration(
    host = "https://api-aus.myconnectwise.net/v4_6_release/apis/3.0"
)


# Enter a context with an instance of the API client
with connectwise_psa.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = connectwise_psa.TimeZoneSetupsApi(api_client)
    id = 56 # int | timeZoneSetupId
    client_id = 'client_id_example' # str | 
    patch_operation = [connectwise_psa.PatchOperation()] # List[PatchOperation] | List of PatchOperation

    try:
        # Patch TimeZoneSetup
        api_response = api_instance.patch_system_time_zone_setups_by_id(id, client_id, patch_operation)
        print("The response of TimeZoneSetupsApi->patch_system_time_zone_setups_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TimeZoneSetupsApi->patch_system_time_zone_setups_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| timeZoneSetupId | 
 **client_id** | **str**|  | 
 **patch_operation** | [**List[PatchOperation]**](PatchOperation.md)| List of PatchOperation | 

### Return type

[**TimeZoneSetup**](TimeZoneSetup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | TimeZoneSetup |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_system_time_zone_setups**
> TimeZoneSetup post_system_time_zone_setups(client_id, time_zone_setup)

Post TimeZoneSetup

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.time_zone_setup import TimeZoneSetup
from connectwise_psa.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api-aus.myconnectwise.net/v4_6_release/apis/3.0
# See configuration.py for a list of all supported configuration parameters.
configuration = connectwise_psa.Configuration(
    host = "https://api-aus.myconnectwise.net/v4_6_release/apis/3.0"
)


# Enter a context with an instance of the API client
with connectwise_psa.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = connectwise_psa.TimeZoneSetupsApi(api_client)
    client_id = 'client_id_example' # str | 
    time_zone_setup = connectwise_psa.TimeZoneSetup() # TimeZoneSetup | timeZoneSetup

    try:
        # Post TimeZoneSetup
        api_response = api_instance.post_system_time_zone_setups(client_id, time_zone_setup)
        print("The response of TimeZoneSetupsApi->post_system_time_zone_setups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TimeZoneSetupsApi->post_system_time_zone_setups: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**|  | 
 **time_zone_setup** | [**TimeZoneSetup**](TimeZoneSetup.md)| timeZoneSetup | 

### Return type

[**TimeZoneSetup**](TimeZoneSetup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | TimeZoneSetup |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_system_time_zone_setups_by_id**
> TimeZoneSetup put_system_time_zone_setups_by_id(id, client_id, time_zone_setup)

Put TimeZoneSetup

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.time_zone_setup import TimeZoneSetup
from connectwise_psa.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api-aus.myconnectwise.net/v4_6_release/apis/3.0
# See configuration.py for a list of all supported configuration parameters.
configuration = connectwise_psa.Configuration(
    host = "https://api-aus.myconnectwise.net/v4_6_release/apis/3.0"
)


# Enter a context with an instance of the API client
with connectwise_psa.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = connectwise_psa.TimeZoneSetupsApi(api_client)
    id = 56 # int | timeZoneSetupId
    client_id = 'client_id_example' # str | 
    time_zone_setup = connectwise_psa.TimeZoneSetup() # TimeZoneSetup | timeZoneSetup

    try:
        # Put TimeZoneSetup
        api_response = api_instance.put_system_time_zone_setups_by_id(id, client_id, time_zone_setup)
        print("The response of TimeZoneSetupsApi->put_system_time_zone_setups_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TimeZoneSetupsApi->put_system_time_zone_setups_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| timeZoneSetupId | 
 **client_id** | **str**|  | 
 **time_zone_setup** | [**TimeZoneSetup**](TimeZoneSetup.md)| timeZoneSetup | 

### Return type

[**TimeZoneSetup**](TimeZoneSetup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | TimeZoneSetup |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

