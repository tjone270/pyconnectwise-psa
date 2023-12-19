# connectwise_psa.TicketTasksApi

All URIs are relative to *https://api-aus.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_project_tickets_by_parent_id_tasks_by_id**](TicketTasksApi.md#delete_project_tickets_by_parent_id_tasks_by_id) | **DELETE** /project/tickets/{parentId}/tasks/{id} | Delete TicketTask
[**delete_service_tickets_by_parent_id_tasks_by_id**](TicketTasksApi.md#delete_service_tickets_by_parent_id_tasks_by_id) | **DELETE** /service/tickets/{parentId}/tasks/{id} | Delete Task
[**get_project_tickets_by_parent_id_tasks**](TicketTasksApi.md#get_project_tickets_by_parent_id_tasks) | **GET** /project/tickets/{parentId}/tasks | Get List of TicketTask
[**get_project_tickets_by_parent_id_tasks_by_id**](TicketTasksApi.md#get_project_tickets_by_parent_id_tasks_by_id) | **GET** /project/tickets/{parentId}/tasks/{id} | Get TicketTask
[**get_project_tickets_by_parent_id_tasks_count**](TicketTasksApi.md#get_project_tickets_by_parent_id_tasks_count) | **GET** /project/tickets/{parentId}/tasks/count | Get Count of TicketTask
[**get_service_tickets_by_parent_id_tasks**](TicketTasksApi.md#get_service_tickets_by_parent_id_tasks) | **GET** /service/tickets/{parentId}/tasks | Get List of Task
[**get_service_tickets_by_parent_id_tasks_by_id**](TicketTasksApi.md#get_service_tickets_by_parent_id_tasks_by_id) | **GET** /service/tickets/{parentId}/tasks/{id} | Get Task
[**get_service_tickets_by_parent_id_tasks_count**](TicketTasksApi.md#get_service_tickets_by_parent_id_tasks_count) | **GET** /service/tickets/{parentId}/tasks/count | Get Count of Task
[**patch_project_tickets_by_parent_id_tasks_by_id**](TicketTasksApi.md#patch_project_tickets_by_parent_id_tasks_by_id) | **PATCH** /project/tickets/{parentId}/tasks/{id} | Patch TicketTask
[**patch_service_tickets_by_parent_id_tasks_by_id**](TicketTasksApi.md#patch_service_tickets_by_parent_id_tasks_by_id) | **PATCH** /service/tickets/{parentId}/tasks/{id} | Patch Task
[**post_project_tickets_by_parent_id_tasks**](TicketTasksApi.md#post_project_tickets_by_parent_id_tasks) | **POST** /project/tickets/{parentId}/tasks | Post TicketTask
[**post_service_tickets_by_parent_id_tasks**](TicketTasksApi.md#post_service_tickets_by_parent_id_tasks) | **POST** /service/tickets/{parentId}/tasks | Post Task
[**put_project_tickets_by_parent_id_tasks_by_id**](TicketTasksApi.md#put_project_tickets_by_parent_id_tasks_by_id) | **PUT** /project/tickets/{parentId}/tasks/{id} | Put TicketTask
[**put_service_tickets_by_parent_id_tasks_by_id**](TicketTasksApi.md#put_service_tickets_by_parent_id_tasks_by_id) | **PUT** /service/tickets/{parentId}/tasks/{id} | Put Task


# **delete_project_tickets_by_parent_id_tasks_by_id**
> delete_project_tickets_by_parent_id_tasks_by_id(id, parent_id, client_id)

Delete TicketTask

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
    api_instance = connectwise_psa.TicketTasksApi(api_client)
    id = 56 # int | taskId
    parent_id = 56 # int | ticketId
    client_id = 'client_id_example' # str | 

    try:
        # Delete TicketTask
        api_instance.delete_project_tickets_by_parent_id_tasks_by_id(id, parent_id, client_id)
    except Exception as e:
        print("Exception when calling TicketTasksApi->delete_project_tickets_by_parent_id_tasks_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| taskId | 
 **parent_id** | **int**| ticketId | 
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

# **delete_service_tickets_by_parent_id_tasks_by_id**
> delete_service_tickets_by_parent_id_tasks_by_id(id, parent_id, client_id)

Delete Task

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
    api_instance = connectwise_psa.TicketTasksApi(api_client)
    id = 56 # int | taskId
    parent_id = 56 # int | ticketId
    client_id = 'client_id_example' # str | 

    try:
        # Delete Task
        api_instance.delete_service_tickets_by_parent_id_tasks_by_id(id, parent_id, client_id)
    except Exception as e:
        print("Exception when calling TicketTasksApi->delete_service_tickets_by_parent_id_tasks_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| taskId | 
 **parent_id** | **int**| ticketId | 
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

# **get_project_tickets_by_parent_id_tasks**
> List[TicketTask] get_project_tickets_by_parent_id_tasks(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of TicketTask

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.ticket_task import TicketTask
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
    api_instance = connectwise_psa.TicketTasksApi(api_client)
    parent_id = 56 # int | ticketId
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
        # Get List of TicketTask
        api_response = api_instance.get_project_tickets_by_parent_id_tasks(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of TicketTasksApi->get_project_tickets_by_parent_id_tasks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TicketTasksApi->get_project_tickets_by_parent_id_tasks: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| ticketId | 
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

[**List[TicketTask]**](TicketTask.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of TicketTask |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_tickets_by_parent_id_tasks_by_id**
> TicketTask get_project_tickets_by_parent_id_tasks_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get TicketTask

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.ticket_task import TicketTask
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
    api_instance = connectwise_psa.TicketTasksApi(api_client)
    id = 56 # int | taskId
    parent_id = 56 # int | ticketId
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
        # Get TicketTask
        api_response = api_instance.get_project_tickets_by_parent_id_tasks_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of TicketTasksApi->get_project_tickets_by_parent_id_tasks_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TicketTasksApi->get_project_tickets_by_parent_id_tasks_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| taskId | 
 **parent_id** | **int**| ticketId | 
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

[**TicketTask**](TicketTask.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | TicketTask |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_tickets_by_parent_id_tasks_count**
> Count get_project_tickets_by_parent_id_tasks_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Count of TicketTask

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
    api_instance = connectwise_psa.TicketTasksApi(api_client)
    parent_id = 56 # int | ticketId
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
        # Get Count of TicketTask
        api_response = api_instance.get_project_tickets_by_parent_id_tasks_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of TicketTasksApi->get_project_tickets_by_parent_id_tasks_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TicketTasksApi->get_project_tickets_by_parent_id_tasks_count: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| ticketId | 
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

# **get_service_tickets_by_parent_id_tasks**
> List[Task] get_service_tickets_by_parent_id_tasks(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of Task

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.task import Task
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
    api_instance = connectwise_psa.TicketTasksApi(api_client)
    parent_id = 56 # int | ticketId
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
        # Get List of Task
        api_response = api_instance.get_service_tickets_by_parent_id_tasks(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of TicketTasksApi->get_service_tickets_by_parent_id_tasks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TicketTasksApi->get_service_tickets_by_parent_id_tasks: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| ticketId | 
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

[**List[Task]**](Task.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of Task |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_service_tickets_by_parent_id_tasks_by_id**
> Task get_service_tickets_by_parent_id_tasks_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Task

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.task import Task
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
    api_instance = connectwise_psa.TicketTasksApi(api_client)
    id = 56 # int | taskId
    parent_id = 56 # int | ticketId
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
        # Get Task
        api_response = api_instance.get_service_tickets_by_parent_id_tasks_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of TicketTasksApi->get_service_tickets_by_parent_id_tasks_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TicketTasksApi->get_service_tickets_by_parent_id_tasks_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| taskId | 
 **parent_id** | **int**| ticketId | 
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

[**Task**](Task.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Task |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_service_tickets_by_parent_id_tasks_count**
> Count get_service_tickets_by_parent_id_tasks_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Count of Task

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
    api_instance = connectwise_psa.TicketTasksApi(api_client)
    parent_id = 56 # int | ticketId
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
        # Get Count of Task
        api_response = api_instance.get_service_tickets_by_parent_id_tasks_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of TicketTasksApi->get_service_tickets_by_parent_id_tasks_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TicketTasksApi->get_service_tickets_by_parent_id_tasks_count: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| ticketId | 
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

# **patch_project_tickets_by_parent_id_tasks_by_id**
> TicketTask patch_project_tickets_by_parent_id_tasks_by_id(id, parent_id, client_id, patch_operation)

Patch TicketTask

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.patch_operation import PatchOperation
from connectwise_psa.models.ticket_task import TicketTask
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
    api_instance = connectwise_psa.TicketTasksApi(api_client)
    id = 56 # int | taskId
    parent_id = 56 # int | ticketId
    client_id = 'client_id_example' # str | 
    patch_operation = [connectwise_psa.PatchOperation()] # List[PatchOperation] | List of PatchOperation

    try:
        # Patch TicketTask
        api_response = api_instance.patch_project_tickets_by_parent_id_tasks_by_id(id, parent_id, client_id, patch_operation)
        print("The response of TicketTasksApi->patch_project_tickets_by_parent_id_tasks_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TicketTasksApi->patch_project_tickets_by_parent_id_tasks_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| taskId | 
 **parent_id** | **int**| ticketId | 
 **client_id** | **str**|  | 
 **patch_operation** | [**List[PatchOperation]**](PatchOperation.md)| List of PatchOperation | 

### Return type

[**TicketTask**](TicketTask.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | TicketTask |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_service_tickets_by_parent_id_tasks_by_id**
> Task patch_service_tickets_by_parent_id_tasks_by_id(id, parent_id, client_id, patch_operation)

Patch Task

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.patch_operation import PatchOperation
from connectwise_psa.models.task import Task
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
    api_instance = connectwise_psa.TicketTasksApi(api_client)
    id = 56 # int | taskId
    parent_id = 56 # int | ticketId
    client_id = 'client_id_example' # str | 
    patch_operation = [connectwise_psa.PatchOperation()] # List[PatchOperation] | List of PatchOperation

    try:
        # Patch Task
        api_response = api_instance.patch_service_tickets_by_parent_id_tasks_by_id(id, parent_id, client_id, patch_operation)
        print("The response of TicketTasksApi->patch_service_tickets_by_parent_id_tasks_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TicketTasksApi->patch_service_tickets_by_parent_id_tasks_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| taskId | 
 **parent_id** | **int**| ticketId | 
 **client_id** | **str**|  | 
 **patch_operation** | [**List[PatchOperation]**](PatchOperation.md)| List of PatchOperation | 

### Return type

[**Task**](Task.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Task |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_project_tickets_by_parent_id_tasks**
> TicketTask post_project_tickets_by_parent_id_tasks(parent_id, client_id, ticket_task)

Post TicketTask

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.ticket_task import TicketTask
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
    api_instance = connectwise_psa.TicketTasksApi(api_client)
    parent_id = 56 # int | ticketId
    client_id = 'client_id_example' # str | 
    ticket_task = connectwise_psa.TicketTask() # TicketTask | ticketTask

    try:
        # Post TicketTask
        api_response = api_instance.post_project_tickets_by_parent_id_tasks(parent_id, client_id, ticket_task)
        print("The response of TicketTasksApi->post_project_tickets_by_parent_id_tasks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TicketTasksApi->post_project_tickets_by_parent_id_tasks: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| ticketId | 
 **client_id** | **str**|  | 
 **ticket_task** | [**TicketTask**](TicketTask.md)| ticketTask | 

### Return type

[**TicketTask**](TicketTask.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | TicketTask |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_service_tickets_by_parent_id_tasks**
> Task post_service_tickets_by_parent_id_tasks(parent_id, client_id, task)

Post Task

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.task import Task
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
    api_instance = connectwise_psa.TicketTasksApi(api_client)
    parent_id = 56 # int | ticketId
    client_id = 'client_id_example' # str | 
    task = connectwise_psa.Task() # Task | task

    try:
        # Post Task
        api_response = api_instance.post_service_tickets_by_parent_id_tasks(parent_id, client_id, task)
        print("The response of TicketTasksApi->post_service_tickets_by_parent_id_tasks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TicketTasksApi->post_service_tickets_by_parent_id_tasks: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| ticketId | 
 **client_id** | **str**|  | 
 **task** | [**Task**](Task.md)| task | 

### Return type

[**Task**](Task.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Task |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_project_tickets_by_parent_id_tasks_by_id**
> TicketTask put_project_tickets_by_parent_id_tasks_by_id(id, parent_id, client_id, ticket_task)

Put TicketTask

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.ticket_task import TicketTask
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
    api_instance = connectwise_psa.TicketTasksApi(api_client)
    id = 56 # int | taskId
    parent_id = 56 # int | ticketId
    client_id = 'client_id_example' # str | 
    ticket_task = connectwise_psa.TicketTask() # TicketTask | ticketTask

    try:
        # Put TicketTask
        api_response = api_instance.put_project_tickets_by_parent_id_tasks_by_id(id, parent_id, client_id, ticket_task)
        print("The response of TicketTasksApi->put_project_tickets_by_parent_id_tasks_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TicketTasksApi->put_project_tickets_by_parent_id_tasks_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| taskId | 
 **parent_id** | **int**| ticketId | 
 **client_id** | **str**|  | 
 **ticket_task** | [**TicketTask**](TicketTask.md)| ticketTask | 

### Return type

[**TicketTask**](TicketTask.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | TicketTask |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_service_tickets_by_parent_id_tasks_by_id**
> Task put_service_tickets_by_parent_id_tasks_by_id(id, parent_id, client_id, task)

Put Task

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.task import Task
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
    api_instance = connectwise_psa.TicketTasksApi(api_client)
    id = 56 # int | taskId
    parent_id = 56 # int | ticketId
    client_id = 'client_id_example' # str | 
    task = connectwise_psa.Task() # Task | task

    try:
        # Put Task
        api_response = api_instance.put_service_tickets_by_parent_id_tasks_by_id(id, parent_id, client_id, task)
        print("The response of TicketTasksApi->put_service_tickets_by_parent_id_tasks_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TicketTasksApi->put_service_tickets_by_parent_id_tasks_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| taskId | 
 **parent_id** | **int**| ticketId | 
 **client_id** | **str**|  | 
 **task** | [**Task**](Task.md)| task | 

### Return type

[**Task**](Task.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Task |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

