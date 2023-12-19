# connectwise_psa.BoardAutoTemplatesApi

All URIs are relative to *https://aus-api.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_service_boards_by_parent_id_auto_templates_by_id**](BoardAutoTemplatesApi.md#delete_service_boards_by_parent_id_auto_templates_by_id) | **DELETE** /service/boards/{parentId}/autoTemplates/{id} | Delete BoardAutoTemplate
[**get_service_boards_by_parent_id_auto_templates**](BoardAutoTemplatesApi.md#get_service_boards_by_parent_id_auto_templates) | **GET** /service/boards/{parentId}/autoTemplates | Get List of BoardAutoTemplate
[**get_service_boards_by_parent_id_auto_templates_by_id**](BoardAutoTemplatesApi.md#get_service_boards_by_parent_id_auto_templates_by_id) | **GET** /service/boards/{parentId}/autoTemplates/{id} | Get BoardAutoTemplate
[**get_service_boards_by_parent_id_auto_templates_count**](BoardAutoTemplatesApi.md#get_service_boards_by_parent_id_auto_templates_count) | **GET** /service/boards/{parentId}/autoTemplates/count | Get Count of BoardAutoTemplate
[**patch_service_boards_by_parent_id_auto_templates_by_id**](BoardAutoTemplatesApi.md#patch_service_boards_by_parent_id_auto_templates_by_id) | **PATCH** /service/boards/{parentId}/autoTemplates/{id} | Patch BoardAutoTemplate
[**post_service_boards_by_parent_id_auto_templates**](BoardAutoTemplatesApi.md#post_service_boards_by_parent_id_auto_templates) | **POST** /service/boards/{parentId}/autoTemplates | Post BoardAutoTemplate
[**put_service_boards_by_parent_id_auto_templates_by_id**](BoardAutoTemplatesApi.md#put_service_boards_by_parent_id_auto_templates_by_id) | **PUT** /service/boards/{parentId}/autoTemplates/{id} | Put BoardAutoTemplate


# **delete_service_boards_by_parent_id_auto_templates_by_id**
> delete_service_boards_by_parent_id_auto_templates_by_id(id, parent_id, client_id)

Delete BoardAutoTemplate

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
    api_instance = connectwise_psa.BoardAutoTemplatesApi(api_client)
    id = 56 # int | autoTemplateId
    parent_id = 56 # int | boardId
    client_id = 'client_id_example' # str | 

    try:
        # Delete BoardAutoTemplate
        api_instance.delete_service_boards_by_parent_id_auto_templates_by_id(id, parent_id, client_id)
    except Exception as e:
        print("Exception when calling BoardAutoTemplatesApi->delete_service_boards_by_parent_id_auto_templates_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| autoTemplateId | 
 **parent_id** | **int**| boardId | 
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

# **get_service_boards_by_parent_id_auto_templates**
> List[BoardAutoTemplate] get_service_boards_by_parent_id_auto_templates(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of BoardAutoTemplate

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.board_auto_template import BoardAutoTemplate
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
    api_instance = connectwise_psa.BoardAutoTemplatesApi(api_client)
    parent_id = 56 # int | boardId
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
        # Get List of BoardAutoTemplate
        api_response = api_instance.get_service_boards_by_parent_id_auto_templates(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of BoardAutoTemplatesApi->get_service_boards_by_parent_id_auto_templates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BoardAutoTemplatesApi->get_service_boards_by_parent_id_auto_templates: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| boardId | 
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

[**List[BoardAutoTemplate]**](BoardAutoTemplate.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of BoardAutoTemplate |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_service_boards_by_parent_id_auto_templates_by_id**
> BoardAutoTemplate get_service_boards_by_parent_id_auto_templates_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get BoardAutoTemplate

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.board_auto_template import BoardAutoTemplate
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
    api_instance = connectwise_psa.BoardAutoTemplatesApi(api_client)
    id = 56 # int | autoTemplateId
    parent_id = 56 # int | boardId
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
        # Get BoardAutoTemplate
        api_response = api_instance.get_service_boards_by_parent_id_auto_templates_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of BoardAutoTemplatesApi->get_service_boards_by_parent_id_auto_templates_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BoardAutoTemplatesApi->get_service_boards_by_parent_id_auto_templates_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| autoTemplateId | 
 **parent_id** | **int**| boardId | 
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

[**BoardAutoTemplate**](BoardAutoTemplate.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | BoardAutoTemplate |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_service_boards_by_parent_id_auto_templates_count**
> Count get_service_boards_by_parent_id_auto_templates_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Count of BoardAutoTemplate

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
    api_instance = connectwise_psa.BoardAutoTemplatesApi(api_client)
    parent_id = 56 # int | boardId
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
        # Get Count of BoardAutoTemplate
        api_response = api_instance.get_service_boards_by_parent_id_auto_templates_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of BoardAutoTemplatesApi->get_service_boards_by_parent_id_auto_templates_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BoardAutoTemplatesApi->get_service_boards_by_parent_id_auto_templates_count: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| boardId | 
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

# **patch_service_boards_by_parent_id_auto_templates_by_id**
> BoardAutoTemplate patch_service_boards_by_parent_id_auto_templates_by_id(id, parent_id, client_id, patch_operation)

Patch BoardAutoTemplate

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.board_auto_template import BoardAutoTemplate
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
    api_instance = connectwise_psa.BoardAutoTemplatesApi(api_client)
    id = 56 # int | autoTemplateId
    parent_id = 56 # int | boardId
    client_id = 'client_id_example' # str | 
    patch_operation = [connectwise_psa.PatchOperation()] # List[PatchOperation] | List of PatchOperation

    try:
        # Patch BoardAutoTemplate
        api_response = api_instance.patch_service_boards_by_parent_id_auto_templates_by_id(id, parent_id, client_id, patch_operation)
        print("The response of BoardAutoTemplatesApi->patch_service_boards_by_parent_id_auto_templates_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BoardAutoTemplatesApi->patch_service_boards_by_parent_id_auto_templates_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| autoTemplateId | 
 **parent_id** | **int**| boardId | 
 **client_id** | **str**|  | 
 **patch_operation** | [**List[PatchOperation]**](PatchOperation.md)| List of PatchOperation | 

### Return type

[**BoardAutoTemplate**](BoardAutoTemplate.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | BoardAutoTemplate |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_service_boards_by_parent_id_auto_templates**
> BoardAutoTemplate post_service_boards_by_parent_id_auto_templates(parent_id, client_id, board_auto_template)

Post BoardAutoTemplate

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.board_auto_template import BoardAutoTemplate
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
    api_instance = connectwise_psa.BoardAutoTemplatesApi(api_client)
    parent_id = 56 # int | boardId
    client_id = 'client_id_example' # str | 
    board_auto_template = connectwise_psa.BoardAutoTemplate() # BoardAutoTemplate | boardAutoTemplate

    try:
        # Post BoardAutoTemplate
        api_response = api_instance.post_service_boards_by_parent_id_auto_templates(parent_id, client_id, board_auto_template)
        print("The response of BoardAutoTemplatesApi->post_service_boards_by_parent_id_auto_templates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BoardAutoTemplatesApi->post_service_boards_by_parent_id_auto_templates: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| boardId | 
 **client_id** | **str**|  | 
 **board_auto_template** | [**BoardAutoTemplate**](BoardAutoTemplate.md)| boardAutoTemplate | 

### Return type

[**BoardAutoTemplate**](BoardAutoTemplate.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | BoardAutoTemplate |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_service_boards_by_parent_id_auto_templates_by_id**
> BoardAutoTemplate put_service_boards_by_parent_id_auto_templates_by_id(id, parent_id, client_id, board_auto_template)

Put BoardAutoTemplate

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.board_auto_template import BoardAutoTemplate
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
    api_instance = connectwise_psa.BoardAutoTemplatesApi(api_client)
    id = 56 # int | autoTemplateId
    parent_id = 56 # int | boardId
    client_id = 'client_id_example' # str | 
    board_auto_template = connectwise_psa.BoardAutoTemplate() # BoardAutoTemplate | boardAutoTemplate

    try:
        # Put BoardAutoTemplate
        api_response = api_instance.put_service_boards_by_parent_id_auto_templates_by_id(id, parent_id, client_id, board_auto_template)
        print("The response of BoardAutoTemplatesApi->put_service_boards_by_parent_id_auto_templates_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BoardAutoTemplatesApi->put_service_boards_by_parent_id_auto_templates_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| autoTemplateId | 
 **parent_id** | **int**| boardId | 
 **client_id** | **str**|  | 
 **board_auto_template** | [**BoardAutoTemplate**](BoardAutoTemplate.md)| boardAutoTemplate | 

### Return type

[**BoardAutoTemplate**](BoardAutoTemplate.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | BoardAutoTemplate |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

