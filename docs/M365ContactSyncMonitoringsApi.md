# connectwise_psa.M365ContactSyncMonitoringsApi

All URIs are relative to *https://api-aus.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_system_contactsync_monitoring_type_by_id**](M365ContactSyncMonitoringsApi.md#delete_system_contactsync_monitoring_type_by_id) | **DELETE** /system/contactsync/monitoring/type/{id} | Delete Async
[**get_system_contactsync_monitoring**](M365ContactSyncMonitoringsApi.md#get_system_contactsync_monitoring) | **GET** /system/contactsync/monitoring | Get List of M365ContactSyncMonitorings
[**get_system_contactsync_monitoring_by_id**](M365ContactSyncMonitoringsApi.md#get_system_contactsync_monitoring_by_id) | **GET** /system/contactsync/monitoring/{id} | Get M365ContactSyncMonitorings
[**get_system_contactsync_monitoring_count**](M365ContactSyncMonitoringsApi.md#get_system_contactsync_monitoring_count) | **GET** /system/contactsync/monitoring/count | Get Count of M365ContactSyncMonitorings
[**get_system_contactsync_monitoring_notificationtype**](M365ContactSyncMonitoringsApi.md#get_system_contactsync_monitoring_notificationtype) | **GET** /system/contactsync/monitoring/notificationtype/ | Get M365ContactSyncMonitoringNotification TypeId Async
[**get_system_contactsync_monitoring_type_by_id**](M365ContactSyncMonitoringsApi.md#get_system_contactsync_monitoring_type_by_id) | **GET** /system/contactsync/monitoring/type/{id} | Get M365ContactSyncMonitoring By TypeId Async
[**patch_system_contactsync_monitoring**](M365ContactSyncMonitoringsApi.md#patch_system_contactsync_monitoring) | **PATCH** /system/contactsync/monitoring/ | Update Async
[**post_system_contactsync_monitoring**](M365ContactSyncMonitoringsApi.md#post_system_contactsync_monitoring) | **POST** /system/contactsync/monitoring/ | Create Async


# **delete_system_contactsync_monitoring_type_by_id**
> delete_system_contactsync_monitoring_type_by_id(id, client_id)

Delete Async

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
    api_instance = connectwise_psa.M365ContactSyncMonitoringsApi(api_client)
    id = 56 # int | M365ContactSyncMonitoringId
    client_id = 'client_id_example' # str | 

    try:
        # Delete Async
        api_instance.delete_system_contactsync_monitoring_type_by_id(id, client_id)
    except Exception as e:
        print("Exception when calling M365ContactSyncMonitoringsApi->delete_system_contactsync_monitoring_type_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| M365ContactSyncMonitoringId | 
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
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_system_contactsync_monitoring**
> List[M365ContactSyncMonitoring] get_system_contactsync_monitoring(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of M365ContactSyncMonitorings

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.m365_contact_sync_monitoring import M365ContactSyncMonitoring
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
    api_instance = connectwise_psa.M365ContactSyncMonitoringsApi(api_client)
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
        # Get List of M365ContactSyncMonitorings
        api_response = api_instance.get_system_contactsync_monitoring(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of M365ContactSyncMonitoringsApi->get_system_contactsync_monitoring:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling M365ContactSyncMonitoringsApi->get_system_contactsync_monitoring: %s\n" % e)
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

[**List[M365ContactSyncMonitoring]**](M365ContactSyncMonitoring.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of M365ContactSyncMonitorings |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_system_contactsync_monitoring_by_id**
> M365ContactSyncMonitoring get_system_contactsync_monitoring_by_id(id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get M365ContactSyncMonitorings

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.m365_contact_sync_monitoring import M365ContactSyncMonitoring
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
    api_instance = connectwise_psa.M365ContactSyncMonitoringsApi(api_client)
    id = 56 # int | M365ContactSyncMonitoringId
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
        # Get M365ContactSyncMonitorings
        api_response = api_instance.get_system_contactsync_monitoring_by_id(id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of M365ContactSyncMonitoringsApi->get_system_contactsync_monitoring_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling M365ContactSyncMonitoringsApi->get_system_contactsync_monitoring_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| M365ContactSyncMonitoringId | 
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

[**M365ContactSyncMonitoring**](M365ContactSyncMonitoring.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | M365ContactSyncMonitoring |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_system_contactsync_monitoring_count**
> Count get_system_contactsync_monitoring_count(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Count of M365ContactSyncMonitorings

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
    api_instance = connectwise_psa.M365ContactSyncMonitoringsApi(api_client)
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
        # Get Count of M365ContactSyncMonitorings
        api_response = api_instance.get_system_contactsync_monitoring_count(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of M365ContactSyncMonitoringsApi->get_system_contactsync_monitoring_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling M365ContactSyncMonitoringsApi->get_system_contactsync_monitoring_count: %s\n" % e)
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

# **get_system_contactsync_monitoring_notificationtype**
> M365ContactSyncMonitoring get_system_contactsync_monitoring_notificationtype(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get M365ContactSyncMonitoringNotification TypeId Async

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.m365_contact_sync_monitoring import M365ContactSyncMonitoring
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
    api_instance = connectwise_psa.M365ContactSyncMonitoringsApi(api_client)
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
        # Get M365ContactSyncMonitoringNotification TypeId Async
        api_response = api_instance.get_system_contactsync_monitoring_notificationtype(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of M365ContactSyncMonitoringsApi->get_system_contactsync_monitoring_notificationtype:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling M365ContactSyncMonitoringsApi->get_system_contactsync_monitoring_notificationtype: %s\n" % e)
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

[**M365ContactSyncMonitoring**](M365ContactSyncMonitoring.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | M365ContactSyncMonitoring |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_system_contactsync_monitoring_type_by_id**
> M365ContactSyncMonitoring get_system_contactsync_monitoring_type_by_id(id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get M365ContactSyncMonitoring By TypeId Async

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.m365_contact_sync_monitoring import M365ContactSyncMonitoring
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
    api_instance = connectwise_psa.M365ContactSyncMonitoringsApi(api_client)
    id = 56 # int | M365ContactSyncMonitoringId
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
        # Get M365ContactSyncMonitoring By TypeId Async
        api_response = api_instance.get_system_contactsync_monitoring_type_by_id(id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of M365ContactSyncMonitoringsApi->get_system_contactsync_monitoring_type_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling M365ContactSyncMonitoringsApi->get_system_contactsync_monitoring_type_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| M365ContactSyncMonitoringId | 
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

[**M365ContactSyncMonitoring**](M365ContactSyncMonitoring.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | M365ContactSyncMonitoring |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_system_contactsync_monitoring**
> M365ContactSyncMonitoring patch_system_contactsync_monitoring(client_id)

Update Async

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.m365_contact_sync_monitoring import M365ContactSyncMonitoring
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
    api_instance = connectwise_psa.M365ContactSyncMonitoringsApi(api_client)
    client_id = 'client_id_example' # str | 

    try:
        # Update Async
        api_response = api_instance.patch_system_contactsync_monitoring(client_id)
        print("The response of M365ContactSyncMonitoringsApi->patch_system_contactsync_monitoring:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling M365ContactSyncMonitoringsApi->patch_system_contactsync_monitoring: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**|  | 

### Return type

[**M365ContactSyncMonitoring**](M365ContactSyncMonitoring.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | M365ContactSyncMonitoring |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_system_contactsync_monitoring**
> M365ContactSyncMonitoring post_system_contactsync_monitoring(client_id)

Create Async

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.m365_contact_sync_monitoring import M365ContactSyncMonitoring
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
    api_instance = connectwise_psa.M365ContactSyncMonitoringsApi(api_client)
    client_id = 'client_id_example' # str | 

    try:
        # Create Async
        api_response = api_instance.post_system_contactsync_monitoring(client_id)
        print("The response of M365ContactSyncMonitoringsApi->post_system_contactsync_monitoring:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling M365ContactSyncMonitoringsApi->post_system_contactsync_monitoring: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**|  | 

### Return type

[**M365ContactSyncMonitoring**](M365ContactSyncMonitoring.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | M365ContactSyncMonitoring |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

