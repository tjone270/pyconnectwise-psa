# connectwise_psa.WorkflowActionUserDefinedFieldsApi

All URIs are relative to *https://aus-api.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_system_workflows_userdefinedfields_actions_by_parent_id**](WorkflowActionUserDefinedFieldsApi.md#delete_system_workflows_userdefinedfields_actions_by_parent_id) | **DELETE** /system/workflows/userdefinedfields/actions/{parentId} | Delete WorkflowActionUserDefinedField
[**get_system_workflows_userdefinedfields_by_grandparent_id_actions_by_parent_id**](WorkflowActionUserDefinedFieldsApi.md#get_system_workflows_userdefinedfields_by_grandparent_id_actions_by_parent_id) | **GET** /system/workflows/userdefinedfields/events{grandparentId}/actions/{parentId} | Get List of WorkflowActionUserDefinedField
[**patch_system_workflows_userdefinedfields_by_id**](WorkflowActionUserDefinedFieldsApi.md#patch_system_workflows_userdefinedfields_by_id) | **PATCH** /system/workflows/userdefinedfields/{id} | Patch WorkflowActionUserDefinedField
[**post_system_workflows_userdefinedfields_events_by_grandparent_id**](WorkflowActionUserDefinedFieldsApi.md#post_system_workflows_userdefinedfields_events_by_grandparent_id) | **POST** /system/workflows/userdefinedfields/events/{grandparentId} | Post WorkflowActionUserDefinedField
[**put_system_workflows_userdefinedfields_by_id**](WorkflowActionUserDefinedFieldsApi.md#put_system_workflows_userdefinedfields_by_id) | **PUT** /system/workflows/userdefinedfields/{id} | Put WorkflowActionUserDefinedField


# **delete_system_workflows_userdefinedfields_actions_by_parent_id**
> delete_system_workflows_userdefinedfields_actions_by_parent_id(parent_id, client_id)

Delete WorkflowActionUserDefinedField

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
    api_instance = connectwise_psa.WorkflowActionUserDefinedFieldsApi(api_client)
    parent_id = 56 # int | actionId
    client_id = 'client_id_example' # str | 

    try:
        # Delete WorkflowActionUserDefinedField
        api_instance.delete_system_workflows_userdefinedfields_actions_by_parent_id(parent_id, client_id)
    except Exception as e:
        print("Exception when calling WorkflowActionUserDefinedFieldsApi->delete_system_workflows_userdefinedfields_actions_by_parent_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| actionId | 
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

# **get_system_workflows_userdefinedfields_by_grandparent_id_actions_by_parent_id**
> List[WorkflowActionUserDefinedField] get_system_workflows_userdefinedfields_by_grandparent_id_actions_by_parent_id(parent_id, grandparent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of WorkflowActionUserDefinedField

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.workflow_action_user_defined_field import WorkflowActionUserDefinedField
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
    api_instance = connectwise_psa.WorkflowActionUserDefinedFieldsApi(api_client)
    parent_id = 56 # int | actionId
    grandparent_id = 56 # int | evnetId
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
        # Get List of WorkflowActionUserDefinedField
        api_response = api_instance.get_system_workflows_userdefinedfields_by_grandparent_id_actions_by_parent_id(parent_id, grandparent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of WorkflowActionUserDefinedFieldsApi->get_system_workflows_userdefinedfields_by_grandparent_id_actions_by_parent_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkflowActionUserDefinedFieldsApi->get_system_workflows_userdefinedfields_by_grandparent_id_actions_by_parent_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| actionId | 
 **grandparent_id** | **int**| evnetId | 
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

[**List[WorkflowActionUserDefinedField]**](WorkflowActionUserDefinedField.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of WorkflowActionUserDefinedField |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_system_workflows_userdefinedfields_by_id**
> WorkflowActionUserDefinedField patch_system_workflows_userdefinedfields_by_id(id, client_id, patch_operation)

Patch WorkflowActionUserDefinedField

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.patch_operation import PatchOperation
from connectwise_psa.models.workflow_action_user_defined_field import WorkflowActionUserDefinedField
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
    api_instance = connectwise_psa.WorkflowActionUserDefinedFieldsApi(api_client)
    id = 56 # int | workflowActionUserDefinedFieldId
    client_id = 'client_id_example' # str | 
    patch_operation = [connectwise_psa.PatchOperation()] # List[PatchOperation] | List of PatchOperation

    try:
        # Patch WorkflowActionUserDefinedField
        api_response = api_instance.patch_system_workflows_userdefinedfields_by_id(id, client_id, patch_operation)
        print("The response of WorkflowActionUserDefinedFieldsApi->patch_system_workflows_userdefinedfields_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkflowActionUserDefinedFieldsApi->patch_system_workflows_userdefinedfields_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| workflowActionUserDefinedFieldId | 
 **client_id** | **str**|  | 
 **patch_operation** | [**List[PatchOperation]**](PatchOperation.md)| List of PatchOperation | 

### Return type

[**WorkflowActionUserDefinedField**](WorkflowActionUserDefinedField.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | WorkflowActionUserDefinedField |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_system_workflows_userdefinedfields_events_by_grandparent_id**
> WorkflowActionUserDefinedField post_system_workflows_userdefinedfields_events_by_grandparent_id(grandparent_id, client_id, workflow_action_user_defined_field)

Post WorkflowActionUserDefinedField

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.workflow_action_user_defined_field import WorkflowActionUserDefinedField
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
    api_instance = connectwise_psa.WorkflowActionUserDefinedFieldsApi(api_client)
    grandparent_id = 56 # int | eventId
    client_id = 'client_id_example' # str | 
    workflow_action_user_defined_field = connectwise_psa.WorkflowActionUserDefinedField() # WorkflowActionUserDefinedField | workflowActionUserDefinedField

    try:
        # Post WorkflowActionUserDefinedField
        api_response = api_instance.post_system_workflows_userdefinedfields_events_by_grandparent_id(grandparent_id, client_id, workflow_action_user_defined_field)
        print("The response of WorkflowActionUserDefinedFieldsApi->post_system_workflows_userdefinedfields_events_by_grandparent_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkflowActionUserDefinedFieldsApi->post_system_workflows_userdefinedfields_events_by_grandparent_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **grandparent_id** | **int**| eventId | 
 **client_id** | **str**|  | 
 **workflow_action_user_defined_field** | [**WorkflowActionUserDefinedField**](WorkflowActionUserDefinedField.md)| workflowActionUserDefinedField | 

### Return type

[**WorkflowActionUserDefinedField**](WorkflowActionUserDefinedField.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | WorkflowActionUserDefinedField |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_system_workflows_userdefinedfields_by_id**
> WorkflowActionUserDefinedField put_system_workflows_userdefinedfields_by_id(id, client_id, workflow_action_user_defined_field)

Put WorkflowActionUserDefinedField

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.workflow_action_user_defined_field import WorkflowActionUserDefinedField
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
    api_instance = connectwise_psa.WorkflowActionUserDefinedFieldsApi(api_client)
    id = 56 # int | workflowActionUserDefinedFieldId
    client_id = 'client_id_example' # str | 
    workflow_action_user_defined_field = connectwise_psa.WorkflowActionUserDefinedField() # WorkflowActionUserDefinedField | workflowActionUserDefinedField

    try:
        # Put WorkflowActionUserDefinedField
        api_response = api_instance.put_system_workflows_userdefinedfields_by_id(id, client_id, workflow_action_user_defined_field)
        print("The response of WorkflowActionUserDefinedFieldsApi->put_system_workflows_userdefinedfields_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkflowActionUserDefinedFieldsApi->put_system_workflows_userdefinedfields_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| workflowActionUserDefinedFieldId | 
 **client_id** | **str**|  | 
 **workflow_action_user_defined_field** | [**WorkflowActionUserDefinedField**](WorkflowActionUserDefinedField.md)| workflowActionUserDefinedField | 

### Return type

[**WorkflowActionUserDefinedField**](WorkflowActionUserDefinedField.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | WorkflowActionUserDefinedField |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

