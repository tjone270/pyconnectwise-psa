# connectwise_psa.PurchaseOrderStatusNotificationsApi

All URIs are relative to *https://aus-api.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_procurement_purchaseorderstatuses_by_parent_id_notifications_by_id**](PurchaseOrderStatusNotificationsApi.md#delete_procurement_purchaseorderstatuses_by_parent_id_notifications_by_id) | **DELETE** /procurement/purchaseorderstatuses/{parentId}/notifications/{id} | Delete PurchaseOrderStatusNotification
[**get_procurement_purchaseorderstatuses_by_parent_id_notifications**](PurchaseOrderStatusNotificationsApi.md#get_procurement_purchaseorderstatuses_by_parent_id_notifications) | **GET** /procurement/purchaseorderstatuses/{parentId}/notifications | Get List of PurchaseOrderStatusNotification
[**get_procurement_purchaseorderstatuses_by_parent_id_notifications_by_id**](PurchaseOrderStatusNotificationsApi.md#get_procurement_purchaseorderstatuses_by_parent_id_notifications_by_id) | **GET** /procurement/purchaseorderstatuses/{parentId}/notifications/{id} | Get PurchaseOrderStatusNotification
[**get_procurement_purchaseorderstatuses_by_parent_id_notifications_count**](PurchaseOrderStatusNotificationsApi.md#get_procurement_purchaseorderstatuses_by_parent_id_notifications_count) | **GET** /procurement/purchaseorderstatuses/{parentId}/notifications/count | Get Count of PurchaseOrderStatusNotification
[**patch_procurement_purchaseorderstatuses_by_parent_id_notifications_by_id**](PurchaseOrderStatusNotificationsApi.md#patch_procurement_purchaseorderstatuses_by_parent_id_notifications_by_id) | **PATCH** /procurement/purchaseorderstatuses/{parentId}/notifications/{id} | Patch PurchaseOrderStatusNotification
[**post_procurement_purchaseorderstatuses_by_parent_id_notifications**](PurchaseOrderStatusNotificationsApi.md#post_procurement_purchaseorderstatuses_by_parent_id_notifications) | **POST** /procurement/purchaseorderstatuses/{parentId}/notifications | Post PurchaseOrderStatusNotification
[**put_procurement_purchaseorderstatuses_by_parent_id_notifications_by_id**](PurchaseOrderStatusNotificationsApi.md#put_procurement_purchaseorderstatuses_by_parent_id_notifications_by_id) | **PUT** /procurement/purchaseorderstatuses/{parentId}/notifications/{id} | Put PurchaseOrderStatusNotification


# **delete_procurement_purchaseorderstatuses_by_parent_id_notifications_by_id**
> delete_procurement_purchaseorderstatuses_by_parent_id_notifications_by_id(id, parent_id, client_id)

Delete PurchaseOrderStatusNotification

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
    api_instance = connectwise_psa.PurchaseOrderStatusNotificationsApi(api_client)
    id = 56 # int | notificationId
    parent_id = 56 # int | purchaseorderstatusId
    client_id = 'client_id_example' # str | 

    try:
        # Delete PurchaseOrderStatusNotification
        api_instance.delete_procurement_purchaseorderstatuses_by_parent_id_notifications_by_id(id, parent_id, client_id)
    except Exception as e:
        print("Exception when calling PurchaseOrderStatusNotificationsApi->delete_procurement_purchaseorderstatuses_by_parent_id_notifications_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| notificationId | 
 **parent_id** | **int**| purchaseorderstatusId | 
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

# **get_procurement_purchaseorderstatuses_by_parent_id_notifications**
> List[PurchaseOrderStatusNotification] get_procurement_purchaseorderstatuses_by_parent_id_notifications(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of PurchaseOrderStatusNotification

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.purchase_order_status_notification import PurchaseOrderStatusNotification
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
    api_instance = connectwise_psa.PurchaseOrderStatusNotificationsApi(api_client)
    parent_id = 56 # int | purchaseorderstatusId
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
        # Get List of PurchaseOrderStatusNotification
        api_response = api_instance.get_procurement_purchaseorderstatuses_by_parent_id_notifications(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of PurchaseOrderStatusNotificationsApi->get_procurement_purchaseorderstatuses_by_parent_id_notifications:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PurchaseOrderStatusNotificationsApi->get_procurement_purchaseorderstatuses_by_parent_id_notifications: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| purchaseorderstatusId | 
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

[**List[PurchaseOrderStatusNotification]**](PurchaseOrderStatusNotification.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of PurchaseOrderStatusNotification |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_procurement_purchaseorderstatuses_by_parent_id_notifications_by_id**
> PurchaseOrderStatusNotification get_procurement_purchaseorderstatuses_by_parent_id_notifications_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get PurchaseOrderStatusNotification

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.purchase_order_status_notification import PurchaseOrderStatusNotification
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
    api_instance = connectwise_psa.PurchaseOrderStatusNotificationsApi(api_client)
    id = 56 # int | notificationId
    parent_id = 56 # int | purchaseorderstatusId
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
        # Get PurchaseOrderStatusNotification
        api_response = api_instance.get_procurement_purchaseorderstatuses_by_parent_id_notifications_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of PurchaseOrderStatusNotificationsApi->get_procurement_purchaseorderstatuses_by_parent_id_notifications_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PurchaseOrderStatusNotificationsApi->get_procurement_purchaseorderstatuses_by_parent_id_notifications_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| notificationId | 
 **parent_id** | **int**| purchaseorderstatusId | 
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

[**PurchaseOrderStatusNotification**](PurchaseOrderStatusNotification.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | PurchaseOrderStatusNotification |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_procurement_purchaseorderstatuses_by_parent_id_notifications_count**
> Count get_procurement_purchaseorderstatuses_by_parent_id_notifications_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Count of PurchaseOrderStatusNotification

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
    api_instance = connectwise_psa.PurchaseOrderStatusNotificationsApi(api_client)
    parent_id = 56 # int | purchaseorderstatusId
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
        # Get Count of PurchaseOrderStatusNotification
        api_response = api_instance.get_procurement_purchaseorderstatuses_by_parent_id_notifications_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of PurchaseOrderStatusNotificationsApi->get_procurement_purchaseorderstatuses_by_parent_id_notifications_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PurchaseOrderStatusNotificationsApi->get_procurement_purchaseorderstatuses_by_parent_id_notifications_count: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| purchaseorderstatusId | 
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

# **patch_procurement_purchaseorderstatuses_by_parent_id_notifications_by_id**
> PurchaseOrderStatusNotification patch_procurement_purchaseorderstatuses_by_parent_id_notifications_by_id(id, parent_id, client_id, patch_operation)

Patch PurchaseOrderStatusNotification

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.patch_operation import PatchOperation
from connectwise_psa.models.purchase_order_status_notification import PurchaseOrderStatusNotification
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
    api_instance = connectwise_psa.PurchaseOrderStatusNotificationsApi(api_client)
    id = 56 # int | notificationId
    parent_id = 56 # int | purchaseorderstatusId
    client_id = 'client_id_example' # str | 
    patch_operation = [connectwise_psa.PatchOperation()] # List[PatchOperation] | List of PatchOperation

    try:
        # Patch PurchaseOrderStatusNotification
        api_response = api_instance.patch_procurement_purchaseorderstatuses_by_parent_id_notifications_by_id(id, parent_id, client_id, patch_operation)
        print("The response of PurchaseOrderStatusNotificationsApi->patch_procurement_purchaseorderstatuses_by_parent_id_notifications_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PurchaseOrderStatusNotificationsApi->patch_procurement_purchaseorderstatuses_by_parent_id_notifications_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| notificationId | 
 **parent_id** | **int**| purchaseorderstatusId | 
 **client_id** | **str**|  | 
 **patch_operation** | [**List[PatchOperation]**](PatchOperation.md)| List of PatchOperation | 

### Return type

[**PurchaseOrderStatusNotification**](PurchaseOrderStatusNotification.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | PurchaseOrderStatusNotification |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_procurement_purchaseorderstatuses_by_parent_id_notifications**
> PurchaseOrderStatusNotification post_procurement_purchaseorderstatuses_by_parent_id_notifications(parent_id, client_id, purchase_order_status_notification)

Post PurchaseOrderStatusNotification

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.purchase_order_status_notification import PurchaseOrderStatusNotification
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
    api_instance = connectwise_psa.PurchaseOrderStatusNotificationsApi(api_client)
    parent_id = 56 # int | purchaseorderstatusId
    client_id = 'client_id_example' # str | 
    purchase_order_status_notification = connectwise_psa.PurchaseOrderStatusNotification() # PurchaseOrderStatusNotification | purchaseOrderStatusNotification

    try:
        # Post PurchaseOrderStatusNotification
        api_response = api_instance.post_procurement_purchaseorderstatuses_by_parent_id_notifications(parent_id, client_id, purchase_order_status_notification)
        print("The response of PurchaseOrderStatusNotificationsApi->post_procurement_purchaseorderstatuses_by_parent_id_notifications:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PurchaseOrderStatusNotificationsApi->post_procurement_purchaseorderstatuses_by_parent_id_notifications: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| purchaseorderstatusId | 
 **client_id** | **str**|  | 
 **purchase_order_status_notification** | [**PurchaseOrderStatusNotification**](PurchaseOrderStatusNotification.md)| purchaseOrderStatusNotification | 

### Return type

[**PurchaseOrderStatusNotification**](PurchaseOrderStatusNotification.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | PurchaseOrderStatusNotification |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_procurement_purchaseorderstatuses_by_parent_id_notifications_by_id**
> PurchaseOrderStatusNotification put_procurement_purchaseorderstatuses_by_parent_id_notifications_by_id(id, parent_id, client_id, purchase_order_status_notification)

Put PurchaseOrderStatusNotification

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.purchase_order_status_notification import PurchaseOrderStatusNotification
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
    api_instance = connectwise_psa.PurchaseOrderStatusNotificationsApi(api_client)
    id = 56 # int | notificationId
    parent_id = 56 # int | purchaseorderstatusId
    client_id = 'client_id_example' # str | 
    purchase_order_status_notification = connectwise_psa.PurchaseOrderStatusNotification() # PurchaseOrderStatusNotification | purchaseOrderStatusNotification

    try:
        # Put PurchaseOrderStatusNotification
        api_response = api_instance.put_procurement_purchaseorderstatuses_by_parent_id_notifications_by_id(id, parent_id, client_id, purchase_order_status_notification)
        print("The response of PurchaseOrderStatusNotificationsApi->put_procurement_purchaseorderstatuses_by_parent_id_notifications_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PurchaseOrderStatusNotificationsApi->put_procurement_purchaseorderstatuses_by_parent_id_notifications_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| notificationId | 
 **parent_id** | **int**| purchaseorderstatusId | 
 **client_id** | **str**|  | 
 **purchase_order_status_notification** | [**PurchaseOrderStatusNotification**](PurchaseOrderStatusNotification.md)| purchaseOrderStatusNotification | 

### Return type

[**PurchaseOrderStatusNotification**](PurchaseOrderStatusNotification.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | PurchaseOrderStatusNotification |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

