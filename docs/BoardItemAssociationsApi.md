# connectwise_psa.BoardItemAssociationsApi

All URIs are relative to *https://aus-api.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_service_boards_by_grandparent_id_items_by_parent_id_associations**](BoardItemAssociationsApi.md#get_service_boards_by_grandparent_id_items_by_parent_id_associations) | **GET** /service/boards/{grandparentId}/items/{parentId}/associations | Get List of BoardItemAssociation
[**get_service_boards_by_grandparent_id_items_by_parent_id_associations_by_id**](BoardItemAssociationsApi.md#get_service_boards_by_grandparent_id_items_by_parent_id_associations_by_id) | **GET** /service/boards/{grandparentId}/items/{parentId}/associations/{id} | Get BoardItemAssociation
[**get_service_boards_by_grandparent_id_items_by_parent_id_associations_count**](BoardItemAssociationsApi.md#get_service_boards_by_grandparent_id_items_by_parent_id_associations_count) | **GET** /service/boards/{grandparentId}/items/{parentId}/associations/count | Get Count of BoardItemAssociation
[**patch_service_boards_by_grandparent_id_items_by_parent_id_associations_by_id**](BoardItemAssociationsApi.md#patch_service_boards_by_grandparent_id_items_by_parent_id_associations_by_id) | **PATCH** /service/boards/{grandparentId}/items/{parentId}/associations/{id} | Patch BoardItemAssociation
[**put_service_boards_by_grandparent_id_items_by_parent_id_associations_by_id**](BoardItemAssociationsApi.md#put_service_boards_by_grandparent_id_items_by_parent_id_associations_by_id) | **PUT** /service/boards/{grandparentId}/items/{parentId}/associations/{id} | Put BoardItemAssociation


# **get_service_boards_by_grandparent_id_items_by_parent_id_associations**
> List[BoardItemAssociation] get_service_boards_by_grandparent_id_items_by_parent_id_associations(parent_id, grandparent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of BoardItemAssociation

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.board_item_association import BoardItemAssociation
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
    api_instance = connectwise_psa.BoardItemAssociationsApi(api_client)
    parent_id = 56 # int | itemId
    grandparent_id = 56 # int | boardId
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
        # Get List of BoardItemAssociation
        api_response = api_instance.get_service_boards_by_grandparent_id_items_by_parent_id_associations(parent_id, grandparent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of BoardItemAssociationsApi->get_service_boards_by_grandparent_id_items_by_parent_id_associations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BoardItemAssociationsApi->get_service_boards_by_grandparent_id_items_by_parent_id_associations: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| itemId | 
 **grandparent_id** | **int**| boardId | 
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

[**List[BoardItemAssociation]**](BoardItemAssociation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of BoardItemAssociation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_service_boards_by_grandparent_id_items_by_parent_id_associations_by_id**
> BoardItemAssociation get_service_boards_by_grandparent_id_items_by_parent_id_associations_by_id(id, parent_id, grandparent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get BoardItemAssociation

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.board_item_association import BoardItemAssociation
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
    api_instance = connectwise_psa.BoardItemAssociationsApi(api_client)
    id = 56 # int | associationId
    parent_id = 56 # int | itemId
    grandparent_id = 56 # int | boardId
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
        # Get BoardItemAssociation
        api_response = api_instance.get_service_boards_by_grandparent_id_items_by_parent_id_associations_by_id(id, parent_id, grandparent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of BoardItemAssociationsApi->get_service_boards_by_grandparent_id_items_by_parent_id_associations_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BoardItemAssociationsApi->get_service_boards_by_grandparent_id_items_by_parent_id_associations_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| associationId | 
 **parent_id** | **int**| itemId | 
 **grandparent_id** | **int**| boardId | 
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

[**BoardItemAssociation**](BoardItemAssociation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | BoardItemAssociation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_service_boards_by_grandparent_id_items_by_parent_id_associations_count**
> Count get_service_boards_by_grandparent_id_items_by_parent_id_associations_count(parent_id, grandparent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Count of BoardItemAssociation

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
    api_instance = connectwise_psa.BoardItemAssociationsApi(api_client)
    parent_id = 56 # int | itemId
    grandparent_id = 56 # int | boardId
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
        # Get Count of BoardItemAssociation
        api_response = api_instance.get_service_boards_by_grandparent_id_items_by_parent_id_associations_count(parent_id, grandparent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of BoardItemAssociationsApi->get_service_boards_by_grandparent_id_items_by_parent_id_associations_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BoardItemAssociationsApi->get_service_boards_by_grandparent_id_items_by_parent_id_associations_count: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| itemId | 
 **grandparent_id** | **int**| boardId | 
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

# **patch_service_boards_by_grandparent_id_items_by_parent_id_associations_by_id**
> BoardItemAssociation patch_service_boards_by_grandparent_id_items_by_parent_id_associations_by_id(id, parent_id, grandparent_id, client_id, patch_operation)

Patch BoardItemAssociation

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.board_item_association import BoardItemAssociation
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
    api_instance = connectwise_psa.BoardItemAssociationsApi(api_client)
    id = 56 # int | associationId
    parent_id = 56 # int | itemId
    grandparent_id = 56 # int | boardId
    client_id = 'client_id_example' # str | 
    patch_operation = [connectwise_psa.PatchOperation()] # List[PatchOperation] | List of PatchOperation

    try:
        # Patch BoardItemAssociation
        api_response = api_instance.patch_service_boards_by_grandparent_id_items_by_parent_id_associations_by_id(id, parent_id, grandparent_id, client_id, patch_operation)
        print("The response of BoardItemAssociationsApi->patch_service_boards_by_grandparent_id_items_by_parent_id_associations_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BoardItemAssociationsApi->patch_service_boards_by_grandparent_id_items_by_parent_id_associations_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| associationId | 
 **parent_id** | **int**| itemId | 
 **grandparent_id** | **int**| boardId | 
 **client_id** | **str**|  | 
 **patch_operation** | [**List[PatchOperation]**](PatchOperation.md)| List of PatchOperation | 

### Return type

[**BoardItemAssociation**](BoardItemAssociation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | BoardItemAssociation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_service_boards_by_grandparent_id_items_by_parent_id_associations_by_id**
> BoardItemAssociation put_service_boards_by_grandparent_id_items_by_parent_id_associations_by_id(id, parent_id, grandparent_id, client_id, board_item_association)

Put BoardItemAssociation

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.board_item_association import BoardItemAssociation
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
    api_instance = connectwise_psa.BoardItemAssociationsApi(api_client)
    id = 56 # int | associationId
    parent_id = 56 # int | itemId
    grandparent_id = 56 # int | boardId
    client_id = 'client_id_example' # str | 
    board_item_association = connectwise_psa.BoardItemAssociation() # BoardItemAssociation | itemAssociation

    try:
        # Put BoardItemAssociation
        api_response = api_instance.put_service_boards_by_grandparent_id_items_by_parent_id_associations_by_id(id, parent_id, grandparent_id, client_id, board_item_association)
        print("The response of BoardItemAssociationsApi->put_service_boards_by_grandparent_id_items_by_parent_id_associations_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BoardItemAssociationsApi->put_service_boards_by_grandparent_id_items_by_parent_id_associations_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| associationId | 
 **parent_id** | **int**| itemId | 
 **grandparent_id** | **int**| boardId | 
 **client_id** | **str**|  | 
 **board_item_association** | [**BoardItemAssociation**](BoardItemAssociation.md)| itemAssociation | 

### Return type

[**BoardItemAssociation**](BoardItemAssociation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | BoardItemAssociation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

