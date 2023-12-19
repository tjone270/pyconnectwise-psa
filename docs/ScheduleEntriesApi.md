# connectwise_psa.ScheduleEntriesApi

All URIs are relative to *https://aus-api.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_schedule_entries_by_id**](ScheduleEntriesApi.md#delete_schedule_entries_by_id) | **DELETE** /schedule/entries/{id} | Delete ScheduleEntry
[**get_schedule_entries**](ScheduleEntriesApi.md#get_schedule_entries) | **GET** /schedule/entries | Get List of ScheduleEntry
[**get_schedule_entries_by_id**](ScheduleEntriesApi.md#get_schedule_entries_by_id) | **GET** /schedule/entries/{id} | Get ScheduleEntry
[**get_schedule_entries_count**](ScheduleEntriesApi.md#get_schedule_entries_count) | **GET** /schedule/entries/count | Get Count of ScheduleEntry
[**patch_schedule_entries_by_id**](ScheduleEntriesApi.md#patch_schedule_entries_by_id) | **PATCH** /schedule/entries/{id} | Patch ScheduleEntry
[**post_schedule_entries**](ScheduleEntriesApi.md#post_schedule_entries) | **POST** /schedule/entries | Post ScheduleEntry
[**put_schedule_entries_by_id**](ScheduleEntriesApi.md#put_schedule_entries_by_id) | **PUT** /schedule/entries/{id} | Put ScheduleEntry


# **delete_schedule_entries_by_id**
> delete_schedule_entries_by_id(id, client_id)

Delete ScheduleEntry

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://aus-api.myconnectwise.net/v4_6_release/apis/3.0
# See configuration.py for a list of all supported configuration parameters.
configuration = connectwise_psa.Configuration(
    host = "https://aus-api.myconnectwise.net/v4_6_release/apis/3.0"
)


# Enter a context with an instance of the API client
with connectwise_psa.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = connectwise_psa.ScheduleEntriesApi(api_client)
    id = 56 # int | entryId
    client_id = 'client_id_example' # str | 

    try:
        # Delete ScheduleEntry
        api_instance.delete_schedule_entries_by_id(id, client_id)
    except Exception as e:
        print("Exception when calling ScheduleEntriesApi->delete_schedule_entries_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| entryId | 
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

# **get_schedule_entries**
> List[ScheduleEntry] get_schedule_entries(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of ScheduleEntry

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.schedule_entry import ScheduleEntry
from connectwise_psa.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://aus-api.myconnectwise.net/v4_6_release/apis/3.0
# See configuration.py for a list of all supported configuration parameters.
configuration = connectwise_psa.Configuration(
    host = "https://aus-api.myconnectwise.net/v4_6_release/apis/3.0"
)


# Enter a context with an instance of the API client
with connectwise_psa.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = connectwise_psa.ScheduleEntriesApi(api_client)
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
        # Get List of ScheduleEntry
        api_response = api_instance.get_schedule_entries(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of ScheduleEntriesApi->get_schedule_entries:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScheduleEntriesApi->get_schedule_entries: %s\n" % e)
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

[**List[ScheduleEntry]**](ScheduleEntry.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of ScheduleEntry |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_schedule_entries_by_id**
> ScheduleEntry get_schedule_entries_by_id(id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get ScheduleEntry

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.schedule_entry import ScheduleEntry
from connectwise_psa.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://aus-api.myconnectwise.net/v4_6_release/apis/3.0
# See configuration.py for a list of all supported configuration parameters.
configuration = connectwise_psa.Configuration(
    host = "https://aus-api.myconnectwise.net/v4_6_release/apis/3.0"
)


# Enter a context with an instance of the API client
with connectwise_psa.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = connectwise_psa.ScheduleEntriesApi(api_client)
    id = 56 # int | entryId
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
        # Get ScheduleEntry
        api_response = api_instance.get_schedule_entries_by_id(id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of ScheduleEntriesApi->get_schedule_entries_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScheduleEntriesApi->get_schedule_entries_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| entryId | 
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

[**ScheduleEntry**](ScheduleEntry.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ScheduleEntry |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_schedule_entries_count**
> Count get_schedule_entries_count(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Count of ScheduleEntry

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.count import Count
from connectwise_psa.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://aus-api.myconnectwise.net/v4_6_release/apis/3.0
# See configuration.py for a list of all supported configuration parameters.
configuration = connectwise_psa.Configuration(
    host = "https://aus-api.myconnectwise.net/v4_6_release/apis/3.0"
)


# Enter a context with an instance of the API client
with connectwise_psa.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = connectwise_psa.ScheduleEntriesApi(api_client)
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
        # Get Count of ScheduleEntry
        api_response = api_instance.get_schedule_entries_count(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of ScheduleEntriesApi->get_schedule_entries_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScheduleEntriesApi->get_schedule_entries_count: %s\n" % e)
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

# **patch_schedule_entries_by_id**
> ScheduleEntry patch_schedule_entries_by_id(id, client_id, patch_operation)

Patch ScheduleEntry

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.patch_operation import PatchOperation
from connectwise_psa.models.schedule_entry import ScheduleEntry
from connectwise_psa.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://aus-api.myconnectwise.net/v4_6_release/apis/3.0
# See configuration.py for a list of all supported configuration parameters.
configuration = connectwise_psa.Configuration(
    host = "https://aus-api.myconnectwise.net/v4_6_release/apis/3.0"
)


# Enter a context with an instance of the API client
with connectwise_psa.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = connectwise_psa.ScheduleEntriesApi(api_client)
    id = 56 # int | entryId
    client_id = 'client_id_example' # str | 
    patch_operation = [connectwise_psa.PatchOperation()] # List[PatchOperation] | List of PatchOperation

    try:
        # Patch ScheduleEntry
        api_response = api_instance.patch_schedule_entries_by_id(id, client_id, patch_operation)
        print("The response of ScheduleEntriesApi->patch_schedule_entries_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScheduleEntriesApi->patch_schedule_entries_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| entryId | 
 **client_id** | **str**|  | 
 **patch_operation** | [**List[PatchOperation]**](PatchOperation.md)| List of PatchOperation | 

### Return type

[**ScheduleEntry**](ScheduleEntry.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ScheduleEntry |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_schedule_entries**
> ScheduleEntry post_schedule_entries(client_id, schedule_entry)

Post ScheduleEntry

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.schedule_entry import ScheduleEntry
from connectwise_psa.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://aus-api.myconnectwise.net/v4_6_release/apis/3.0
# See configuration.py for a list of all supported configuration parameters.
configuration = connectwise_psa.Configuration(
    host = "https://aus-api.myconnectwise.net/v4_6_release/apis/3.0"
)


# Enter a context with an instance of the API client
with connectwise_psa.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = connectwise_psa.ScheduleEntriesApi(api_client)
    client_id = 'client_id_example' # str | 
    schedule_entry = connectwise_psa.ScheduleEntry() # ScheduleEntry | scheduleEntry

    try:
        # Post ScheduleEntry
        api_response = api_instance.post_schedule_entries(client_id, schedule_entry)
        print("The response of ScheduleEntriesApi->post_schedule_entries:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScheduleEntriesApi->post_schedule_entries: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**|  | 
 **schedule_entry** | [**ScheduleEntry**](ScheduleEntry.md)| scheduleEntry | 

### Return type

[**ScheduleEntry**](ScheduleEntry.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | ScheduleEntry |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_schedule_entries_by_id**
> ScheduleEntry put_schedule_entries_by_id(id, client_id, schedule_entry)

Put ScheduleEntry

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.schedule_entry import ScheduleEntry
from connectwise_psa.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://aus-api.myconnectwise.net/v4_6_release/apis/3.0
# See configuration.py for a list of all supported configuration parameters.
configuration = connectwise_psa.Configuration(
    host = "https://aus-api.myconnectwise.net/v4_6_release/apis/3.0"
)


# Enter a context with an instance of the API client
with connectwise_psa.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = connectwise_psa.ScheduleEntriesApi(api_client)
    id = 56 # int | entryId
    client_id = 'client_id_example' # str | 
    schedule_entry = connectwise_psa.ScheduleEntry() # ScheduleEntry | scheduleEntry

    try:
        # Put ScheduleEntry
        api_response = api_instance.put_schedule_entries_by_id(id, client_id, schedule_entry)
        print("The response of ScheduleEntriesApi->put_schedule_entries_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScheduleEntriesApi->put_schedule_entries_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| entryId | 
 **client_id** | **str**|  | 
 **schedule_entry** | [**ScheduleEntry**](ScheduleEntry.md)| scheduleEntry | 

### Return type

[**ScheduleEntry**](ScheduleEntry.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ScheduleEntry |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

