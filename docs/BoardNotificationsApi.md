# connectwise_psa.BoardNotificationsApi

All URIs are relative to *https://api-aus.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_service_boards_by_parent_id_notifications_by_id**](BoardNotificationsApi.md#delete_service_boards_by_parent_id_notifications_by_id) | **DELETE** /service/boards/{parentId}/notifications/{id} | Delete BoardNotification
[**get_service_boards_by_parent_id_notifications**](BoardNotificationsApi.md#get_service_boards_by_parent_id_notifications) | **GET** /service/boards/{parentId}/notifications | Get List of BoardNotification
[**get_service_boards_by_parent_id_notifications_by_id**](BoardNotificationsApi.md#get_service_boards_by_parent_id_notifications_by_id) | **GET** /service/boards/{parentId}/notifications/{id} | Get BoardNotification
[**get_service_boards_by_parent_id_notifications_count**](BoardNotificationsApi.md#get_service_boards_by_parent_id_notifications_count) | **GET** /service/boards/{parentId}/notifications/count | Get Count of BoardNotification
[**patch_service_boards_by_parent_id_notifications_by_id**](BoardNotificationsApi.md#patch_service_boards_by_parent_id_notifications_by_id) | **PATCH** /service/boards/{parentId}/notifications/{id} | Patch BoardNotification
[**post_service_boards_by_parent_id_notifications**](BoardNotificationsApi.md#post_service_boards_by_parent_id_notifications) | **POST** /service/boards/{parentId}/notifications | Post BoardNotification
[**put_service_boards_by_parent_id_notifications_by_id**](BoardNotificationsApi.md#put_service_boards_by_parent_id_notifications_by_id) | **PUT** /service/boards/{parentId}/notifications/{id} | Put BoardNotification


# **delete_service_boards_by_parent_id_notifications_by_id**
> delete_service_boards_by_parent_id_notifications_by_id(id, parent_id, client_id)

Delete BoardNotification

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
    api_instance = connectwise_psa.BoardNotificationsApi(api_client)
    id = 56 # int | notificationId
    parent_id = 56 # int | boardId
    client_id = 'client_id_example' # str | 

    try:
        # Delete BoardNotification
        api_instance.delete_service_boards_by_parent_id_notifications_by_id(id, parent_id, client_id)
    except Exception as e:
        print("Exception when calling BoardNotificationsApi->delete_service_boards_by_parent_id_notifications_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| notificationId | 
 **parent_id** | **int**| boardId | 
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

# **get_service_boards_by_parent_id_notifications**
> List[BoardNotification] get_service_boards_by_parent_id_notifications(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of BoardNotification

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.board_notification import BoardNotification
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
    api_instance = connectwise_psa.BoardNotificationsApi(api_client)
    parent_id = 56 # int | boardId
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
        # Get List of BoardNotification
        api_response = api_instance.get_service_boards_by_parent_id_notifications(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of BoardNotificationsApi->get_service_boards_by_parent_id_notifications:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BoardNotificationsApi->get_service_boards_by_parent_id_notifications: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| boardId | 
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

[**List[BoardNotification]**](BoardNotification.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of BoardNotification |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_service_boards_by_parent_id_notifications_by_id**
> BoardNotification get_service_boards_by_parent_id_notifications_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get BoardNotification

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.board_notification import BoardNotification
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
    api_instance = connectwise_psa.BoardNotificationsApi(api_client)
    id = 56 # int | notificationId
    parent_id = 56 # int | boardId
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
        # Get BoardNotification
        api_response = api_instance.get_service_boards_by_parent_id_notifications_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of BoardNotificationsApi->get_service_boards_by_parent_id_notifications_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BoardNotificationsApi->get_service_boards_by_parent_id_notifications_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| notificationId | 
 **parent_id** | **int**| boardId | 
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

[**BoardNotification**](BoardNotification.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | BoardNotification |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_service_boards_by_parent_id_notifications_count**
> Count get_service_boards_by_parent_id_notifications_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Count of BoardNotification

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
    api_instance = connectwise_psa.BoardNotificationsApi(api_client)
    parent_id = 56 # int | boardId
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
        # Get Count of BoardNotification
        api_response = api_instance.get_service_boards_by_parent_id_notifications_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of BoardNotificationsApi->get_service_boards_by_parent_id_notifications_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BoardNotificationsApi->get_service_boards_by_parent_id_notifications_count: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| boardId | 
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

# **patch_service_boards_by_parent_id_notifications_by_id**
> BoardNotification patch_service_boards_by_parent_id_notifications_by_id(id, parent_id, client_id, patch_operation)

Patch BoardNotification

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.board_notification import BoardNotification
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
    api_instance = connectwise_psa.BoardNotificationsApi(api_client)
    id = 56 # int | notificationId
    parent_id = 56 # int | boardId
    client_id = 'client_id_example' # str | 
    patch_operation = [connectwise_psa.PatchOperation()] # List[PatchOperation] | List of PatchOperation

    try:
        # Patch BoardNotification
        api_response = api_instance.patch_service_boards_by_parent_id_notifications_by_id(id, parent_id, client_id, patch_operation)
        print("The response of BoardNotificationsApi->patch_service_boards_by_parent_id_notifications_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BoardNotificationsApi->patch_service_boards_by_parent_id_notifications_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| notificationId | 
 **parent_id** | **int**| boardId | 
 **client_id** | **str**|  | 
 **patch_operation** | [**List[PatchOperation]**](PatchOperation.md)| List of PatchOperation | 

### Return type

[**BoardNotification**](BoardNotification.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | BoardNotification |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_service_boards_by_parent_id_notifications**
> BoardNotification post_service_boards_by_parent_id_notifications(parent_id, client_id, board_notification)

Post BoardNotification

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.board_notification import BoardNotification
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
    api_instance = connectwise_psa.BoardNotificationsApi(api_client)
    parent_id = 56 # int | boardId
    client_id = 'client_id_example' # str | 
    board_notification = connectwise_psa.BoardNotification() # BoardNotification | boardNotification

    try:
        # Post BoardNotification
        api_response = api_instance.post_service_boards_by_parent_id_notifications(parent_id, client_id, board_notification)
        print("The response of BoardNotificationsApi->post_service_boards_by_parent_id_notifications:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BoardNotificationsApi->post_service_boards_by_parent_id_notifications: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| boardId | 
 **client_id** | **str**|  | 
 **board_notification** | [**BoardNotification**](BoardNotification.md)| boardNotification | 

### Return type

[**BoardNotification**](BoardNotification.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | BoardNotification |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_service_boards_by_parent_id_notifications_by_id**
> BoardNotification put_service_boards_by_parent_id_notifications_by_id(id, parent_id, client_id, board_notification)

Put BoardNotification

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.board_notification import BoardNotification
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
    api_instance = connectwise_psa.BoardNotificationsApi(api_client)
    id = 56 # int | notificationId
    parent_id = 56 # int | boardId
    client_id = 'client_id_example' # str | 
    board_notification = connectwise_psa.BoardNotification() # BoardNotification | boardNotification

    try:
        # Put BoardNotification
        api_response = api_instance.put_service_boards_by_parent_id_notifications_by_id(id, parent_id, client_id, board_notification)
        print("The response of BoardNotificationsApi->put_service_boards_by_parent_id_notifications_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BoardNotificationsApi->put_service_boards_by_parent_id_notifications_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| notificationId | 
 **parent_id** | **int**| boardId | 
 **client_id** | **str**|  | 
 **board_notification** | [**BoardNotification**](BoardNotification.md)| boardNotification | 

### Return type

[**BoardNotification**](BoardNotification.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | BoardNotification |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

