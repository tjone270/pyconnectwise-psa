# connectwise_psa.WorkflowActionsApi

All URIs are relative to *https://api-aus.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_system_workflows_by_grandparent_id_events_by_parent_id_actions_by_id**](WorkflowActionsApi.md#delete_system_workflows_by_grandparent_id_events_by_parent_id_actions_by_id) | **DELETE** /system/workflows/{grandparentId}/events/{parentId}/actions/{id} | Delete WorkflowAction
[**get_system_workflows_by_grandparent_id_events_by_parent_id_actions**](WorkflowActionsApi.md#get_system_workflows_by_grandparent_id_events_by_parent_id_actions) | **GET** /system/workflows/{grandparentId}/events/{parentId}/actions | Get List of WorkflowAction
[**get_system_workflows_by_grandparent_id_events_by_parent_id_actions_by_id**](WorkflowActionsApi.md#get_system_workflows_by_grandparent_id_events_by_parent_id_actions_by_id) | **GET** /system/workflows/{grandparentId}/events/{parentId}/actions/{id} | Get WorkflowAction
[**get_system_workflows_by_grandparent_id_events_by_parent_id_actions_count**](WorkflowActionsApi.md#get_system_workflows_by_grandparent_id_events_by_parent_id_actions_count) | **GET** /system/workflows/{grandparentId}/events/{parentId}/actions/count | Get Count of WorkflowAction
[**patch_system_workflows_by_grandparent_id_events_by_parent_id_actions_by_id**](WorkflowActionsApi.md#patch_system_workflows_by_grandparent_id_events_by_parent_id_actions_by_id) | **PATCH** /system/workflows/{grandparentId}/events/{parentId}/actions/{id} | Patch WorkflowAction
[**post_system_workflows_by_grandparent_id_events_by_parent_id_actions**](WorkflowActionsApi.md#post_system_workflows_by_grandparent_id_events_by_parent_id_actions) | **POST** /system/workflows/{grandparentId}/events/{parentId}/actions | Post WorkflowAction
[**put_system_workflows_by_grandparent_id_events_by_parent_id_actions_by_id**](WorkflowActionsApi.md#put_system_workflows_by_grandparent_id_events_by_parent_id_actions_by_id) | **PUT** /system/workflows/{grandparentId}/events/{parentId}/actions/{id} | Put WorkflowAction


# **delete_system_workflows_by_grandparent_id_events_by_parent_id_actions_by_id**
> delete_system_workflows_by_grandparent_id_events_by_parent_id_actions_by_id(id, parent_id, grandparent_id, client_id)

Delete WorkflowAction

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
    api_instance = connectwise_psa.WorkflowActionsApi(api_client)
    id = 56 # int | actionId
    parent_id = 56 # int | eventId
    grandparent_id = 56 # int | workflowId
    client_id = 'client_id_example' # str | 

    try:
        # Delete WorkflowAction
        api_instance.delete_system_workflows_by_grandparent_id_events_by_parent_id_actions_by_id(id, parent_id, grandparent_id, client_id)
    except Exception as e:
        print("Exception when calling WorkflowActionsApi->delete_system_workflows_by_grandparent_id_events_by_parent_id_actions_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| actionId | 
 **parent_id** | **int**| eventId | 
 **grandparent_id** | **int**| workflowId | 
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

# **get_system_workflows_by_grandparent_id_events_by_parent_id_actions**
> List[WorkflowAction] get_system_workflows_by_grandparent_id_events_by_parent_id_actions(parent_id, grandparent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of WorkflowAction

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.workflow_action import WorkflowAction
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
    api_instance = connectwise_psa.WorkflowActionsApi(api_client)
    parent_id = 56 # int | eventId
    grandparent_id = 56 # int | workflowId
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
        # Get List of WorkflowAction
        api_response = api_instance.get_system_workflows_by_grandparent_id_events_by_parent_id_actions(parent_id, grandparent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of WorkflowActionsApi->get_system_workflows_by_grandparent_id_events_by_parent_id_actions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkflowActionsApi->get_system_workflows_by_grandparent_id_events_by_parent_id_actions: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| eventId | 
 **grandparent_id** | **int**| workflowId | 
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

[**List[WorkflowAction]**](WorkflowAction.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of WorkflowAction |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_system_workflows_by_grandparent_id_events_by_parent_id_actions_by_id**
> WorkflowAction get_system_workflows_by_grandparent_id_events_by_parent_id_actions_by_id(id, parent_id, grandparent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get WorkflowAction

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.workflow_action import WorkflowAction
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
    api_instance = connectwise_psa.WorkflowActionsApi(api_client)
    id = 56 # int | actionId
    parent_id = 56 # int | eventId
    grandparent_id = 56 # int | workflowId
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
        # Get WorkflowAction
        api_response = api_instance.get_system_workflows_by_grandparent_id_events_by_parent_id_actions_by_id(id, parent_id, grandparent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of WorkflowActionsApi->get_system_workflows_by_grandparent_id_events_by_parent_id_actions_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkflowActionsApi->get_system_workflows_by_grandparent_id_events_by_parent_id_actions_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| actionId | 
 **parent_id** | **int**| eventId | 
 **grandparent_id** | **int**| workflowId | 
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

[**WorkflowAction**](WorkflowAction.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | WorkflowAction |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_system_workflows_by_grandparent_id_events_by_parent_id_actions_count**
> Count get_system_workflows_by_grandparent_id_events_by_parent_id_actions_count(parent_id, grandparent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Count of WorkflowAction

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
    api_instance = connectwise_psa.WorkflowActionsApi(api_client)
    parent_id = 56 # int | eventId
    grandparent_id = 56 # int | workflowId
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
        # Get Count of WorkflowAction
        api_response = api_instance.get_system_workflows_by_grandparent_id_events_by_parent_id_actions_count(parent_id, grandparent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of WorkflowActionsApi->get_system_workflows_by_grandparent_id_events_by_parent_id_actions_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkflowActionsApi->get_system_workflows_by_grandparent_id_events_by_parent_id_actions_count: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| eventId | 
 **grandparent_id** | **int**| workflowId | 
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

# **patch_system_workflows_by_grandparent_id_events_by_parent_id_actions_by_id**
> WorkflowAction patch_system_workflows_by_grandparent_id_events_by_parent_id_actions_by_id(id, parent_id, grandparent_id, client_id, patch_operation)

Patch WorkflowAction

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.patch_operation import PatchOperation
from connectwise_psa.models.workflow_action import WorkflowAction
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
    api_instance = connectwise_psa.WorkflowActionsApi(api_client)
    id = 56 # int | actionId
    parent_id = 56 # int | eventId
    grandparent_id = 56 # int | workflowId
    client_id = 'client_id_example' # str | 
    patch_operation = [connectwise_psa.PatchOperation()] # List[PatchOperation] | List of PatchOperation

    try:
        # Patch WorkflowAction
        api_response = api_instance.patch_system_workflows_by_grandparent_id_events_by_parent_id_actions_by_id(id, parent_id, grandparent_id, client_id, patch_operation)
        print("The response of WorkflowActionsApi->patch_system_workflows_by_grandparent_id_events_by_parent_id_actions_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkflowActionsApi->patch_system_workflows_by_grandparent_id_events_by_parent_id_actions_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| actionId | 
 **parent_id** | **int**| eventId | 
 **grandparent_id** | **int**| workflowId | 
 **client_id** | **str**|  | 
 **patch_operation** | [**List[PatchOperation]**](PatchOperation.md)| List of PatchOperation | 

### Return type

[**WorkflowAction**](WorkflowAction.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | WorkflowAction |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_system_workflows_by_grandparent_id_events_by_parent_id_actions**
> WorkflowAction post_system_workflows_by_grandparent_id_events_by_parent_id_actions(parent_id, grandparent_id, client_id, workflow_action)

Post WorkflowAction

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.workflow_action import WorkflowAction
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
    api_instance = connectwise_psa.WorkflowActionsApi(api_client)
    parent_id = 56 # int | eventId
    grandparent_id = 56 # int | workflowId
    client_id = 'client_id_example' # str | 
    workflow_action = connectwise_psa.WorkflowAction() # WorkflowAction | workflowAction

    try:
        # Post WorkflowAction
        api_response = api_instance.post_system_workflows_by_grandparent_id_events_by_parent_id_actions(parent_id, grandparent_id, client_id, workflow_action)
        print("The response of WorkflowActionsApi->post_system_workflows_by_grandparent_id_events_by_parent_id_actions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkflowActionsApi->post_system_workflows_by_grandparent_id_events_by_parent_id_actions: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| eventId | 
 **grandparent_id** | **int**| workflowId | 
 **client_id** | **str**|  | 
 **workflow_action** | [**WorkflowAction**](WorkflowAction.md)| workflowAction | 

### Return type

[**WorkflowAction**](WorkflowAction.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | WorkflowAction |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_system_workflows_by_grandparent_id_events_by_parent_id_actions_by_id**
> WorkflowAction put_system_workflows_by_grandparent_id_events_by_parent_id_actions_by_id(id, parent_id, grandparent_id, client_id, workflow_action)

Put WorkflowAction

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.workflow_action import WorkflowAction
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
    api_instance = connectwise_psa.WorkflowActionsApi(api_client)
    id = 56 # int | actionId
    parent_id = 56 # int | eventId
    grandparent_id = 56 # int | workflowId
    client_id = 'client_id_example' # str | 
    workflow_action = connectwise_psa.WorkflowAction() # WorkflowAction | workflowAction

    try:
        # Put WorkflowAction
        api_response = api_instance.put_system_workflows_by_grandparent_id_events_by_parent_id_actions_by_id(id, parent_id, grandparent_id, client_id, workflow_action)
        print("The response of WorkflowActionsApi->put_system_workflows_by_grandparent_id_events_by_parent_id_actions_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkflowActionsApi->put_system_workflows_by_grandparent_id_events_by_parent_id_actions_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| actionId | 
 **parent_id** | **int**| eventId | 
 **grandparent_id** | **int**| workflowId | 
 **client_id** | **str**|  | 
 **workflow_action** | [**WorkflowAction**](WorkflowAction.md)| workflowAction | 

### Return type

[**WorkflowAction**](WorkflowAction.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | WorkflowAction |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

