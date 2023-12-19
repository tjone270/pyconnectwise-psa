# connectwise_psa.ScheduleReminderTimeApi

All URIs are relative to *https://aus-api.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_schedule_reminder_times**](ScheduleReminderTimeApi.md#get_schedule_reminder_times) | **GET** /schedule/reminderTimes | Get List of ScheduleReminderTime
[**get_schedule_reminder_times_by_id**](ScheduleReminderTimeApi.md#get_schedule_reminder_times_by_id) | **GET** /schedule/reminderTimes/{id} | Get ScheduleReminderTime
[**get_schedule_reminder_times_count**](ScheduleReminderTimeApi.md#get_schedule_reminder_times_count) | **GET** /schedule/reminderTimes/count | Get Count of ScheduleReminderTime
[**patch_schedule_reminder_times_by_id**](ScheduleReminderTimeApi.md#patch_schedule_reminder_times_by_id) | **PATCH** /schedule/reminderTimes/{id} | Patch ScheduleReminderTime
[**put_schedule_reminder_times_by_id**](ScheduleReminderTimeApi.md#put_schedule_reminder_times_by_id) | **PUT** /schedule/reminderTimes/{id} | Put ScheduleReminderTime


# **get_schedule_reminder_times**
> List[ScheduleReminderTime] get_schedule_reminder_times(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of ScheduleReminderTime

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.schedule_reminder_time import ScheduleReminderTime
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
    api_instance = connectwise_psa.ScheduleReminderTimeApi(api_client)
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
        # Get List of ScheduleReminderTime
        api_response = api_instance.get_schedule_reminder_times(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of ScheduleReminderTimeApi->get_schedule_reminder_times:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScheduleReminderTimeApi->get_schedule_reminder_times: %s\n" % e)
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

[**List[ScheduleReminderTime]**](ScheduleReminderTime.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of ScheduleReminderTime |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_schedule_reminder_times_by_id**
> ScheduleReminderTime get_schedule_reminder_times_by_id(id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get ScheduleReminderTime

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.schedule_reminder_time import ScheduleReminderTime
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
    api_instance = connectwise_psa.ScheduleReminderTimeApi(api_client)
    id = 56 # int | reminderTimeId
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
        # Get ScheduleReminderTime
        api_response = api_instance.get_schedule_reminder_times_by_id(id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of ScheduleReminderTimeApi->get_schedule_reminder_times_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScheduleReminderTimeApi->get_schedule_reminder_times_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| reminderTimeId | 
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

[**ScheduleReminderTime**](ScheduleReminderTime.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ScheduleReminderTime |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_schedule_reminder_times_count**
> Count get_schedule_reminder_times_count(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Count of ScheduleReminderTime

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
    api_instance = connectwise_psa.ScheduleReminderTimeApi(api_client)
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
        # Get Count of ScheduleReminderTime
        api_response = api_instance.get_schedule_reminder_times_count(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of ScheduleReminderTimeApi->get_schedule_reminder_times_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScheduleReminderTimeApi->get_schedule_reminder_times_count: %s\n" % e)
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

# **patch_schedule_reminder_times_by_id**
> ScheduleReminderTime patch_schedule_reminder_times_by_id(id, client_id, patch_operation)

Patch ScheduleReminderTime

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.patch_operation import PatchOperation
from connectwise_psa.models.schedule_reminder_time import ScheduleReminderTime
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
    api_instance = connectwise_psa.ScheduleReminderTimeApi(api_client)
    id = 56 # int | reminderTimeId
    client_id = 'client_id_example' # str | 
    patch_operation = [connectwise_psa.PatchOperation()] # List[PatchOperation] | List of PatchOperation

    try:
        # Patch ScheduleReminderTime
        api_response = api_instance.patch_schedule_reminder_times_by_id(id, client_id, patch_operation)
        print("The response of ScheduleReminderTimeApi->patch_schedule_reminder_times_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScheduleReminderTimeApi->patch_schedule_reminder_times_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| reminderTimeId | 
 **client_id** | **str**|  | 
 **patch_operation** | [**List[PatchOperation]**](PatchOperation.md)| List of PatchOperation | 

### Return type

[**ScheduleReminderTime**](ScheduleReminderTime.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ScheduleReminderTime |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_schedule_reminder_times_by_id**
> ScheduleReminderTime put_schedule_reminder_times_by_id(id, client_id, schedule_reminder_time)

Put ScheduleReminderTime

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.schedule_reminder_time import ScheduleReminderTime
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
    api_instance = connectwise_psa.ScheduleReminderTimeApi(api_client)
    id = 56 # int | reminderTimeId
    client_id = 'client_id_example' # str | 
    schedule_reminder_time = connectwise_psa.ScheduleReminderTime() # ScheduleReminderTime | reminderTime

    try:
        # Put ScheduleReminderTime
        api_response = api_instance.put_schedule_reminder_times_by_id(id, client_id, schedule_reminder_time)
        print("The response of ScheduleReminderTimeApi->put_schedule_reminder_times_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScheduleReminderTimeApi->put_schedule_reminder_times_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| reminderTimeId | 
 **client_id** | **str**|  | 
 **schedule_reminder_time** | [**ScheduleReminderTime**](ScheduleReminderTime.md)| reminderTime | 

### Return type

[**ScheduleReminderTime**](ScheduleReminderTime.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ScheduleReminderTime |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

