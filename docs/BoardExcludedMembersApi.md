# connectwise_psa.BoardExcludedMembersApi

All URIs are relative to *https://api-aus.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_service_boards_by_parent_id_excluded_members_by_id**](BoardExcludedMembersApi.md#delete_service_boards_by_parent_id_excluded_members_by_id) | **DELETE** /service/boards/{parentId}/excludedMembers/{id} | Delete BoardExcludedMember
[**get_service_boards_by_parent_id_excluded_members**](BoardExcludedMembersApi.md#get_service_boards_by_parent_id_excluded_members) | **GET** /service/boards/{parentId}/excludedMembers | Get List of BoardExcludedMember
[**get_service_boards_by_parent_id_excluded_members_by_id**](BoardExcludedMembersApi.md#get_service_boards_by_parent_id_excluded_members_by_id) | **GET** /service/boards/{parentId}/excludedMembers/{id} | Get BoardExcludedMember
[**get_service_boards_by_parent_id_excluded_members_count**](BoardExcludedMembersApi.md#get_service_boards_by_parent_id_excluded_members_count) | **GET** /service/boards/{parentId}/excludedMembers/count | Get Count of BoardExcludedMember
[**post_service_boards_by_parent_id_excluded_members**](BoardExcludedMembersApi.md#post_service_boards_by_parent_id_excluded_members) | **POST** /service/boards/{parentId}/excludedMembers | Post BoardExcludedMember


# **delete_service_boards_by_parent_id_excluded_members_by_id**
> delete_service_boards_by_parent_id_excluded_members_by_id(id, parent_id, client_id)

Delete BoardExcludedMember

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
    api_instance = connectwise_psa.BoardExcludedMembersApi(api_client)
    id = 56 # int | excludedMemberId
    parent_id = 56 # int | boardId
    client_id = 'client_id_example' # str | 

    try:
        # Delete BoardExcludedMember
        api_instance.delete_service_boards_by_parent_id_excluded_members_by_id(id, parent_id, client_id)
    except Exception as e:
        print("Exception when calling BoardExcludedMembersApi->delete_service_boards_by_parent_id_excluded_members_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| excludedMemberId | 
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

# **get_service_boards_by_parent_id_excluded_members**
> List[BoardExcludedMember] get_service_boards_by_parent_id_excluded_members(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of BoardExcludedMember

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.board_excluded_member import BoardExcludedMember
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
    api_instance = connectwise_psa.BoardExcludedMembersApi(api_client)
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
        # Get List of BoardExcludedMember
        api_response = api_instance.get_service_boards_by_parent_id_excluded_members(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of BoardExcludedMembersApi->get_service_boards_by_parent_id_excluded_members:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BoardExcludedMembersApi->get_service_boards_by_parent_id_excluded_members: %s\n" % e)
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

[**List[BoardExcludedMember]**](BoardExcludedMember.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of BoardExcludedMember |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_service_boards_by_parent_id_excluded_members_by_id**
> BoardExcludedMember get_service_boards_by_parent_id_excluded_members_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get BoardExcludedMember

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.board_excluded_member import BoardExcludedMember
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
    api_instance = connectwise_psa.BoardExcludedMembersApi(api_client)
    id = 56 # int | excludedMemberId
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
        # Get BoardExcludedMember
        api_response = api_instance.get_service_boards_by_parent_id_excluded_members_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of BoardExcludedMembersApi->get_service_boards_by_parent_id_excluded_members_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BoardExcludedMembersApi->get_service_boards_by_parent_id_excluded_members_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| excludedMemberId | 
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

[**BoardExcludedMember**](BoardExcludedMember.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | BoardExcludedMember |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_service_boards_by_parent_id_excluded_members_count**
> Count get_service_boards_by_parent_id_excluded_members_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Count of BoardExcludedMember

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
    api_instance = connectwise_psa.BoardExcludedMembersApi(api_client)
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
        # Get Count of BoardExcludedMember
        api_response = api_instance.get_service_boards_by_parent_id_excluded_members_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of BoardExcludedMembersApi->get_service_boards_by_parent_id_excluded_members_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BoardExcludedMembersApi->get_service_boards_by_parent_id_excluded_members_count: %s\n" % e)
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

# **post_service_boards_by_parent_id_excluded_members**
> BoardExcludedMember post_service_boards_by_parent_id_excluded_members(parent_id, client_id, board_excluded_member)

Post BoardExcludedMember

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.board_excluded_member import BoardExcludedMember
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
    api_instance = connectwise_psa.BoardExcludedMembersApi(api_client)
    parent_id = 56 # int | boardId
    client_id = 'client_id_example' # str | 
    board_excluded_member = connectwise_psa.BoardExcludedMember() # BoardExcludedMember | boardExcludedMember

    try:
        # Post BoardExcludedMember
        api_response = api_instance.post_service_boards_by_parent_id_excluded_members(parent_id, client_id, board_excluded_member)
        print("The response of BoardExcludedMembersApi->post_service_boards_by_parent_id_excluded_members:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BoardExcludedMembersApi->post_service_boards_by_parent_id_excluded_members: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| boardId | 
 **client_id** | **str**|  | 
 **board_excluded_member** | [**BoardExcludedMember**](BoardExcludedMember.md)| boardExcludedMember | 

### Return type

[**BoardExcludedMember**](BoardExcludedMember.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | BoardExcludedMember |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

