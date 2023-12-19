# connectwise_psa.CatalogComponentsApi

All URIs are relative to *https://aus-api.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_procurement_catalog_by_parent_id_components_by_id**](CatalogComponentsApi.md#delete_procurement_catalog_by_parent_id_components_by_id) | **DELETE** /procurement/catalog/{parentId}/components/{id} | Delete CatalogComponent
[**get_procurement_catalog_by_parent_id_components**](CatalogComponentsApi.md#get_procurement_catalog_by_parent_id_components) | **GET** /procurement/catalog/{parentId}/components | Get List of CatalogComponent
[**get_procurement_catalog_by_parent_id_components_by_id**](CatalogComponentsApi.md#get_procurement_catalog_by_parent_id_components_by_id) | **GET** /procurement/catalog/{parentId}/components/{id} | Get CatalogComponent
[**get_procurement_catalog_by_parent_id_components_count**](CatalogComponentsApi.md#get_procurement_catalog_by_parent_id_components_count) | **GET** /procurement/catalog/{parentId}/components/count | Get Count of CatalogComponent
[**patch_procurement_catalog_by_parent_id_components_by_id**](CatalogComponentsApi.md#patch_procurement_catalog_by_parent_id_components_by_id) | **PATCH** /procurement/catalog/{parentId}/components/{id} | Patch CatalogComponent
[**post_procurement_catalog_by_parent_id_components**](CatalogComponentsApi.md#post_procurement_catalog_by_parent_id_components) | **POST** /procurement/catalog/{parentId}/components | Post CatalogComponent
[**put_procurement_catalog_by_parent_id_components_by_id**](CatalogComponentsApi.md#put_procurement_catalog_by_parent_id_components_by_id) | **PUT** /procurement/catalog/{parentId}/components/{id} | Put CatalogComponent


# **delete_procurement_catalog_by_parent_id_components_by_id**
> delete_procurement_catalog_by_parent_id_components_by_id(id, parent_id, client_id)

Delete CatalogComponent

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
    api_instance = connectwise_psa.CatalogComponentsApi(api_client)
    id = 56 # int | componentId
    parent_id = 56 # int | catalogId
    client_id = 'client_id_example' # str | 

    try:
        # Delete CatalogComponent
        api_instance.delete_procurement_catalog_by_parent_id_components_by_id(id, parent_id, client_id)
    except Exception as e:
        print("Exception when calling CatalogComponentsApi->delete_procurement_catalog_by_parent_id_components_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| componentId | 
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

# **get_procurement_catalog_by_parent_id_components**
> List[CatalogComponent] get_procurement_catalog_by_parent_id_components(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of CatalogComponent

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.catalog_component import CatalogComponent
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
    api_instance = connectwise_psa.CatalogComponentsApi(api_client)
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
        # Get List of CatalogComponent
        api_response = api_instance.get_procurement_catalog_by_parent_id_components(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of CatalogComponentsApi->get_procurement_catalog_by_parent_id_components:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CatalogComponentsApi->get_procurement_catalog_by_parent_id_components: %s\n" % e)
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

[**List[CatalogComponent]**](CatalogComponent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of CatalogComponent |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_procurement_catalog_by_parent_id_components_by_id**
> CatalogComponent get_procurement_catalog_by_parent_id_components_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get CatalogComponent

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.catalog_component import CatalogComponent
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
    api_instance = connectwise_psa.CatalogComponentsApi(api_client)
    id = 56 # int | componentId
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
        # Get CatalogComponent
        api_response = api_instance.get_procurement_catalog_by_parent_id_components_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of CatalogComponentsApi->get_procurement_catalog_by_parent_id_components_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CatalogComponentsApi->get_procurement_catalog_by_parent_id_components_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| componentId | 
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

[**CatalogComponent**](CatalogComponent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | CatalogComponent |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_procurement_catalog_by_parent_id_components_count**
> Count get_procurement_catalog_by_parent_id_components_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Count of CatalogComponent

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
    api_instance = connectwise_psa.CatalogComponentsApi(api_client)
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
        # Get Count of CatalogComponent
        api_response = api_instance.get_procurement_catalog_by_parent_id_components_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of CatalogComponentsApi->get_procurement_catalog_by_parent_id_components_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CatalogComponentsApi->get_procurement_catalog_by_parent_id_components_count: %s\n" % e)
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

# **patch_procurement_catalog_by_parent_id_components_by_id**
> CatalogComponent patch_procurement_catalog_by_parent_id_components_by_id(id, parent_id, client_id, patch_operation)

Patch CatalogComponent

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.catalog_component import CatalogComponent
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
    api_instance = connectwise_psa.CatalogComponentsApi(api_client)
    id = 56 # int | componentId
    parent_id = 56 # int | catalogId
    client_id = 'client_id_example' # str | 
    patch_operation = [connectwise_psa.PatchOperation()] # List[PatchOperation] | List of PatchOperation

    try:
        # Patch CatalogComponent
        api_response = api_instance.patch_procurement_catalog_by_parent_id_components_by_id(id, parent_id, client_id, patch_operation)
        print("The response of CatalogComponentsApi->patch_procurement_catalog_by_parent_id_components_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CatalogComponentsApi->patch_procurement_catalog_by_parent_id_components_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| componentId | 
 **parent_id** | **int**| catalogId | 
 **client_id** | **str**|  | 
 **patch_operation** | [**List[PatchOperation]**](PatchOperation.md)| List of PatchOperation | 

### Return type

[**CatalogComponent**](CatalogComponent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | CatalogComponent |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_procurement_catalog_by_parent_id_components**
> CatalogComponent post_procurement_catalog_by_parent_id_components(parent_id, client_id, catalog_component)

Post CatalogComponent

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.catalog_component import CatalogComponent
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
    api_instance = connectwise_psa.CatalogComponentsApi(api_client)
    parent_id = 56 # int | catalogId
    client_id = 'client_id_example' # str | 
    catalog_component = connectwise_psa.CatalogComponent() # CatalogComponent | catalogComponent

    try:
        # Post CatalogComponent
        api_response = api_instance.post_procurement_catalog_by_parent_id_components(parent_id, client_id, catalog_component)
        print("The response of CatalogComponentsApi->post_procurement_catalog_by_parent_id_components:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CatalogComponentsApi->post_procurement_catalog_by_parent_id_components: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| catalogId | 
 **client_id** | **str**|  | 
 **catalog_component** | [**CatalogComponent**](CatalogComponent.md)| catalogComponent | 

### Return type

[**CatalogComponent**](CatalogComponent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | CatalogComponent |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_procurement_catalog_by_parent_id_components_by_id**
> CatalogComponent put_procurement_catalog_by_parent_id_components_by_id(id, parent_id, client_id, catalog_component)

Put CatalogComponent

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.catalog_component import CatalogComponent
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
    api_instance = connectwise_psa.CatalogComponentsApi(api_client)
    id = 56 # int | componentId
    parent_id = 56 # int | catalogId
    client_id = 'client_id_example' # str | 
    catalog_component = connectwise_psa.CatalogComponent() # CatalogComponent | catalogComponent

    try:
        # Put CatalogComponent
        api_response = api_instance.put_procurement_catalog_by_parent_id_components_by_id(id, parent_id, client_id, catalog_component)
        print("The response of CatalogComponentsApi->put_procurement_catalog_by_parent_id_components_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CatalogComponentsApi->put_procurement_catalog_by_parent_id_components_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| componentId | 
 **parent_id** | **int**| catalogId | 
 **client_id** | **str**|  | 
 **catalog_component** | [**CatalogComponent**](CatalogComponent.md)| catalogComponent | 

### Return type

[**CatalogComponent**](CatalogComponent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | CatalogComponent |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

