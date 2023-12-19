# connectwise_psa.LegacySubCategoriesApi

All URIs are relative to *https://api-aus.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_procurement_categories_by_parent_id_subcategories_by_id**](LegacySubCategoriesApi.md#delete_procurement_categories_by_parent_id_subcategories_by_id) | **DELETE** /procurement/categories/{parentId}/subcategories/{id} | Delete LegacySubCategory
[**get_procurement_categories_by_parent_id_subcategories**](LegacySubCategoriesApi.md#get_procurement_categories_by_parent_id_subcategories) | **GET** /procurement/categories/{parentId}/subcategories/ | Get List of LegacySubCategory
[**get_procurement_categories_by_parent_id_subcategories_by_id**](LegacySubCategoriesApi.md#get_procurement_categories_by_parent_id_subcategories_by_id) | **GET** /procurement/categories/{parentId}/subcategories/{id} | Get LegacySubCategory
[**get_procurement_categories_by_parent_id_subcategories_count**](LegacySubCategoriesApi.md#get_procurement_categories_by_parent_id_subcategories_count) | **GET** /procurement/categories/{parentId}/subcategories/count | Get Count of LegacySubCategory
[**patch_procurement_categories_by_parent_id_subcategories_by_id**](LegacySubCategoriesApi.md#patch_procurement_categories_by_parent_id_subcategories_by_id) | **PATCH** /procurement/categories/{parentId}/subcategories/{id} | Patch LegacySubCategory
[**post_procurement_categories_by_parent_id_subcategories**](LegacySubCategoriesApi.md#post_procurement_categories_by_parent_id_subcategories) | **POST** /procurement/categories/{parentId}/subcategories/ | Post LegacySubCategory
[**put_procurement_categories_by_parent_id_subcategories_by_id**](LegacySubCategoriesApi.md#put_procurement_categories_by_parent_id_subcategories_by_id) | **PUT** /procurement/categories/{parentId}/subcategories/{id} | Put LegacySubCategory


# **delete_procurement_categories_by_parent_id_subcategories_by_id**
> delete_procurement_categories_by_parent_id_subcategories_by_id(id, parent_id, client_id)

Delete LegacySubCategory

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
    api_instance = connectwise_psa.LegacySubCategoriesApi(api_client)
    id = 56 # int | subcategoryId
    parent_id = 56 # int | categoryId
    client_id = 'client_id_example' # str | 

    try:
        # Delete LegacySubCategory
        api_instance.delete_procurement_categories_by_parent_id_subcategories_by_id(id, parent_id, client_id)
    except Exception as e:
        print("Exception when calling LegacySubCategoriesApi->delete_procurement_categories_by_parent_id_subcategories_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| subcategoryId | 
 **parent_id** | **int**| categoryId | 
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

# **get_procurement_categories_by_parent_id_subcategories**
> List[LegacySubCategory] get_procurement_categories_by_parent_id_subcategories(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of LegacySubCategory

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.legacy_sub_category import LegacySubCategory
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
    api_instance = connectwise_psa.LegacySubCategoriesApi(api_client)
    parent_id = 56 # int | categoryId
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
        # Get List of LegacySubCategory
        api_response = api_instance.get_procurement_categories_by_parent_id_subcategories(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of LegacySubCategoriesApi->get_procurement_categories_by_parent_id_subcategories:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LegacySubCategoriesApi->get_procurement_categories_by_parent_id_subcategories: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| categoryId | 
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

[**List[LegacySubCategory]**](LegacySubCategory.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of LegacySubCategory |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_procurement_categories_by_parent_id_subcategories_by_id**
> LegacySubCategory get_procurement_categories_by_parent_id_subcategories_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get LegacySubCategory

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.legacy_sub_category import LegacySubCategory
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
    api_instance = connectwise_psa.LegacySubCategoriesApi(api_client)
    id = 56 # int | subcategoryId
    parent_id = 56 # int | categoryId
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
        # Get LegacySubCategory
        api_response = api_instance.get_procurement_categories_by_parent_id_subcategories_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of LegacySubCategoriesApi->get_procurement_categories_by_parent_id_subcategories_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LegacySubCategoriesApi->get_procurement_categories_by_parent_id_subcategories_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| subcategoryId | 
 **parent_id** | **int**| categoryId | 
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

[**LegacySubCategory**](LegacySubCategory.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | LegacySubCategory |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_procurement_categories_by_parent_id_subcategories_count**
> Count get_procurement_categories_by_parent_id_subcategories_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Count of LegacySubCategory

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
    api_instance = connectwise_psa.LegacySubCategoriesApi(api_client)
    parent_id = 56 # int | categoryId
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
        # Get Count of LegacySubCategory
        api_response = api_instance.get_procurement_categories_by_parent_id_subcategories_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of LegacySubCategoriesApi->get_procurement_categories_by_parent_id_subcategories_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LegacySubCategoriesApi->get_procurement_categories_by_parent_id_subcategories_count: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| categoryId | 
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

# **patch_procurement_categories_by_parent_id_subcategories_by_id**
> LegacySubCategory patch_procurement_categories_by_parent_id_subcategories_by_id(id, parent_id, client_id, patch_operation)

Patch LegacySubCategory

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.legacy_sub_category import LegacySubCategory
from connectwise_psa.models.patch_operation import PatchOperation
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
    api_instance = connectwise_psa.LegacySubCategoriesApi(api_client)
    id = 56 # int | subcategoryId
    parent_id = 56 # int | categoryId
    client_id = 'client_id_example' # str | 
    patch_operation = [connectwise_psa.PatchOperation()] # List[PatchOperation] | List of PatchOperation

    try:
        # Patch LegacySubCategory
        api_response = api_instance.patch_procurement_categories_by_parent_id_subcategories_by_id(id, parent_id, client_id, patch_operation)
        print("The response of LegacySubCategoriesApi->patch_procurement_categories_by_parent_id_subcategories_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LegacySubCategoriesApi->patch_procurement_categories_by_parent_id_subcategories_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| subcategoryId | 
 **parent_id** | **int**| categoryId | 
 **client_id** | **str**|  | 
 **patch_operation** | [**List[PatchOperation]**](PatchOperation.md)| List of PatchOperation | 

### Return type

[**LegacySubCategory**](LegacySubCategory.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | LegacySubCategory |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_procurement_categories_by_parent_id_subcategories**
> LegacySubCategory post_procurement_categories_by_parent_id_subcategories(parent_id, client_id, legacy_sub_category)

Post LegacySubCategory

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.legacy_sub_category import LegacySubCategory
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
    api_instance = connectwise_psa.LegacySubCategoriesApi(api_client)
    parent_id = 56 # int | categoryId
    client_id = 'client_id_example' # str | 
    legacy_sub_category = connectwise_psa.LegacySubCategory() # LegacySubCategory | subCategory

    try:
        # Post LegacySubCategory
        api_response = api_instance.post_procurement_categories_by_parent_id_subcategories(parent_id, client_id, legacy_sub_category)
        print("The response of LegacySubCategoriesApi->post_procurement_categories_by_parent_id_subcategories:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LegacySubCategoriesApi->post_procurement_categories_by_parent_id_subcategories: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| categoryId | 
 **client_id** | **str**|  | 
 **legacy_sub_category** | [**LegacySubCategory**](LegacySubCategory.md)| subCategory | 

### Return type

[**LegacySubCategory**](LegacySubCategory.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | LegacySubCategory |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_procurement_categories_by_parent_id_subcategories_by_id**
> LegacySubCategory put_procurement_categories_by_parent_id_subcategories_by_id(id, parent_id, client_id, legacy_sub_category)

Put LegacySubCategory

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.legacy_sub_category import LegacySubCategory
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
    api_instance = connectwise_psa.LegacySubCategoriesApi(api_client)
    id = 56 # int | subcategoryId
    parent_id = 56 # int | categoryId
    client_id = 'client_id_example' # str | 
    legacy_sub_category = connectwise_psa.LegacySubCategory() # LegacySubCategory | subCategory

    try:
        # Put LegacySubCategory
        api_response = api_instance.put_procurement_categories_by_parent_id_subcategories_by_id(id, parent_id, client_id, legacy_sub_category)
        print("The response of LegacySubCategoriesApi->put_procurement_categories_by_parent_id_subcategories_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LegacySubCategoriesApi->put_procurement_categories_by_parent_id_subcategories_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| subcategoryId | 
 **parent_id** | **int**| categoryId | 
 **client_id** | **str**|  | 
 **legacy_sub_category** | [**LegacySubCategory**](LegacySubCategory.md)| subCategory | 

### Return type

[**LegacySubCategory**](LegacySubCategory.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | LegacySubCategory |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

