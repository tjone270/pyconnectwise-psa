# connectwise_psa.WarehouseBinsApi

All URIs are relative to *https://api-aus.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_procurement_warehouse_bins_by_id**](WarehouseBinsApi.md#delete_procurement_warehouse_bins_by_id) | **DELETE** /procurement/warehouseBins/{id} | Delete WarehouseBin
[**get_procurement_warehouse_bins**](WarehouseBinsApi.md#get_procurement_warehouse_bins) | **GET** /procurement/warehouseBins | Get List of WarehouseBin
[**get_procurement_warehouse_bins_by_id**](WarehouseBinsApi.md#get_procurement_warehouse_bins_by_id) | **GET** /procurement/warehouseBins/{id} | Get WarehouseBin
[**get_procurement_warehouse_bins_count**](WarehouseBinsApi.md#get_procurement_warehouse_bins_count) | **GET** /procurement/warehouseBins/count | Get Count of WarehouseBin
[**patch_procurement_warehouse_bins_by_id**](WarehouseBinsApi.md#patch_procurement_warehouse_bins_by_id) | **PATCH** /procurement/warehouseBins/{id} | Patch WarehouseBin
[**post_procurement_warehouse_bins**](WarehouseBinsApi.md#post_procurement_warehouse_bins) | **POST** /procurement/warehouseBins | Post WarehouseBin
[**put_procurement_warehouse_bins_by_id**](WarehouseBinsApi.md#put_procurement_warehouse_bins_by_id) | **PUT** /procurement/warehouseBins/{id} | Put WarehouseBin


# **delete_procurement_warehouse_bins_by_id**
> delete_procurement_warehouse_bins_by_id(id, client_id)

Delete WarehouseBin

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
    api_instance = connectwise_psa.WarehouseBinsApi(api_client)
    id = 56 # int | warehouseBinId
    client_id = 'client_id_example' # str | 

    try:
        # Delete WarehouseBin
        api_instance.delete_procurement_warehouse_bins_by_id(id, client_id)
    except Exception as e:
        print("Exception when calling WarehouseBinsApi->delete_procurement_warehouse_bins_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| warehouseBinId | 
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

# **get_procurement_warehouse_bins**
> List[WarehouseBin] get_procurement_warehouse_bins(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of WarehouseBin

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.warehouse_bin import WarehouseBin
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
    api_instance = connectwise_psa.WarehouseBinsApi(api_client)
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
        # Get List of WarehouseBin
        api_response = api_instance.get_procurement_warehouse_bins(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of WarehouseBinsApi->get_procurement_warehouse_bins:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WarehouseBinsApi->get_procurement_warehouse_bins: %s\n" % e)
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

[**List[WarehouseBin]**](WarehouseBin.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of WarehouseBin |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_procurement_warehouse_bins_by_id**
> WarehouseBin get_procurement_warehouse_bins_by_id(id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get WarehouseBin

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.warehouse_bin import WarehouseBin
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
    api_instance = connectwise_psa.WarehouseBinsApi(api_client)
    id = 56 # int | warehouseBinId
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
        # Get WarehouseBin
        api_response = api_instance.get_procurement_warehouse_bins_by_id(id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of WarehouseBinsApi->get_procurement_warehouse_bins_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WarehouseBinsApi->get_procurement_warehouse_bins_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| warehouseBinId | 
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

[**WarehouseBin**](WarehouseBin.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | WarehouseBin |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_procurement_warehouse_bins_count**
> Count get_procurement_warehouse_bins_count(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Count of WarehouseBin

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
    api_instance = connectwise_psa.WarehouseBinsApi(api_client)
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
        # Get Count of WarehouseBin
        api_response = api_instance.get_procurement_warehouse_bins_count(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of WarehouseBinsApi->get_procurement_warehouse_bins_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WarehouseBinsApi->get_procurement_warehouse_bins_count: %s\n" % e)
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

# **patch_procurement_warehouse_bins_by_id**
> WarehouseBin patch_procurement_warehouse_bins_by_id(id, client_id, patch_operation)

Patch WarehouseBin

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.patch_operation import PatchOperation
from connectwise_psa.models.warehouse_bin import WarehouseBin
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
    api_instance = connectwise_psa.WarehouseBinsApi(api_client)
    id = 56 # int | warehouseBinId
    client_id = 'client_id_example' # str | 
    patch_operation = [connectwise_psa.PatchOperation()] # List[PatchOperation] | List of PatchOperation

    try:
        # Patch WarehouseBin
        api_response = api_instance.patch_procurement_warehouse_bins_by_id(id, client_id, patch_operation)
        print("The response of WarehouseBinsApi->patch_procurement_warehouse_bins_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WarehouseBinsApi->patch_procurement_warehouse_bins_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| warehouseBinId | 
 **client_id** | **str**|  | 
 **patch_operation** | [**List[PatchOperation]**](PatchOperation.md)| List of PatchOperation | 

### Return type

[**WarehouseBin**](WarehouseBin.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | WarehouseBin |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_procurement_warehouse_bins**
> WarehouseBin post_procurement_warehouse_bins(client_id, warehouse_bin)

Post WarehouseBin

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.warehouse_bin import WarehouseBin
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
    api_instance = connectwise_psa.WarehouseBinsApi(api_client)
    client_id = 'client_id_example' # str | 
    warehouse_bin = connectwise_psa.WarehouseBin() # WarehouseBin | warehouseBin

    try:
        # Post WarehouseBin
        api_response = api_instance.post_procurement_warehouse_bins(client_id, warehouse_bin)
        print("The response of WarehouseBinsApi->post_procurement_warehouse_bins:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WarehouseBinsApi->post_procurement_warehouse_bins: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**|  | 
 **warehouse_bin** | [**WarehouseBin**](WarehouseBin.md)| warehouseBin | 

### Return type

[**WarehouseBin**](WarehouseBin.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | WarehouseBin |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_procurement_warehouse_bins_by_id**
> WarehouseBin put_procurement_warehouse_bins_by_id(id, client_id, warehouse_bin)

Put WarehouseBin

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.warehouse_bin import WarehouseBin
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
    api_instance = connectwise_psa.WarehouseBinsApi(api_client)
    id = 56 # int | warehouseBinId
    client_id = 'client_id_example' # str | 
    warehouse_bin = connectwise_psa.WarehouseBin() # WarehouseBin | warehouseBin

    try:
        # Put WarehouseBin
        api_response = api_instance.put_procurement_warehouse_bins_by_id(id, client_id, warehouse_bin)
        print("The response of WarehouseBinsApi->put_procurement_warehouse_bins_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WarehouseBinsApi->put_procurement_warehouse_bins_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| warehouseBinId | 
 **client_id** | **str**|  | 
 **warehouse_bin** | [**WarehouseBin**](WarehouseBin.md)| warehouseBin | 

### Return type

[**WarehouseBin**](WarehouseBin.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | WarehouseBin |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

