# connectwise_psa.InventoryOnHandsApi

All URIs are relative to *https://api-aus.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_procurement_warehouse_bins_by_parent_id_inventory_on_hand**](InventoryOnHandsApi.md#get_procurement_warehouse_bins_by_parent_id_inventory_on_hand) | **GET** /procurement/warehouseBins/{parentId}/inventoryOnHand | Get List of InventoryOnHand
[**get_procurement_warehouse_bins_by_parent_id_inventory_on_hand_by_id**](InventoryOnHandsApi.md#get_procurement_warehouse_bins_by_parent_id_inventory_on_hand_by_id) | **GET** /procurement/warehouseBins/{parentId}/inventoryOnHand/{id} | Get InventoryOnHand
[**get_procurement_warehouse_bins_by_parent_id_inventory_on_hand_count**](InventoryOnHandsApi.md#get_procurement_warehouse_bins_by_parent_id_inventory_on_hand_count) | **GET** /procurement/warehouseBins/{parentId}/inventoryOnHand/count | Get Count of InventoryOnHand


# **get_procurement_warehouse_bins_by_parent_id_inventory_on_hand**
> List[InventoryOnHand] get_procurement_warehouse_bins_by_parent_id_inventory_on_hand(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of InventoryOnHand

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.inventory_on_hand import InventoryOnHand
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
    api_instance = connectwise_psa.InventoryOnHandsApi(api_client)
    parent_id = 56 # int | warehouseBinId
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
        # Get List of InventoryOnHand
        api_response = api_instance.get_procurement_warehouse_bins_by_parent_id_inventory_on_hand(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of InventoryOnHandsApi->get_procurement_warehouse_bins_by_parent_id_inventory_on_hand:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InventoryOnHandsApi->get_procurement_warehouse_bins_by_parent_id_inventory_on_hand: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| warehouseBinId | 
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

[**List[InventoryOnHand]**](InventoryOnHand.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of InventoryOnHand |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_procurement_warehouse_bins_by_parent_id_inventory_on_hand_by_id**
> InventoryOnHand get_procurement_warehouse_bins_by_parent_id_inventory_on_hand_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get InventoryOnHand

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.inventory_on_hand import InventoryOnHand
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
    api_instance = connectwise_psa.InventoryOnHandsApi(api_client)
    id = 56 # int | inventoryOnHandId
    parent_id = 56 # int | warehouseBinId
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
        # Get InventoryOnHand
        api_response = api_instance.get_procurement_warehouse_bins_by_parent_id_inventory_on_hand_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of InventoryOnHandsApi->get_procurement_warehouse_bins_by_parent_id_inventory_on_hand_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InventoryOnHandsApi->get_procurement_warehouse_bins_by_parent_id_inventory_on_hand_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| inventoryOnHandId | 
 **parent_id** | **int**| warehouseBinId | 
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

[**InventoryOnHand**](InventoryOnHand.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | InventoryOnHand |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_procurement_warehouse_bins_by_parent_id_inventory_on_hand_count**
> Count get_procurement_warehouse_bins_by_parent_id_inventory_on_hand_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Count of InventoryOnHand

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
    api_instance = connectwise_psa.InventoryOnHandsApi(api_client)
    parent_id = 56 # int | warehouseBinId
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
        # Get Count of InventoryOnHand
        api_response = api_instance.get_procurement_warehouse_bins_by_parent_id_inventory_on_hand_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of InventoryOnHandsApi->get_procurement_warehouse_bins_by_parent_id_inventory_on_hand_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InventoryOnHandsApi->get_procurement_warehouse_bins_by_parent_id_inventory_on_hand_count: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| warehouseBinId | 
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

