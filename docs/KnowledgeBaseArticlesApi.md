# connectwise_psa.KnowledgeBaseArticlesApi

All URIs are relative to *https://aus-api.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_service_knowledge_base_articles_by_id**](KnowledgeBaseArticlesApi.md#delete_service_knowledge_base_articles_by_id) | **DELETE** /service/knowledgeBaseArticles/{id} | Delete KnowledgeBaseArticle
[**get_service_knowledge_base_articles**](KnowledgeBaseArticlesApi.md#get_service_knowledge_base_articles) | **GET** /service/knowledgeBaseArticles | Get List of KnowledgeBaseArticle
[**get_service_knowledge_base_articles_by_id**](KnowledgeBaseArticlesApi.md#get_service_knowledge_base_articles_by_id) | **GET** /service/knowledgeBaseArticles/{id} | Get KnowledgeBaseArticle
[**get_service_knowledge_base_articles_count**](KnowledgeBaseArticlesApi.md#get_service_knowledge_base_articles_count) | **GET** /service/knowledgeBaseArticles/count | Get Count of KnowledgeBaseArticle
[**patch_service_knowledge_base_articles_by_id**](KnowledgeBaseArticlesApi.md#patch_service_knowledge_base_articles_by_id) | **PATCH** /service/knowledgeBaseArticles/{id} | Patch KnowledgeBaseArticle
[**post_service_knowledge_base_articles**](KnowledgeBaseArticlesApi.md#post_service_knowledge_base_articles) | **POST** /service/knowledgeBaseArticles | Post KnowledgeBaseArticle
[**put_service_knowledge_base_articles_by_id**](KnowledgeBaseArticlesApi.md#put_service_knowledge_base_articles_by_id) | **PUT** /service/knowledgeBaseArticles/{id} | Put KnowledgeBaseArticle


# **delete_service_knowledge_base_articles_by_id**
> delete_service_knowledge_base_articles_by_id(id, client_id)

Delete KnowledgeBaseArticle

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
    api_instance = connectwise_psa.KnowledgeBaseArticlesApi(api_client)
    id = 56 # int | knowledgeBaseArticleId
    client_id = 'client_id_example' # str | 

    try:
        # Delete KnowledgeBaseArticle
        api_instance.delete_service_knowledge_base_articles_by_id(id, client_id)
    except Exception as e:
        print("Exception when calling KnowledgeBaseArticlesApi->delete_service_knowledge_base_articles_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| knowledgeBaseArticleId | 
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

# **get_service_knowledge_base_articles**
> List[KnowledgeBaseArticle] get_service_knowledge_base_articles(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of KnowledgeBaseArticle

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.knowledge_base_article import KnowledgeBaseArticle
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
    api_instance = connectwise_psa.KnowledgeBaseArticlesApi(api_client)
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
        # Get List of KnowledgeBaseArticle
        api_response = api_instance.get_service_knowledge_base_articles(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of KnowledgeBaseArticlesApi->get_service_knowledge_base_articles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KnowledgeBaseArticlesApi->get_service_knowledge_base_articles: %s\n" % e)
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

[**List[KnowledgeBaseArticle]**](KnowledgeBaseArticle.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of KnowledgeBaseArticle |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_service_knowledge_base_articles_by_id**
> KnowledgeBaseArticle get_service_knowledge_base_articles_by_id(id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get KnowledgeBaseArticle

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.knowledge_base_article import KnowledgeBaseArticle
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
    api_instance = connectwise_psa.KnowledgeBaseArticlesApi(api_client)
    id = 56 # int | knowledgeBaseArticleId
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
        # Get KnowledgeBaseArticle
        api_response = api_instance.get_service_knowledge_base_articles_by_id(id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of KnowledgeBaseArticlesApi->get_service_knowledge_base_articles_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KnowledgeBaseArticlesApi->get_service_knowledge_base_articles_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| knowledgeBaseArticleId | 
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

[**KnowledgeBaseArticle**](KnowledgeBaseArticle.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | KnowledgeBaseArticle |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_service_knowledge_base_articles_count**
> Count get_service_knowledge_base_articles_count(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Count of KnowledgeBaseArticle

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
    api_instance = connectwise_psa.KnowledgeBaseArticlesApi(api_client)
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
        # Get Count of KnowledgeBaseArticle
        api_response = api_instance.get_service_knowledge_base_articles_count(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of KnowledgeBaseArticlesApi->get_service_knowledge_base_articles_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KnowledgeBaseArticlesApi->get_service_knowledge_base_articles_count: %s\n" % e)
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

# **patch_service_knowledge_base_articles_by_id**
> KnowledgeBaseArticle patch_service_knowledge_base_articles_by_id(id, client_id, patch_operation)

Patch KnowledgeBaseArticle

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.knowledge_base_article import KnowledgeBaseArticle
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
    api_instance = connectwise_psa.KnowledgeBaseArticlesApi(api_client)
    id = 56 # int | knowledgeBaseArticleId
    client_id = 'client_id_example' # str | 
    patch_operation = [connectwise_psa.PatchOperation()] # List[PatchOperation] | List of PatchOperation

    try:
        # Patch KnowledgeBaseArticle
        api_response = api_instance.patch_service_knowledge_base_articles_by_id(id, client_id, patch_operation)
        print("The response of KnowledgeBaseArticlesApi->patch_service_knowledge_base_articles_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KnowledgeBaseArticlesApi->patch_service_knowledge_base_articles_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| knowledgeBaseArticleId | 
 **client_id** | **str**|  | 
 **patch_operation** | [**List[PatchOperation]**](PatchOperation.md)| List of PatchOperation | 

### Return type

[**KnowledgeBaseArticle**](KnowledgeBaseArticle.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | KnowledgeBaseArticle |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_service_knowledge_base_articles**
> KnowledgeBaseArticle post_service_knowledge_base_articles(client_id, knowledge_base_article)

Post KnowledgeBaseArticle

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.knowledge_base_article import KnowledgeBaseArticle
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
    api_instance = connectwise_psa.KnowledgeBaseArticlesApi(api_client)
    client_id = 'client_id_example' # str | 
    knowledge_base_article = connectwise_psa.KnowledgeBaseArticle() # KnowledgeBaseArticle | knowledgeBaseArticle

    try:
        # Post KnowledgeBaseArticle
        api_response = api_instance.post_service_knowledge_base_articles(client_id, knowledge_base_article)
        print("The response of KnowledgeBaseArticlesApi->post_service_knowledge_base_articles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KnowledgeBaseArticlesApi->post_service_knowledge_base_articles: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**|  | 
 **knowledge_base_article** | [**KnowledgeBaseArticle**](KnowledgeBaseArticle.md)| knowledgeBaseArticle | 

### Return type

[**KnowledgeBaseArticle**](KnowledgeBaseArticle.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | KnowledgeBaseArticle |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_service_knowledge_base_articles_by_id**
> KnowledgeBaseArticle put_service_knowledge_base_articles_by_id(id, client_id, knowledge_base_article)

Put KnowledgeBaseArticle

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.knowledge_base_article import KnowledgeBaseArticle
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
    api_instance = connectwise_psa.KnowledgeBaseArticlesApi(api_client)
    id = 56 # int | knowledgeBaseArticleId
    client_id = 'client_id_example' # str | 
    knowledge_base_article = connectwise_psa.KnowledgeBaseArticle() # KnowledgeBaseArticle | knowledgeBaseArticle

    try:
        # Put KnowledgeBaseArticle
        api_response = api_instance.put_service_knowledge_base_articles_by_id(id, client_id, knowledge_base_article)
        print("The response of KnowledgeBaseArticlesApi->put_service_knowledge_base_articles_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KnowledgeBaseArticlesApi->put_service_knowledge_base_articles_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| knowledgeBaseArticleId | 
 **client_id** | **str**|  | 
 **knowledge_base_article** | [**KnowledgeBaseArticle**](KnowledgeBaseArticle.md)| knowledgeBaseArticle | 

### Return type

[**KnowledgeBaseArticle**](KnowledgeBaseArticle.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | KnowledgeBaseArticle |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

