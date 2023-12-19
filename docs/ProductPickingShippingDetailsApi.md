# connectwise_psa.ProductPickingShippingDetailsApi

All URIs are relative to *https://api-aus.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_procurement_products_by_parent_id_picking_shipping_details_by_id**](ProductPickingShippingDetailsApi.md#delete_procurement_products_by_parent_id_picking_shipping_details_by_id) | **DELETE** /procurement/products/{parentId}/pickingShippingDetails/{id} | Delete ProductPickingShippingDetail
[**get_procurement_products_by_parent_id_picking_shipping_details**](ProductPickingShippingDetailsApi.md#get_procurement_products_by_parent_id_picking_shipping_details) | **GET** /procurement/products/{parentId}/pickingShippingDetails | Get List of ProductPickingShippingDetail
[**get_procurement_products_by_parent_id_picking_shipping_details_by_id**](ProductPickingShippingDetailsApi.md#get_procurement_products_by_parent_id_picking_shipping_details_by_id) | **GET** /procurement/products/{parentId}/pickingShippingDetails/{id} | Get List of ProductPickingShippingDetail
[**get_procurement_products_by_parent_id_picking_shipping_details_count**](ProductPickingShippingDetailsApi.md#get_procurement_products_by_parent_id_picking_shipping_details_count) | **GET** /procurement/products/{parentId}/pickingShippingDetails/count | Get Count of ProductPickingShippingDetail
[**patch_procurement_products_by_parent_id_picking_shipping_details_by_id**](ProductPickingShippingDetailsApi.md#patch_procurement_products_by_parent_id_picking_shipping_details_by_id) | **PATCH** /procurement/products/{parentId}/pickingShippingDetails/{id} | Patch List of ProductPickingShippingDetail
[**post_procurement_products_by_parent_id_picking_shipping_details**](ProductPickingShippingDetailsApi.md#post_procurement_products_by_parent_id_picking_shipping_details) | **POST** /procurement/products/{parentId}/pickingShippingDetails | Post List of ProductPickingShippingDetail
[**put_procurement_products_by_parent_id_picking_shipping_details_by_id**](ProductPickingShippingDetailsApi.md#put_procurement_products_by_parent_id_picking_shipping_details_by_id) | **PUT** /procurement/products/{parentId}/pickingShippingDetails/{id} | Put List of ProductPickingShippingDetail


# **delete_procurement_products_by_parent_id_picking_shipping_details_by_id**
> delete_procurement_products_by_parent_id_picking_shipping_details_by_id(id, parent_id, client_id)

Delete ProductPickingShippingDetail

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
    api_instance = connectwise_psa.ProductPickingShippingDetailsApi(api_client)
    id = 56 # int | pickingShippingDetailId
    parent_id = 56 # int | productId
    client_id = 'client_id_example' # str | 

    try:
        # Delete ProductPickingShippingDetail
        api_instance.delete_procurement_products_by_parent_id_picking_shipping_details_by_id(id, parent_id, client_id)
    except Exception as e:
        print("Exception when calling ProductPickingShippingDetailsApi->delete_procurement_products_by_parent_id_picking_shipping_details_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| pickingShippingDetailId | 
 **parent_id** | **int**| productId | 
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

# **get_procurement_products_by_parent_id_picking_shipping_details**
> List[ProductPickingShippingDetail] get_procurement_products_by_parent_id_picking_shipping_details(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of ProductPickingShippingDetail

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.product_picking_shipping_detail import ProductPickingShippingDetail
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
    api_instance = connectwise_psa.ProductPickingShippingDetailsApi(api_client)
    parent_id = 56 # int | productId
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
        # Get List of ProductPickingShippingDetail
        api_response = api_instance.get_procurement_products_by_parent_id_picking_shipping_details(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of ProductPickingShippingDetailsApi->get_procurement_products_by_parent_id_picking_shipping_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductPickingShippingDetailsApi->get_procurement_products_by_parent_id_picking_shipping_details: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| productId | 
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

[**List[ProductPickingShippingDetail]**](ProductPickingShippingDetail.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of ProductPickingShippingDetail |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_procurement_products_by_parent_id_picking_shipping_details_by_id**
> List[ProductPickingShippingDetail] get_procurement_products_by_parent_id_picking_shipping_details_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of ProductPickingShippingDetail

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.product_picking_shipping_detail import ProductPickingShippingDetail
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
    api_instance = connectwise_psa.ProductPickingShippingDetailsApi(api_client)
    id = 56 # int | pickingShippingDetailId
    parent_id = 56 # int | productId
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
        # Get List of ProductPickingShippingDetail
        api_response = api_instance.get_procurement_products_by_parent_id_picking_shipping_details_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of ProductPickingShippingDetailsApi->get_procurement_products_by_parent_id_picking_shipping_details_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductPickingShippingDetailsApi->get_procurement_products_by_parent_id_picking_shipping_details_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| pickingShippingDetailId | 
 **parent_id** | **int**| productId | 
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

[**List[ProductPickingShippingDetail]**](ProductPickingShippingDetail.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of ProductPickingShippingDetail |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_procurement_products_by_parent_id_picking_shipping_details_count**
> Count get_procurement_products_by_parent_id_picking_shipping_details_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Count of ProductPickingShippingDetail

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
    api_instance = connectwise_psa.ProductPickingShippingDetailsApi(api_client)
    parent_id = 56 # int | productId
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
        # Get Count of ProductPickingShippingDetail
        api_response = api_instance.get_procurement_products_by_parent_id_picking_shipping_details_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of ProductPickingShippingDetailsApi->get_procurement_products_by_parent_id_picking_shipping_details_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductPickingShippingDetailsApi->get_procurement_products_by_parent_id_picking_shipping_details_count: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| productId | 
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

# **patch_procurement_products_by_parent_id_picking_shipping_details_by_id**
> List[ProductPickingShippingDetail] patch_procurement_products_by_parent_id_picking_shipping_details_by_id(id, parent_id, client_id, patch_operation)

Patch List of ProductPickingShippingDetail

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.patch_operation import PatchOperation
from connectwise_psa.models.product_picking_shipping_detail import ProductPickingShippingDetail
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
    api_instance = connectwise_psa.ProductPickingShippingDetailsApi(api_client)
    id = 56 # int | pickingShippingDetailId
    parent_id = 56 # int | productId
    client_id = 'client_id_example' # str | 
    patch_operation = [connectwise_psa.PatchOperation()] # List[PatchOperation] | List of PatchOperation

    try:
        # Patch List of ProductPickingShippingDetail
        api_response = api_instance.patch_procurement_products_by_parent_id_picking_shipping_details_by_id(id, parent_id, client_id, patch_operation)
        print("The response of ProductPickingShippingDetailsApi->patch_procurement_products_by_parent_id_picking_shipping_details_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductPickingShippingDetailsApi->patch_procurement_products_by_parent_id_picking_shipping_details_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| pickingShippingDetailId | 
 **parent_id** | **int**| productId | 
 **client_id** | **str**|  | 
 **patch_operation** | [**List[PatchOperation]**](PatchOperation.md)| List of PatchOperation | 

### Return type

[**List[ProductPickingShippingDetail]**](ProductPickingShippingDetail.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of ProductPickingShippingDetail |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_procurement_products_by_parent_id_picking_shipping_details**
> List[ProductPickingShippingDetail] post_procurement_products_by_parent_id_picking_shipping_details(parent_id, client_id, product_picking_shipping_detail)

Post List of ProductPickingShippingDetail

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.product_picking_shipping_detail import ProductPickingShippingDetail
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
    api_instance = connectwise_psa.ProductPickingShippingDetailsApi(api_client)
    parent_id = 56 # int | productId
    client_id = 'client_id_example' # str | 
    product_picking_shipping_detail = connectwise_psa.ProductPickingShippingDetail() # ProductPickingShippingDetail | productPickingShippingDetails

    try:
        # Post List of ProductPickingShippingDetail
        api_response = api_instance.post_procurement_products_by_parent_id_picking_shipping_details(parent_id, client_id, product_picking_shipping_detail)
        print("The response of ProductPickingShippingDetailsApi->post_procurement_products_by_parent_id_picking_shipping_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductPickingShippingDetailsApi->post_procurement_products_by_parent_id_picking_shipping_details: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| productId | 
 **client_id** | **str**|  | 
 **product_picking_shipping_detail** | [**ProductPickingShippingDetail**](ProductPickingShippingDetail.md)| productPickingShippingDetails | 

### Return type

[**List[ProductPickingShippingDetail]**](ProductPickingShippingDetail.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of ProductPickingShippingDetail |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_procurement_products_by_parent_id_picking_shipping_details_by_id**
> List[ProductPickingShippingDetail] put_procurement_products_by_parent_id_picking_shipping_details_by_id(id, parent_id, client_id, product_picking_shipping_detail)

Put List of ProductPickingShippingDetail

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.product_picking_shipping_detail import ProductPickingShippingDetail
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
    api_instance = connectwise_psa.ProductPickingShippingDetailsApi(api_client)
    id = 56 # int | pickingShippingDetailId
    parent_id = 56 # int | productId
    client_id = 'client_id_example' # str | 
    product_picking_shipping_detail = connectwise_psa.ProductPickingShippingDetail() # ProductPickingShippingDetail | productPickingShippingDetails

    try:
        # Put List of ProductPickingShippingDetail
        api_response = api_instance.put_procurement_products_by_parent_id_picking_shipping_details_by_id(id, parent_id, client_id, product_picking_shipping_detail)
        print("The response of ProductPickingShippingDetailsApi->put_procurement_products_by_parent_id_picking_shipping_details_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductPickingShippingDetailsApi->put_procurement_products_by_parent_id_picking_shipping_details_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| pickingShippingDetailId | 
 **parent_id** | **int**| productId | 
 **client_id** | **str**|  | 
 **product_picking_shipping_detail** | [**ProductPickingShippingDetail**](ProductPickingShippingDetail.md)| productPickingShippingDetails | 

### Return type

[**List[ProductPickingShippingDetail]**](ProductPickingShippingDetail.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of ProductPickingShippingDetail |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

