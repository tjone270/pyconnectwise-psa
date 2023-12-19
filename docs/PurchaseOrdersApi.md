# connectwise_psa.PurchaseOrdersApi

All URIs are relative to *https://api-aus.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_procurement_purchaseorders_by_id**](PurchaseOrdersApi.md#delete_procurement_purchaseorders_by_id) | **DELETE** /procurement/purchaseorders/{id} | Delete PurchaseOrder
[**get_procurement_purchaseorders**](PurchaseOrdersApi.md#get_procurement_purchaseorders) | **GET** /procurement/purchaseorders | Get List of PurchaseOrder
[**get_procurement_purchaseorders_by_id**](PurchaseOrdersApi.md#get_procurement_purchaseorders_by_id) | **GET** /procurement/purchaseorders/{id} | Get PurchaseOrder
[**get_procurement_purchaseorders_count**](PurchaseOrdersApi.md#get_procurement_purchaseorders_count) | **GET** /procurement/purchaseorders/count | Get Count of PurchaseOrder
[**patch_procurement_purchaseorders_by_id**](PurchaseOrdersApi.md#patch_procurement_purchaseorders_by_id) | **PATCH** /procurement/purchaseorders/{id} | Patch PurchaseOrder
[**post_procurement_purchaseorders**](PurchaseOrdersApi.md#post_procurement_purchaseorders) | **POST** /procurement/purchaseorders | Post PurchaseOrder
[**post_procurement_purchaseorders_by_id_rebatch**](PurchaseOrdersApi.md#post_procurement_purchaseorders_by_id_rebatch) | **POST** /procurement/purchaseorders/{id}/rebatch | Post RebatchPurchaseOrder
[**post_procurement_purchaseorders_by_id_unbatch**](PurchaseOrdersApi.md#post_procurement_purchaseorders_by_id_unbatch) | **POST** /procurement/purchaseorders/{id}/unbatch | Post UnbatchPurchaseOrder
[**put_procurement_purchaseorders_by_id**](PurchaseOrdersApi.md#put_procurement_purchaseorders_by_id) | **PUT** /procurement/purchaseorders/{id} | Put PurchaseOrder


# **delete_procurement_purchaseorders_by_id**
> delete_procurement_purchaseorders_by_id(id, client_id)

Delete PurchaseOrder

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
    api_instance = connectwise_psa.PurchaseOrdersApi(api_client)
    id = 56 # int | purchaseorderId
    client_id = 'client_id_example' # str | 

    try:
        # Delete PurchaseOrder
        api_instance.delete_procurement_purchaseorders_by_id(id, client_id)
    except Exception as e:
        print("Exception when calling PurchaseOrdersApi->delete_procurement_purchaseorders_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| purchaseorderId | 
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

# **get_procurement_purchaseorders**
> List[PurchaseOrder] get_procurement_purchaseorders(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of PurchaseOrder

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.purchase_order import PurchaseOrder
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
    api_instance = connectwise_psa.PurchaseOrdersApi(api_client)
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
        # Get List of PurchaseOrder
        api_response = api_instance.get_procurement_purchaseorders(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of PurchaseOrdersApi->get_procurement_purchaseorders:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PurchaseOrdersApi->get_procurement_purchaseorders: %s\n" % e)
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

[**List[PurchaseOrder]**](PurchaseOrder.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of PurchaseOrder |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_procurement_purchaseorders_by_id**
> PurchaseOrder get_procurement_purchaseorders_by_id(id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get PurchaseOrder

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.purchase_order import PurchaseOrder
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
    api_instance = connectwise_psa.PurchaseOrdersApi(api_client)
    id = 56 # int | purchaseorderId
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
        # Get PurchaseOrder
        api_response = api_instance.get_procurement_purchaseorders_by_id(id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of PurchaseOrdersApi->get_procurement_purchaseorders_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PurchaseOrdersApi->get_procurement_purchaseorders_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| purchaseorderId | 
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

[**PurchaseOrder**](PurchaseOrder.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | PurchaseOrder |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_procurement_purchaseorders_count**
> Count get_procurement_purchaseorders_count(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Count of PurchaseOrder

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
    api_instance = connectwise_psa.PurchaseOrdersApi(api_client)
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
        # Get Count of PurchaseOrder
        api_response = api_instance.get_procurement_purchaseorders_count(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of PurchaseOrdersApi->get_procurement_purchaseorders_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PurchaseOrdersApi->get_procurement_purchaseorders_count: %s\n" % e)
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

# **patch_procurement_purchaseorders_by_id**
> PurchaseOrder patch_procurement_purchaseorders_by_id(id, client_id, patch_operation)

Patch PurchaseOrder

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.patch_operation import PatchOperation
from connectwise_psa.models.purchase_order import PurchaseOrder
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
    api_instance = connectwise_psa.PurchaseOrdersApi(api_client)
    id = 56 # int | purchaseorderId
    client_id = 'client_id_example' # str | 
    patch_operation = [connectwise_psa.PatchOperation()] # List[PatchOperation] | List of PatchOperation

    try:
        # Patch PurchaseOrder
        api_response = api_instance.patch_procurement_purchaseorders_by_id(id, client_id, patch_operation)
        print("The response of PurchaseOrdersApi->patch_procurement_purchaseorders_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PurchaseOrdersApi->patch_procurement_purchaseorders_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| purchaseorderId | 
 **client_id** | **str**|  | 
 **patch_operation** | [**List[PatchOperation]**](PatchOperation.md)| List of PatchOperation | 

### Return type

[**PurchaseOrder**](PurchaseOrder.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | PurchaseOrder |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_procurement_purchaseorders**
> PurchaseOrder post_procurement_purchaseorders(client_id, purchase_order)

Post PurchaseOrder

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.purchase_order import PurchaseOrder
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
    api_instance = connectwise_psa.PurchaseOrdersApi(api_client)
    client_id = 'client_id_example' # str | 
    purchase_order = connectwise_psa.PurchaseOrder() # PurchaseOrder | purchaseOrder

    try:
        # Post PurchaseOrder
        api_response = api_instance.post_procurement_purchaseorders(client_id, purchase_order)
        print("The response of PurchaseOrdersApi->post_procurement_purchaseorders:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PurchaseOrdersApi->post_procurement_purchaseorders: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**|  | 
 **purchase_order** | [**PurchaseOrder**](PurchaseOrder.md)| purchaseOrder | 

### Return type

[**PurchaseOrder**](PurchaseOrder.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | PurchaseOrder |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_procurement_purchaseorders_by_id_rebatch**
> SuccessResponse post_procurement_purchaseorders_by_id_rebatch(id, client_id)

Post RebatchPurchaseOrder

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.success_response import SuccessResponse
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
    api_instance = connectwise_psa.PurchaseOrdersApi(api_client)
    id = 56 # int | purchaseOrderId
    client_id = 'client_id_example' # str | 

    try:
        # Post RebatchPurchaseOrder
        api_response = api_instance.post_procurement_purchaseorders_by_id_rebatch(id, client_id)
        print("The response of PurchaseOrdersApi->post_procurement_purchaseorders_by_id_rebatch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PurchaseOrdersApi->post_procurement_purchaseorders_by_id_rebatch: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| purchaseOrderId | 
 **client_id** | **str**|  | 

### Return type

[**SuccessResponse**](SuccessResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | SuccessResponse |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_procurement_purchaseorders_by_id_unbatch**
> SuccessResponse post_procurement_purchaseorders_by_id_unbatch(id, client_id)

Post UnbatchPurchaseOrder

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.success_response import SuccessResponse
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
    api_instance = connectwise_psa.PurchaseOrdersApi(api_client)
    id = 56 # int | purchaseOrderId
    client_id = 'client_id_example' # str | 

    try:
        # Post UnbatchPurchaseOrder
        api_response = api_instance.post_procurement_purchaseorders_by_id_unbatch(id, client_id)
        print("The response of PurchaseOrdersApi->post_procurement_purchaseorders_by_id_unbatch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PurchaseOrdersApi->post_procurement_purchaseorders_by_id_unbatch: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| purchaseOrderId | 
 **client_id** | **str**|  | 

### Return type

[**SuccessResponse**](SuccessResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | SuccessResponse |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_procurement_purchaseorders_by_id**
> PurchaseOrder put_procurement_purchaseorders_by_id(id, client_id, purchase_order)

Put PurchaseOrder

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.purchase_order import PurchaseOrder
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
    api_instance = connectwise_psa.PurchaseOrdersApi(api_client)
    id = 56 # int | purchaseorderId
    client_id = 'client_id_example' # str | 
    purchase_order = connectwise_psa.PurchaseOrder() # PurchaseOrder | purchaseOrder

    try:
        # Put PurchaseOrder
        api_response = api_instance.put_procurement_purchaseorders_by_id(id, client_id, purchase_order)
        print("The response of PurchaseOrdersApi->put_procurement_purchaseorders_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PurchaseOrdersApi->put_procurement_purchaseorders_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| purchaseorderId | 
 **client_id** | **str**|  | 
 **purchase_order** | [**PurchaseOrder**](PurchaseOrder.md)| purchaseOrder | 

### Return type

[**PurchaseOrder**](PurchaseOrder.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | PurchaseOrder |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

