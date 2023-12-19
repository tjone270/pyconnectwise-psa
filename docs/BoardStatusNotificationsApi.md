# connectwise_psa.BoardStatusNotificationsApi

All URIs are relative to *https://aus-api.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_service_boards_by_grandparent_id_statuses_by_parent_id_notifications_by_id**](BoardStatusNotificationsApi.md#delete_service_boards_by_grandparent_id_statuses_by_parent_id_notifications_by_id) | **DELETE** /service/boards/{grandparentId}/statuses/{parentId}/notifications/{id} | Delete BoardStatusNotification
[**get_service_boards_by_grandparent_id_statuses_by_parent_id_notifications**](BoardStatusNotificationsApi.md#get_service_boards_by_grandparent_id_statuses_by_parent_id_notifications) | **GET** /service/boards/{grandparentId}/statuses/{parentId}/notifications | Get List of BoardStatusNotification
[**get_service_boards_by_grandparent_id_statuses_by_parent_id_notifications_by_id**](BoardStatusNotificationsApi.md#get_service_boards_by_grandparent_id_statuses_by_parent_id_notifications_by_id) | **GET** /service/boards/{grandparentId}/statuses/{parentId}/notifications/{id} | Get BoardStatusNotification
[**get_service_boards_by_grandparent_id_statuses_by_parent_id_notifications_count**](BoardStatusNotificationsApi.md#get_service_boards_by_grandparent_id_statuses_by_parent_id_notifications_count) | **GET** /service/boards/{grandparentId}/statuses/{parentId}/notifications/count | Get Count of BoardStatusNotification
[**patch_service_boards_by_grandparent_id_statuses_by_parent_id_notifications_by_id**](BoardStatusNotificationsApi.md#patch_service_boards_by_grandparent_id_statuses_by_parent_id_notifications_by_id) | **PATCH** /service/boards/{grandparentId}/statuses/{parentId}/notifications/{id} | Patch BoardStatusNotification
[**post_service_boards_by_grandparent_id_statuses_by_parent_id_notifications**](BoardStatusNotificationsApi.md#post_service_boards_by_grandparent_id_statuses_by_parent_id_notifications) | **POST** /service/boards/{grandparentId}/statuses/{parentId}/notifications | Post BoardStatusNotification
[**put_service_boards_by_grandparent_id_statuses_by_parent_id_notifications_by_id**](BoardStatusNotificationsApi.md#put_service_boards_by_grandparent_id_statuses_by_parent_id_notifications_by_id) | **PUT** /service/boards/{grandparentId}/statuses/{parentId}/notifications/{id} | Put BoardStatusNotification


# **delete_service_boards_by_grandparent_id_statuses_by_parent_id_notifications_by_id**
> delete_service_boards_by_grandparent_id_statuses_by_parent_id_notifications_by_id(id, parent_id, grandparent_id, client_id)

Delete BoardStatusNotification

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
    api_instance = connectwise_psa.BoardStatusNotificationsApi(api_client)
    id = 56 # int | notificationId
    parent_id = 56 # int | statusId
    grandparent_id = 56 # int | boardId
    client_id = 'client_id_example' # str | 

    try:
        # Delete BoardStatusNotification
        api_instance.delete_service_boards_by_grandparent_id_statuses_by_parent_id_notifications_by_id(id, parent_id, grandparent_id, client_id)
    except Exception as e:
        print("Exception when calling BoardStatusNotificationsApi->delete_service_boards_by_grandparent_id_statuses_by_parent_id_notifications_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| notificationId | 
 **parent_id** | **int**| statusId | 
 **grandparent_id** | **int**| boardId | 
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

# **get_service_boards_by_grandparent_id_statuses_by_parent_id_notifications**
> List[BoardStatusNotification] get_service_boards_by_grandparent_id_statuses_by_parent_id_notifications(parent_id, grandparent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of BoardStatusNotification

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.board_status_notification import BoardStatusNotification
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
    api_instance = connectwise_psa.BoardStatusNotificationsApi(api_client)
    parent_id = 56 # int | statusId
    grandparent_id = 56 # int | boardId
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
        # Get List of BoardStatusNotification
        api_response = api_instance.get_service_boards_by_grandparent_id_statuses_by_parent_id_notifications(parent_id, grandparent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of BoardStatusNotificationsApi->get_service_boards_by_grandparent_id_statuses_by_parent_id_notifications:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BoardStatusNotificationsApi->get_service_boards_by_grandparent_id_statuses_by_parent_id_notifications: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| statusId | 
 **grandparent_id** | **int**| boardId | 
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

[**List[BoardStatusNotification]**](BoardStatusNotification.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of BoardStatusNotification |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_service_boards_by_grandparent_id_statuses_by_parent_id_notifications_by_id**
> BoardStatusNotification get_service_boards_by_grandparent_id_statuses_by_parent_id_notifications_by_id(id, parent_id, grandparent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get BoardStatusNotification

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.board_status_notification import BoardStatusNotification
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
    api_instance = connectwise_psa.BoardStatusNotificationsApi(api_client)
    id = 56 # int | notificationId
    parent_id = 56 # int | statusId
    grandparent_id = 56 # int | boardId
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
        # Get BoardStatusNotification
        api_response = api_instance.get_service_boards_by_grandparent_id_statuses_by_parent_id_notifications_by_id(id, parent_id, grandparent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of BoardStatusNotificationsApi->get_service_boards_by_grandparent_id_statuses_by_parent_id_notifications_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BoardStatusNotificationsApi->get_service_boards_by_grandparent_id_statuses_by_parent_id_notifications_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| notificationId | 
 **parent_id** | **int**| statusId | 
 **grandparent_id** | **int**| boardId | 
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

[**BoardStatusNotification**](BoardStatusNotification.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | BoardStatusNotification |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_service_boards_by_grandparent_id_statuses_by_parent_id_notifications_count**
> Count get_service_boards_by_grandparent_id_statuses_by_parent_id_notifications_count(parent_id, grandparent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Count of BoardStatusNotification

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
    api_instance = connectwise_psa.BoardStatusNotificationsApi(api_client)
    parent_id = 56 # int | statusId
    grandparent_id = 56 # int | boardId
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
        # Get Count of BoardStatusNotification
        api_response = api_instance.get_service_boards_by_grandparent_id_statuses_by_parent_id_notifications_count(parent_id, grandparent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of BoardStatusNotificationsApi->get_service_boards_by_grandparent_id_statuses_by_parent_id_notifications_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BoardStatusNotificationsApi->get_service_boards_by_grandparent_id_statuses_by_parent_id_notifications_count: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| statusId | 
 **grandparent_id** | **int**| boardId | 
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

# **patch_service_boards_by_grandparent_id_statuses_by_parent_id_notifications_by_id**
> BoardStatusNotification patch_service_boards_by_grandparent_id_statuses_by_parent_id_notifications_by_id(id, parent_id, grandparent_id, client_id, patch_operation)

Patch BoardStatusNotification

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.board_status_notification import BoardStatusNotification
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
    api_instance = connectwise_psa.BoardStatusNotificationsApi(api_client)
    id = 56 # int | notificationId
    parent_id = 56 # int | statusId
    grandparent_id = 56 # int | boardId
    client_id = 'client_id_example' # str | 
    patch_operation = [connectwise_psa.PatchOperation()] # List[PatchOperation] | List of PatchOperation

    try:
        # Patch BoardStatusNotification
        api_response = api_instance.patch_service_boards_by_grandparent_id_statuses_by_parent_id_notifications_by_id(id, parent_id, grandparent_id, client_id, patch_operation)
        print("The response of BoardStatusNotificationsApi->patch_service_boards_by_grandparent_id_statuses_by_parent_id_notifications_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BoardStatusNotificationsApi->patch_service_boards_by_grandparent_id_statuses_by_parent_id_notifications_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| notificationId | 
 **parent_id** | **int**| statusId | 
 **grandparent_id** | **int**| boardId | 
 **client_id** | **str**|  | 
 **patch_operation** | [**List[PatchOperation]**](PatchOperation.md)| List of PatchOperation | 

### Return type

[**BoardStatusNotification**](BoardStatusNotification.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | BoardStatusNotification |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_service_boards_by_grandparent_id_statuses_by_parent_id_notifications**
> BoardStatusNotification post_service_boards_by_grandparent_id_statuses_by_parent_id_notifications(parent_id, grandparent_id, client_id, board_status_notification)

Post BoardStatusNotification

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.board_status_notification import BoardStatusNotification
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
    api_instance = connectwise_psa.BoardStatusNotificationsApi(api_client)
    parent_id = 56 # int | statusId
    grandparent_id = 56 # int | boardId
    client_id = 'client_id_example' # str | 
    board_status_notification = connectwise_psa.BoardStatusNotification() # BoardStatusNotification | boardStatusNotification

    try:
        # Post BoardStatusNotification
        api_response = api_instance.post_service_boards_by_grandparent_id_statuses_by_parent_id_notifications(parent_id, grandparent_id, client_id, board_status_notification)
        print("The response of BoardStatusNotificationsApi->post_service_boards_by_grandparent_id_statuses_by_parent_id_notifications:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BoardStatusNotificationsApi->post_service_boards_by_grandparent_id_statuses_by_parent_id_notifications: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| statusId | 
 **grandparent_id** | **int**| boardId | 
 **client_id** | **str**|  | 
 **board_status_notification** | [**BoardStatusNotification**](BoardStatusNotification.md)| boardStatusNotification | 

### Return type

[**BoardStatusNotification**](BoardStatusNotification.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | BoardStatusNotification |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_service_boards_by_grandparent_id_statuses_by_parent_id_notifications_by_id**
> BoardStatusNotification put_service_boards_by_grandparent_id_statuses_by_parent_id_notifications_by_id(id, parent_id, grandparent_id, client_id, board_status_notification)

Put BoardStatusNotification

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.board_status_notification import BoardStatusNotification
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
    api_instance = connectwise_psa.BoardStatusNotificationsApi(api_client)
    id = 56 # int | notificationId
    parent_id = 56 # int | statusId
    grandparent_id = 56 # int | boardId
    client_id = 'client_id_example' # str | 
    board_status_notification = connectwise_psa.BoardStatusNotification() # BoardStatusNotification | boardStatusNotification

    try:
        # Put BoardStatusNotification
        api_response = api_instance.put_service_boards_by_grandparent_id_statuses_by_parent_id_notifications_by_id(id, parent_id, grandparent_id, client_id, board_status_notification)
        print("The response of BoardStatusNotificationsApi->put_service_boards_by_grandparent_id_statuses_by_parent_id_notifications_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BoardStatusNotificationsApi->put_service_boards_by_grandparent_id_statuses_by_parent_id_notifications_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| notificationId | 
 **parent_id** | **int**| statusId | 
 **grandparent_id** | **int**| boardId | 
 **client_id** | **str**|  | 
 **board_status_notification** | [**BoardStatusNotification**](BoardStatusNotification.md)| boardStatusNotification | 

### Return type

[**BoardStatusNotification**](BoardStatusNotification.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | BoardStatusNotification |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

