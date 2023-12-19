# connectwise_psa.PurchaseOrderLineItemsApi

All URIs are relative to *https://api-aus.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_procurement_purchaseorders_by_parent_id_lineitems**](PurchaseOrderLineItemsApi.md#delete_procurement_purchaseorders_by_parent_id_lineitems) | **DELETE** /procurement/purchaseorders/{parentId}/lineitems | Delete PurchaseOrderLineItem
[**delete_procurement_purchaseorders_by_parent_id_lineitems_bulk**](PurchaseOrderLineItemsApi.md#delete_procurement_purchaseorders_by_parent_id_lineitems_bulk) | **DELETE** /procurement/purchaseorders/{parentId}/lineitems/bulk | Delete BulkResult
[**get_procurement_purchaseorders_by_parent_id_lineitems**](PurchaseOrderLineItemsApi.md#get_procurement_purchaseorders_by_parent_id_lineitems) | **GET** /procurement/purchaseorders/{parentId}/lineitems | Get List of PurchaseOrderLineItem
[**get_procurement_purchaseorders_by_parent_id_lineitems_by_id**](PurchaseOrderLineItemsApi.md#get_procurement_purchaseorders_by_parent_id_lineitems_by_id) | **GET** /procurement/purchaseorders/{parentId}/lineitems/{id} | Get PurchaseOrderLineItem
[**get_procurement_purchaseorders_by_parent_id_lineitems_count**](PurchaseOrderLineItemsApi.md#get_procurement_purchaseorders_by_parent_id_lineitems_count) | **GET** /procurement/purchaseorders/{parentId}/lineitems/count | Get Count of PurchaseOrderLineItem
[**patch_procurement_purchaseorders_by_parent_id_lineitems_by_id**](PurchaseOrderLineItemsApi.md#patch_procurement_purchaseorders_by_parent_id_lineitems_by_id) | **PATCH** /procurement/purchaseorders/{parentId}/lineitems/{id} | Patch PurchaseOrderLineItem
[**post_procurement_purchaseorders_by_parent_id_lineitems**](PurchaseOrderLineItemsApi.md#post_procurement_purchaseorders_by_parent_id_lineitems) | **POST** /procurement/purchaseorders/{parentId}/lineitems | Post PurchaseOrderLineItem
[**post_procurement_purchaseorders_by_parent_id_lineitems_bulk**](PurchaseOrderLineItemsApi.md#post_procurement_purchaseorders_by_parent_id_lineitems_bulk) | **POST** /procurement/purchaseorders/{parentId}/lineitems/bulk | Post BulkResult
[**put_procurement_purchaseorders_by_parent_id_lineitems_bulk**](PurchaseOrderLineItemsApi.md#put_procurement_purchaseorders_by_parent_id_lineitems_bulk) | **PUT** /procurement/purchaseorders/{parentId}/lineitems/bulk | Put BulkResult
[**put_procurement_purchaseorders_by_parent_id_lineitems_by_id**](PurchaseOrderLineItemsApi.md#put_procurement_purchaseorders_by_parent_id_lineitems_by_id) | **PUT** /procurement/purchaseorders/{parentId}/lineitems/{id} | Put PurchaseOrderLineItem


# **delete_procurement_purchaseorders_by_parent_id_lineitems**
> delete_procurement_purchaseorders_by_parent_id_lineitems(parent_id, client_id, id)

Delete PurchaseOrderLineItem

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
    api_instance = connectwise_psa.PurchaseOrderLineItemsApi(api_client)
    parent_id = 56 # int | purchaseorderId
    client_id = 'client_id_example' # str | 
    id = 56 # int | lineitemId

    try:
        # Delete PurchaseOrderLineItem
        api_instance.delete_procurement_purchaseorders_by_parent_id_lineitems(parent_id, client_id, id)
    except Exception as e:
        print("Exception when calling PurchaseOrderLineItemsApi->delete_procurement_purchaseorders_by_parent_id_lineitems: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| purchaseorderId | 
 **client_id** | **str**|  | 
 **id** | **int**| lineitemId | 

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

# **delete_procurement_purchaseorders_by_parent_id_lineitems_bulk**
> BulkResult delete_procurement_purchaseorders_by_parent_id_lineitems_bulk(parent_id, client_id, id_collection)

Delete BulkResult

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.bulk_result import BulkResult
from connectwise_psa.models.id_collection import IdCollection
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
    api_instance = connectwise_psa.PurchaseOrderLineItemsApi(api_client)
    parent_id = 56 # int | purchaseorderId
    client_id = 'client_id_example' # str | 
    id_collection = connectwise_psa.IdCollection() # IdCollection | purchaseOrderLineItems

    try:
        # Delete BulkResult
        api_response = api_instance.delete_procurement_purchaseorders_by_parent_id_lineitems_bulk(parent_id, client_id, id_collection)
        print("The response of PurchaseOrderLineItemsApi->delete_procurement_purchaseorders_by_parent_id_lineitems_bulk:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PurchaseOrderLineItemsApi->delete_procurement_purchaseorders_by_parent_id_lineitems_bulk: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| purchaseorderId | 
 **client_id** | **str**|  | 
 **id_collection** | [**IdCollection**](IdCollection.md)| purchaseOrderLineItems | 

### Return type

[**BulkResult**](BulkResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**207** | BulkResult |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_procurement_purchaseorders_by_parent_id_lineitems**
> List[PurchaseOrderLineItem] get_procurement_purchaseorders_by_parent_id_lineitems(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of PurchaseOrderLineItem

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.purchase_order_line_item import PurchaseOrderLineItem
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
    api_instance = connectwise_psa.PurchaseOrderLineItemsApi(api_client)
    parent_id = 56 # int | purchaseorderId
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
        # Get List of PurchaseOrderLineItem
        api_response = api_instance.get_procurement_purchaseorders_by_parent_id_lineitems(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of PurchaseOrderLineItemsApi->get_procurement_purchaseorders_by_parent_id_lineitems:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PurchaseOrderLineItemsApi->get_procurement_purchaseorders_by_parent_id_lineitems: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| purchaseorderId | 
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

[**List[PurchaseOrderLineItem]**](PurchaseOrderLineItem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of PurchaseOrderLineItem |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_procurement_purchaseorders_by_parent_id_lineitems_by_id**
> PurchaseOrderLineItem get_procurement_purchaseorders_by_parent_id_lineitems_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get PurchaseOrderLineItem

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.purchase_order_line_item import PurchaseOrderLineItem
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
    api_instance = connectwise_psa.PurchaseOrderLineItemsApi(api_client)
    id = 56 # int | lineitemId
    parent_id = 56 # int | purchaseorderId
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
        # Get PurchaseOrderLineItem
        api_response = api_instance.get_procurement_purchaseorders_by_parent_id_lineitems_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of PurchaseOrderLineItemsApi->get_procurement_purchaseorders_by_parent_id_lineitems_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PurchaseOrderLineItemsApi->get_procurement_purchaseorders_by_parent_id_lineitems_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| lineitemId | 
 **parent_id** | **int**| purchaseorderId | 
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

[**PurchaseOrderLineItem**](PurchaseOrderLineItem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | PurchaseOrderLineItem |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_procurement_purchaseorders_by_parent_id_lineitems_count**
> Count get_procurement_purchaseorders_by_parent_id_lineitems_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Count of PurchaseOrderLineItem

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
    api_instance = connectwise_psa.PurchaseOrderLineItemsApi(api_client)
    parent_id = 56 # int | purchaseorderId
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
        # Get Count of PurchaseOrderLineItem
        api_response = api_instance.get_procurement_purchaseorders_by_parent_id_lineitems_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of PurchaseOrderLineItemsApi->get_procurement_purchaseorders_by_parent_id_lineitems_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PurchaseOrderLineItemsApi->get_procurement_purchaseorders_by_parent_id_lineitems_count: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| purchaseorderId | 
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

# **patch_procurement_purchaseorders_by_parent_id_lineitems_by_id**
> PurchaseOrderLineItem patch_procurement_purchaseorders_by_parent_id_lineitems_by_id(id, parent_id, client_id, patch_operation)

Patch PurchaseOrderLineItem

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.patch_operation import PatchOperation
from connectwise_psa.models.purchase_order_line_item import PurchaseOrderLineItem
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
    api_instance = connectwise_psa.PurchaseOrderLineItemsApi(api_client)
    id = 56 # int | lineitemId
    parent_id = 56 # int | purchaseorderId
    client_id = 'client_id_example' # str | 
    patch_operation = [connectwise_psa.PatchOperation()] # List[PatchOperation] | List of PatchOperation

    try:
        # Patch PurchaseOrderLineItem
        api_response = api_instance.patch_procurement_purchaseorders_by_parent_id_lineitems_by_id(id, parent_id, client_id, patch_operation)
        print("The response of PurchaseOrderLineItemsApi->patch_procurement_purchaseorders_by_parent_id_lineitems_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PurchaseOrderLineItemsApi->patch_procurement_purchaseorders_by_parent_id_lineitems_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| lineitemId | 
 **parent_id** | **int**| purchaseorderId | 
 **client_id** | **str**|  | 
 **patch_operation** | [**List[PatchOperation]**](PatchOperation.md)| List of PatchOperation | 

### Return type

[**PurchaseOrderLineItem**](PurchaseOrderLineItem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | PurchaseOrderLineItem |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_procurement_purchaseorders_by_parent_id_lineitems**
> PurchaseOrderLineItem post_procurement_purchaseorders_by_parent_id_lineitems(parent_id, client_id, purchase_order_line_item)

Post PurchaseOrderLineItem

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.purchase_order_line_item import PurchaseOrderLineItem
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
    api_instance = connectwise_psa.PurchaseOrderLineItemsApi(api_client)
    parent_id = 56 # int | purchaseorderId
    client_id = 'client_id_example' # str | 
    purchase_order_line_item = connectwise_psa.PurchaseOrderLineItem() # PurchaseOrderLineItem | purchaseOrderLineItem

    try:
        # Post PurchaseOrderLineItem
        api_response = api_instance.post_procurement_purchaseorders_by_parent_id_lineitems(parent_id, client_id, purchase_order_line_item)
        print("The response of PurchaseOrderLineItemsApi->post_procurement_purchaseorders_by_parent_id_lineitems:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PurchaseOrderLineItemsApi->post_procurement_purchaseorders_by_parent_id_lineitems: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| purchaseorderId | 
 **client_id** | **str**|  | 
 **purchase_order_line_item** | [**PurchaseOrderLineItem**](PurchaseOrderLineItem.md)| purchaseOrderLineItem | 

### Return type

[**PurchaseOrderLineItem**](PurchaseOrderLineItem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | PurchaseOrderLineItem |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_procurement_purchaseorders_by_parent_id_lineitems_bulk**
> BulkResult post_procurement_purchaseorders_by_parent_id_lineitems_bulk(parent_id, client_id, purchase_order_line_item)

Post BulkResult

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.bulk_result import BulkResult
from connectwise_psa.models.purchase_order_line_item import PurchaseOrderLineItem
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
    api_instance = connectwise_psa.PurchaseOrderLineItemsApi(api_client)
    parent_id = 56 # int | purchaseorderId
    client_id = 'client_id_example' # str | 
    purchase_order_line_item = [connectwise_psa.PurchaseOrderLineItem()] # List[PurchaseOrderLineItem] | List of PurchaseOrderLineItem

    try:
        # Post BulkResult
        api_response = api_instance.post_procurement_purchaseorders_by_parent_id_lineitems_bulk(parent_id, client_id, purchase_order_line_item)
        print("The response of PurchaseOrderLineItemsApi->post_procurement_purchaseorders_by_parent_id_lineitems_bulk:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PurchaseOrderLineItemsApi->post_procurement_purchaseorders_by_parent_id_lineitems_bulk: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| purchaseorderId | 
 **client_id** | **str**|  | 
 **purchase_order_line_item** | [**List[PurchaseOrderLineItem]**](PurchaseOrderLineItem.md)| List of PurchaseOrderLineItem | 

### Return type

[**BulkResult**](BulkResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**207** | BulkResult |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_procurement_purchaseorders_by_parent_id_lineitems_bulk**
> BulkResult put_procurement_purchaseorders_by_parent_id_lineitems_bulk(parent_id, client_id, purchase_order_line_item)

Put BulkResult

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.bulk_result import BulkResult
from connectwise_psa.models.purchase_order_line_item import PurchaseOrderLineItem
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
    api_instance = connectwise_psa.PurchaseOrderLineItemsApi(api_client)
    parent_id = 56 # int | purchaseorderId
    client_id = 'client_id_example' # str | 
    purchase_order_line_item = [connectwise_psa.PurchaseOrderLineItem()] # List[PurchaseOrderLineItem] | List of PurchaseOrderLineItem

    try:
        # Put BulkResult
        api_response = api_instance.put_procurement_purchaseorders_by_parent_id_lineitems_bulk(parent_id, client_id, purchase_order_line_item)
        print("The response of PurchaseOrderLineItemsApi->put_procurement_purchaseorders_by_parent_id_lineitems_bulk:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PurchaseOrderLineItemsApi->put_procurement_purchaseorders_by_parent_id_lineitems_bulk: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| purchaseorderId | 
 **client_id** | **str**|  | 
 **purchase_order_line_item** | [**List[PurchaseOrderLineItem]**](PurchaseOrderLineItem.md)| List of PurchaseOrderLineItem | 

### Return type

[**BulkResult**](BulkResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**207** | BulkResult |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_procurement_purchaseorders_by_parent_id_lineitems_by_id**
> PurchaseOrderLineItem put_procurement_purchaseorders_by_parent_id_lineitems_by_id(id, parent_id, client_id, purchase_order_line_item)

Put PurchaseOrderLineItem

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.purchase_order_line_item import PurchaseOrderLineItem
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
    api_instance = connectwise_psa.PurchaseOrderLineItemsApi(api_client)
    id = 56 # int | lineitemId
    parent_id = 56 # int | purchaseorderId
    client_id = 'client_id_example' # str | 
    purchase_order_line_item = connectwise_psa.PurchaseOrderLineItem() # PurchaseOrderLineItem | purchaseOrderLineItem

    try:
        # Put PurchaseOrderLineItem
        api_response = api_instance.put_procurement_purchaseorders_by_parent_id_lineitems_by_id(id, parent_id, client_id, purchase_order_line_item)
        print("The response of PurchaseOrderLineItemsApi->put_procurement_purchaseorders_by_parent_id_lineitems_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PurchaseOrderLineItemsApi->put_procurement_purchaseorders_by_parent_id_lineitems_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| lineitemId | 
 **parent_id** | **int**| purchaseorderId | 
 **client_id** | **str**|  | 
 **purchase_order_line_item** | [**PurchaseOrderLineItem**](PurchaseOrderLineItem.md)| purchaseOrderLineItem | 

### Return type

[**PurchaseOrderLineItem**](PurchaseOrderLineItem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | PurchaseOrderLineItem |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

