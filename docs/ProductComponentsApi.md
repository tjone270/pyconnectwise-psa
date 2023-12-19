# connectwise_psa.ProductComponentsApi

All URIs are relative to *https://api-aus.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_procurement_products_by_parent_id_components_by_id**](ProductComponentsApi.md#delete_procurement_products_by_parent_id_components_by_id) | **DELETE** /procurement/products/{parentId}/components/{id} | Delete ProductComponent
[**get_procurement_products_by_parent_id_components**](ProductComponentsApi.md#get_procurement_products_by_parent_id_components) | **GET** /procurement/products/{parentId}/components | Get List of ProductComponent
[**get_procurement_products_by_parent_id_components_by_id**](ProductComponentsApi.md#get_procurement_products_by_parent_id_components_by_id) | **GET** /procurement/products/{parentId}/components/{id} | Get List of ProductComponent
[**get_procurement_products_by_parent_id_components_count**](ProductComponentsApi.md#get_procurement_products_by_parent_id_components_count) | **GET** /procurement/products/{parentId}/components/count | Get Count of ProductComponent
[**patch_procurement_products_by_parent_id_components_by_id**](ProductComponentsApi.md#patch_procurement_products_by_parent_id_components_by_id) | **PATCH** /procurement/products/{parentId}/components/{id} | Patch List of ProductComponent
[**post_procurement_products_by_parent_id_components**](ProductComponentsApi.md#post_procurement_products_by_parent_id_components) | **POST** /procurement/products/{parentId}/components | Post List of ProductComponent
[**put_procurement_products_by_parent_id_components_by_id**](ProductComponentsApi.md#put_procurement_products_by_parent_id_components_by_id) | **PUT** /procurement/products/{parentId}/components/{id} | Put List of ProductComponent


# **delete_procurement_products_by_parent_id_components_by_id**
> delete_procurement_products_by_parent_id_components_by_id(id, parent_id, client_id)

Delete ProductComponent

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
    api_instance = connectwise_psa.ProductComponentsApi(api_client)
    id = 56 # int | componentId
    parent_id = 56 # int | productId
    client_id = 'client_id_example' # str | 

    try:
        # Delete ProductComponent
        api_instance.delete_procurement_products_by_parent_id_components_by_id(id, parent_id, client_id)
    except Exception as e:
        print("Exception when calling ProductComponentsApi->delete_procurement_products_by_parent_id_components_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| componentId | 
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

# **get_procurement_products_by_parent_id_components**
> List[ProductComponent] get_procurement_products_by_parent_id_components(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of ProductComponent

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.product_component import ProductComponent
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
    api_instance = connectwise_psa.ProductComponentsApi(api_client)
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
        # Get List of ProductComponent
        api_response = api_instance.get_procurement_products_by_parent_id_components(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of ProductComponentsApi->get_procurement_products_by_parent_id_components:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductComponentsApi->get_procurement_products_by_parent_id_components: %s\n" % e)
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

[**List[ProductComponent]**](ProductComponent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of ProductComponent |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_procurement_products_by_parent_id_components_by_id**
> List[ProductComponent] get_procurement_products_by_parent_id_components_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of ProductComponent

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.product_component import ProductComponent
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
    api_instance = connectwise_psa.ProductComponentsApi(api_client)
    id = 56 # int | componentId
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
        # Get List of ProductComponent
        api_response = api_instance.get_procurement_products_by_parent_id_components_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of ProductComponentsApi->get_procurement_products_by_parent_id_components_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductComponentsApi->get_procurement_products_by_parent_id_components_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| componentId | 
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

[**List[ProductComponent]**](ProductComponent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of ProductComponent |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_procurement_products_by_parent_id_components_count**
> Count get_procurement_products_by_parent_id_components_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Count of ProductComponent

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
    api_instance = connectwise_psa.ProductComponentsApi(api_client)
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
        # Get Count of ProductComponent
        api_response = api_instance.get_procurement_products_by_parent_id_components_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of ProductComponentsApi->get_procurement_products_by_parent_id_components_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductComponentsApi->get_procurement_products_by_parent_id_components_count: %s\n" % e)
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

# **patch_procurement_products_by_parent_id_components_by_id**
> List[ProductComponent] patch_procurement_products_by_parent_id_components_by_id(id, parent_id, client_id, patch_operation)

Patch List of ProductComponent

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.patch_operation import PatchOperation
from connectwise_psa.models.product_component import ProductComponent
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
    api_instance = connectwise_psa.ProductComponentsApi(api_client)
    id = 56 # int | componentId
    parent_id = 56 # int | productId
    client_id = 'client_id_example' # str | 
    patch_operation = [connectwise_psa.PatchOperation()] # List[PatchOperation] | List of PatchOperation

    try:
        # Patch List of ProductComponent
        api_response = api_instance.patch_procurement_products_by_parent_id_components_by_id(id, parent_id, client_id, patch_operation)
        print("The response of ProductComponentsApi->patch_procurement_products_by_parent_id_components_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductComponentsApi->patch_procurement_products_by_parent_id_components_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| componentId | 
 **parent_id** | **int**| productId | 
 **client_id** | **str**|  | 
 **patch_operation** | [**List[PatchOperation]**](PatchOperation.md)| List of PatchOperation | 

### Return type

[**List[ProductComponent]**](ProductComponent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of ProductComponent |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_procurement_products_by_parent_id_components**
> List[ProductComponent] post_procurement_products_by_parent_id_components(parent_id, client_id, product_component)

Post List of ProductComponent

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.product_component import ProductComponent
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
    api_instance = connectwise_psa.ProductComponentsApi(api_client)
    parent_id = 56 # int | productId
    client_id = 'client_id_example' # str | 
    product_component = connectwise_psa.ProductComponent() # ProductComponent | productComponent

    try:
        # Post List of ProductComponent
        api_response = api_instance.post_procurement_products_by_parent_id_components(parent_id, client_id, product_component)
        print("The response of ProductComponentsApi->post_procurement_products_by_parent_id_components:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductComponentsApi->post_procurement_products_by_parent_id_components: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| productId | 
 **client_id** | **str**|  | 
 **product_component** | [**ProductComponent**](ProductComponent.md)| productComponent | 

### Return type

[**List[ProductComponent]**](ProductComponent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of ProductComponent |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_procurement_products_by_parent_id_components_by_id**
> List[ProductComponent] put_procurement_products_by_parent_id_components_by_id(id, parent_id, client_id, product_component)

Put List of ProductComponent

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.product_component import ProductComponent
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
    api_instance = connectwise_psa.ProductComponentsApi(api_client)
    id = 56 # int | componentId
    parent_id = 56 # int | productId
    client_id = 'client_id_example' # str | 
    product_component = connectwise_psa.ProductComponent() # ProductComponent | productComponent

    try:
        # Put List of ProductComponent
        api_response = api_instance.put_procurement_products_by_parent_id_components_by_id(id, parent_id, client_id, product_component)
        print("The response of ProductComponentsApi->put_procurement_products_by_parent_id_components_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductComponentsApi->put_procurement_products_by_parent_id_components_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| componentId | 
 **parent_id** | **int**| productId | 
 **client_id** | **str**|  | 
 **product_component** | [**ProductComponent**](ProductComponent.md)| productComponent | 

### Return type

[**List[ProductComponent]**](ProductComponent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of ProductComponent |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

