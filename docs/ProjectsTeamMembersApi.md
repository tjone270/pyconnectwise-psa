# connectwise_psa.ProjectsTeamMembersApi

All URIs are relative to *https://api-aus.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_project_projects_by_parent_id_team_members_by_id**](ProjectsTeamMembersApi.md#delete_project_projects_by_parent_id_team_members_by_id) | **DELETE** /project/projects/{parentId}/teamMembers/{id} | Delete ProjectTeamMember
[**get_project_projects_by_parent_id_team_members**](ProjectsTeamMembersApi.md#get_project_projects_by_parent_id_team_members) | **GET** /project/projects/{parentId}/teamMembers | Get List of ProjectTeamMember
[**get_project_projects_by_parent_id_team_members_by_id**](ProjectsTeamMembersApi.md#get_project_projects_by_parent_id_team_members_by_id) | **GET** /project/projects/{parentId}/teamMembers/{id} | Get ProjectTeamMember
[**get_project_projects_by_parent_id_team_members_count**](ProjectsTeamMembersApi.md#get_project_projects_by_parent_id_team_members_count) | **GET** /project/projects/{parentId}/teamMembers/count | Get Count of ProjectTeamMember
[**patch_project_projects_by_parent_id_team_members_by_id**](ProjectsTeamMembersApi.md#patch_project_projects_by_parent_id_team_members_by_id) | **PATCH** /project/projects/{parentId}/teamMembers/{id} | Patch ProjectTeamMember
[**post_project_projects_by_parent_id_team_members**](ProjectsTeamMembersApi.md#post_project_projects_by_parent_id_team_members) | **POST** /project/projects/{parentId}/teamMembers | Post ProjectTeamMember
[**put_project_projects_by_parent_id_team_members_by_id**](ProjectsTeamMembersApi.md#put_project_projects_by_parent_id_team_members_by_id) | **PUT** /project/projects/{parentId}/teamMembers/{id} | Put ProjectTeamMember


# **delete_project_projects_by_parent_id_team_members_by_id**
> delete_project_projects_by_parent_id_team_members_by_id(id, parent_id, client_id)

Delete ProjectTeamMember

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
    api_instance = connectwise_psa.ProjectsTeamMembersApi(api_client)
    id = 56 # int | teamMemberId
    parent_id = 56 # int | projectId
    client_id = 'client_id_example' # str | 

    try:
        # Delete ProjectTeamMember
        api_instance.delete_project_projects_by_parent_id_team_members_by_id(id, parent_id, client_id)
    except Exception as e:
        print("Exception when calling ProjectsTeamMembersApi->delete_project_projects_by_parent_id_team_members_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| teamMemberId | 
 **parent_id** | **int**| projectId | 
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

# **get_project_projects_by_parent_id_team_members**
> List[ProjectTeamMember] get_project_projects_by_parent_id_team_members(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of ProjectTeamMember

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.project_team_member import ProjectTeamMember
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
    api_instance = connectwise_psa.ProjectsTeamMembersApi(api_client)
    parent_id = 56 # int | projectId
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
        # Get List of ProjectTeamMember
        api_response = api_instance.get_project_projects_by_parent_id_team_members(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of ProjectsTeamMembersApi->get_project_projects_by_parent_id_team_members:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsTeamMembersApi->get_project_projects_by_parent_id_team_members: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| projectId | 
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

[**List[ProjectTeamMember]**](ProjectTeamMember.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of ProjectTeamMember |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_projects_by_parent_id_team_members_by_id**
> ProjectTeamMember get_project_projects_by_parent_id_team_members_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get ProjectTeamMember

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.project_team_member import ProjectTeamMember
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
    api_instance = connectwise_psa.ProjectsTeamMembersApi(api_client)
    id = 56 # int | teamMemberId
    parent_id = 56 # int | projectId
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
        # Get ProjectTeamMember
        api_response = api_instance.get_project_projects_by_parent_id_team_members_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of ProjectsTeamMembersApi->get_project_projects_by_parent_id_team_members_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsTeamMembersApi->get_project_projects_by_parent_id_team_members_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| teamMemberId | 
 **parent_id** | **int**| projectId | 
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

[**ProjectTeamMember**](ProjectTeamMember.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ProjectTeamMember |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_projects_by_parent_id_team_members_count**
> Count get_project_projects_by_parent_id_team_members_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Count of ProjectTeamMember

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
    api_instance = connectwise_psa.ProjectsTeamMembersApi(api_client)
    parent_id = 56 # int | projectId
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
        # Get Count of ProjectTeamMember
        api_response = api_instance.get_project_projects_by_parent_id_team_members_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of ProjectsTeamMembersApi->get_project_projects_by_parent_id_team_members_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsTeamMembersApi->get_project_projects_by_parent_id_team_members_count: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| projectId | 
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

# **patch_project_projects_by_parent_id_team_members_by_id**
> ProjectTeamMember patch_project_projects_by_parent_id_team_members_by_id(id, parent_id, client_id, patch_operation)

Patch ProjectTeamMember

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.patch_operation import PatchOperation
from connectwise_psa.models.project_team_member import ProjectTeamMember
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
    api_instance = connectwise_psa.ProjectsTeamMembersApi(api_client)
    id = 56 # int | teamMemberId
    parent_id = 56 # int | projectId
    client_id = 'client_id_example' # str | 
    patch_operation = [connectwise_psa.PatchOperation()] # List[PatchOperation] | List of PatchOperation

    try:
        # Patch ProjectTeamMember
        api_response = api_instance.patch_project_projects_by_parent_id_team_members_by_id(id, parent_id, client_id, patch_operation)
        print("The response of ProjectsTeamMembersApi->patch_project_projects_by_parent_id_team_members_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsTeamMembersApi->patch_project_projects_by_parent_id_team_members_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| teamMemberId | 
 **parent_id** | **int**| projectId | 
 **client_id** | **str**|  | 
 **patch_operation** | [**List[PatchOperation]**](PatchOperation.md)| List of PatchOperation | 

### Return type

[**ProjectTeamMember**](ProjectTeamMember.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ProjectTeamMember |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_project_projects_by_parent_id_team_members**
> ProjectTeamMember post_project_projects_by_parent_id_team_members(parent_id, client_id, project_team_member)

Post ProjectTeamMember

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.project_team_member import ProjectTeamMember
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
    api_instance = connectwise_psa.ProjectsTeamMembersApi(api_client)
    parent_id = 56 # int | projectId
    client_id = 'client_id_example' # str | 
    project_team_member = connectwise_psa.ProjectTeamMember() # ProjectTeamMember | teamMember

    try:
        # Post ProjectTeamMember
        api_response = api_instance.post_project_projects_by_parent_id_team_members(parent_id, client_id, project_team_member)
        print("The response of ProjectsTeamMembersApi->post_project_projects_by_parent_id_team_members:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsTeamMembersApi->post_project_projects_by_parent_id_team_members: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| projectId | 
 **client_id** | **str**|  | 
 **project_team_member** | [**ProjectTeamMember**](ProjectTeamMember.md)| teamMember | 

### Return type

[**ProjectTeamMember**](ProjectTeamMember.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | ProjectTeamMember |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_project_projects_by_parent_id_team_members_by_id**
> ProjectTeamMember put_project_projects_by_parent_id_team_members_by_id(id, parent_id, client_id, project_team_member)

Put ProjectTeamMember

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.project_team_member import ProjectTeamMember
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
    api_instance = connectwise_psa.ProjectsTeamMembersApi(api_client)
    id = 56 # int | teamMemberId
    parent_id = 56 # int | projectId
    client_id = 'client_id_example' # str | 
    project_team_member = connectwise_psa.ProjectTeamMember() # ProjectTeamMember | teamMember

    try:
        # Put ProjectTeamMember
        api_response = api_instance.put_project_projects_by_parent_id_team_members_by_id(id, parent_id, client_id, project_team_member)
        print("The response of ProjectsTeamMembersApi->put_project_projects_by_parent_id_team_members_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsTeamMembersApi->put_project_projects_by_parent_id_team_members_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| teamMemberId | 
 **parent_id** | **int**| projectId | 
 **client_id** | **str**|  | 
 **project_team_member** | [**ProjectTeamMember**](ProjectTeamMember.md)| teamMember | 

### Return type

[**ProjectTeamMember**](ProjectTeamMember.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ProjectTeamMember |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

