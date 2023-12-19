# connectwise_psa.ProjectPhasesApi

All URIs are relative to *https://api-aus.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_project_projects_by_parent_id_phases_by_id**](ProjectPhasesApi.md#delete_project_projects_by_parent_id_phases_by_id) | **DELETE** /project/projects/{parentId}/phases/{id} | Delete ProjectPhase
[**get_project_projects_by_parent_id_phases**](ProjectPhasesApi.md#get_project_projects_by_parent_id_phases) | **GET** /project/projects/{parentId}/phases | Get List of ProjectPhase
[**get_project_projects_by_parent_id_phases_by_id**](ProjectPhasesApi.md#get_project_projects_by_parent_id_phases_by_id) | **GET** /project/projects/{parentId}/phases/{id} | Get ProjectPhase
[**get_project_projects_by_parent_id_phases_count**](ProjectPhasesApi.md#get_project_projects_by_parent_id_phases_count) | **GET** /project/projects/{parentId}/phases/count | Get Count of ProjectPhase
[**patch_project_projects_by_parent_id_phases_by_id**](ProjectPhasesApi.md#patch_project_projects_by_parent_id_phases_by_id) | **PATCH** /project/projects/{parentId}/phases/{id} | Patch ProjectPhase
[**post_project_projects_by_parent_id_phases**](ProjectPhasesApi.md#post_project_projects_by_parent_id_phases) | **POST** /project/projects/{parentId}/phases | Post ProjectPhase
[**put_project_projects_by_parent_id_phases_by_id**](ProjectPhasesApi.md#put_project_projects_by_parent_id_phases_by_id) | **PUT** /project/projects/{parentId}/phases/{id} | Put ProjectPhase


# **delete_project_projects_by_parent_id_phases_by_id**
> delete_project_projects_by_parent_id_phases_by_id(id, parent_id, client_id)

Delete ProjectPhase

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
    api_instance = connectwise_psa.ProjectPhasesApi(api_client)
    id = 56 # int | phasId
    parent_id = 56 # int | projectId
    client_id = 'client_id_example' # str | 

    try:
        # Delete ProjectPhase
        api_instance.delete_project_projects_by_parent_id_phases_by_id(id, parent_id, client_id)
    except Exception as e:
        print("Exception when calling ProjectPhasesApi->delete_project_projects_by_parent_id_phases_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| phasId | 
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

# **get_project_projects_by_parent_id_phases**
> List[ProjectPhase] get_project_projects_by_parent_id_phases(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of ProjectPhase

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.project_phase import ProjectPhase
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
    api_instance = connectwise_psa.ProjectPhasesApi(api_client)
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
        # Get List of ProjectPhase
        api_response = api_instance.get_project_projects_by_parent_id_phases(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of ProjectPhasesApi->get_project_projects_by_parent_id_phases:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectPhasesApi->get_project_projects_by_parent_id_phases: %s\n" % e)
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

[**List[ProjectPhase]**](ProjectPhase.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of ProjectPhase |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_projects_by_parent_id_phases_by_id**
> ProjectPhase get_project_projects_by_parent_id_phases_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get ProjectPhase

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.project_phase import ProjectPhase
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
    api_instance = connectwise_psa.ProjectPhasesApi(api_client)
    id = 56 # int | phasId
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
        # Get ProjectPhase
        api_response = api_instance.get_project_projects_by_parent_id_phases_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of ProjectPhasesApi->get_project_projects_by_parent_id_phases_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectPhasesApi->get_project_projects_by_parent_id_phases_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| phasId | 
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

[**ProjectPhase**](ProjectPhase.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ProjectPhase |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_projects_by_parent_id_phases_count**
> Count get_project_projects_by_parent_id_phases_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Count of ProjectPhase

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
    api_instance = connectwise_psa.ProjectPhasesApi(api_client)
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
        # Get Count of ProjectPhase
        api_response = api_instance.get_project_projects_by_parent_id_phases_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of ProjectPhasesApi->get_project_projects_by_parent_id_phases_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectPhasesApi->get_project_projects_by_parent_id_phases_count: %s\n" % e)
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

# **patch_project_projects_by_parent_id_phases_by_id**
> ProjectPhase patch_project_projects_by_parent_id_phases_by_id(id, parent_id, client_id, patch_operation)

Patch ProjectPhase

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.patch_operation import PatchOperation
from connectwise_psa.models.project_phase import ProjectPhase
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
    api_instance = connectwise_psa.ProjectPhasesApi(api_client)
    id = 56 # int | phasId
    parent_id = 56 # int | projectId
    client_id = 'client_id_example' # str | 
    patch_operation = [connectwise_psa.PatchOperation()] # List[PatchOperation] | List of PatchOperation

    try:
        # Patch ProjectPhase
        api_response = api_instance.patch_project_projects_by_parent_id_phases_by_id(id, parent_id, client_id, patch_operation)
        print("The response of ProjectPhasesApi->patch_project_projects_by_parent_id_phases_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectPhasesApi->patch_project_projects_by_parent_id_phases_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| phasId | 
 **parent_id** | **int**| projectId | 
 **client_id** | **str**|  | 
 **patch_operation** | [**List[PatchOperation]**](PatchOperation.md)| List of PatchOperation | 

### Return type

[**ProjectPhase**](ProjectPhase.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ProjectPhase |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_project_projects_by_parent_id_phases**
> ProjectPhase post_project_projects_by_parent_id_phases(parent_id, client_id, project_phase)

Post ProjectPhase

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.project_phase import ProjectPhase
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
    api_instance = connectwise_psa.ProjectPhasesApi(api_client)
    parent_id = 56 # int | projectId
    client_id = 'client_id_example' # str | 
    project_phase = connectwise_psa.ProjectPhase() # ProjectPhase | projectPhase

    try:
        # Post ProjectPhase
        api_response = api_instance.post_project_projects_by_parent_id_phases(parent_id, client_id, project_phase)
        print("The response of ProjectPhasesApi->post_project_projects_by_parent_id_phases:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectPhasesApi->post_project_projects_by_parent_id_phases: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| projectId | 
 **client_id** | **str**|  | 
 **project_phase** | [**ProjectPhase**](ProjectPhase.md)| projectPhase | 

### Return type

[**ProjectPhase**](ProjectPhase.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | ProjectPhase |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_project_projects_by_parent_id_phases_by_id**
> ProjectPhase put_project_projects_by_parent_id_phases_by_id(id, parent_id, client_id, project_phase)

Put ProjectPhase

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.project_phase import ProjectPhase
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
    api_instance = connectwise_psa.ProjectPhasesApi(api_client)
    id = 56 # int | phasId
    parent_id = 56 # int | projectId
    client_id = 'client_id_example' # str | 
    project_phase = connectwise_psa.ProjectPhase() # ProjectPhase | projectPhase

    try:
        # Put ProjectPhase
        api_response = api_instance.put_project_projects_by_parent_id_phases_by_id(id, parent_id, client_id, project_phase)
        print("The response of ProjectPhasesApi->put_project_projects_by_parent_id_phases_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectPhasesApi->put_project_projects_by_parent_id_phases_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| phasId | 
 **parent_id** | **int**| projectId | 
 **client_id** | **str**|  | 
 **project_phase** | [**ProjectPhase**](ProjectPhase.md)| projectPhase | 

### Return type

[**ProjectPhase**](ProjectPhase.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ProjectPhase |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

