# connectwise_psa.AutoSyncTimesApi

All URIs are relative to *https://aus-api.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_system_auto_sync_time_by_id**](AutoSyncTimesApi.md#delete_system_auto_sync_time_by_id) | **DELETE** /system/autoSyncTime/{id} | Delete AutoSyncTime
[**get_system_auto_sync_time**](AutoSyncTimesApi.md#get_system_auto_sync_time) | **GET** /system/autoSyncTime | Get List of AutoSyncTime
[**get_system_auto_sync_time_by_id**](AutoSyncTimesApi.md#get_system_auto_sync_time_by_id) | **GET** /system/autoSyncTime/{id} | Get AutoSyncTime
[**get_system_auto_sync_time_count**](AutoSyncTimesApi.md#get_system_auto_sync_time_count) | **GET** /system/autoSyncTime/count | Get Count of AutoSyncTime
[**patch_system_auto_sync_time_by_id**](AutoSyncTimesApi.md#patch_system_auto_sync_time_by_id) | **PATCH** /system/autoSyncTime/{id} | Patch AutoSyncTime
[**post_system_auto_sync_time**](AutoSyncTimesApi.md#post_system_auto_sync_time) | **POST** /system/autoSyncTime | Post AutoSyncTime
[**put_system_auto_sync_time_by_id**](AutoSyncTimesApi.md#put_system_auto_sync_time_by_id) | **PUT** /system/autoSyncTime/{id} | Put AutoSyncTime


# **delete_system_auto_sync_time_by_id**
> delete_system_auto_sync_time_by_id(id, client_id)

Delete AutoSyncTime

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
    api_instance = connectwise_psa.AutoSyncTimesApi(api_client)
    id = 56 # int | autoSyncTimeId
    client_id = 'client_id_example' # str | 

    try:
        # Delete AutoSyncTime
        api_instance.delete_system_auto_sync_time_by_id(id, client_id)
    except Exception as e:
        print("Exception when calling AutoSyncTimesApi->delete_system_auto_sync_time_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| autoSyncTimeId | 
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

# **get_system_auto_sync_time**
> List[AutoSyncTime] get_system_auto_sync_time(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of AutoSyncTime

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.auto_sync_time import AutoSyncTime
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
    api_instance = connectwise_psa.AutoSyncTimesApi(api_client)
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
        # Get List of AutoSyncTime
        api_response = api_instance.get_system_auto_sync_time(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of AutoSyncTimesApi->get_system_auto_sync_time:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutoSyncTimesApi->get_system_auto_sync_time: %s\n" % e)
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

[**List[AutoSyncTime]**](AutoSyncTime.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of AutoSyncTime |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_system_auto_sync_time_by_id**
> AutoSyncTime get_system_auto_sync_time_by_id(id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get AutoSyncTime

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.auto_sync_time import AutoSyncTime
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
    api_instance = connectwise_psa.AutoSyncTimesApi(api_client)
    id = 56 # int | autoSyncTimeId
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
        # Get AutoSyncTime
        api_response = api_instance.get_system_auto_sync_time_by_id(id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of AutoSyncTimesApi->get_system_auto_sync_time_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutoSyncTimesApi->get_system_auto_sync_time_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| autoSyncTimeId | 
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

[**AutoSyncTime**](AutoSyncTime.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | AutoSyncTime |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_system_auto_sync_time_count**
> Count get_system_auto_sync_time_count(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Count of AutoSyncTime

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
    api_instance = connectwise_psa.AutoSyncTimesApi(api_client)
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
        # Get Count of AutoSyncTime
        api_response = api_instance.get_system_auto_sync_time_count(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of AutoSyncTimesApi->get_system_auto_sync_time_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutoSyncTimesApi->get_system_auto_sync_time_count: %s\n" % e)
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

# **patch_system_auto_sync_time_by_id**
> AutoSyncTime patch_system_auto_sync_time_by_id(id, client_id, patch_operation)

Patch AutoSyncTime

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.auto_sync_time import AutoSyncTime
from connectwise_psa.models.patch_operation import PatchOperation
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
    api_instance = connectwise_psa.AutoSyncTimesApi(api_client)
    id = 56 # int | autoSyncTimeId
    client_id = 'client_id_example' # str | 
    patch_operation = [connectwise_psa.PatchOperation()] # List[PatchOperation] | List of PatchOperation

    try:
        # Patch AutoSyncTime
        api_response = api_instance.patch_system_auto_sync_time_by_id(id, client_id, patch_operation)
        print("The response of AutoSyncTimesApi->patch_system_auto_sync_time_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutoSyncTimesApi->patch_system_auto_sync_time_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| autoSyncTimeId | 
 **client_id** | **str**|  | 
 **patch_operation** | [**List[PatchOperation]**](PatchOperation.md)| List of PatchOperation | 

### Return type

[**AutoSyncTime**](AutoSyncTime.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | AutoSyncTime |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_system_auto_sync_time**
> AutoSyncTime post_system_auto_sync_time(client_id, auto_sync_time)

Post AutoSyncTime

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.auto_sync_time import AutoSyncTime
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
    api_instance = connectwise_psa.AutoSyncTimesApi(api_client)
    client_id = 'client_id_example' # str | 
    auto_sync_time = connectwise_psa.AutoSyncTime() # AutoSyncTime | autoSyncTime

    try:
        # Post AutoSyncTime
        api_response = api_instance.post_system_auto_sync_time(client_id, auto_sync_time)
        print("The response of AutoSyncTimesApi->post_system_auto_sync_time:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutoSyncTimesApi->post_system_auto_sync_time: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**|  | 
 **auto_sync_time** | [**AutoSyncTime**](AutoSyncTime.md)| autoSyncTime | 

### Return type

[**AutoSyncTime**](AutoSyncTime.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | AutoSyncTime |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_system_auto_sync_time_by_id**
> AutoSyncTime put_system_auto_sync_time_by_id(id, client_id, auto_sync_time)

Put AutoSyncTime

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.auto_sync_time import AutoSyncTime
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
    api_instance = connectwise_psa.AutoSyncTimesApi(api_client)
    id = 56 # int | autoSyncTimeId
    client_id = 'client_id_example' # str | 
    auto_sync_time = connectwise_psa.AutoSyncTime() # AutoSyncTime | autoSyncTime

    try:
        # Put AutoSyncTime
        api_response = api_instance.put_system_auto_sync_time_by_id(id, client_id, auto_sync_time)
        print("The response of AutoSyncTimesApi->put_system_auto_sync_time_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutoSyncTimesApi->put_system_auto_sync_time_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| autoSyncTimeId | 
 **client_id** | **str**|  | 
 **auto_sync_time** | [**AutoSyncTime**](AutoSyncTime.md)| autoSyncTime | 

### Return type

[**AutoSyncTime**](AutoSyncTime.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | AutoSyncTime |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

