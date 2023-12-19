# connectwise_psa.WorkflowEventsApi

All URIs are relative to *https://api-aus.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_system_workflows_by_parent_id_events_by_id**](WorkflowEventsApi.md#delete_system_workflows_by_parent_id_events_by_id) | **DELETE** /system/workflows/{parentId}/events/{id} | Delete WorkflowEvent
[**get_system_workflows_by_parent_id_events**](WorkflowEventsApi.md#get_system_workflows_by_parent_id_events) | **GET** /system/workflows/{parentId}/events | Get List of WorkflowEvent
[**get_system_workflows_by_parent_id_events_by_id**](WorkflowEventsApi.md#get_system_workflows_by_parent_id_events_by_id) | **GET** /system/workflows/{parentId}/events/{id} | Get WorkflowEvent
[**get_system_workflows_by_parent_id_events_by_id_test**](WorkflowEventsApi.md#get_system_workflows_by_parent_id_events_by_id_test) | **GET** /system/workflows/{parentId}/events/{id}/test | Get workflow test results
[**get_system_workflows_by_parent_id_events_count**](WorkflowEventsApi.md#get_system_workflows_by_parent_id_events_count) | **GET** /system/workflows/{parentId}/events/count | Get Count of WorkflowEvent
[**patch_system_workflows_by_parent_id_events_by_id**](WorkflowEventsApi.md#patch_system_workflows_by_parent_id_events_by_id) | **PATCH** /system/workflows/{parentId}/events/{id} | Patch WorkflowEvent
[**post_system_workflows_by_parent_id_events**](WorkflowEventsApi.md#post_system_workflows_by_parent_id_events) | **POST** /system/workflows/{parentId}/events | Post WorkflowEvent
[**post_system_workflows_by_parent_id_events_by_id_copy**](WorkflowEventsApi.md#post_system_workflows_by_parent_id_events_by_id_copy) | **POST** /system/workflows/{parentId}/events/{id}/copy | Post WorkflowEvent
[**put_system_workflows_by_parent_id_events_by_id**](WorkflowEventsApi.md#put_system_workflows_by_parent_id_events_by_id) | **PUT** /system/workflows/{parentId}/events/{id} | Put WorkflowEvent


# **delete_system_workflows_by_parent_id_events_by_id**
> delete_system_workflows_by_parent_id_events_by_id(id, parent_id, client_id)

Delete WorkflowEvent

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
    api_instance = connectwise_psa.WorkflowEventsApi(api_client)
    id = 56 # int | eventId
    parent_id = 56 # int | workflowId
    client_id = 'client_id_example' # str | 

    try:
        # Delete WorkflowEvent
        api_instance.delete_system_workflows_by_parent_id_events_by_id(id, parent_id, client_id)
    except Exception as e:
        print("Exception when calling WorkflowEventsApi->delete_system_workflows_by_parent_id_events_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| eventId | 
 **parent_id** | **int**| workflowId | 
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

# **get_system_workflows_by_parent_id_events**
> List[WorkflowEvent] get_system_workflows_by_parent_id_events(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of WorkflowEvent

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.workflow_event import WorkflowEvent
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
    api_instance = connectwise_psa.WorkflowEventsApi(api_client)
    parent_id = 56 # int | workflowId
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
        # Get List of WorkflowEvent
        api_response = api_instance.get_system_workflows_by_parent_id_events(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of WorkflowEventsApi->get_system_workflows_by_parent_id_events:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkflowEventsApi->get_system_workflows_by_parent_id_events: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| workflowId | 
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

[**List[WorkflowEvent]**](WorkflowEvent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of WorkflowEvent |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_system_workflows_by_parent_id_events_by_id**
> WorkflowEvent get_system_workflows_by_parent_id_events_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get WorkflowEvent

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.workflow_event import WorkflowEvent
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
    api_instance = connectwise_psa.WorkflowEventsApi(api_client)
    id = 56 # int | eventId
    parent_id = 56 # int | workflowId
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
        # Get WorkflowEvent
        api_response = api_instance.get_system_workflows_by_parent_id_events_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of WorkflowEventsApi->get_system_workflows_by_parent_id_events_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkflowEventsApi->get_system_workflows_by_parent_id_events_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| eventId | 
 **parent_id** | **int**| workflowId | 
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

[**WorkflowEvent**](WorkflowEvent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | WorkflowEvent |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_system_workflows_by_parent_id_events_by_id_test**
> List[Dict[str, object]] get_system_workflows_by_parent_id_events_by_id_test(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get workflow test results

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
    api_instance = connectwise_psa.WorkflowEventsApi(api_client)
    id = 56 # int | eventId
    parent_id = 56 # int | workflowId
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
        # Get workflow test results
        api_response = api_instance.get_system_workflows_by_parent_id_events_by_id_test(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of WorkflowEventsApi->get_system_workflows_by_parent_id_events_by_id_test:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkflowEventsApi->get_system_workflows_by_parent_id_events_by_id_test: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| eventId | 
 **parent_id** | **int**| workflowId | 
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

**List[Dict[str, object]]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of test results |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_system_workflows_by_parent_id_events_count**
> Count get_system_workflows_by_parent_id_events_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Count of WorkflowEvent

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
    api_instance = connectwise_psa.WorkflowEventsApi(api_client)
    parent_id = 56 # int | workflowId
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
        # Get Count of WorkflowEvent
        api_response = api_instance.get_system_workflows_by_parent_id_events_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of WorkflowEventsApi->get_system_workflows_by_parent_id_events_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkflowEventsApi->get_system_workflows_by_parent_id_events_count: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| workflowId | 
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

# **patch_system_workflows_by_parent_id_events_by_id**
> WorkflowEvent patch_system_workflows_by_parent_id_events_by_id(id, parent_id, client_id, patch_operation)

Patch WorkflowEvent

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.patch_operation import PatchOperation
from connectwise_psa.models.workflow_event import WorkflowEvent
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
    api_instance = connectwise_psa.WorkflowEventsApi(api_client)
    id = 56 # int | eventId
    parent_id = 56 # int | workflowId
    client_id = 'client_id_example' # str | 
    patch_operation = [connectwise_psa.PatchOperation()] # List[PatchOperation] | List of PatchOperation

    try:
        # Patch WorkflowEvent
        api_response = api_instance.patch_system_workflows_by_parent_id_events_by_id(id, parent_id, client_id, patch_operation)
        print("The response of WorkflowEventsApi->patch_system_workflows_by_parent_id_events_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkflowEventsApi->patch_system_workflows_by_parent_id_events_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| eventId | 
 **parent_id** | **int**| workflowId | 
 **client_id** | **str**|  | 
 **patch_operation** | [**List[PatchOperation]**](PatchOperation.md)| List of PatchOperation | 

### Return type

[**WorkflowEvent**](WorkflowEvent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | WorkflowEvent |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_system_workflows_by_parent_id_events**
> WorkflowEvent post_system_workflows_by_parent_id_events(parent_id, client_id, workflow_event)

Post WorkflowEvent

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.workflow_event import WorkflowEvent
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
    api_instance = connectwise_psa.WorkflowEventsApi(api_client)
    parent_id = 56 # int | workflowId
    client_id = 'client_id_example' # str | 
    workflow_event = connectwise_psa.WorkflowEvent() # WorkflowEvent | workflowEvent

    try:
        # Post WorkflowEvent
        api_response = api_instance.post_system_workflows_by_parent_id_events(parent_id, client_id, workflow_event)
        print("The response of WorkflowEventsApi->post_system_workflows_by_parent_id_events:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkflowEventsApi->post_system_workflows_by_parent_id_events: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| workflowId | 
 **client_id** | **str**|  | 
 **workflow_event** | [**WorkflowEvent**](WorkflowEvent.md)| workflowEvent | 

### Return type

[**WorkflowEvent**](WorkflowEvent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | WorkflowEvent |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_system_workflows_by_parent_id_events_by_id_copy**
> WorkflowEvent post_system_workflows_by_parent_id_events_by_id_copy(id, parent_id, client_id)

Post WorkflowEvent

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.workflow_event import WorkflowEvent
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
    api_instance = connectwise_psa.WorkflowEventsApi(api_client)
    id = 56 # int | eventId
    parent_id = 56 # int | workflowId
    client_id = 'client_id_example' # str | 

    try:
        # Post WorkflowEvent
        api_response = api_instance.post_system_workflows_by_parent_id_events_by_id_copy(id, parent_id, client_id)
        print("The response of WorkflowEventsApi->post_system_workflows_by_parent_id_events_by_id_copy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkflowEventsApi->post_system_workflows_by_parent_id_events_by_id_copy: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| eventId | 
 **parent_id** | **int**| workflowId | 
 **client_id** | **str**|  | 

### Return type

[**WorkflowEvent**](WorkflowEvent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | WorkflowEvent |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_system_workflows_by_parent_id_events_by_id**
> WorkflowEvent put_system_workflows_by_parent_id_events_by_id(id, parent_id, client_id, workflow_event)

Put WorkflowEvent

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.workflow_event import WorkflowEvent
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
    api_instance = connectwise_psa.WorkflowEventsApi(api_client)
    id = 56 # int | eventId
    parent_id = 56 # int | workflowId
    client_id = 'client_id_example' # str | 
    workflow_event = connectwise_psa.WorkflowEvent() # WorkflowEvent | workflowEvent

    try:
        # Put WorkflowEvent
        api_response = api_instance.put_system_workflows_by_parent_id_events_by_id(id, parent_id, client_id, workflow_event)
        print("The response of WorkflowEventsApi->put_system_workflows_by_parent_id_events_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkflowEventsApi->put_system_workflows_by_parent_id_events_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| eventId | 
 **parent_id** | **int**| workflowId | 
 **client_id** | **str**|  | 
 **workflow_event** | [**WorkflowEvent**](WorkflowEvent.md)| workflowEvent | 

### Return type

[**WorkflowEvent**](WorkflowEvent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | WorkflowEvent |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

