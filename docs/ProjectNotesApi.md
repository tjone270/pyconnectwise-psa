# connectwise_psa.ProjectNotesApi

All URIs are relative to *https://api-aus.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_project_projects_by_parent_id_notes_by_id**](ProjectNotesApi.md#delete_project_projects_by_parent_id_notes_by_id) | **DELETE** /project/projects/{parentId}/notes/{id} | Delete ProjectNote
[**get_project_projects_by_parent_id_notes**](ProjectNotesApi.md#get_project_projects_by_parent_id_notes) | **GET** /project/projects/{parentId}/notes | Get List of ProjectNote
[**get_project_projects_by_parent_id_notes_by_id**](ProjectNotesApi.md#get_project_projects_by_parent_id_notes_by_id) | **GET** /project/projects/{parentId}/notes/{id} | Get ProjectNote
[**get_project_projects_by_parent_id_notes_count**](ProjectNotesApi.md#get_project_projects_by_parent_id_notes_count) | **GET** /project/projects/{parentId}/notes/count | Get Count of ProjectNote
[**patch_project_projects_by_parent_id_notes_by_id**](ProjectNotesApi.md#patch_project_projects_by_parent_id_notes_by_id) | **PATCH** /project/projects/{parentId}/notes/{id} | Patch ProjectNote
[**post_project_projects_by_parent_id_notes**](ProjectNotesApi.md#post_project_projects_by_parent_id_notes) | **POST** /project/projects/{parentId}/notes | Post ProjectNote
[**put_project_projects_by_parent_id_notes_by_id**](ProjectNotesApi.md#put_project_projects_by_parent_id_notes_by_id) | **PUT** /project/projects/{parentId}/notes/{id} | Put ProjectNote


# **delete_project_projects_by_parent_id_notes_by_id**
> delete_project_projects_by_parent_id_notes_by_id(id, parent_id, client_id)

Delete ProjectNote

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
    api_instance = connectwise_psa.ProjectNotesApi(api_client)
    id = 56 # int | noteId
    parent_id = 56 # int | projectId
    client_id = 'client_id_example' # str | 

    try:
        # Delete ProjectNote
        api_instance.delete_project_projects_by_parent_id_notes_by_id(id, parent_id, client_id)
    except Exception as e:
        print("Exception when calling ProjectNotesApi->delete_project_projects_by_parent_id_notes_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| noteId | 
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

# **get_project_projects_by_parent_id_notes**
> List[ProjectNote] get_project_projects_by_parent_id_notes(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of ProjectNote

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.project_note import ProjectNote
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
    api_instance = connectwise_psa.ProjectNotesApi(api_client)
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
        # Get List of ProjectNote
        api_response = api_instance.get_project_projects_by_parent_id_notes(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of ProjectNotesApi->get_project_projects_by_parent_id_notes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectNotesApi->get_project_projects_by_parent_id_notes: %s\n" % e)
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

[**List[ProjectNote]**](ProjectNote.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of ProjectNote |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_projects_by_parent_id_notes_by_id**
> ProjectNote get_project_projects_by_parent_id_notes_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get ProjectNote

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.project_note import ProjectNote
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
    api_instance = connectwise_psa.ProjectNotesApi(api_client)
    id = 56 # int | noteId
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
        # Get ProjectNote
        api_response = api_instance.get_project_projects_by_parent_id_notes_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of ProjectNotesApi->get_project_projects_by_parent_id_notes_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectNotesApi->get_project_projects_by_parent_id_notes_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| noteId | 
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

[**ProjectNote**](ProjectNote.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ProjectNote |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_projects_by_parent_id_notes_count**
> Count get_project_projects_by_parent_id_notes_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Count of ProjectNote

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
    api_instance = connectwise_psa.ProjectNotesApi(api_client)
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
        # Get Count of ProjectNote
        api_response = api_instance.get_project_projects_by_parent_id_notes_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of ProjectNotesApi->get_project_projects_by_parent_id_notes_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectNotesApi->get_project_projects_by_parent_id_notes_count: %s\n" % e)
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

# **patch_project_projects_by_parent_id_notes_by_id**
> ProjectNote patch_project_projects_by_parent_id_notes_by_id(id, parent_id, client_id, patch_operation)

Patch ProjectNote

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.patch_operation import PatchOperation
from connectwise_psa.models.project_note import ProjectNote
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
    api_instance = connectwise_psa.ProjectNotesApi(api_client)
    id = 56 # int | noteId
    parent_id = 56 # int | projectId
    client_id = 'client_id_example' # str | 
    patch_operation = [connectwise_psa.PatchOperation()] # List[PatchOperation] | List of PatchOperation

    try:
        # Patch ProjectNote
        api_response = api_instance.patch_project_projects_by_parent_id_notes_by_id(id, parent_id, client_id, patch_operation)
        print("The response of ProjectNotesApi->patch_project_projects_by_parent_id_notes_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectNotesApi->patch_project_projects_by_parent_id_notes_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| noteId | 
 **parent_id** | **int**| projectId | 
 **client_id** | **str**|  | 
 **patch_operation** | [**List[PatchOperation]**](PatchOperation.md)| List of PatchOperation | 

### Return type

[**ProjectNote**](ProjectNote.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ProjectNote |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_project_projects_by_parent_id_notes**
> ProjectNote post_project_projects_by_parent_id_notes(parent_id, client_id, project_note)

Post ProjectNote

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.project_note import ProjectNote
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
    api_instance = connectwise_psa.ProjectNotesApi(api_client)
    parent_id = 56 # int | projectId
    client_id = 'client_id_example' # str | 
    project_note = connectwise_psa.ProjectNote() # ProjectNote | note

    try:
        # Post ProjectNote
        api_response = api_instance.post_project_projects_by_parent_id_notes(parent_id, client_id, project_note)
        print("The response of ProjectNotesApi->post_project_projects_by_parent_id_notes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectNotesApi->post_project_projects_by_parent_id_notes: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| projectId | 
 **client_id** | **str**|  | 
 **project_note** | [**ProjectNote**](ProjectNote.md)| note | 

### Return type

[**ProjectNote**](ProjectNote.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | ProjectNote |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_project_projects_by_parent_id_notes_by_id**
> ProjectNote put_project_projects_by_parent_id_notes_by_id(id, parent_id, client_id, project_note)

Put ProjectNote

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.project_note import ProjectNote
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
    api_instance = connectwise_psa.ProjectNotesApi(api_client)
    id = 56 # int | noteId
    parent_id = 56 # int | projectId
    client_id = 'client_id_example' # str | 
    project_note = connectwise_psa.ProjectNote() # ProjectNote | note

    try:
        # Put ProjectNote
        api_response = api_instance.put_project_projects_by_parent_id_notes_by_id(id, parent_id, client_id, project_note)
        print("The response of ProjectNotesApi->put_project_projects_by_parent_id_notes_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectNotesApi->put_project_projects_by_parent_id_notes_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| noteId | 
 **parent_id** | **int**| projectId | 
 **client_id** | **str**|  | 
 **project_note** | [**ProjectNote**](ProjectNote.md)| note | 

### Return type

[**ProjectNote**](ProjectNote.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ProjectNote |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

