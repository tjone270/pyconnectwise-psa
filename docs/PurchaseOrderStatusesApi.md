# connectwise_psa.PurchaseOrderStatusesApi

All URIs are relative to *https://api-aus.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_procurement_purchaseorderstatuses_by_id**](PurchaseOrderStatusesApi.md#delete_procurement_purchaseorderstatuses_by_id) | **DELETE** /procurement/purchaseorderstatuses/{id} | Delete PurchaseOrderStatus
[**get_procurement_purchaseorderstatuses**](PurchaseOrderStatusesApi.md#get_procurement_purchaseorderstatuses) | **GET** /procurement/purchaseorderstatuses | Get List of PurchaseOrderStatus
[**get_procurement_purchaseorderstatuses_by_id**](PurchaseOrderStatusesApi.md#get_procurement_purchaseorderstatuses_by_id) | **GET** /procurement/purchaseorderstatuses/{id} | Get PurchaseOrderStatus
[**get_procurement_purchaseorderstatuses_by_id_usages**](PurchaseOrderStatusesApi.md#get_procurement_purchaseorderstatuses_by_id_usages) | **GET** /procurement/purchaseorderstatuses/{id}/usages | Get List of Usage Count
[**get_procurement_purchaseorderstatuses_by_id_usages_list**](PurchaseOrderStatusesApi.md#get_procurement_purchaseorderstatuses_by_id_usages_list) | **GET** /procurement/purchaseorderstatuses/{id}/usages/list | Get List of Usage
[**get_procurement_purchaseorderstatuses_count**](PurchaseOrderStatusesApi.md#get_procurement_purchaseorderstatuses_count) | **GET** /procurement/purchaseorderstatuses/count | Get Count of PurchaseOrderStatus
[**patch_procurement_purchaseorderstatuses_by_id**](PurchaseOrderStatusesApi.md#patch_procurement_purchaseorderstatuses_by_id) | **PATCH** /procurement/purchaseorderstatuses/{id} | Patch PurchaseOrderStatus
[**post_procurement_purchaseorderstatuses**](PurchaseOrderStatusesApi.md#post_procurement_purchaseorderstatuses) | **POST** /procurement/purchaseorderstatuses | Post PurchaseOrderStatus
[**put_procurement_purchaseorderstatuses_by_id**](PurchaseOrderStatusesApi.md#put_procurement_purchaseorderstatuses_by_id) | **PUT** /procurement/purchaseorderstatuses/{id} | Put PurchaseOrderStatus


# **delete_procurement_purchaseorderstatuses_by_id**
> delete_procurement_purchaseorderstatuses_by_id(id, client_id)

Delete PurchaseOrderStatus

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
    api_instance = connectwise_psa.PurchaseOrderStatusesApi(api_client)
    id = 56 # int | purchaseorderstatusId
    client_id = 'client_id_example' # str | 

    try:
        # Delete PurchaseOrderStatus
        api_instance.delete_procurement_purchaseorderstatuses_by_id(id, client_id)
    except Exception as e:
        print("Exception when calling PurchaseOrderStatusesApi->delete_procurement_purchaseorderstatuses_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| purchaseorderstatusId | 
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

# **get_procurement_purchaseorderstatuses**
> List[PurchaseOrderStatus] get_procurement_purchaseorderstatuses(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of PurchaseOrderStatus

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.purchase_order_status import PurchaseOrderStatus
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
    api_instance = connectwise_psa.PurchaseOrderStatusesApi(api_client)
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
        # Get List of PurchaseOrderStatus
        api_response = api_instance.get_procurement_purchaseorderstatuses(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of PurchaseOrderStatusesApi->get_procurement_purchaseorderstatuses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PurchaseOrderStatusesApi->get_procurement_purchaseorderstatuses: %s\n" % e)
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

[**List[PurchaseOrderStatus]**](PurchaseOrderStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of PurchaseOrderStatus |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_procurement_purchaseorderstatuses_by_id**
> PurchaseOrderStatus get_procurement_purchaseorderstatuses_by_id(id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get PurchaseOrderStatus

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.purchase_order_status import PurchaseOrderStatus
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
    api_instance = connectwise_psa.PurchaseOrderStatusesApi(api_client)
    id = 56 # int | purchaseorderstatusId
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
        # Get PurchaseOrderStatus
        api_response = api_instance.get_procurement_purchaseorderstatuses_by_id(id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of PurchaseOrderStatusesApi->get_procurement_purchaseorderstatuses_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PurchaseOrderStatusesApi->get_procurement_purchaseorderstatuses_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| purchaseorderstatusId | 
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

[**PurchaseOrderStatus**](PurchaseOrderStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | PurchaseOrderStatus |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_procurement_purchaseorderstatuses_by_id_usages**
> List[Usage] get_procurement_purchaseorderstatuses_by_id_usages(id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of Usage Count

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.usage import Usage
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
    api_instance = connectwise_psa.PurchaseOrderStatusesApi(api_client)
    id = 56 # int | purchaseorderstatusId
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
        # Get List of Usage Count
        api_response = api_instance.get_procurement_purchaseorderstatuses_by_id_usages(id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of PurchaseOrderStatusesApi->get_procurement_purchaseorderstatuses_by_id_usages:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PurchaseOrderStatusesApi->get_procurement_purchaseorderstatuses_by_id_usages: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| purchaseorderstatusId | 
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

[**List[Usage]**](Usage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of Usage |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_procurement_purchaseorderstatuses_by_id_usages_list**
> List[Usage] get_procurement_purchaseorderstatuses_by_id_usages_list(id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of Usage

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.usage import Usage
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
    api_instance = connectwise_psa.PurchaseOrderStatusesApi(api_client)
    id = 56 # int | purchaseorderstatusId
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
        # Get List of Usage
        api_response = api_instance.get_procurement_purchaseorderstatuses_by_id_usages_list(id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of PurchaseOrderStatusesApi->get_procurement_purchaseorderstatuses_by_id_usages_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PurchaseOrderStatusesApi->get_procurement_purchaseorderstatuses_by_id_usages_list: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| purchaseorderstatusId | 
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

[**List[Usage]**](Usage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of Usage |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_procurement_purchaseorderstatuses_count**
> Count get_procurement_purchaseorderstatuses_count(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Count of PurchaseOrderStatus

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
    api_instance = connectwise_psa.PurchaseOrderStatusesApi(api_client)
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
        # Get Count of PurchaseOrderStatus
        api_response = api_instance.get_procurement_purchaseorderstatuses_count(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of PurchaseOrderStatusesApi->get_procurement_purchaseorderstatuses_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PurchaseOrderStatusesApi->get_procurement_purchaseorderstatuses_count: %s\n" % e)
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

# **patch_procurement_purchaseorderstatuses_by_id**
> PurchaseOrderStatus patch_procurement_purchaseorderstatuses_by_id(id, client_id, patch_operation)

Patch PurchaseOrderStatus

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.patch_operation import PatchOperation
from connectwise_psa.models.purchase_order_status import PurchaseOrderStatus
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
    api_instance = connectwise_psa.PurchaseOrderStatusesApi(api_client)
    id = 56 # int | purchaseorderstatusId
    client_id = 'client_id_example' # str | 
    patch_operation = [connectwise_psa.PatchOperation()] # List[PatchOperation] | List of PatchOperation

    try:
        # Patch PurchaseOrderStatus
        api_response = api_instance.patch_procurement_purchaseorderstatuses_by_id(id, client_id, patch_operation)
        print("The response of PurchaseOrderStatusesApi->patch_procurement_purchaseorderstatuses_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PurchaseOrderStatusesApi->patch_procurement_purchaseorderstatuses_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| purchaseorderstatusId | 
 **client_id** | **str**|  | 
 **patch_operation** | [**List[PatchOperation]**](PatchOperation.md)| List of PatchOperation | 

### Return type

[**PurchaseOrderStatus**](PurchaseOrderStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | PurchaseOrderStatus |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_procurement_purchaseorderstatuses**
> PurchaseOrderStatus post_procurement_purchaseorderstatuses(client_id, purchase_order_status)

Post PurchaseOrderStatus

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.purchase_order_status import PurchaseOrderStatus
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
    api_instance = connectwise_psa.PurchaseOrderStatusesApi(api_client)
    client_id = 'client_id_example' # str | 
    purchase_order_status = connectwise_psa.PurchaseOrderStatus() # PurchaseOrderStatus | poStatus

    try:
        # Post PurchaseOrderStatus
        api_response = api_instance.post_procurement_purchaseorderstatuses(client_id, purchase_order_status)
        print("The response of PurchaseOrderStatusesApi->post_procurement_purchaseorderstatuses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PurchaseOrderStatusesApi->post_procurement_purchaseorderstatuses: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**|  | 
 **purchase_order_status** | [**PurchaseOrderStatus**](PurchaseOrderStatus.md)| poStatus | 

### Return type

[**PurchaseOrderStatus**](PurchaseOrderStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | PurchaseOrderStatus |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_procurement_purchaseorderstatuses_by_id**
> PurchaseOrderStatus put_procurement_purchaseorderstatuses_by_id(id, client_id, purchase_order_status)

Put PurchaseOrderStatus

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.purchase_order_status import PurchaseOrderStatus
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
    api_instance = connectwise_psa.PurchaseOrderStatusesApi(api_client)
    id = 56 # int | purchaseorderstatusId
    client_id = 'client_id_example' # str | 
    purchase_order_status = connectwise_psa.PurchaseOrderStatus() # PurchaseOrderStatus | purchaseOrderStatus

    try:
        # Put PurchaseOrderStatus
        api_response = api_instance.put_procurement_purchaseorderstatuses_by_id(id, client_id, purchase_order_status)
        print("The response of PurchaseOrderStatusesApi->put_procurement_purchaseorderstatuses_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PurchaseOrderStatusesApi->put_procurement_purchaseorderstatuses_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| purchaseorderstatusId | 
 **client_id** | **str**|  | 
 **purchase_order_status** | [**PurchaseOrderStatus**](PurchaseOrderStatus.md)| purchaseOrderStatus | 

### Return type

[**PurchaseOrderStatus**](PurchaseOrderStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | PurchaseOrderStatus |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

