# connectwise_psa.KnowledgeBaseSubCategoriesApi

All URIs are relative to *https://aus-api.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_service_knowledge_base_sub_categories_by_id**](KnowledgeBaseSubCategoriesApi.md#delete_service_knowledge_base_sub_categories_by_id) | **DELETE** /service/knowledgeBaseSubCategories/{id} | Delete KnowledgeBaseSubCategory
[**get_service_knowledge_base_sub_categories**](KnowledgeBaseSubCategoriesApi.md#get_service_knowledge_base_sub_categories) | **GET** /service/knowledgeBaseSubCategories | Get List of KnowledgeBaseSubCategory
[**get_service_knowledge_base_sub_categories_by_id**](KnowledgeBaseSubCategoriesApi.md#get_service_knowledge_base_sub_categories_by_id) | **GET** /service/knowledgeBaseSubCategories/{id} | Get KnowledgeBaseSubCategory
[**get_service_knowledge_base_sub_categories_by_id_usages**](KnowledgeBaseSubCategoriesApi.md#get_service_knowledge_base_sub_categories_by_id_usages) | **GET** /service/knowledgeBaseSubCategories/{id}/usages | Get List of Usage Count
[**get_service_knowledge_base_sub_categories_by_id_usages_list**](KnowledgeBaseSubCategoriesApi.md#get_service_knowledge_base_sub_categories_by_id_usages_list) | **GET** /service/knowledgeBaseSubCategories/{id}/usages/list | Get List of Usage
[**get_service_knowledge_base_sub_categories_count**](KnowledgeBaseSubCategoriesApi.md#get_service_knowledge_base_sub_categories_count) | **GET** /service/knowledgeBaseSubCategories/count | Get Count of KnowledgeBaseSubCategory
[**patch_service_knowledge_base_sub_categories_by_id**](KnowledgeBaseSubCategoriesApi.md#patch_service_knowledge_base_sub_categories_by_id) | **PATCH** /service/knowledgeBaseSubCategories/{id} | Patch KnowledgeBaseSubCategory
[**post_service_knowledge_base_sub_categories**](KnowledgeBaseSubCategoriesApi.md#post_service_knowledge_base_sub_categories) | **POST** /service/knowledgeBaseSubCategories | Post KnowledgeBaseSubCategory
[**put_service_knowledge_base_sub_categories_by_id**](KnowledgeBaseSubCategoriesApi.md#put_service_knowledge_base_sub_categories_by_id) | **PUT** /service/knowledgeBaseSubCategories/{id} | Put KnowledgeBaseSubCategory


# **delete_service_knowledge_base_sub_categories_by_id**
> delete_service_knowledge_base_sub_categories_by_id(id, client_id)

Delete KnowledgeBaseSubCategory

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
    api_instance = connectwise_psa.KnowledgeBaseSubCategoriesApi(api_client)
    id = 56 # int | knowledgeBaseSubCategoryId
    client_id = 'client_id_example' # str | 

    try:
        # Delete KnowledgeBaseSubCategory
        api_instance.delete_service_knowledge_base_sub_categories_by_id(id, client_id)
    except Exception as e:
        print("Exception when calling KnowledgeBaseSubCategoriesApi->delete_service_knowledge_base_sub_categories_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| knowledgeBaseSubCategoryId | 
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

# **get_service_knowledge_base_sub_categories**
> List[KnowledgeBaseSubCategory] get_service_knowledge_base_sub_categories(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of KnowledgeBaseSubCategory

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.knowledge_base_sub_category import KnowledgeBaseSubCategory
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
    api_instance = connectwise_psa.KnowledgeBaseSubCategoriesApi(api_client)
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
        # Get List of KnowledgeBaseSubCategory
        api_response = api_instance.get_service_knowledge_base_sub_categories(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of KnowledgeBaseSubCategoriesApi->get_service_knowledge_base_sub_categories:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KnowledgeBaseSubCategoriesApi->get_service_knowledge_base_sub_categories: %s\n" % e)
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

[**List[KnowledgeBaseSubCategory]**](KnowledgeBaseSubCategory.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of KnowledgeBaseSubCategory |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_service_knowledge_base_sub_categories_by_id**
> KnowledgeBaseSubCategory get_service_knowledge_base_sub_categories_by_id(id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get KnowledgeBaseSubCategory

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.knowledge_base_sub_category import KnowledgeBaseSubCategory
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
    api_instance = connectwise_psa.KnowledgeBaseSubCategoriesApi(api_client)
    id = 56 # int | knowledgeBaseSubCategoryId
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
        # Get KnowledgeBaseSubCategory
        api_response = api_instance.get_service_knowledge_base_sub_categories_by_id(id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of KnowledgeBaseSubCategoriesApi->get_service_knowledge_base_sub_categories_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KnowledgeBaseSubCategoriesApi->get_service_knowledge_base_sub_categories_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| knowledgeBaseSubCategoryId | 
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

[**KnowledgeBaseSubCategory**](KnowledgeBaseSubCategory.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | KnowledgeBaseSubCategory |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_service_knowledge_base_sub_categories_by_id_usages**
> List[Usage] get_service_knowledge_base_sub_categories_by_id_usages(id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of Usage Count

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.usage import Usage
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
    api_instance = connectwise_psa.KnowledgeBaseSubCategoriesApi(api_client)
    id = 56 # int | knowledgeBaseSubCategoryId
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
        api_response = api_instance.get_service_knowledge_base_sub_categories_by_id_usages(id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of KnowledgeBaseSubCategoriesApi->get_service_knowledge_base_sub_categories_by_id_usages:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KnowledgeBaseSubCategoriesApi->get_service_knowledge_base_sub_categories_by_id_usages: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| knowledgeBaseSubCategoryId | 
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

# **get_service_knowledge_base_sub_categories_by_id_usages_list**
> List[Usage] get_service_knowledge_base_sub_categories_by_id_usages_list(id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of Usage

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.usage import Usage
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
    api_instance = connectwise_psa.KnowledgeBaseSubCategoriesApi(api_client)
    id = 56 # int | knowledgeBaseSubCategoryId
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
        api_response = api_instance.get_service_knowledge_base_sub_categories_by_id_usages_list(id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of KnowledgeBaseSubCategoriesApi->get_service_knowledge_base_sub_categories_by_id_usages_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KnowledgeBaseSubCategoriesApi->get_service_knowledge_base_sub_categories_by_id_usages_list: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| knowledgeBaseSubCategoryId | 
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

# **get_service_knowledge_base_sub_categories_count**
> Count get_service_knowledge_base_sub_categories_count(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Count of KnowledgeBaseSubCategory

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
    api_instance = connectwise_psa.KnowledgeBaseSubCategoriesApi(api_client)
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
        # Get Count of KnowledgeBaseSubCategory
        api_response = api_instance.get_service_knowledge_base_sub_categories_count(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of KnowledgeBaseSubCategoriesApi->get_service_knowledge_base_sub_categories_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KnowledgeBaseSubCategoriesApi->get_service_knowledge_base_sub_categories_count: %s\n" % e)
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

# **patch_service_knowledge_base_sub_categories_by_id**
> KnowledgeBaseSubCategory patch_service_knowledge_base_sub_categories_by_id(id, client_id, patch_operation)

Patch KnowledgeBaseSubCategory

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.knowledge_base_sub_category import KnowledgeBaseSubCategory
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
    api_instance = connectwise_psa.KnowledgeBaseSubCategoriesApi(api_client)
    id = 56 # int | knowledgeBaseSubCategoryId
    client_id = 'client_id_example' # str | 
    patch_operation = [connectwise_psa.PatchOperation()] # List[PatchOperation] | List of PatchOperation

    try:
        # Patch KnowledgeBaseSubCategory
        api_response = api_instance.patch_service_knowledge_base_sub_categories_by_id(id, client_id, patch_operation)
        print("The response of KnowledgeBaseSubCategoriesApi->patch_service_knowledge_base_sub_categories_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KnowledgeBaseSubCategoriesApi->patch_service_knowledge_base_sub_categories_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| knowledgeBaseSubCategoryId | 
 **client_id** | **str**|  | 
 **patch_operation** | [**List[PatchOperation]**](PatchOperation.md)| List of PatchOperation | 

### Return type

[**KnowledgeBaseSubCategory**](KnowledgeBaseSubCategory.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | KnowledgeBaseSubCategory |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_service_knowledge_base_sub_categories**
> KnowledgeBaseSubCategory post_service_knowledge_base_sub_categories(client_id, knowledge_base_sub_category)

Post KnowledgeBaseSubCategory

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.knowledge_base_sub_category import KnowledgeBaseSubCategory
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
    api_instance = connectwise_psa.KnowledgeBaseSubCategoriesApi(api_client)
    client_id = 'client_id_example' # str | 
    knowledge_base_sub_category = connectwise_psa.KnowledgeBaseSubCategory() # KnowledgeBaseSubCategory | knowledgeBaseSubCategory

    try:
        # Post KnowledgeBaseSubCategory
        api_response = api_instance.post_service_knowledge_base_sub_categories(client_id, knowledge_base_sub_category)
        print("The response of KnowledgeBaseSubCategoriesApi->post_service_knowledge_base_sub_categories:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KnowledgeBaseSubCategoriesApi->post_service_knowledge_base_sub_categories: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**|  | 
 **knowledge_base_sub_category** | [**KnowledgeBaseSubCategory**](KnowledgeBaseSubCategory.md)| knowledgeBaseSubCategory | 

### Return type

[**KnowledgeBaseSubCategory**](KnowledgeBaseSubCategory.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | KnowledgeBaseSubCategory |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_service_knowledge_base_sub_categories_by_id**
> KnowledgeBaseSubCategory put_service_knowledge_base_sub_categories_by_id(id, client_id, knowledge_base_sub_category)

Put KnowledgeBaseSubCategory

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.knowledge_base_sub_category import KnowledgeBaseSubCategory
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
    api_instance = connectwise_psa.KnowledgeBaseSubCategoriesApi(api_client)
    id = 56 # int | knowledgeBaseSubCategoryId
    client_id = 'client_id_example' # str | 
    knowledge_base_sub_category = connectwise_psa.KnowledgeBaseSubCategory() # KnowledgeBaseSubCategory | knowledgeBaseSubCategory

    try:
        # Put KnowledgeBaseSubCategory
        api_response = api_instance.put_service_knowledge_base_sub_categories_by_id(id, client_id, knowledge_base_sub_category)
        print("The response of KnowledgeBaseSubCategoriesApi->put_service_knowledge_base_sub_categories_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KnowledgeBaseSubCategoriesApi->put_service_knowledge_base_sub_categories_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| knowledgeBaseSubCategoryId | 
 **client_id** | **str**|  | 
 **knowledge_base_sub_category** | [**KnowledgeBaseSubCategory**](KnowledgeBaseSubCategory.md)| knowledgeBaseSubCategory | 

### Return type

[**KnowledgeBaseSubCategory**](KnowledgeBaseSubCategory.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | KnowledgeBaseSubCategory |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

