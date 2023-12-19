# connectwise_psa.WorkflowActionAutomateParametersApi

All URIs are relative to *https://aus-api.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_system_workflow_actions_by_parent_id_automate_parameters_by_id**](WorkflowActionAutomateParametersApi.md#delete_system_workflow_actions_by_parent_id_automate_parameters_by_id) | **DELETE** /system/workflowActions/{parentId}/automateParameters/{id} | Delete WorkflowActionAutomateParameter
[**get_system_workflow_actions_by_parent_id_automate_parameters**](WorkflowActionAutomateParametersApi.md#get_system_workflow_actions_by_parent_id_automate_parameters) | **GET** /system/workflowActions/{parentId}/automateParameters | Get List of WorkflowActionAutomateParameter
[**get_system_workflow_actions_by_parent_id_automate_parameters_by_id**](WorkflowActionAutomateParametersApi.md#get_system_workflow_actions_by_parent_id_automate_parameters_by_id) | **GET** /system/workflowActions/{parentId}/automateParameters/{id} | Get WorkflowActionAutomateParameter
[**get_system_workflow_actions_by_parent_id_automate_parameters_count**](WorkflowActionAutomateParametersApi.md#get_system_workflow_actions_by_parent_id_automate_parameters_count) | **GET** /system/workflowActions/{parentId}/automateParameters/count | Get Count of WorkflowActionAutomateParameter
[**patch_system_workflow_actions_by_parent_id_automate_parameters_by_id**](WorkflowActionAutomateParametersApi.md#patch_system_workflow_actions_by_parent_id_automate_parameters_by_id) | **PATCH** /system/workflowActions/{parentId}/automateParameters/{id} | Patch WorkflowActionAutomateParameter
[**post_system_workflow_actions_by_parent_id_automate_parameters**](WorkflowActionAutomateParametersApi.md#post_system_workflow_actions_by_parent_id_automate_parameters) | **POST** /system/workflowActions/{parentId}/automateParameters | Post WorkflowActionAutomateParameter
[**put_system_workflow_actions_by_parent_id_automate_parameters_by_id**](WorkflowActionAutomateParametersApi.md#put_system_workflow_actions_by_parent_id_automate_parameters_by_id) | **PUT** /system/workflowActions/{parentId}/automateParameters/{id} | Put WorkflowActionAutomateParameter


# **delete_system_workflow_actions_by_parent_id_automate_parameters_by_id**
> delete_system_workflow_actions_by_parent_id_automate_parameters_by_id(id, parent_id, client_id)

Delete WorkflowActionAutomateParameter

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
    api_instance = connectwise_psa.WorkflowActionAutomateParametersApi(api_client)
    id = 56 # int | automateParameterId
    parent_id = 56 # int | workflowActionId
    client_id = 'client_id_example' # str | 

    try:
        # Delete WorkflowActionAutomateParameter
        api_instance.delete_system_workflow_actions_by_parent_id_automate_parameters_by_id(id, parent_id, client_id)
    except Exception as e:
        print("Exception when calling WorkflowActionAutomateParametersApi->delete_system_workflow_actions_by_parent_id_automate_parameters_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| automateParameterId | 
 **parent_id** | **int**| workflowActionId | 
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

# **get_system_workflow_actions_by_parent_id_automate_parameters**
> List[WorkflowActionAutomateParameter] get_system_workflow_actions_by_parent_id_automate_parameters(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of WorkflowActionAutomateParameter

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.workflow_action_automate_parameter import WorkflowActionAutomateParameter
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
    api_instance = connectwise_psa.WorkflowActionAutomateParametersApi(api_client)
    parent_id = 56 # int | workflowActionId
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
        # Get List of WorkflowActionAutomateParameter
        api_response = api_instance.get_system_workflow_actions_by_parent_id_automate_parameters(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of WorkflowActionAutomateParametersApi->get_system_workflow_actions_by_parent_id_automate_parameters:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkflowActionAutomateParametersApi->get_system_workflow_actions_by_parent_id_automate_parameters: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| workflowActionId | 
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

[**List[WorkflowActionAutomateParameter]**](WorkflowActionAutomateParameter.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of WorkflowActionAutomateParameter |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_system_workflow_actions_by_parent_id_automate_parameters_by_id**
> WorkflowActionAutomateParameter get_system_workflow_actions_by_parent_id_automate_parameters_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get WorkflowActionAutomateParameter

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.workflow_action_automate_parameter import WorkflowActionAutomateParameter
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
    api_instance = connectwise_psa.WorkflowActionAutomateParametersApi(api_client)
    id = 56 # int | automateParameterId
    parent_id = 56 # int | workflowActionId
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
        # Get WorkflowActionAutomateParameter
        api_response = api_instance.get_system_workflow_actions_by_parent_id_automate_parameters_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of WorkflowActionAutomateParametersApi->get_system_workflow_actions_by_parent_id_automate_parameters_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkflowActionAutomateParametersApi->get_system_workflow_actions_by_parent_id_automate_parameters_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| automateParameterId | 
 **parent_id** | **int**| workflowActionId | 
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

[**WorkflowActionAutomateParameter**](WorkflowActionAutomateParameter.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | WorkflowActionAutomateParameter |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_system_workflow_actions_by_parent_id_automate_parameters_count**
> Count get_system_workflow_actions_by_parent_id_automate_parameters_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Count of WorkflowActionAutomateParameter

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
    api_instance = connectwise_psa.WorkflowActionAutomateParametersApi(api_client)
    parent_id = 56 # int | workflowActionId
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
        # Get Count of WorkflowActionAutomateParameter
        api_response = api_instance.get_system_workflow_actions_by_parent_id_automate_parameters_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of WorkflowActionAutomateParametersApi->get_system_workflow_actions_by_parent_id_automate_parameters_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkflowActionAutomateParametersApi->get_system_workflow_actions_by_parent_id_automate_parameters_count: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| workflowActionId | 
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

# **patch_system_workflow_actions_by_parent_id_automate_parameters_by_id**
> WorkflowActionAutomateParameter patch_system_workflow_actions_by_parent_id_automate_parameters_by_id(id, parent_id, client_id, patch_operation)

Patch WorkflowActionAutomateParameter

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.patch_operation import PatchOperation
from connectwise_psa.models.workflow_action_automate_parameter import WorkflowActionAutomateParameter
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
    api_instance = connectwise_psa.WorkflowActionAutomateParametersApi(api_client)
    id = 56 # int | automateParameterId
    parent_id = 56 # int | workflowActionId
    client_id = 'client_id_example' # str | 
    patch_operation = [connectwise_psa.PatchOperation()] # List[PatchOperation] | List of PatchOperation

    try:
        # Patch WorkflowActionAutomateParameter
        api_response = api_instance.patch_system_workflow_actions_by_parent_id_automate_parameters_by_id(id, parent_id, client_id, patch_operation)
        print("The response of WorkflowActionAutomateParametersApi->patch_system_workflow_actions_by_parent_id_automate_parameters_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkflowActionAutomateParametersApi->patch_system_workflow_actions_by_parent_id_automate_parameters_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| automateParameterId | 
 **parent_id** | **int**| workflowActionId | 
 **client_id** | **str**|  | 
 **patch_operation** | [**List[PatchOperation]**](PatchOperation.md)| List of PatchOperation | 

### Return type

[**WorkflowActionAutomateParameter**](WorkflowActionAutomateParameter.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | WorkflowActionAutomateParameter |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_system_workflow_actions_by_parent_id_automate_parameters**
> WorkflowActionAutomateParameter post_system_workflow_actions_by_parent_id_automate_parameters(parent_id, client_id, workflow_action_automate_parameter)

Post WorkflowActionAutomateParameter

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.workflow_action_automate_parameter import WorkflowActionAutomateParameter
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
    api_instance = connectwise_psa.WorkflowActionAutomateParametersApi(api_client)
    parent_id = 56 # int | workflowActionId
    client_id = 'client_id_example' # str | 
    workflow_action_automate_parameter = connectwise_psa.WorkflowActionAutomateParameter() # WorkflowActionAutomateParameter | workflowActionAutomateParameter

    try:
        # Post WorkflowActionAutomateParameter
        api_response = api_instance.post_system_workflow_actions_by_parent_id_automate_parameters(parent_id, client_id, workflow_action_automate_parameter)
        print("The response of WorkflowActionAutomateParametersApi->post_system_workflow_actions_by_parent_id_automate_parameters:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkflowActionAutomateParametersApi->post_system_workflow_actions_by_parent_id_automate_parameters: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| workflowActionId | 
 **client_id** | **str**|  | 
 **workflow_action_automate_parameter** | [**WorkflowActionAutomateParameter**](WorkflowActionAutomateParameter.md)| workflowActionAutomateParameter | 

### Return type

[**WorkflowActionAutomateParameter**](WorkflowActionAutomateParameter.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | WorkflowActionAutomateParameter |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_system_workflow_actions_by_parent_id_automate_parameters_by_id**
> WorkflowActionAutomateParameter put_system_workflow_actions_by_parent_id_automate_parameters_by_id(id, parent_id, client_id, workflow_action_automate_parameter)

Put WorkflowActionAutomateParameter

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.workflow_action_automate_parameter import WorkflowActionAutomateParameter
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
    api_instance = connectwise_psa.WorkflowActionAutomateParametersApi(api_client)
    id = 56 # int | automateParameterId
    parent_id = 56 # int | workflowActionId
    client_id = 'client_id_example' # str | 
    workflow_action_automate_parameter = connectwise_psa.WorkflowActionAutomateParameter() # WorkflowActionAutomateParameter | workflowActionAutomateParameter

    try:
        # Put WorkflowActionAutomateParameter
        api_response = api_instance.put_system_workflow_actions_by_parent_id_automate_parameters_by_id(id, parent_id, client_id, workflow_action_automate_parameter)
        print("The response of WorkflowActionAutomateParametersApi->put_system_workflow_actions_by_parent_id_automate_parameters_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkflowActionAutomateParametersApi->put_system_workflow_actions_by_parent_id_automate_parameters_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| automateParameterId | 
 **parent_id** | **int**| workflowActionId | 
 **client_id** | **str**|  | 
 **workflow_action_automate_parameter** | [**WorkflowActionAutomateParameter**](WorkflowActionAutomateParameter.md)| workflowActionAutomateParameter | 

### Return type

[**WorkflowActionAutomateParameter**](WorkflowActionAutomateParameter.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | WorkflowActionAutomateParameter |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

