# connectwise_psa.OrderStatusNotificationsApi

All URIs are relative to *https://api-aus.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_sales_orders_statuses_by_parent_id_notifications_by_id**](OrderStatusNotificationsApi.md#delete_sales_orders_statuses_by_parent_id_notifications_by_id) | **DELETE** /sales/orders/statuses/{parentId}/notifications/{id} | Delete OrderStatusNotification
[**get_sales_orders_statuses_by_parent_id_notifications**](OrderStatusNotificationsApi.md#get_sales_orders_statuses_by_parent_id_notifications) | **GET** /sales/orders/statuses/{parentId}/notifications | Get List of OrderStatusNotification
[**get_sales_orders_statuses_by_parent_id_notifications_by_id**](OrderStatusNotificationsApi.md#get_sales_orders_statuses_by_parent_id_notifications_by_id) | **GET** /sales/orders/statuses/{parentId}/notifications/{id} | Get OrderStatusNotification
[**get_sales_orders_statuses_by_parent_id_notifications_count**](OrderStatusNotificationsApi.md#get_sales_orders_statuses_by_parent_id_notifications_count) | **GET** /sales/orders/statuses/{parentId}/notifications/count | Get Count of OrderStatusNotification
[**patch_sales_orders_statuses_by_parent_id_notifications_by_id**](OrderStatusNotificationsApi.md#patch_sales_orders_statuses_by_parent_id_notifications_by_id) | **PATCH** /sales/orders/statuses/{parentId}/notifications/{id} | Patch OrderStatusNotification
[**post_sales_orders_statuses_by_parent_id_notifications**](OrderStatusNotificationsApi.md#post_sales_orders_statuses_by_parent_id_notifications) | **POST** /sales/orders/statuses/{parentId}/notifications | Post OrderStatusNotification
[**put_sales_orders_statuses_by_parent_id_notifications_by_id**](OrderStatusNotificationsApi.md#put_sales_orders_statuses_by_parent_id_notifications_by_id) | **PUT** /sales/orders/statuses/{parentId}/notifications/{id} | Put OrderStatusNotification


# **delete_sales_orders_statuses_by_parent_id_notifications_by_id**
> delete_sales_orders_statuses_by_parent_id_notifications_by_id(id, parent_id, client_id)

Delete OrderStatusNotification

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
    api_instance = connectwise_psa.OrderStatusNotificationsApi(api_client)
    id = 56 # int | notificationId
    parent_id = 56 # int | statusId
    client_id = 'client_id_example' # str | 

    try:
        # Delete OrderStatusNotification
        api_instance.delete_sales_orders_statuses_by_parent_id_notifications_by_id(id, parent_id, client_id)
    except Exception as e:
        print("Exception when calling OrderStatusNotificationsApi->delete_sales_orders_statuses_by_parent_id_notifications_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| notificationId | 
 **parent_id** | **int**| statusId | 
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

# **get_sales_orders_statuses_by_parent_id_notifications**
> List[OrderStatusNotification] get_sales_orders_statuses_by_parent_id_notifications(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of OrderStatusNotification

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.order_status_notification import OrderStatusNotification
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
    api_instance = connectwise_psa.OrderStatusNotificationsApi(api_client)
    parent_id = 56 # int | statusId
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
        # Get List of OrderStatusNotification
        api_response = api_instance.get_sales_orders_statuses_by_parent_id_notifications(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of OrderStatusNotificationsApi->get_sales_orders_statuses_by_parent_id_notifications:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrderStatusNotificationsApi->get_sales_orders_statuses_by_parent_id_notifications: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| statusId | 
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

[**List[OrderStatusNotification]**](OrderStatusNotification.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of OrderStatusNotification |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sales_orders_statuses_by_parent_id_notifications_by_id**
> OrderStatusNotification get_sales_orders_statuses_by_parent_id_notifications_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get OrderStatusNotification

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.order_status_notification import OrderStatusNotification
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
    api_instance = connectwise_psa.OrderStatusNotificationsApi(api_client)
    id = 56 # int | notificationId
    parent_id = 56 # int | statusId
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
        # Get OrderStatusNotification
        api_response = api_instance.get_sales_orders_statuses_by_parent_id_notifications_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of OrderStatusNotificationsApi->get_sales_orders_statuses_by_parent_id_notifications_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrderStatusNotificationsApi->get_sales_orders_statuses_by_parent_id_notifications_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| notificationId | 
 **parent_id** | **int**| statusId | 
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

[**OrderStatusNotification**](OrderStatusNotification.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OrderStatusNotification |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sales_orders_statuses_by_parent_id_notifications_count**
> Count get_sales_orders_statuses_by_parent_id_notifications_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Count of OrderStatusNotification

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
    api_instance = connectwise_psa.OrderStatusNotificationsApi(api_client)
    parent_id = 56 # int | statusId
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
        # Get Count of OrderStatusNotification
        api_response = api_instance.get_sales_orders_statuses_by_parent_id_notifications_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of OrderStatusNotificationsApi->get_sales_orders_statuses_by_parent_id_notifications_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrderStatusNotificationsApi->get_sales_orders_statuses_by_parent_id_notifications_count: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| statusId | 
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

# **patch_sales_orders_statuses_by_parent_id_notifications_by_id**
> OrderStatusNotification patch_sales_orders_statuses_by_parent_id_notifications_by_id(id, parent_id, client_id, patch_operation)

Patch OrderStatusNotification

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.order_status_notification import OrderStatusNotification
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
    api_instance = connectwise_psa.OrderStatusNotificationsApi(api_client)
    id = 56 # int | notificationId
    parent_id = 56 # int | statusId
    client_id = 'client_id_example' # str | 
    patch_operation = [connectwise_psa.PatchOperation()] # List[PatchOperation] | List of PatchOperation

    try:
        # Patch OrderStatusNotification
        api_response = api_instance.patch_sales_orders_statuses_by_parent_id_notifications_by_id(id, parent_id, client_id, patch_operation)
        print("The response of OrderStatusNotificationsApi->patch_sales_orders_statuses_by_parent_id_notifications_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrderStatusNotificationsApi->patch_sales_orders_statuses_by_parent_id_notifications_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| notificationId | 
 **parent_id** | **int**| statusId | 
 **client_id** | **str**|  | 
 **patch_operation** | [**List[PatchOperation]**](PatchOperation.md)| List of PatchOperation | 

### Return type

[**OrderStatusNotification**](OrderStatusNotification.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OrderStatusNotification |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_sales_orders_statuses_by_parent_id_notifications**
> OrderStatusNotification post_sales_orders_statuses_by_parent_id_notifications(parent_id, client_id, order_status_notification)

Post OrderStatusNotification

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.order_status_notification import OrderStatusNotification
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
    api_instance = connectwise_psa.OrderStatusNotificationsApi(api_client)
    parent_id = 56 # int | statusId
    client_id = 'client_id_example' # str | 
    order_status_notification = connectwise_psa.OrderStatusNotification() # OrderStatusNotification | orderStatusNotification

    try:
        # Post OrderStatusNotification
        api_response = api_instance.post_sales_orders_statuses_by_parent_id_notifications(parent_id, client_id, order_status_notification)
        print("The response of OrderStatusNotificationsApi->post_sales_orders_statuses_by_parent_id_notifications:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrderStatusNotificationsApi->post_sales_orders_statuses_by_parent_id_notifications: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| statusId | 
 **client_id** | **str**|  | 
 **order_status_notification** | [**OrderStatusNotification**](OrderStatusNotification.md)| orderStatusNotification | 

### Return type

[**OrderStatusNotification**](OrderStatusNotification.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | OrderStatusNotification |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_sales_orders_statuses_by_parent_id_notifications_by_id**
> OrderStatusNotification put_sales_orders_statuses_by_parent_id_notifications_by_id(id, parent_id, client_id, order_status_notification)

Put OrderStatusNotification

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.order_status_notification import OrderStatusNotification
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
    api_instance = connectwise_psa.OrderStatusNotificationsApi(api_client)
    id = 56 # int | notificationId
    parent_id = 56 # int | statusId
    client_id = 'client_id_example' # str | 
    order_status_notification = connectwise_psa.OrderStatusNotification() # OrderStatusNotification | orderStatusNotification

    try:
        # Put OrderStatusNotification
        api_response = api_instance.put_sales_orders_statuses_by_parent_id_notifications_by_id(id, parent_id, client_id, order_status_notification)
        print("The response of OrderStatusNotificationsApi->put_sales_orders_statuses_by_parent_id_notifications_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrderStatusNotificationsApi->put_sales_orders_statuses_by_parent_id_notifications_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| notificationId | 
 **parent_id** | **int**| statusId | 
 **client_id** | **str**|  | 
 **order_status_notification** | [**OrderStatusNotification**](OrderStatusNotification.md)| orderStatusNotification | 

### Return type

[**OrderStatusNotification**](OrderStatusNotification.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OrderStatusNotification |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

