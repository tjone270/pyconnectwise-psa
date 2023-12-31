# connectwise_psa.ActivityStopwatchesApi

All URIs are relative to *https://api-aus.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_time_activitystopwatches_by_id**](ActivityStopwatchesApi.md#delete_time_activitystopwatches_by_id) | **DELETE** /time/activitystopwatches/{id} | Delete ActivityStopwatch
[**get_time_activitystopwatches**](ActivityStopwatchesApi.md#get_time_activitystopwatches) | **GET** /time/activitystopwatches | Get List of ActivityStopwatch
[**get_time_activitystopwatches_by_id**](ActivityStopwatchesApi.md#get_time_activitystopwatches_by_id) | **GET** /time/activitystopwatches/{id} | Get ActivityStopwatch
[**get_time_activitystopwatches_count**](ActivityStopwatchesApi.md#get_time_activitystopwatches_count) | **GET** /time/activitystopwatches/count | Get Count of ActivityStopwatch
[**patch_time_activitystopwatches_by_id**](ActivityStopwatchesApi.md#patch_time_activitystopwatches_by_id) | **PATCH** /time/activitystopwatches/{id} | Patch ActivityStopwatch
[**post_time_activitystopwatches**](ActivityStopwatchesApi.md#post_time_activitystopwatches) | **POST** /time/activitystopwatches | Post ActivityStopwatch
[**put_time_activitystopwatches_by_id**](ActivityStopwatchesApi.md#put_time_activitystopwatches_by_id) | **PUT** /time/activitystopwatches/{id} | Put ActivityStopwatch


# **delete_time_activitystopwatches_by_id**
> delete_time_activitystopwatches_by_id(id, client_id)

Delete ActivityStopwatch

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
    api_instance = connectwise_psa.ActivityStopwatchesApi(api_client)
    id = 56 # int | activitystopwatcheId
    client_id = 'client_id_example' # str | 

    try:
        # Delete ActivityStopwatch
        api_instance.delete_time_activitystopwatches_by_id(id, client_id)
    except Exception as e:
        print("Exception when calling ActivityStopwatchesApi->delete_time_activitystopwatches_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| activitystopwatcheId | 
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

# **get_time_activitystopwatches**
> List[ActivityStopwatch] get_time_activitystopwatches(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of ActivityStopwatch

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.activity_stopwatch import ActivityStopwatch
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
    api_instance = connectwise_psa.ActivityStopwatchesApi(api_client)
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
        # Get List of ActivityStopwatch
        api_response = api_instance.get_time_activitystopwatches(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of ActivityStopwatchesApi->get_time_activitystopwatches:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityStopwatchesApi->get_time_activitystopwatches: %s\n" % e)
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

[**List[ActivityStopwatch]**](ActivityStopwatch.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of ActivityStopwatch |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_time_activitystopwatches_by_id**
> ActivityStopwatch get_time_activitystopwatches_by_id(id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get ActivityStopwatch

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.activity_stopwatch import ActivityStopwatch
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
    api_instance = connectwise_psa.ActivityStopwatchesApi(api_client)
    id = 56 # int | activitystopwatcheId
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
        # Get ActivityStopwatch
        api_response = api_instance.get_time_activitystopwatches_by_id(id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of ActivityStopwatchesApi->get_time_activitystopwatches_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityStopwatchesApi->get_time_activitystopwatches_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| activitystopwatcheId | 
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

[**ActivityStopwatch**](ActivityStopwatch.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ActivityStopwatch |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_time_activitystopwatches_count**
> Count get_time_activitystopwatches_count(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Count of ActivityStopwatch

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
    api_instance = connectwise_psa.ActivityStopwatchesApi(api_client)
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
        # Get Count of ActivityStopwatch
        api_response = api_instance.get_time_activitystopwatches_count(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of ActivityStopwatchesApi->get_time_activitystopwatches_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityStopwatchesApi->get_time_activitystopwatches_count: %s\n" % e)
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

# **patch_time_activitystopwatches_by_id**
> ActivityStopwatch patch_time_activitystopwatches_by_id(id, client_id, patch_operation)

Patch ActivityStopwatch

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.activity_stopwatch import ActivityStopwatch
from connectwise_psa.models.patch_operation import PatchOperation
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
    api_instance = connectwise_psa.ActivityStopwatchesApi(api_client)
    id = 56 # int | activitystopwatcheId
    client_id = 'client_id_example' # str | 
    patch_operation = [connectwise_psa.PatchOperation()] # List[PatchOperation] | List of PatchOperation

    try:
        # Patch ActivityStopwatch
        api_response = api_instance.patch_time_activitystopwatches_by_id(id, client_id, patch_operation)
        print("The response of ActivityStopwatchesApi->patch_time_activitystopwatches_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityStopwatchesApi->patch_time_activitystopwatches_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| activitystopwatcheId | 
 **client_id** | **str**|  | 
 **patch_operation** | [**List[PatchOperation]**](PatchOperation.md)| List of PatchOperation | 

### Return type

[**ActivityStopwatch**](ActivityStopwatch.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ActivityStopwatch |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_time_activitystopwatches**
> ActivityStopwatch post_time_activitystopwatches(client_id, activity_stopwatch)

Post ActivityStopwatch

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.activity_stopwatch import ActivityStopwatch
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
    api_instance = connectwise_psa.ActivityStopwatchesApi(api_client)
    client_id = 'client_id_example' # str | 
    activity_stopwatch = connectwise_psa.ActivityStopwatch() # ActivityStopwatch | activityStopwatch

    try:
        # Post ActivityStopwatch
        api_response = api_instance.post_time_activitystopwatches(client_id, activity_stopwatch)
        print("The response of ActivityStopwatchesApi->post_time_activitystopwatches:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityStopwatchesApi->post_time_activitystopwatches: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**|  | 
 **activity_stopwatch** | [**ActivityStopwatch**](ActivityStopwatch.md)| activityStopwatch | 

### Return type

[**ActivityStopwatch**](ActivityStopwatch.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | ActivityStopwatch |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_time_activitystopwatches_by_id**
> ActivityStopwatch put_time_activitystopwatches_by_id(id, client_id, activity_stopwatch)

Put ActivityStopwatch

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.activity_stopwatch import ActivityStopwatch
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
    api_instance = connectwise_psa.ActivityStopwatchesApi(api_client)
    id = 56 # int | activitystopwatcheId
    client_id = 'client_id_example' # str | 
    activity_stopwatch = connectwise_psa.ActivityStopwatch() # ActivityStopwatch | activityStopwatch

    try:
        # Put ActivityStopwatch
        api_response = api_instance.put_time_activitystopwatches_by_id(id, client_id, activity_stopwatch)
        print("The response of ActivityStopwatchesApi->put_time_activitystopwatches_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityStopwatchesApi->put_time_activitystopwatches_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| activitystopwatcheId | 
 **client_id** | **str**|  | 
 **activity_stopwatch** | [**ActivityStopwatch**](ActivityStopwatch.md)| activityStopwatch | 

### Return type

[**ActivityStopwatch**](ActivityStopwatch.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ActivityStopwatch |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

