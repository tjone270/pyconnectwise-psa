# connectwise_psa.RmaStatusNotificationsApi

All URIs are relative to *https://aus-api.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_procurement_rma_statuses_by_parent_id_notifications_by_id**](RmaStatusNotificationsApi.md#delete_procurement_rma_statuses_by_parent_id_notifications_by_id) | **DELETE** /procurement/rmaStatuses/{parentId}/notifications/{id} | Delete RmaStatusNotification
[**get_procurement_rma_statuses_by_parent_id_notifications**](RmaStatusNotificationsApi.md#get_procurement_rma_statuses_by_parent_id_notifications) | **GET** /procurement/rmaStatuses/{parentId}/notifications | Get List of RmaStatusNotification
[**get_procurement_rma_statuses_by_parent_id_notifications_by_id**](RmaStatusNotificationsApi.md#get_procurement_rma_statuses_by_parent_id_notifications_by_id) | **GET** /procurement/rmaStatuses/{parentId}/notifications/{id} | Get RmaStatusNotification
[**get_procurement_rma_statuses_by_parent_id_notifications_count**](RmaStatusNotificationsApi.md#get_procurement_rma_statuses_by_parent_id_notifications_count) | **GET** /procurement/rmaStatuses/{parentId}/notifications/count | Get Count of RmaStatusNotification
[**patch_procurement_rma_statuses_by_parent_id_notifications_by_id**](RmaStatusNotificationsApi.md#patch_procurement_rma_statuses_by_parent_id_notifications_by_id) | **PATCH** /procurement/rmaStatuses/{parentId}/notifications/{id} | Patch RmaStatusNotification
[**post_procurement_rma_statuses_by_parent_id_notifications**](RmaStatusNotificationsApi.md#post_procurement_rma_statuses_by_parent_id_notifications) | **POST** /procurement/rmaStatuses/{parentId}/notifications | Post RmaStatusNotification
[**put_procurement_rma_statuses_by_parent_id_notifications_by_id**](RmaStatusNotificationsApi.md#put_procurement_rma_statuses_by_parent_id_notifications_by_id) | **PUT** /procurement/rmaStatuses/{parentId}/notifications/{id} | Put RmaStatusNotification


# **delete_procurement_rma_statuses_by_parent_id_notifications_by_id**
> delete_procurement_rma_statuses_by_parent_id_notifications_by_id(id, parent_id, client_id)

Delete RmaStatusNotification

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
    api_instance = connectwise_psa.RmaStatusNotificationsApi(api_client)
    id = 56 # int | notificationId
    parent_id = 56 # int | rmaStatusId
    client_id = 'client_id_example' # str | 

    try:
        # Delete RmaStatusNotification
        api_instance.delete_procurement_rma_statuses_by_parent_id_notifications_by_id(id, parent_id, client_id)
    except Exception as e:
        print("Exception when calling RmaStatusNotificationsApi->delete_procurement_rma_statuses_by_parent_id_notifications_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| notificationId | 
 **parent_id** | **int**| rmaStatusId | 
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

# **get_procurement_rma_statuses_by_parent_id_notifications**
> List[RmaStatusNotification] get_procurement_rma_statuses_by_parent_id_notifications(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of RmaStatusNotification

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.rma_status_notification import RmaStatusNotification
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
    api_instance = connectwise_psa.RmaStatusNotificationsApi(api_client)
    parent_id = 56 # int | rmaStatusId
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
        # Get List of RmaStatusNotification
        api_response = api_instance.get_procurement_rma_statuses_by_parent_id_notifications(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of RmaStatusNotificationsApi->get_procurement_rma_statuses_by_parent_id_notifications:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RmaStatusNotificationsApi->get_procurement_rma_statuses_by_parent_id_notifications: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| rmaStatusId | 
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

[**List[RmaStatusNotification]**](RmaStatusNotification.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of RmaStatusNotification |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_procurement_rma_statuses_by_parent_id_notifications_by_id**
> RmaStatusNotification get_procurement_rma_statuses_by_parent_id_notifications_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get RmaStatusNotification

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.rma_status_notification import RmaStatusNotification
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
    api_instance = connectwise_psa.RmaStatusNotificationsApi(api_client)
    id = 56 # int | notificationId
    parent_id = 56 # int | rmaStatusId
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
        # Get RmaStatusNotification
        api_response = api_instance.get_procurement_rma_statuses_by_parent_id_notifications_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of RmaStatusNotificationsApi->get_procurement_rma_statuses_by_parent_id_notifications_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RmaStatusNotificationsApi->get_procurement_rma_statuses_by_parent_id_notifications_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| notificationId | 
 **parent_id** | **int**| rmaStatusId | 
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

[**RmaStatusNotification**](RmaStatusNotification.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | RmaStatusNotification |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_procurement_rma_statuses_by_parent_id_notifications_count**
> Count get_procurement_rma_statuses_by_parent_id_notifications_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Count of RmaStatusNotification

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
    api_instance = connectwise_psa.RmaStatusNotificationsApi(api_client)
    parent_id = 56 # int | rmaStatusId
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
        # Get Count of RmaStatusNotification
        api_response = api_instance.get_procurement_rma_statuses_by_parent_id_notifications_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of RmaStatusNotificationsApi->get_procurement_rma_statuses_by_parent_id_notifications_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RmaStatusNotificationsApi->get_procurement_rma_statuses_by_parent_id_notifications_count: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| rmaStatusId | 
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

# **patch_procurement_rma_statuses_by_parent_id_notifications_by_id**
> RmaStatusNotification patch_procurement_rma_statuses_by_parent_id_notifications_by_id(id, parent_id, client_id, patch_operation)

Patch RmaStatusNotification

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.patch_operation import PatchOperation
from connectwise_psa.models.rma_status_notification import RmaStatusNotification
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
    api_instance = connectwise_psa.RmaStatusNotificationsApi(api_client)
    id = 56 # int | notificationId
    parent_id = 56 # int | rmaStatusId
    client_id = 'client_id_example' # str | 
    patch_operation = [connectwise_psa.PatchOperation()] # List[PatchOperation] | List of PatchOperation

    try:
        # Patch RmaStatusNotification
        api_response = api_instance.patch_procurement_rma_statuses_by_parent_id_notifications_by_id(id, parent_id, client_id, patch_operation)
        print("The response of RmaStatusNotificationsApi->patch_procurement_rma_statuses_by_parent_id_notifications_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RmaStatusNotificationsApi->patch_procurement_rma_statuses_by_parent_id_notifications_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| notificationId | 
 **parent_id** | **int**| rmaStatusId | 
 **client_id** | **str**|  | 
 **patch_operation** | [**List[PatchOperation]**](PatchOperation.md)| List of PatchOperation | 

### Return type

[**RmaStatusNotification**](RmaStatusNotification.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | RmaStatusNotification |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_procurement_rma_statuses_by_parent_id_notifications**
> RmaStatusNotification post_procurement_rma_statuses_by_parent_id_notifications(parent_id, client_id, rma_status_notification)

Post RmaStatusNotification

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.rma_status_notification import RmaStatusNotification
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
    api_instance = connectwise_psa.RmaStatusNotificationsApi(api_client)
    parent_id = 56 # int | rmaStatusId
    client_id = 'client_id_example' # str | 
    rma_status_notification = connectwise_psa.RmaStatusNotification() # RmaStatusNotification | rmaStatusNotification

    try:
        # Post RmaStatusNotification
        api_response = api_instance.post_procurement_rma_statuses_by_parent_id_notifications(parent_id, client_id, rma_status_notification)
        print("The response of RmaStatusNotificationsApi->post_procurement_rma_statuses_by_parent_id_notifications:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RmaStatusNotificationsApi->post_procurement_rma_statuses_by_parent_id_notifications: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| rmaStatusId | 
 **client_id** | **str**|  | 
 **rma_status_notification** | [**RmaStatusNotification**](RmaStatusNotification.md)| rmaStatusNotification | 

### Return type

[**RmaStatusNotification**](RmaStatusNotification.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | RmaStatusNotification |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_procurement_rma_statuses_by_parent_id_notifications_by_id**
> RmaStatusNotification put_procurement_rma_statuses_by_parent_id_notifications_by_id(id, parent_id, client_id, rma_status_notification)

Put RmaStatusNotification

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.rma_status_notification import RmaStatusNotification
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
    api_instance = connectwise_psa.RmaStatusNotificationsApi(api_client)
    id = 56 # int | notificationId
    parent_id = 56 # int | rmaStatusId
    client_id = 'client_id_example' # str | 
    rma_status_notification = connectwise_psa.RmaStatusNotification() # RmaStatusNotification | rmaStatusNotification

    try:
        # Put RmaStatusNotification
        api_response = api_instance.put_procurement_rma_statuses_by_parent_id_notifications_by_id(id, parent_id, client_id, rma_status_notification)
        print("The response of RmaStatusNotificationsApi->put_procurement_rma_statuses_by_parent_id_notifications_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RmaStatusNotificationsApi->put_procurement_rma_statuses_by_parent_id_notifications_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| notificationId | 
 **parent_id** | **int**| rmaStatusId | 
 **client_id** | **str**|  | 
 **rma_status_notification** | [**RmaStatusNotification**](RmaStatusNotification.md)| rmaStatusNotification | 

### Return type

[**RmaStatusNotification**](RmaStatusNotification.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | RmaStatusNotification |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

