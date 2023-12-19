# connectwise_psa.BoardStatusesApi

All URIs are relative to *https://aus-api.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_service_boards_by_parent_id_statuses_by_id**](BoardStatusesApi.md#delete_service_boards_by_parent_id_statuses_by_id) | **DELETE** /service/boards/{parentId}/statuses/{id} | Delete BoardStatus
[**get_service_boards_by_parent_id_statuses**](BoardStatusesApi.md#get_service_boards_by_parent_id_statuses) | **GET** /service/boards/{parentId}/statuses | Get List of BoardStatus
[**get_service_boards_by_parent_id_statuses_by_id**](BoardStatusesApi.md#get_service_boards_by_parent_id_statuses_by_id) | **GET** /service/boards/{parentId}/statuses/{id} | Get BoardStatus
[**get_service_boards_by_parent_id_statuses_by_id_usages**](BoardStatusesApi.md#get_service_boards_by_parent_id_statuses_by_id_usages) | **GET** /service/boards/{parentId}/statuses/{id}/usages | Get List of Usage Count
[**get_service_boards_by_parent_id_statuses_by_id_usages_list**](BoardStatusesApi.md#get_service_boards_by_parent_id_statuses_by_id_usages_list) | **GET** /service/boards/{parentId}/statuses/{id}/usages/list | Get List of Usage
[**get_service_boards_by_parent_id_statuses_count**](BoardStatusesApi.md#get_service_boards_by_parent_id_statuses_count) | **GET** /service/boards/{parentId}/statuses/count | Get Count of BoardStatus
[**patch_service_boards_by_parent_id_statuses_by_id**](BoardStatusesApi.md#patch_service_boards_by_parent_id_statuses_by_id) | **PATCH** /service/boards/{parentId}/statuses/{id} | Patch BoardStatus
[**post_service_boards_by_parent_id_statuses**](BoardStatusesApi.md#post_service_boards_by_parent_id_statuses) | **POST** /service/boards/{parentId}/statuses | Post BoardStatus
[**put_service_boards_by_parent_id_statuses_by_id**](BoardStatusesApi.md#put_service_boards_by_parent_id_statuses_by_id) | **PUT** /service/boards/{parentId}/statuses/{id} | Put BoardStatus


# **delete_service_boards_by_parent_id_statuses_by_id**
> delete_service_boards_by_parent_id_statuses_by_id(id, parent_id, client_id)

Delete BoardStatus

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
    api_instance = connectwise_psa.BoardStatusesApi(api_client)
    id = 56 # int | statusId
    parent_id = 56 # int | boardId
    client_id = 'client_id_example' # str | 

    try:
        # Delete BoardStatus
        api_instance.delete_service_boards_by_parent_id_statuses_by_id(id, parent_id, client_id)
    except Exception as e:
        print("Exception when calling BoardStatusesApi->delete_service_boards_by_parent_id_statuses_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| statusId | 
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

# **get_service_boards_by_parent_id_statuses**
> List[BoardStatus] get_service_boards_by_parent_id_statuses(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of BoardStatus

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.board_status import BoardStatus
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
    api_instance = connectwise_psa.BoardStatusesApi(api_client)
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
        # Get List of BoardStatus
        api_response = api_instance.get_service_boards_by_parent_id_statuses(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of BoardStatusesApi->get_service_boards_by_parent_id_statuses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BoardStatusesApi->get_service_boards_by_parent_id_statuses: %s\n" % e)
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

[**List[BoardStatus]**](BoardStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of BoardStatus |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_service_boards_by_parent_id_statuses_by_id**
> BoardStatus get_service_boards_by_parent_id_statuses_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get BoardStatus

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.board_status import BoardStatus
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
    api_instance = connectwise_psa.BoardStatusesApi(api_client)
    id = 56 # int | statusId
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
        # Get BoardStatus
        api_response = api_instance.get_service_boards_by_parent_id_statuses_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of BoardStatusesApi->get_service_boards_by_parent_id_statuses_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BoardStatusesApi->get_service_boards_by_parent_id_statuses_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| statusId | 
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

[**BoardStatus**](BoardStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | BoardStatus |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_service_boards_by_parent_id_statuses_by_id_usages**
> List[Usage] get_service_boards_by_parent_id_statuses_by_id_usages(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

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
    api_instance = connectwise_psa.BoardStatusesApi(api_client)
    id = 56 # int | statusId
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
        # Get List of Usage Count
        api_response = api_instance.get_service_boards_by_parent_id_statuses_by_id_usages(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of BoardStatusesApi->get_service_boards_by_parent_id_statuses_by_id_usages:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BoardStatusesApi->get_service_boards_by_parent_id_statuses_by_id_usages: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| statusId | 
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

# **get_service_boards_by_parent_id_statuses_by_id_usages_list**
> List[Usage] get_service_boards_by_parent_id_statuses_by_id_usages_list(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

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
    api_instance = connectwise_psa.BoardStatusesApi(api_client)
    id = 56 # int | statusId
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
        # Get List of Usage
        api_response = api_instance.get_service_boards_by_parent_id_statuses_by_id_usages_list(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of BoardStatusesApi->get_service_boards_by_parent_id_statuses_by_id_usages_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BoardStatusesApi->get_service_boards_by_parent_id_statuses_by_id_usages_list: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| statusId | 
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

# **get_service_boards_by_parent_id_statuses_count**
> Count get_service_boards_by_parent_id_statuses_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Count of BoardStatus

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
    api_instance = connectwise_psa.BoardStatusesApi(api_client)
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
        # Get Count of BoardStatus
        api_response = api_instance.get_service_boards_by_parent_id_statuses_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of BoardStatusesApi->get_service_boards_by_parent_id_statuses_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BoardStatusesApi->get_service_boards_by_parent_id_statuses_count: %s\n" % e)
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

# **patch_service_boards_by_parent_id_statuses_by_id**
> BoardStatus patch_service_boards_by_parent_id_statuses_by_id(id, parent_id, client_id, patch_operation)

Patch BoardStatus

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.board_status import BoardStatus
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
    api_instance = connectwise_psa.BoardStatusesApi(api_client)
    id = 56 # int | statusId
    parent_id = 56 # int | boardId
    client_id = 'client_id_example' # str | 
    patch_operation = [connectwise_psa.PatchOperation()] # List[PatchOperation] | List of PatchOperation

    try:
        # Patch BoardStatus
        api_response = api_instance.patch_service_boards_by_parent_id_statuses_by_id(id, parent_id, client_id, patch_operation)
        print("The response of BoardStatusesApi->patch_service_boards_by_parent_id_statuses_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BoardStatusesApi->patch_service_boards_by_parent_id_statuses_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| statusId | 
 **parent_id** | **int**| boardId | 
 **client_id** | **str**|  | 
 **patch_operation** | [**List[PatchOperation]**](PatchOperation.md)| List of PatchOperation | 

### Return type

[**BoardStatus**](BoardStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | BoardStatus |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_service_boards_by_parent_id_statuses**
> BoardStatus post_service_boards_by_parent_id_statuses(parent_id, client_id, board_status)

Post BoardStatus

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.board_status import BoardStatus
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
    api_instance = connectwise_psa.BoardStatusesApi(api_client)
    parent_id = 56 # int | boardId
    client_id = 'client_id_example' # str | 
    board_status = connectwise_psa.BoardStatus() # BoardStatus | boardStatus

    try:
        # Post BoardStatus
        api_response = api_instance.post_service_boards_by_parent_id_statuses(parent_id, client_id, board_status)
        print("The response of BoardStatusesApi->post_service_boards_by_parent_id_statuses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BoardStatusesApi->post_service_boards_by_parent_id_statuses: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| boardId | 
 **client_id** | **str**|  | 
 **board_status** | [**BoardStatus**](BoardStatus.md)| boardStatus | 

### Return type

[**BoardStatus**](BoardStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | BoardStatus |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_service_boards_by_parent_id_statuses_by_id**
> BoardStatus put_service_boards_by_parent_id_statuses_by_id(id, parent_id, client_id, board_status)

Put BoardStatus

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.board_status import BoardStatus
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
    api_instance = connectwise_psa.BoardStatusesApi(api_client)
    id = 56 # int | statusId
    parent_id = 56 # int | boardId
    client_id = 'client_id_example' # str | 
    board_status = connectwise_psa.BoardStatus() # BoardStatus | boardStatus

    try:
        # Put BoardStatus
        api_response = api_instance.put_service_boards_by_parent_id_statuses_by_id(id, parent_id, client_id, board_status)
        print("The response of BoardStatusesApi->put_service_boards_by_parent_id_statuses_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BoardStatusesApi->put_service_boards_by_parent_id_statuses_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| statusId | 
 **parent_id** | **int**| boardId | 
 **client_id** | **str**|  | 
 **board_status** | [**BoardStatus**](BoardStatus.md)| boardStatus | 

### Return type

[**BoardStatus**](BoardStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | BoardStatus |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

