# connectwise_psa.ScheduleStopwatchApi

All URIs are relative to *https://aus-api.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_time_schedulestopwatches_by_id**](ScheduleStopwatchApi.md#delete_time_schedulestopwatches_by_id) | **DELETE** /time/schedulestopwatches/{id} | Delete ScheduleStopwatch
[**get_time_schedulestopwatches**](ScheduleStopwatchApi.md#get_time_schedulestopwatches) | **GET** /time/schedulestopwatches | Get List of ScheduleStopwatch
[**get_time_schedulestopwatches_by_id**](ScheduleStopwatchApi.md#get_time_schedulestopwatches_by_id) | **GET** /time/schedulestopwatches/{id} | Get ScheduleStopwatch
[**get_time_schedulestopwatches_count**](ScheduleStopwatchApi.md#get_time_schedulestopwatches_count) | **GET** /time/schedulestopwatches/count | Get Count of ScheduleStopwatch
[**patch_time_schedulestopwatches_by_id**](ScheduleStopwatchApi.md#patch_time_schedulestopwatches_by_id) | **PATCH** /time/schedulestopwatches/{id} | Patch ScheduleStopwatch
[**post_time_schedulestopwatches**](ScheduleStopwatchApi.md#post_time_schedulestopwatches) | **POST** /time/schedulestopwatches | Post ScheduleStopwatch
[**put_time_schedulestopwatches_by_id**](ScheduleStopwatchApi.md#put_time_schedulestopwatches_by_id) | **PUT** /time/schedulestopwatches/{id} | Put ScheduleStopwatch


# **delete_time_schedulestopwatches_by_id**
> delete_time_schedulestopwatches_by_id(id, client_id)

Delete ScheduleStopwatch

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
    api_instance = connectwise_psa.ScheduleStopwatchApi(api_client)
    id = 56 # int | schedulestopwatcheId
    client_id = 'client_id_example' # str | 

    try:
        # Delete ScheduleStopwatch
        api_instance.delete_time_schedulestopwatches_by_id(id, client_id)
    except Exception as e:
        print("Exception when calling ScheduleStopwatchApi->delete_time_schedulestopwatches_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| schedulestopwatcheId | 
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

# **get_time_schedulestopwatches**
> List[ScheduleStopwatch] get_time_schedulestopwatches(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of ScheduleStopwatch

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.schedule_stopwatch import ScheduleStopwatch
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
    api_instance = connectwise_psa.ScheduleStopwatchApi(api_client)
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
        # Get List of ScheduleStopwatch
        api_response = api_instance.get_time_schedulestopwatches(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of ScheduleStopwatchApi->get_time_schedulestopwatches:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScheduleStopwatchApi->get_time_schedulestopwatches: %s\n" % e)
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

[**List[ScheduleStopwatch]**](ScheduleStopwatch.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of ScheduleStopwatch |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_time_schedulestopwatches_by_id**
> ScheduleStopwatch get_time_schedulestopwatches_by_id(id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get ScheduleStopwatch

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.schedule_stopwatch import ScheduleStopwatch
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
    api_instance = connectwise_psa.ScheduleStopwatchApi(api_client)
    id = 56 # int | schedulestopwatcheId
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
        # Get ScheduleStopwatch
        api_response = api_instance.get_time_schedulestopwatches_by_id(id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of ScheduleStopwatchApi->get_time_schedulestopwatches_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScheduleStopwatchApi->get_time_schedulestopwatches_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| schedulestopwatcheId | 
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

[**ScheduleStopwatch**](ScheduleStopwatch.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ScheduleStopwatch |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_time_schedulestopwatches_count**
> Count get_time_schedulestopwatches_count(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Count of ScheduleStopwatch

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
    api_instance = connectwise_psa.ScheduleStopwatchApi(api_client)
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
        # Get Count of ScheduleStopwatch
        api_response = api_instance.get_time_schedulestopwatches_count(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of ScheduleStopwatchApi->get_time_schedulestopwatches_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScheduleStopwatchApi->get_time_schedulestopwatches_count: %s\n" % e)
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

# **patch_time_schedulestopwatches_by_id**
> ScheduleStopwatch patch_time_schedulestopwatches_by_id(id, client_id, patch_operation)

Patch ScheduleStopwatch

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.patch_operation import PatchOperation
from connectwise_psa.models.schedule_stopwatch import ScheduleStopwatch
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
    api_instance = connectwise_psa.ScheduleStopwatchApi(api_client)
    id = 56 # int | schedulestopwatcheId
    client_id = 'client_id_example' # str | 
    patch_operation = [connectwise_psa.PatchOperation()] # List[PatchOperation] | List of PatchOperation

    try:
        # Patch ScheduleStopwatch
        api_response = api_instance.patch_time_schedulestopwatches_by_id(id, client_id, patch_operation)
        print("The response of ScheduleStopwatchApi->patch_time_schedulestopwatches_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScheduleStopwatchApi->patch_time_schedulestopwatches_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| schedulestopwatcheId | 
 **client_id** | **str**|  | 
 **patch_operation** | [**List[PatchOperation]**](PatchOperation.md)| List of PatchOperation | 

### Return type

[**ScheduleStopwatch**](ScheduleStopwatch.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ScheduleStopwatch |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_time_schedulestopwatches**
> ScheduleStopwatch post_time_schedulestopwatches(client_id, schedule_stopwatch)

Post ScheduleStopwatch

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.schedule_stopwatch import ScheduleStopwatch
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
    api_instance = connectwise_psa.ScheduleStopwatchApi(api_client)
    client_id = 'client_id_example' # str | 
    schedule_stopwatch = connectwise_psa.ScheduleStopwatch() # ScheduleStopwatch | scheduleStopwatch

    try:
        # Post ScheduleStopwatch
        api_response = api_instance.post_time_schedulestopwatches(client_id, schedule_stopwatch)
        print("The response of ScheduleStopwatchApi->post_time_schedulestopwatches:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScheduleStopwatchApi->post_time_schedulestopwatches: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**|  | 
 **schedule_stopwatch** | [**ScheduleStopwatch**](ScheduleStopwatch.md)| scheduleStopwatch | 

### Return type

[**ScheduleStopwatch**](ScheduleStopwatch.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | ScheduleStopwatch |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_time_schedulestopwatches_by_id**
> ScheduleStopwatch put_time_schedulestopwatches_by_id(id, client_id, schedule_stopwatch)

Put ScheduleStopwatch

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.schedule_stopwatch import ScheduleStopwatch
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
    api_instance = connectwise_psa.ScheduleStopwatchApi(api_client)
    id = 56 # int | schedulestopwatcheId
    client_id = 'client_id_example' # str | 
    schedule_stopwatch = connectwise_psa.ScheduleStopwatch() # ScheduleStopwatch | scheduleStopwatch

    try:
        # Put ScheduleStopwatch
        api_response = api_instance.put_time_schedulestopwatches_by_id(id, client_id, schedule_stopwatch)
        print("The response of ScheduleStopwatchApi->put_time_schedulestopwatches_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScheduleStopwatchApi->put_time_schedulestopwatches_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| schedulestopwatcheId | 
 **client_id** | **str**|  | 
 **schedule_stopwatch** | [**ScheduleStopwatch**](ScheduleStopwatch.md)| scheduleStopwatch | 

### Return type

[**ScheduleStopwatch**](ScheduleStopwatch.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ScheduleStopwatch |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

