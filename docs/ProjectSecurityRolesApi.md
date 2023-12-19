# connectwise_psa.ProjectSecurityRolesApi

All URIs are relative to *https://aus-api.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_project_security_roles_by_id**](ProjectSecurityRolesApi.md#delete_project_security_roles_by_id) | **DELETE** /project/securityRoles/{id} | Delete ProjectSecurityRole
[**get_project_security_roles**](ProjectSecurityRolesApi.md#get_project_security_roles) | **GET** /project/securityRoles | Get List of ProjectSecurityRole
[**get_project_security_roles_by_id**](ProjectSecurityRolesApi.md#get_project_security_roles_by_id) | **GET** /project/securityRoles/{id} | Get ProjectSecurityRole
[**get_project_security_roles_count**](ProjectSecurityRolesApi.md#get_project_security_roles_count) | **GET** /project/securityRoles/count | Get Count of ProjectSecurityRole
[**patch_project_security_roles_by_id**](ProjectSecurityRolesApi.md#patch_project_security_roles_by_id) | **PATCH** /project/securityRoles/{id} | Patch ProjectSecurityRole
[**post_project_security_roles**](ProjectSecurityRolesApi.md#post_project_security_roles) | **POST** /project/securityRoles | Post ProjectSecurityRole
[**put_project_security_roles_by_id**](ProjectSecurityRolesApi.md#put_project_security_roles_by_id) | **PUT** /project/securityRoles/{id} | Put ProjectSecurityRole


# **delete_project_security_roles_by_id**
> delete_project_security_roles_by_id(id, client_id)

Delete ProjectSecurityRole

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
    api_instance = connectwise_psa.ProjectSecurityRolesApi(api_client)
    id = 56 # int | securityRoleId
    client_id = 'client_id_example' # str | 

    try:
        # Delete ProjectSecurityRole
        api_instance.delete_project_security_roles_by_id(id, client_id)
    except Exception as e:
        print("Exception when calling ProjectSecurityRolesApi->delete_project_security_roles_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| securityRoleId | 
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

# **get_project_security_roles**
> List[ProjectSecurityRole] get_project_security_roles(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of ProjectSecurityRole

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.project_security_role import ProjectSecurityRole
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
    api_instance = connectwise_psa.ProjectSecurityRolesApi(api_client)
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
        # Get List of ProjectSecurityRole
        api_response = api_instance.get_project_security_roles(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of ProjectSecurityRolesApi->get_project_security_roles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectSecurityRolesApi->get_project_security_roles: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

[**List[ProjectSecurityRole]**](ProjectSecurityRole.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of ProjectSecurityRole |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_security_roles_by_id**
> ProjectSecurityRole get_project_security_roles_by_id(id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get ProjectSecurityRole

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.project_security_role import ProjectSecurityRole
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
    api_instance = connectwise_psa.ProjectSecurityRolesApi(api_client)
    id = 56 # int | securityRoleId
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
        # Get ProjectSecurityRole
        api_response = api_instance.get_project_security_roles_by_id(id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of ProjectSecurityRolesApi->get_project_security_roles_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectSecurityRolesApi->get_project_security_roles_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| securityRoleId | 
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

[**ProjectSecurityRole**](ProjectSecurityRole.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ProjectSecurityRole |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_security_roles_count**
> Count get_project_security_roles_count(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Count of ProjectSecurityRole

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
    api_instance = connectwise_psa.ProjectSecurityRolesApi(api_client)
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
        # Get Count of ProjectSecurityRole
        api_response = api_instance.get_project_security_roles_count(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of ProjectSecurityRolesApi->get_project_security_roles_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectSecurityRolesApi->get_project_security_roles_count: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **patch_project_security_roles_by_id**
> ProjectSecurityRole patch_project_security_roles_by_id(id, client_id, patch_operation)

Patch ProjectSecurityRole

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.patch_operation import PatchOperation
from connectwise_psa.models.project_security_role import ProjectSecurityRole
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
    api_instance = connectwise_psa.ProjectSecurityRolesApi(api_client)
    id = 56 # int | securityRoleId
    client_id = 'client_id_example' # str | 
    patch_operation = [connectwise_psa.PatchOperation()] # List[PatchOperation] | List of PatchOperation

    try:
        # Patch ProjectSecurityRole
        api_response = api_instance.patch_project_security_roles_by_id(id, client_id, patch_operation)
        print("The response of ProjectSecurityRolesApi->patch_project_security_roles_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectSecurityRolesApi->patch_project_security_roles_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| securityRoleId | 
 **client_id** | **str**|  | 
 **patch_operation** | [**List[PatchOperation]**](PatchOperation.md)| List of PatchOperation | 

### Return type

[**ProjectSecurityRole**](ProjectSecurityRole.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ProjectSecurityRole |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_project_security_roles**
> ProjectSecurityRole post_project_security_roles(client_id, project_security_role)

Post ProjectSecurityRole

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.project_security_role import ProjectSecurityRole
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
    api_instance = connectwise_psa.ProjectSecurityRolesApi(api_client)
    client_id = 'client_id_example' # str | 
    project_security_role = connectwise_psa.ProjectSecurityRole() # ProjectSecurityRole | projectSecurityRole

    try:
        # Post ProjectSecurityRole
        api_response = api_instance.post_project_security_roles(client_id, project_security_role)
        print("The response of ProjectSecurityRolesApi->post_project_security_roles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectSecurityRolesApi->post_project_security_roles: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**|  | 
 **project_security_role** | [**ProjectSecurityRole**](ProjectSecurityRole.md)| projectSecurityRole | 

### Return type

[**ProjectSecurityRole**](ProjectSecurityRole.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | ProjectSecurityRole |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_project_security_roles_by_id**
> ProjectSecurityRole put_project_security_roles_by_id(id, client_id, project_security_role)

Put ProjectSecurityRole

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.project_security_role import ProjectSecurityRole
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
    api_instance = connectwise_psa.ProjectSecurityRolesApi(api_client)
    id = 56 # int | securityRoleId
    client_id = 'client_id_example' # str | 
    project_security_role = connectwise_psa.ProjectSecurityRole() # ProjectSecurityRole | projectSecurityRole

    try:
        # Put ProjectSecurityRole
        api_response = api_instance.put_project_security_roles_by_id(id, client_id, project_security_role)
        print("The response of ProjectSecurityRolesApi->put_project_security_roles_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectSecurityRolesApi->put_project_security_roles_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| securityRoleId | 
 **client_id** | **str**|  | 
 **project_security_role** | [**ProjectSecurityRole**](ProjectSecurityRole.md)| projectSecurityRole | 

### Return type

[**ProjectSecurityRole**](ProjectSecurityRole.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ProjectSecurityRole |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

