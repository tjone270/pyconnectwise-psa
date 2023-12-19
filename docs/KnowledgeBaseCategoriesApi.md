# connectwise_psa.KnowledgeBaseCategoriesApi

All URIs are relative to *https://aus-api.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_service_knowledge_base_categories_by_id**](KnowledgeBaseCategoriesApi.md#delete_service_knowledge_base_categories_by_id) | **DELETE** /service/knowledgeBaseCategories/{id} | Delete KnowledgeBaseCategory
[**get_service_knowledge_base_categories**](KnowledgeBaseCategoriesApi.md#get_service_knowledge_base_categories) | **GET** /service/knowledgeBaseCategories | Get List of KnowledgeBaseCategory
[**get_service_knowledge_base_categories_by_id**](KnowledgeBaseCategoriesApi.md#get_service_knowledge_base_categories_by_id) | **GET** /service/knowledgeBaseCategories/{id} | Get KnowledgeBaseCategory
[**get_service_knowledge_base_categories_count**](KnowledgeBaseCategoriesApi.md#get_service_knowledge_base_categories_count) | **GET** /service/knowledgeBaseCategories/count | Get Count of KnowledgeBaseCategory
[**patch_service_knowledge_base_categories_by_id**](KnowledgeBaseCategoriesApi.md#patch_service_knowledge_base_categories_by_id) | **PATCH** /service/knowledgeBaseCategories/{id} | Patch KnowledgeBaseCategory
[**post_service_knowledge_base_categories**](KnowledgeBaseCategoriesApi.md#post_service_knowledge_base_categories) | **POST** /service/knowledgeBaseCategories | Post KnowledgeBaseCategory
[**put_service_knowledge_base_categories_by_id**](KnowledgeBaseCategoriesApi.md#put_service_knowledge_base_categories_by_id) | **PUT** /service/knowledgeBaseCategories/{id} | Put KnowledgeBaseCategory


# **delete_service_knowledge_base_categories_by_id**
> delete_service_knowledge_base_categories_by_id(id, client_id)

Delete KnowledgeBaseCategory

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
    api_instance = connectwise_psa.KnowledgeBaseCategoriesApi(api_client)
    id = 56 # int | knowledgeBaseCategoryId
    client_id = 'client_id_example' # str | 

    try:
        # Delete KnowledgeBaseCategory
        api_instance.delete_service_knowledge_base_categories_by_id(id, client_id)
    except Exception as e:
        print("Exception when calling KnowledgeBaseCategoriesApi->delete_service_knowledge_base_categories_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| knowledgeBaseCategoryId | 
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

# **get_service_knowledge_base_categories**
> List[KnowledgeBaseCategory] get_service_knowledge_base_categories(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of KnowledgeBaseCategory

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.knowledge_base_category import KnowledgeBaseCategory
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
    api_instance = connectwise_psa.KnowledgeBaseCategoriesApi(api_client)
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
        # Get List of KnowledgeBaseCategory
        api_response = api_instance.get_service_knowledge_base_categories(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of KnowledgeBaseCategoriesApi->get_service_knowledge_base_categories:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KnowledgeBaseCategoriesApi->get_service_knowledge_base_categories: %s\n" % e)
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

[**List[KnowledgeBaseCategory]**](KnowledgeBaseCategory.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of KnowledgeBaseCategory |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_service_knowledge_base_categories_by_id**
> KnowledgeBaseCategory get_service_knowledge_base_categories_by_id(id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get KnowledgeBaseCategory

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.knowledge_base_category import KnowledgeBaseCategory
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
    api_instance = connectwise_psa.KnowledgeBaseCategoriesApi(api_client)
    id = 56 # int | knowledgeBaseCategoryId
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
        # Get KnowledgeBaseCategory
        api_response = api_instance.get_service_knowledge_base_categories_by_id(id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of KnowledgeBaseCategoriesApi->get_service_knowledge_base_categories_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KnowledgeBaseCategoriesApi->get_service_knowledge_base_categories_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| knowledgeBaseCategoryId | 
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

[**KnowledgeBaseCategory**](KnowledgeBaseCategory.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | KnowledgeBaseCategory |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_service_knowledge_base_categories_count**
> Count get_service_knowledge_base_categories_count(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Count of KnowledgeBaseCategory

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
    api_instance = connectwise_psa.KnowledgeBaseCategoriesApi(api_client)
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
        # Get Count of KnowledgeBaseCategory
        api_response = api_instance.get_service_knowledge_base_categories_count(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of KnowledgeBaseCategoriesApi->get_service_knowledge_base_categories_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KnowledgeBaseCategoriesApi->get_service_knowledge_base_categories_count: %s\n" % e)
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

# **patch_service_knowledge_base_categories_by_id**
> KnowledgeBaseCategory patch_service_knowledge_base_categories_by_id(id, client_id, patch_operation)

Patch KnowledgeBaseCategory

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.knowledge_base_category import KnowledgeBaseCategory
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
    api_instance = connectwise_psa.KnowledgeBaseCategoriesApi(api_client)
    id = 56 # int | knowledgeBaseCategoryId
    client_id = 'client_id_example' # str | 
    patch_operation = [connectwise_psa.PatchOperation()] # List[PatchOperation] | List of PatchOperation

    try:
        # Patch KnowledgeBaseCategory
        api_response = api_instance.patch_service_knowledge_base_categories_by_id(id, client_id, patch_operation)
        print("The response of KnowledgeBaseCategoriesApi->patch_service_knowledge_base_categories_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KnowledgeBaseCategoriesApi->patch_service_knowledge_base_categories_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| knowledgeBaseCategoryId | 
 **client_id** | **str**|  | 
 **patch_operation** | [**List[PatchOperation]**](PatchOperation.md)| List of PatchOperation | 

### Return type

[**KnowledgeBaseCategory**](KnowledgeBaseCategory.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | KnowledgeBaseCategory |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_service_knowledge_base_categories**
> KnowledgeBaseCategory post_service_knowledge_base_categories(client_id, knowledge_base_category)

Post KnowledgeBaseCategory

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.knowledge_base_category import KnowledgeBaseCategory
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
    api_instance = connectwise_psa.KnowledgeBaseCategoriesApi(api_client)
    client_id = 'client_id_example' # str | 
    knowledge_base_category = connectwise_psa.KnowledgeBaseCategory() # KnowledgeBaseCategory | knowledgeBaseCategory

    try:
        # Post KnowledgeBaseCategory
        api_response = api_instance.post_service_knowledge_base_categories(client_id, knowledge_base_category)
        print("The response of KnowledgeBaseCategoriesApi->post_service_knowledge_base_categories:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KnowledgeBaseCategoriesApi->post_service_knowledge_base_categories: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**|  | 
 **knowledge_base_category** | [**KnowledgeBaseCategory**](KnowledgeBaseCategory.md)| knowledgeBaseCategory | 

### Return type

[**KnowledgeBaseCategory**](KnowledgeBaseCategory.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | KnowledgeBaseCategory |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_service_knowledge_base_categories_by_id**
> KnowledgeBaseCategory put_service_knowledge_base_categories_by_id(id, client_id, knowledge_base_category)

Put KnowledgeBaseCategory

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.knowledge_base_category import KnowledgeBaseCategory
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
    api_instance = connectwise_psa.KnowledgeBaseCategoriesApi(api_client)
    id = 56 # int | knowledgeBaseCategoryId
    client_id = 'client_id_example' # str | 
    knowledge_base_category = connectwise_psa.KnowledgeBaseCategory() # KnowledgeBaseCategory | knowledgeBaseCategory

    try:
        # Put KnowledgeBaseCategory
        api_response = api_instance.put_service_knowledge_base_categories_by_id(id, client_id, knowledge_base_category)
        print("The response of KnowledgeBaseCategoriesApi->put_service_knowledge_base_categories_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KnowledgeBaseCategoriesApi->put_service_knowledge_base_categories_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| knowledgeBaseCategoryId | 
 **client_id** | **str**|  | 
 **knowledge_base_category** | [**KnowledgeBaseCategory**](KnowledgeBaseCategory.md)| knowledgeBaseCategory | 

### Return type

[**KnowledgeBaseCategory**](KnowledgeBaseCategory.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | KnowledgeBaseCategory |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

