# connectwise_psa.ProjectBoardTeamMembersApi

All URIs are relative to *https://aus-api.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_project_boards_by_grandparent_id_teams_by_parent_id_members_by_id**](ProjectBoardTeamMembersApi.md#delete_project_boards_by_grandparent_id_teams_by_parent_id_members_by_id) | **DELETE** /project/boards/{grandparentId}/teams/{parentId}/members/{id} | Delete ProjectBoardTeamMember
[**get_project_boards_by_grandparent_id_teams_by_parent_id_members**](ProjectBoardTeamMembersApi.md#get_project_boards_by_grandparent_id_teams_by_parent_id_members) | **GET** /project/boards/{grandparentId}/teams/{parentId}/members | Get List of ProjectBoardTeamMember
[**get_project_boards_by_grandparent_id_teams_by_parent_id_members_by_id**](ProjectBoardTeamMembersApi.md#get_project_boards_by_grandparent_id_teams_by_parent_id_members_by_id) | **GET** /project/boards/{grandparentId}/teams/{parentId}/members/{id} | Get ProjectBoardTeamMember
[**patch_project_boards_by_grandparent_id_teams_by_parent_id_members_by_id**](ProjectBoardTeamMembersApi.md#patch_project_boards_by_grandparent_id_teams_by_parent_id_members_by_id) | **PATCH** /project/boards/{grandparentId}/teams/{parentId}/members/{id} | Patch ProjectBoardTeamMember
[**post_project_boards_by_grandparent_id_teams_by_parent_id_members**](ProjectBoardTeamMembersApi.md#post_project_boards_by_grandparent_id_teams_by_parent_id_members) | **POST** /project/boards/{grandparentId}/teams/{parentId}/members | Post ProjectBoardTeamMember
[**put_project_boards_by_grandparent_id_teams_by_parent_id_members_by_id**](ProjectBoardTeamMembersApi.md#put_project_boards_by_grandparent_id_teams_by_parent_id_members_by_id) | **PUT** /project/boards/{grandparentId}/teams/{parentId}/members/{id} | Put ProjectBoardTeamMember


# **delete_project_boards_by_grandparent_id_teams_by_parent_id_members_by_id**
> delete_project_boards_by_grandparent_id_teams_by_parent_id_members_by_id(id, parent_id, grandparent_id, client_id)

Delete ProjectBoardTeamMember

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
    api_instance = connectwise_psa.ProjectBoardTeamMembersApi(api_client)
    id = 56 # int | memberId
    parent_id = 56 # int | teamId
    grandparent_id = 56 # int | boardId
    client_id = 'client_id_example' # str | 

    try:
        # Delete ProjectBoardTeamMember
        api_instance.delete_project_boards_by_grandparent_id_teams_by_parent_id_members_by_id(id, parent_id, grandparent_id, client_id)
    except Exception as e:
        print("Exception when calling ProjectBoardTeamMembersApi->delete_project_boards_by_grandparent_id_teams_by_parent_id_members_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| memberId | 
 **parent_id** | **int**| teamId | 
 **grandparent_id** | **int**| boardId | 
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

# **get_project_boards_by_grandparent_id_teams_by_parent_id_members**
> List[ProjectBoardTeamMember] get_project_boards_by_grandparent_id_teams_by_parent_id_members(parent_id, grandparent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of ProjectBoardTeamMember

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.project_board_team_member import ProjectBoardTeamMember
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
    api_instance = connectwise_psa.ProjectBoardTeamMembersApi(api_client)
    parent_id = 56 # int | teamId
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
        # Get List of ProjectBoardTeamMember
        api_response = api_instance.get_project_boards_by_grandparent_id_teams_by_parent_id_members(parent_id, grandparent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of ProjectBoardTeamMembersApi->get_project_boards_by_grandparent_id_teams_by_parent_id_members:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectBoardTeamMembersApi->get_project_boards_by_grandparent_id_teams_by_parent_id_members: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| teamId | 
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

[**List[ProjectBoardTeamMember]**](ProjectBoardTeamMember.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of ProjectBoardTeamMember |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_boards_by_grandparent_id_teams_by_parent_id_members_by_id**
> ProjectBoardTeamMember get_project_boards_by_grandparent_id_teams_by_parent_id_members_by_id(id, parent_id, grandparent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get ProjectBoardTeamMember

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.project_board_team_member import ProjectBoardTeamMember
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
    api_instance = connectwise_psa.ProjectBoardTeamMembersApi(api_client)
    id = 56 # int | memberId
    parent_id = 56 # int | teamId
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
        # Get ProjectBoardTeamMember
        api_response = api_instance.get_project_boards_by_grandparent_id_teams_by_parent_id_members_by_id(id, parent_id, grandparent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of ProjectBoardTeamMembersApi->get_project_boards_by_grandparent_id_teams_by_parent_id_members_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectBoardTeamMembersApi->get_project_boards_by_grandparent_id_teams_by_parent_id_members_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| memberId | 
 **parent_id** | **int**| teamId | 
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

[**ProjectBoardTeamMember**](ProjectBoardTeamMember.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ProjectBoardTeamMember |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_project_boards_by_grandparent_id_teams_by_parent_id_members_by_id**
> ProjectBoardTeamMember patch_project_boards_by_grandparent_id_teams_by_parent_id_members_by_id(id, parent_id, grandparent_id, client_id, patch_operation)

Patch ProjectBoardTeamMember

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.patch_operation import PatchOperation
from connectwise_psa.models.project_board_team_member import ProjectBoardTeamMember
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
    api_instance = connectwise_psa.ProjectBoardTeamMembersApi(api_client)
    id = 56 # int | memberId
    parent_id = 56 # int | teamId
    grandparent_id = 56 # int | boardId
    client_id = 'client_id_example' # str | 
    patch_operation = [connectwise_psa.PatchOperation()] # List[PatchOperation] | List of PatchOperation

    try:
        # Patch ProjectBoardTeamMember
        api_response = api_instance.patch_project_boards_by_grandparent_id_teams_by_parent_id_members_by_id(id, parent_id, grandparent_id, client_id, patch_operation)
        print("The response of ProjectBoardTeamMembersApi->patch_project_boards_by_grandparent_id_teams_by_parent_id_members_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectBoardTeamMembersApi->patch_project_boards_by_grandparent_id_teams_by_parent_id_members_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| memberId | 
 **parent_id** | **int**| teamId | 
 **grandparent_id** | **int**| boardId | 
 **client_id** | **str**|  | 
 **patch_operation** | [**List[PatchOperation]**](PatchOperation.md)| List of PatchOperation | 

### Return type

[**ProjectBoardTeamMember**](ProjectBoardTeamMember.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ProjectBoardTeamMember |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_project_boards_by_grandparent_id_teams_by_parent_id_members**
> ProjectBoardTeamMember post_project_boards_by_grandparent_id_teams_by_parent_id_members(parent_id, grandparent_id, client_id, project_board_team_member)

Post ProjectBoardTeamMember

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.project_board_team_member import ProjectBoardTeamMember
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
    api_instance = connectwise_psa.ProjectBoardTeamMembersApi(api_client)
    parent_id = 56 # int | teamId
    grandparent_id = 56 # int | boardId
    client_id = 'client_id_example' # str | 
    project_board_team_member = connectwise_psa.ProjectBoardTeamMember() # ProjectBoardTeamMember | teamMember

    try:
        # Post ProjectBoardTeamMember
        api_response = api_instance.post_project_boards_by_grandparent_id_teams_by_parent_id_members(parent_id, grandparent_id, client_id, project_board_team_member)
        print("The response of ProjectBoardTeamMembersApi->post_project_boards_by_grandparent_id_teams_by_parent_id_members:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectBoardTeamMembersApi->post_project_boards_by_grandparent_id_teams_by_parent_id_members: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| teamId | 
 **grandparent_id** | **int**| boardId | 
 **client_id** | **str**|  | 
 **project_board_team_member** | [**ProjectBoardTeamMember**](ProjectBoardTeamMember.md)| teamMember | 

### Return type

[**ProjectBoardTeamMember**](ProjectBoardTeamMember.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | ProjectBoardTeamMember |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_project_boards_by_grandparent_id_teams_by_parent_id_members_by_id**
> ProjectBoardTeamMember put_project_boards_by_grandparent_id_teams_by_parent_id_members_by_id(id, parent_id, grandparent_id, client_id, project_board_team_member)

Put ProjectBoardTeamMember

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.project_board_team_member import ProjectBoardTeamMember
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
    api_instance = connectwise_psa.ProjectBoardTeamMembersApi(api_client)
    id = 56 # int | memberId
    parent_id = 56 # int | teamId
    grandparent_id = 56 # int | boardId
    client_id = 'client_id_example' # str | 
    project_board_team_member = connectwise_psa.ProjectBoardTeamMember() # ProjectBoardTeamMember | teamMember

    try:
        # Put ProjectBoardTeamMember
        api_response = api_instance.put_project_boards_by_grandparent_id_teams_by_parent_id_members_by_id(id, parent_id, grandparent_id, client_id, project_board_team_member)
        print("The response of ProjectBoardTeamMembersApi->put_project_boards_by_grandparent_id_teams_by_parent_id_members_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectBoardTeamMembersApi->put_project_boards_by_grandparent_id_teams_by_parent_id_members_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| memberId | 
 **parent_id** | **int**| teamId | 
 **grandparent_id** | **int**| boardId | 
 **client_id** | **str**|  | 
 **project_board_team_member** | [**ProjectBoardTeamMember**](ProjectBoardTeamMember.md)| teamMember | 

### Return type

[**ProjectBoardTeamMember**](ProjectBoardTeamMember.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ProjectBoardTeamMember |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

