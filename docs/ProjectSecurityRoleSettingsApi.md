# connectwise_psa.ProjectSecurityRoleSettingsApi

All URIs are relative to *https://api-aus.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_project_security_roles_by_parent_id_settings**](ProjectSecurityRoleSettingsApi.md#get_project_security_roles_by_parent_id_settings) | **GET** /project/securityRoles/{parentId}/settings | Get List of ProjectSecurityRoleSetting
[**get_project_security_roles_by_parent_id_settings_by_id**](ProjectSecurityRoleSettingsApi.md#get_project_security_roles_by_parent_id_settings_by_id) | **GET** /project/securityRoles/{parentId}/settings/{id} | Get ProjectSecurityRoleSetting
[**get_project_security_roles_by_parent_id_settings_count**](ProjectSecurityRoleSettingsApi.md#get_project_security_roles_by_parent_id_settings_count) | **GET** /project/securityRoles/{parentId}/settings/count | Get Count of ProjectSecurityRoleSetting
[**patch_project_security_roles_by_parent_id_settings_by_id**](ProjectSecurityRoleSettingsApi.md#patch_project_security_roles_by_parent_id_settings_by_id) | **PATCH** /project/securityRoles/{parentId}/settings/{id} | Patch ProjectSecurityRoleSetting
[**put_project_security_roles_by_parent_id_settings_by_id**](ProjectSecurityRoleSettingsApi.md#put_project_security_roles_by_parent_id_settings_by_id) | **PUT** /project/securityRoles/{parentId}/settings/{id} | Put ProjectSecurityRoleSetting


# **get_project_security_roles_by_parent_id_settings**
> List[ProjectSecurityRoleSetting] get_project_security_roles_by_parent_id_settings(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of ProjectSecurityRoleSetting

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.project_security_role_setting import ProjectSecurityRoleSetting
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
    api_instance = connectwise_psa.ProjectSecurityRoleSettingsApi(api_client)
    parent_id = 56 # int | securityRoleId
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
        # Get List of ProjectSecurityRoleSetting
        api_response = api_instance.get_project_security_roles_by_parent_id_settings(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of ProjectSecurityRoleSettingsApi->get_project_security_roles_by_parent_id_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectSecurityRoleSettingsApi->get_project_security_roles_by_parent_id_settings: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| securityRoleId | 
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

[**List[ProjectSecurityRoleSetting]**](ProjectSecurityRoleSetting.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of ProjectSecurityRoleSetting |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_security_roles_by_parent_id_settings_by_id**
> ProjectSecurityRoleSetting get_project_security_roles_by_parent_id_settings_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get ProjectSecurityRoleSetting

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.project_security_role_setting import ProjectSecurityRoleSetting
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
    api_instance = connectwise_psa.ProjectSecurityRoleSettingsApi(api_client)
    id = 56 # int | settingId
    parent_id = 56 # int | securityRoleId
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
        # Get ProjectSecurityRoleSetting
        api_response = api_instance.get_project_security_roles_by_parent_id_settings_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of ProjectSecurityRoleSettingsApi->get_project_security_roles_by_parent_id_settings_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectSecurityRoleSettingsApi->get_project_security_roles_by_parent_id_settings_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| settingId | 
 **parent_id** | **int**| securityRoleId | 
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

[**ProjectSecurityRoleSetting**](ProjectSecurityRoleSetting.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ProjectSecurityRoleSetting |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_security_roles_by_parent_id_settings_count**
> Count get_project_security_roles_by_parent_id_settings_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Count of ProjectSecurityRoleSetting

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
    api_instance = connectwise_psa.ProjectSecurityRoleSettingsApi(api_client)
    parent_id = 56 # int | securityRoleId
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
        # Get Count of ProjectSecurityRoleSetting
        api_response = api_instance.get_project_security_roles_by_parent_id_settings_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of ProjectSecurityRoleSettingsApi->get_project_security_roles_by_parent_id_settings_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectSecurityRoleSettingsApi->get_project_security_roles_by_parent_id_settings_count: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| securityRoleId | 
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

# **patch_project_security_roles_by_parent_id_settings_by_id**
> ProjectSecurityRoleSetting patch_project_security_roles_by_parent_id_settings_by_id(id, parent_id, client_id, patch_operation)

Patch ProjectSecurityRoleSetting

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.patch_operation import PatchOperation
from connectwise_psa.models.project_security_role_setting import ProjectSecurityRoleSetting
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
    api_instance = connectwise_psa.ProjectSecurityRoleSettingsApi(api_client)
    id = 56 # int | settingId
    parent_id = 56 # int | securityRoleId
    client_id = 'client_id_example' # str | 
    patch_operation = [connectwise_psa.PatchOperation()] # List[PatchOperation] | List of PatchOperation

    try:
        # Patch ProjectSecurityRoleSetting
        api_response = api_instance.patch_project_security_roles_by_parent_id_settings_by_id(id, parent_id, client_id, patch_operation)
        print("The response of ProjectSecurityRoleSettingsApi->patch_project_security_roles_by_parent_id_settings_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectSecurityRoleSettingsApi->patch_project_security_roles_by_parent_id_settings_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| settingId | 
 **parent_id** | **int**| securityRoleId | 
 **client_id** | **str**|  | 
 **patch_operation** | [**List[PatchOperation]**](PatchOperation.md)| List of PatchOperation | 

### Return type

[**ProjectSecurityRoleSetting**](ProjectSecurityRoleSetting.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ProjectSecurityRoleSetting |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_project_security_roles_by_parent_id_settings_by_id**
> ProjectSecurityRoleSetting put_project_security_roles_by_parent_id_settings_by_id(id, parent_id, client_id, project_security_role_setting)

Put ProjectSecurityRoleSetting

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.project_security_role_setting import ProjectSecurityRoleSetting
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
    api_instance = connectwise_psa.ProjectSecurityRoleSettingsApi(api_client)
    id = 56 # int | settingId
    parent_id = 56 # int | securityRoleId
    client_id = 'client_id_example' # str | 
    project_security_role_setting = connectwise_psa.ProjectSecurityRoleSetting() # ProjectSecurityRoleSetting | projectSecurityRoleSetting

    try:
        # Put ProjectSecurityRoleSetting
        api_response = api_instance.put_project_security_roles_by_parent_id_settings_by_id(id, parent_id, client_id, project_security_role_setting)
        print("The response of ProjectSecurityRoleSettingsApi->put_project_security_roles_by_parent_id_settings_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectSecurityRoleSettingsApi->put_project_security_roles_by_parent_id_settings_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| settingId | 
 **parent_id** | **int**| securityRoleId | 
 **client_id** | **str**|  | 
 **project_security_role_setting** | [**ProjectSecurityRoleSetting**](ProjectSecurityRoleSetting.md)| projectSecurityRoleSetting | 

### Return type

[**ProjectSecurityRoleSetting**](ProjectSecurityRoleSetting.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ProjectSecurityRoleSetting |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

