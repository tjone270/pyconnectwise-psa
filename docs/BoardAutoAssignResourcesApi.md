# connectwise_psa.BoardAutoAssignResourcesApi

All URIs are relative to *https://api-aus.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_service_boards_by_parent_id_auto_assign_resources_by_id**](BoardAutoAssignResourcesApi.md#delete_service_boards_by_parent_id_auto_assign_resources_by_id) | **DELETE** /service/boards/{parentId}/autoAssignResources/{id} | Delete BoardAutoAssignResource
[**get_service_boards_by_parent_id_auto_assign_resources**](BoardAutoAssignResourcesApi.md#get_service_boards_by_parent_id_auto_assign_resources) | **GET** /service/boards/{parentId}/autoAssignResources | Get List of BoardAutoAssignResource
[**get_service_boards_by_parent_id_auto_assign_resources_by_id**](BoardAutoAssignResourcesApi.md#get_service_boards_by_parent_id_auto_assign_resources_by_id) | **GET** /service/boards/{parentId}/autoAssignResources/{id} | Get BoardAutoAssignResource
[**get_service_boards_by_parent_id_auto_assign_resources_count**](BoardAutoAssignResourcesApi.md#get_service_boards_by_parent_id_auto_assign_resources_count) | **GET** /service/boards/{parentId}/autoAssignResources/count | Get Count of BoardAutoAssignResource
[**patch_service_boards_by_parent_id_auto_assign_resources_by_id**](BoardAutoAssignResourcesApi.md#patch_service_boards_by_parent_id_auto_assign_resources_by_id) | **PATCH** /service/boards/{parentId}/autoAssignResources/{id} | Patch BoardAutoAssignResource
[**post_service_boards_by_parent_id_auto_assign_resources**](BoardAutoAssignResourcesApi.md#post_service_boards_by_parent_id_auto_assign_resources) | **POST** /service/boards/{parentId}/autoAssignResources | Post BoardAutoAssignResource
[**put_service_boards_by_parent_id_auto_assign_resources_by_id**](BoardAutoAssignResourcesApi.md#put_service_boards_by_parent_id_auto_assign_resources_by_id) | **PUT** /service/boards/{parentId}/autoAssignResources/{id} | Put BoardAutoAssignResource


# **delete_service_boards_by_parent_id_auto_assign_resources_by_id**
> delete_service_boards_by_parent_id_auto_assign_resources_by_id(id, parent_id, client_id)

Delete BoardAutoAssignResource

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
    api_instance = connectwise_psa.BoardAutoAssignResourcesApi(api_client)
    id = 56 # int | autoAssignResourceId
    parent_id = 56 # int | boardId
    client_id = 'client_id_example' # str | 

    try:
        # Delete BoardAutoAssignResource
        api_instance.delete_service_boards_by_parent_id_auto_assign_resources_by_id(id, parent_id, client_id)
    except Exception as e:
        print("Exception when calling BoardAutoAssignResourcesApi->delete_service_boards_by_parent_id_auto_assign_resources_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| autoAssignResourceId | 
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

# **get_service_boards_by_parent_id_auto_assign_resources**
> List[BoardAutoAssignResource] get_service_boards_by_parent_id_auto_assign_resources(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of BoardAutoAssignResource

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.board_auto_assign_resource import BoardAutoAssignResource
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
    api_instance = connectwise_psa.BoardAutoAssignResourcesApi(api_client)
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
        # Get List of BoardAutoAssignResource
        api_response = api_instance.get_service_boards_by_parent_id_auto_assign_resources(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of BoardAutoAssignResourcesApi->get_service_boards_by_parent_id_auto_assign_resources:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BoardAutoAssignResourcesApi->get_service_boards_by_parent_id_auto_assign_resources: %s\n" % e)
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

[**List[BoardAutoAssignResource]**](BoardAutoAssignResource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of BoardAutoAssignResource |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_service_boards_by_parent_id_auto_assign_resources_by_id**
> BoardAutoAssignResource get_service_boards_by_parent_id_auto_assign_resources_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get BoardAutoAssignResource

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.board_auto_assign_resource import BoardAutoAssignResource
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
    api_instance = connectwise_psa.BoardAutoAssignResourcesApi(api_client)
    id = 56 # int | autoAssignResourceId
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
        # Get BoardAutoAssignResource
        api_response = api_instance.get_service_boards_by_parent_id_auto_assign_resources_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of BoardAutoAssignResourcesApi->get_service_boards_by_parent_id_auto_assign_resources_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BoardAutoAssignResourcesApi->get_service_boards_by_parent_id_auto_assign_resources_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| autoAssignResourceId | 
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

[**BoardAutoAssignResource**](BoardAutoAssignResource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | BoardAutoAssignResource |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_service_boards_by_parent_id_auto_assign_resources_count**
> Count get_service_boards_by_parent_id_auto_assign_resources_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Count of BoardAutoAssignResource

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
    api_instance = connectwise_psa.BoardAutoAssignResourcesApi(api_client)
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
        # Get Count of BoardAutoAssignResource
        api_response = api_instance.get_service_boards_by_parent_id_auto_assign_resources_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of BoardAutoAssignResourcesApi->get_service_boards_by_parent_id_auto_assign_resources_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BoardAutoAssignResourcesApi->get_service_boards_by_parent_id_auto_assign_resources_count: %s\n" % e)
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

# **patch_service_boards_by_parent_id_auto_assign_resources_by_id**
> BoardAutoAssignResource patch_service_boards_by_parent_id_auto_assign_resources_by_id(id, parent_id, client_id, patch_operation)

Patch BoardAutoAssignResource

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.board_auto_assign_resource import BoardAutoAssignResource
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
    api_instance = connectwise_psa.BoardAutoAssignResourcesApi(api_client)
    id = 56 # int | autoAssignResourceId
    parent_id = 56 # int | boardId
    client_id = 'client_id_example' # str | 
    patch_operation = [connectwise_psa.PatchOperation()] # List[PatchOperation] | List of PatchOperation

    try:
        # Patch BoardAutoAssignResource
        api_response = api_instance.patch_service_boards_by_parent_id_auto_assign_resources_by_id(id, parent_id, client_id, patch_operation)
        print("The response of BoardAutoAssignResourcesApi->patch_service_boards_by_parent_id_auto_assign_resources_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BoardAutoAssignResourcesApi->patch_service_boards_by_parent_id_auto_assign_resources_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| autoAssignResourceId | 
 **parent_id** | **int**| boardId | 
 **client_id** | **str**|  | 
 **patch_operation** | [**List[PatchOperation]**](PatchOperation.md)| List of PatchOperation | 

### Return type

[**BoardAutoAssignResource**](BoardAutoAssignResource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | BoardAutoAssignResource |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_service_boards_by_parent_id_auto_assign_resources**
> BoardAutoAssignResource post_service_boards_by_parent_id_auto_assign_resources(parent_id, client_id, board_auto_assign_resource)

Post BoardAutoAssignResource

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.board_auto_assign_resource import BoardAutoAssignResource
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
    api_instance = connectwise_psa.BoardAutoAssignResourcesApi(api_client)
    parent_id = 56 # int | boardId
    client_id = 'client_id_example' # str | 
    board_auto_assign_resource = connectwise_psa.BoardAutoAssignResource() # BoardAutoAssignResource | boardAutoAssignResource

    try:
        # Post BoardAutoAssignResource
        api_response = api_instance.post_service_boards_by_parent_id_auto_assign_resources(parent_id, client_id, board_auto_assign_resource)
        print("The response of BoardAutoAssignResourcesApi->post_service_boards_by_parent_id_auto_assign_resources:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BoardAutoAssignResourcesApi->post_service_boards_by_parent_id_auto_assign_resources: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| boardId | 
 **client_id** | **str**|  | 
 **board_auto_assign_resource** | [**BoardAutoAssignResource**](BoardAutoAssignResource.md)| boardAutoAssignResource | 

### Return type

[**BoardAutoAssignResource**](BoardAutoAssignResource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | BoardAutoAssignResource |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_service_boards_by_parent_id_auto_assign_resources_by_id**
> BoardAutoAssignResource put_service_boards_by_parent_id_auto_assign_resources_by_id(id, parent_id, client_id, board_auto_assign_resource)

Put BoardAutoAssignResource

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.board_auto_assign_resource import BoardAutoAssignResource
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
    api_instance = connectwise_psa.BoardAutoAssignResourcesApi(api_client)
    id = 56 # int | autoAssignResourceId
    parent_id = 56 # int | boardId
    client_id = 'client_id_example' # str | 
    board_auto_assign_resource = connectwise_psa.BoardAutoAssignResource() # BoardAutoAssignResource | boardAutoAssignResource

    try:
        # Put BoardAutoAssignResource
        api_response = api_instance.put_service_boards_by_parent_id_auto_assign_resources_by_id(id, parent_id, client_id, board_auto_assign_resource)
        print("The response of BoardAutoAssignResourcesApi->put_service_boards_by_parent_id_auto_assign_resources_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BoardAutoAssignResourcesApi->put_service_boards_by_parent_id_auto_assign_resources_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| autoAssignResourceId | 
 **parent_id** | **int**| boardId | 
 **client_id** | **str**|  | 
 **board_auto_assign_resource** | [**BoardAutoAssignResource**](BoardAutoAssignResource.md)| boardAutoAssignResource | 

### Return type

[**BoardAutoAssignResource**](BoardAutoAssignResource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | BoardAutoAssignResource |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

