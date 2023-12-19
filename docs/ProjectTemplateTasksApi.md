# connectwise_psa.ProjectTemplateTasksApi

All URIs are relative to *https://aus-api.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_project_project_templates_by_grand_parent_id_project_template_tickets_by_parent_id_tasks_by_id**](ProjectTemplateTasksApi.md#delete_project_project_templates_by_grand_parent_id_project_template_tickets_by_parent_id_tasks_by_id) | **DELETE** /project/projectTemplates/{grandParentId}/projectTemplateTickets/{parentId}/tasks/{id} | Delete ProjectTemplateTasks
[**get_project_project_templates_by_grand_parent_id_project_template_tickets_by_parent_id_tasks**](ProjectTemplateTasksApi.md#get_project_project_templates_by_grand_parent_id_project_template_tickets_by_parent_id_tasks) | **GET** /project/projectTemplates/{grandParentId}/projectTemplateTickets/{parentId}/tasks | Get List of ProjectTemplateTasks
[**get_project_project_templates_by_grand_parent_id_project_template_tickets_by_parent_id_tasks_by_id**](ProjectTemplateTasksApi.md#get_project_project_templates_by_grand_parent_id_project_template_tickets_by_parent_id_tasks_by_id) | **GET** /project/projectTemplates/{grandParentId}/projectTemplateTickets/{parentId}/tasks/{id} | Get ProjectTemplateTasks
[**get_project_project_templates_by_grand_parent_id_project_template_tickets_by_parent_id_tasks_count**](ProjectTemplateTasksApi.md#get_project_project_templates_by_grand_parent_id_project_template_tickets_by_parent_id_tasks_count) | **GET** /project/projectTemplates/{grandParentId}/projectTemplateTickets/{parentId}/tasks/count | Get Count of ProjectTemplateTasks
[**patch_project_project_templates_by_grand_parent_id_project_template_tickets_by_parent_id_tasks_by_id**](ProjectTemplateTasksApi.md#patch_project_project_templates_by_grand_parent_id_project_template_tickets_by_parent_id_tasks_by_id) | **PATCH** /project/projectTemplates/{grandParentId}/projectTemplateTickets/{parentId}/tasks/{id} | Patch ProjectTemplateTasks
[**post_project_project_templates_by_grand_parent_id_project_template_tickets_by_parent_id_tasks**](ProjectTemplateTasksApi.md#post_project_project_templates_by_grand_parent_id_project_template_tickets_by_parent_id_tasks) | **POST** /project/projectTemplates/{grandParentId}/projectTemplateTickets/{parentId}/tasks | Post ProjectTemplateTasks
[**put_project_project_templates_by_grand_parent_id_project_template_tickets_by_parent_id_tasks_by_id**](ProjectTemplateTasksApi.md#put_project_project_templates_by_grand_parent_id_project_template_tickets_by_parent_id_tasks_by_id) | **PUT** /project/projectTemplates/{grandParentId}/projectTemplateTickets/{parentId}/tasks/{id} | Put ProjectTemplateTasks


# **delete_project_project_templates_by_grand_parent_id_project_template_tickets_by_parent_id_tasks_by_id**
> delete_project_project_templates_by_grand_parent_id_project_template_tickets_by_parent_id_tasks_by_id(id, grand_parent_id, parent_id, client_id)

Delete ProjectTemplateTasks

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
    api_instance = connectwise_psa.ProjectTemplateTasksApi(api_client)
    id = 56 # int | ProjectTemplateTaskId
    grand_parent_id = 56 # int | ProjectTemplateId
    parent_id = 56 # int | ProjectTemplateTicketId
    client_id = 'client_id_example' # str | 

    try:
        # Delete ProjectTemplateTasks
        api_instance.delete_project_project_templates_by_grand_parent_id_project_template_tickets_by_parent_id_tasks_by_id(id, grand_parent_id, parent_id, client_id)
    except Exception as e:
        print("Exception when calling ProjectTemplateTasksApi->delete_project_project_templates_by_grand_parent_id_project_template_tickets_by_parent_id_tasks_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ProjectTemplateTaskId | 
 **grand_parent_id** | **int**| ProjectTemplateId | 
 **parent_id** | **int**| ProjectTemplateTicketId | 
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

# **get_project_project_templates_by_grand_parent_id_project_template_tickets_by_parent_id_tasks**
> List[ProjectTemplateTask] get_project_project_templates_by_grand_parent_id_project_template_tickets_by_parent_id_tasks(grand_parent_id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of ProjectTemplateTasks

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.project_template_task import ProjectTemplateTask
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
    api_instance = connectwise_psa.ProjectTemplateTasksApi(api_client)
    grand_parent_id = 56 # int | ProjectTemplateId
    parent_id = 56 # int | ProjectTemplateTicketId
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
        # Get List of ProjectTemplateTasks
        api_response = api_instance.get_project_project_templates_by_grand_parent_id_project_template_tickets_by_parent_id_tasks(grand_parent_id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of ProjectTemplateTasksApi->get_project_project_templates_by_grand_parent_id_project_template_tickets_by_parent_id_tasks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectTemplateTasksApi->get_project_project_templates_by_grand_parent_id_project_template_tickets_by_parent_id_tasks: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **grand_parent_id** | **int**| ProjectTemplateId | 
 **parent_id** | **int**| ProjectTemplateTicketId | 
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

[**List[ProjectTemplateTask]**](ProjectTemplateTask.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of projectTemplateTaskses |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_project_templates_by_grand_parent_id_project_template_tickets_by_parent_id_tasks_by_id**
> ProjectTemplateTask get_project_project_templates_by_grand_parent_id_project_template_tickets_by_parent_id_tasks_by_id(id, grand_parent_id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get ProjectTemplateTasks

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.project_template_task import ProjectTemplateTask
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
    api_instance = connectwise_psa.ProjectTemplateTasksApi(api_client)
    id = 56 # int | ProjectTemplateTaskId
    grand_parent_id = 56 # int | ProjectTemplateId
    parent_id = 56 # int | ProjectTemplateTicketId
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
        # Get ProjectTemplateTasks
        api_response = api_instance.get_project_project_templates_by_grand_parent_id_project_template_tickets_by_parent_id_tasks_by_id(id, grand_parent_id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of ProjectTemplateTasksApi->get_project_project_templates_by_grand_parent_id_project_template_tickets_by_parent_id_tasks_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectTemplateTasksApi->get_project_project_templates_by_grand_parent_id_project_template_tickets_by_parent_id_tasks_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ProjectTemplateTaskId | 
 **grand_parent_id** | **int**| ProjectTemplateId | 
 **parent_id** | **int**| ProjectTemplateTicketId | 
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

[**ProjectTemplateTask**](ProjectTemplateTask.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ProjectTemplateTask |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_project_templates_by_grand_parent_id_project_template_tickets_by_parent_id_tasks_count**
> Count get_project_project_templates_by_grand_parent_id_project_template_tickets_by_parent_id_tasks_count(grand_parent_id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Count of ProjectTemplateTasks

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
    api_instance = connectwise_psa.ProjectTemplateTasksApi(api_client)
    grand_parent_id = 56 # int | ProjectTemplateId
    parent_id = 56 # int | ProjectTemplateTicketId
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
        # Get Count of ProjectTemplateTasks
        api_response = api_instance.get_project_project_templates_by_grand_parent_id_project_template_tickets_by_parent_id_tasks_count(grand_parent_id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of ProjectTemplateTasksApi->get_project_project_templates_by_grand_parent_id_project_template_tickets_by_parent_id_tasks_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectTemplateTasksApi->get_project_project_templates_by_grand_parent_id_project_template_tickets_by_parent_id_tasks_count: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **grand_parent_id** | **int**| ProjectTemplateId | 
 **parent_id** | **int**| ProjectTemplateTicketId | 
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

# **patch_project_project_templates_by_grand_parent_id_project_template_tickets_by_parent_id_tasks_by_id**
> ProjectTemplateTask patch_project_project_templates_by_grand_parent_id_project_template_tickets_by_parent_id_tasks_by_id(id, grand_parent_id, parent_id, client_id, patch_operation)

Patch ProjectTemplateTasks

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.patch_operation import PatchOperation
from connectwise_psa.models.project_template_task import ProjectTemplateTask
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
    api_instance = connectwise_psa.ProjectTemplateTasksApi(api_client)
    id = 56 # int | ProjectTemplateTaskId
    grand_parent_id = 56 # int | ProjectTemplateId
    parent_id = 56 # int | ProjectTemplateTicketId
    client_id = 'client_id_example' # str | 
    patch_operation = [connectwise_psa.PatchOperation()] # List[PatchOperation] | List of PatchOperation

    try:
        # Patch ProjectTemplateTasks
        api_response = api_instance.patch_project_project_templates_by_grand_parent_id_project_template_tickets_by_parent_id_tasks_by_id(id, grand_parent_id, parent_id, client_id, patch_operation)
        print("The response of ProjectTemplateTasksApi->patch_project_project_templates_by_grand_parent_id_project_template_tickets_by_parent_id_tasks_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectTemplateTasksApi->patch_project_project_templates_by_grand_parent_id_project_template_tickets_by_parent_id_tasks_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ProjectTemplateTaskId | 
 **grand_parent_id** | **int**| ProjectTemplateId | 
 **parent_id** | **int**| ProjectTemplateTicketId | 
 **client_id** | **str**|  | 
 **patch_operation** | [**List[PatchOperation]**](PatchOperation.md)| List of PatchOperation | 

### Return type

[**ProjectTemplateTask**](ProjectTemplateTask.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ProjectTemplateTask |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_project_project_templates_by_grand_parent_id_project_template_tickets_by_parent_id_tasks**
> ProjectTemplateTask post_project_project_templates_by_grand_parent_id_project_template_tickets_by_parent_id_tasks(grand_parent_id, parent_id, client_id, project_template_task)

Post ProjectTemplateTasks

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.project_template_task import ProjectTemplateTask
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
    api_instance = connectwise_psa.ProjectTemplateTasksApi(api_client)
    grand_parent_id = 56 # int | ProjectTemplateId
    parent_id = 56 # int | ProjectTemplateTicketId
    client_id = 'client_id_example' # str | 
    project_template_task = connectwise_psa.ProjectTemplateTask() # ProjectTemplateTask | ProjectTemplateTask

    try:
        # Post ProjectTemplateTasks
        api_response = api_instance.post_project_project_templates_by_grand_parent_id_project_template_tickets_by_parent_id_tasks(grand_parent_id, parent_id, client_id, project_template_task)
        print("The response of ProjectTemplateTasksApi->post_project_project_templates_by_grand_parent_id_project_template_tickets_by_parent_id_tasks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectTemplateTasksApi->post_project_project_templates_by_grand_parent_id_project_template_tickets_by_parent_id_tasks: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **grand_parent_id** | **int**| ProjectTemplateId | 
 **parent_id** | **int**| ProjectTemplateTicketId | 
 **client_id** | **str**|  | 
 **project_template_task** | [**ProjectTemplateTask**](ProjectTemplateTask.md)| ProjectTemplateTask | 

### Return type

[**ProjectTemplateTask**](ProjectTemplateTask.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | ProjectTemplateTask |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_project_project_templates_by_grand_parent_id_project_template_tickets_by_parent_id_tasks_by_id**
> ProjectTemplateTask put_project_project_templates_by_grand_parent_id_project_template_tickets_by_parent_id_tasks_by_id(id, grand_parent_id, parent_id, client_id, project_template_task)

Put ProjectTemplateTasks

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.project_template_task import ProjectTemplateTask
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
    api_instance = connectwise_psa.ProjectTemplateTasksApi(api_client)
    id = 56 # int | ProjectTemplateTaskId
    grand_parent_id = 56 # int | ProjectTemplateId
    parent_id = 56 # int | ProjectTemplateTicketId
    client_id = 'client_id_example' # str | 
    project_template_task = connectwise_psa.ProjectTemplateTask() # ProjectTemplateTask | companyTypeAssociation

    try:
        # Put ProjectTemplateTasks
        api_response = api_instance.put_project_project_templates_by_grand_parent_id_project_template_tickets_by_parent_id_tasks_by_id(id, grand_parent_id, parent_id, client_id, project_template_task)
        print("The response of ProjectTemplateTasksApi->put_project_project_templates_by_grand_parent_id_project_template_tickets_by_parent_id_tasks_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectTemplateTasksApi->put_project_project_templates_by_grand_parent_id_project_template_tickets_by_parent_id_tasks_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ProjectTemplateTaskId | 
 **grand_parent_id** | **int**| ProjectTemplateId | 
 **parent_id** | **int**| ProjectTemplateTicketId | 
 **client_id** | **str**|  | 
 **project_template_task** | [**ProjectTemplateTask**](ProjectTemplateTask.md)| companyTypeAssociation | 

### Return type

[**ProjectTemplateTask**](ProjectTemplateTask.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ProjectTemplateTask |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

