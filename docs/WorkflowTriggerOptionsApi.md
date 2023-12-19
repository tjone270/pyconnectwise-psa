# connectwise_psa.WorkflowTriggerOptionsApi

All URIs are relative to *https://api-aus.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_system_workflows_by_grandparent_id_triggers_by_parent_id_options**](WorkflowTriggerOptionsApi.md#get_system_workflows_by_grandparent_id_triggers_by_parent_id_options) | **GET** /system/workflows/{grandparentId}/triggers/{parentId}/options | Get List of WorkflowTriggerOption
[**get_system_workflows_by_grandparent_id_triggers_by_parent_id_options_count**](WorkflowTriggerOptionsApi.md#get_system_workflows_by_grandparent_id_triggers_by_parent_id_options_count) | **GET** /system/workflows/{grandparentId}/triggers/{parentId}/options/count | Get Count of WorkflowTriggerOption


# **get_system_workflows_by_grandparent_id_triggers_by_parent_id_options**
> List[WorkflowTriggerOption] get_system_workflows_by_grandparent_id_triggers_by_parent_id_options(parent_id, grandparent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of WorkflowTriggerOption

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.workflow_trigger_option import WorkflowTriggerOption
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
    api_instance = connectwise_psa.WorkflowTriggerOptionsApi(api_client)
    parent_id = 56 # int | triggerId
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
        # Get List of WorkflowTriggerOption
        api_response = api_instance.get_system_workflows_by_grandparent_id_triggers_by_parent_id_options(parent_id, grandparent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of WorkflowTriggerOptionsApi->get_system_workflows_by_grandparent_id_triggers_by_parent_id_options:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkflowTriggerOptionsApi->get_system_workflows_by_grandparent_id_triggers_by_parent_id_options: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| triggerId | 
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

[**List[WorkflowTriggerOption]**](WorkflowTriggerOption.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of WorkflowTriggerOption |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_system_workflows_by_grandparent_id_triggers_by_parent_id_options_count**
> Count get_system_workflows_by_grandparent_id_triggers_by_parent_id_options_count(parent_id, grandparent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Count of WorkflowTriggerOption

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
    api_instance = connectwise_psa.WorkflowTriggerOptionsApi(api_client)
    parent_id = 56 # int | triggerId
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
        # Get Count of WorkflowTriggerOption
        api_response = api_instance.get_system_workflows_by_grandparent_id_triggers_by_parent_id_options_count(parent_id, grandparent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of WorkflowTriggerOptionsApi->get_system_workflows_by_grandparent_id_triggers_by_parent_id_options_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkflowTriggerOptionsApi->get_system_workflows_by_grandparent_id_triggers_by_parent_id_options_count: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| triggerId | 
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

