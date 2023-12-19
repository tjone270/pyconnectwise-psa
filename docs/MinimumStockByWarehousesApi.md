# connectwise_psa.MinimumStockByWarehousesApi

All URIs are relative to *https://aus-api.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_procurement_catalog_by_parent_id_minimum_stock_by_warehouse_by_id**](MinimumStockByWarehousesApi.md#delete_procurement_catalog_by_parent_id_minimum_stock_by_warehouse_by_id) | **DELETE** /procurement/catalog/{parentId}/minimumStockByWarehouse/{id} | Delete MinimumStockByWarehouse
[**get_procurement_catalog_by_parent_id_minimum_stock_by_warehouse**](MinimumStockByWarehousesApi.md#get_procurement_catalog_by_parent_id_minimum_stock_by_warehouse) | **GET** /procurement/catalog/{parentId}/minimumStockByWarehouse | Get List of MinimumStockByWarehouse
[**get_procurement_catalog_by_parent_id_minimum_stock_by_warehouse_by_id**](MinimumStockByWarehousesApi.md#get_procurement_catalog_by_parent_id_minimum_stock_by_warehouse_by_id) | **GET** /procurement/catalog/{parentId}/minimumStockByWarehouse/{id} | Get MinimumStockByWarehouse
[**get_procurement_catalog_by_parent_id_minimum_stock_by_warehouse_count**](MinimumStockByWarehousesApi.md#get_procurement_catalog_by_parent_id_minimum_stock_by_warehouse_count) | **GET** /procurement/catalog/{parentId}/minimumStockByWarehouse/count | Get Count of MinimumStockByWarehouse
[**patch_procurement_catalog_by_parent_id_minimum_stock_by_warehouse_by_id**](MinimumStockByWarehousesApi.md#patch_procurement_catalog_by_parent_id_minimum_stock_by_warehouse_by_id) | **PATCH** /procurement/catalog/{parentId}/minimumStockByWarehouse/{id} | Patch MinimumStockByWarehouse
[**post_procurement_catalog_by_parent_id_minimum_stock_by_warehouse**](MinimumStockByWarehousesApi.md#post_procurement_catalog_by_parent_id_minimum_stock_by_warehouse) | **POST** /procurement/catalog/{parentId}/minimumStockByWarehouse | Post MinimumStockByWarehouse
[**put_procurement_catalog_by_parent_id_minimum_stock_by_warehouse_by_id**](MinimumStockByWarehousesApi.md#put_procurement_catalog_by_parent_id_minimum_stock_by_warehouse_by_id) | **PUT** /procurement/catalog/{parentId}/minimumStockByWarehouse/{id} | Put MinimumStockByWarehouse


# **delete_procurement_catalog_by_parent_id_minimum_stock_by_warehouse_by_id**
> delete_procurement_catalog_by_parent_id_minimum_stock_by_warehouse_by_id(id, parent_id, client_id)

Delete MinimumStockByWarehouse

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
    api_instance = connectwise_psa.MinimumStockByWarehousesApi(api_client)
    id = 56 # int | minimumStockByWarehouseId
    parent_id = 56 # int | catalogId
    client_id = 'client_id_example' # str | 

    try:
        # Delete MinimumStockByWarehouse
        api_instance.delete_procurement_catalog_by_parent_id_minimum_stock_by_warehouse_by_id(id, parent_id, client_id)
    except Exception as e:
        print("Exception when calling MinimumStockByWarehousesApi->delete_procurement_catalog_by_parent_id_minimum_stock_by_warehouse_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| minimumStockByWarehouseId | 
 **parent_id** | **int**| catalogId | 
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

# **get_procurement_catalog_by_parent_id_minimum_stock_by_warehouse**
> List[MinimumStockByWarehouse] get_procurement_catalog_by_parent_id_minimum_stock_by_warehouse(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of MinimumStockByWarehouse

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.minimum_stock_by_warehouse import MinimumStockByWarehouse
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
    api_instance = connectwise_psa.MinimumStockByWarehousesApi(api_client)
    parent_id = 56 # int | catalogId
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
        # Get List of MinimumStockByWarehouse
        api_response = api_instance.get_procurement_catalog_by_parent_id_minimum_stock_by_warehouse(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of MinimumStockByWarehousesApi->get_procurement_catalog_by_parent_id_minimum_stock_by_warehouse:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MinimumStockByWarehousesApi->get_procurement_catalog_by_parent_id_minimum_stock_by_warehouse: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| catalogId | 
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

[**List[MinimumStockByWarehouse]**](MinimumStockByWarehouse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of MinimumStockByWarehouse |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_procurement_catalog_by_parent_id_minimum_stock_by_warehouse_by_id**
> MinimumStockByWarehouse get_procurement_catalog_by_parent_id_minimum_stock_by_warehouse_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get MinimumStockByWarehouse

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.minimum_stock_by_warehouse import MinimumStockByWarehouse
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
    api_instance = connectwise_psa.MinimumStockByWarehousesApi(api_client)
    id = 56 # int | minimumStockByWarehouseId
    parent_id = 56 # int | catalogId
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
        # Get MinimumStockByWarehouse
        api_response = api_instance.get_procurement_catalog_by_parent_id_minimum_stock_by_warehouse_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of MinimumStockByWarehousesApi->get_procurement_catalog_by_parent_id_minimum_stock_by_warehouse_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MinimumStockByWarehousesApi->get_procurement_catalog_by_parent_id_minimum_stock_by_warehouse_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| minimumStockByWarehouseId | 
 **parent_id** | **int**| catalogId | 
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

[**MinimumStockByWarehouse**](MinimumStockByWarehouse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | MinimumStockByWarehouse |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_procurement_catalog_by_parent_id_minimum_stock_by_warehouse_count**
> Count get_procurement_catalog_by_parent_id_minimum_stock_by_warehouse_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Count of MinimumStockByWarehouse

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
    api_instance = connectwise_psa.MinimumStockByWarehousesApi(api_client)
    parent_id = 56 # int | catalogId
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
        # Get Count of MinimumStockByWarehouse
        api_response = api_instance.get_procurement_catalog_by_parent_id_minimum_stock_by_warehouse_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of MinimumStockByWarehousesApi->get_procurement_catalog_by_parent_id_minimum_stock_by_warehouse_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MinimumStockByWarehousesApi->get_procurement_catalog_by_parent_id_minimum_stock_by_warehouse_count: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| catalogId | 
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

# **patch_procurement_catalog_by_parent_id_minimum_stock_by_warehouse_by_id**
> MinimumStockByWarehouse patch_procurement_catalog_by_parent_id_minimum_stock_by_warehouse_by_id(id, parent_id, client_id, patch_operation)

Patch MinimumStockByWarehouse

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.minimum_stock_by_warehouse import MinimumStockByWarehouse
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
    api_instance = connectwise_psa.MinimumStockByWarehousesApi(api_client)
    id = 56 # int | minimumStockByWarehouseId
    parent_id = 56 # int | catalogId
    client_id = 'client_id_example' # str | 
    patch_operation = [connectwise_psa.PatchOperation()] # List[PatchOperation] | List of PatchOperation

    try:
        # Patch MinimumStockByWarehouse
        api_response = api_instance.patch_procurement_catalog_by_parent_id_minimum_stock_by_warehouse_by_id(id, parent_id, client_id, patch_operation)
        print("The response of MinimumStockByWarehousesApi->patch_procurement_catalog_by_parent_id_minimum_stock_by_warehouse_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MinimumStockByWarehousesApi->patch_procurement_catalog_by_parent_id_minimum_stock_by_warehouse_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| minimumStockByWarehouseId | 
 **parent_id** | **int**| catalogId | 
 **client_id** | **str**|  | 
 **patch_operation** | [**List[PatchOperation]**](PatchOperation.md)| List of PatchOperation | 

### Return type

[**MinimumStockByWarehouse**](MinimumStockByWarehouse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | MinimumStockByWarehouse |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_procurement_catalog_by_parent_id_minimum_stock_by_warehouse**
> MinimumStockByWarehouse post_procurement_catalog_by_parent_id_minimum_stock_by_warehouse(parent_id, client_id, minimum_stock_by_warehouse)

Post MinimumStockByWarehouse

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.minimum_stock_by_warehouse import MinimumStockByWarehouse
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
    api_instance = connectwise_psa.MinimumStockByWarehousesApi(api_client)
    parent_id = 56 # int | catalogId
    client_id = 'client_id_example' # str | 
    minimum_stock_by_warehouse = connectwise_psa.MinimumStockByWarehouse() # MinimumStockByWarehouse | minimumStockByWarehouse

    try:
        # Post MinimumStockByWarehouse
        api_response = api_instance.post_procurement_catalog_by_parent_id_minimum_stock_by_warehouse(parent_id, client_id, minimum_stock_by_warehouse)
        print("The response of MinimumStockByWarehousesApi->post_procurement_catalog_by_parent_id_minimum_stock_by_warehouse:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MinimumStockByWarehousesApi->post_procurement_catalog_by_parent_id_minimum_stock_by_warehouse: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| catalogId | 
 **client_id** | **str**|  | 
 **minimum_stock_by_warehouse** | [**MinimumStockByWarehouse**](MinimumStockByWarehouse.md)| minimumStockByWarehouse | 

### Return type

[**MinimumStockByWarehouse**](MinimumStockByWarehouse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | MinimumStockByWarehouse |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_procurement_catalog_by_parent_id_minimum_stock_by_warehouse_by_id**
> MinimumStockByWarehouse put_procurement_catalog_by_parent_id_minimum_stock_by_warehouse_by_id(id, parent_id, client_id, minimum_stock_by_warehouse)

Put MinimumStockByWarehouse

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.minimum_stock_by_warehouse import MinimumStockByWarehouse
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
    api_instance = connectwise_psa.MinimumStockByWarehousesApi(api_client)
    id = 56 # int | minimumStockByWarehouseId
    parent_id = 56 # int | catalogId
    client_id = 'client_id_example' # str | 
    minimum_stock_by_warehouse = connectwise_psa.MinimumStockByWarehouse() # MinimumStockByWarehouse | minimumStockByWarehouse

    try:
        # Put MinimumStockByWarehouse
        api_response = api_instance.put_procurement_catalog_by_parent_id_minimum_stock_by_warehouse_by_id(id, parent_id, client_id, minimum_stock_by_warehouse)
        print("The response of MinimumStockByWarehousesApi->put_procurement_catalog_by_parent_id_minimum_stock_by_warehouse_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MinimumStockByWarehousesApi->put_procurement_catalog_by_parent_id_minimum_stock_by_warehouse_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| minimumStockByWarehouseId | 
 **parent_id** | **int**| catalogId | 
 **client_id** | **str**|  | 
 **minimum_stock_by_warehouse** | [**MinimumStockByWarehouse**](MinimumStockByWarehouse.md)| minimumStockByWarehouse | 

### Return type

[**MinimumStockByWarehouse**](MinimumStockByWarehouse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | MinimumStockByWarehouse |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

