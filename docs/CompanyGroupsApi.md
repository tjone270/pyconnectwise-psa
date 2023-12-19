# connectwise_psa.CompanyGroupsApi

All URIs are relative to *https://api-aus.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_company_companies_by_parent_id_groups_by_id**](CompanyGroupsApi.md#delete_company_companies_by_parent_id_groups_by_id) | **DELETE** /company/companies/{parentId}/groups/{id} | Delete CompanyGroup
[**get_company_companies_by_parent_id_groups**](CompanyGroupsApi.md#get_company_companies_by_parent_id_groups) | **GET** /company/companies/{parentId}/groups | Get List of CompanyGroup
[**get_company_companies_by_parent_id_groups_by_id**](CompanyGroupsApi.md#get_company_companies_by_parent_id_groups_by_id) | **GET** /company/companies/{parentId}/groups/{id} | Get CompanyGroup
[**get_company_companies_by_parent_id_groups_count**](CompanyGroupsApi.md#get_company_companies_by_parent_id_groups_count) | **GET** /company/companies/{parentId}/groups/count | Get Count of CompanyGroup
[**patch_company_companies_by_parent_id_groups_by_id**](CompanyGroupsApi.md#patch_company_companies_by_parent_id_groups_by_id) | **PATCH** /company/companies/{parentId}/groups/{id} | Patch CompanyGroup
[**post_company_companies_by_parent_id_groups**](CompanyGroupsApi.md#post_company_companies_by_parent_id_groups) | **POST** /company/companies/{parentId}/groups | Post CompanyGroup
[**put_company_companies_by_parent_id_groups_by_id**](CompanyGroupsApi.md#put_company_companies_by_parent_id_groups_by_id) | **PUT** /company/companies/{parentId}/groups/{id} | Put CompanyGroup


# **delete_company_companies_by_parent_id_groups_by_id**
> delete_company_companies_by_parent_id_groups_by_id(id, parent_id, client_id)

Delete CompanyGroup

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
    api_instance = connectwise_psa.CompanyGroupsApi(api_client)
    id = 56 # int | groupId
    parent_id = 56 # int | companyId
    client_id = 'client_id_example' # str | 

    try:
        # Delete CompanyGroup
        api_instance.delete_company_companies_by_parent_id_groups_by_id(id, parent_id, client_id)
    except Exception as e:
        print("Exception when calling CompanyGroupsApi->delete_company_companies_by_parent_id_groups_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| groupId | 
 **parent_id** | **int**| companyId | 
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

# **get_company_companies_by_parent_id_groups**
> List[CompanyGroup] get_company_companies_by_parent_id_groups(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of CompanyGroup

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.company_group import CompanyGroup
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
    api_instance = connectwise_psa.CompanyGroupsApi(api_client)
    parent_id = 56 # int | companyId
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
        # Get List of CompanyGroup
        api_response = api_instance.get_company_companies_by_parent_id_groups(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of CompanyGroupsApi->get_company_companies_by_parent_id_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompanyGroupsApi->get_company_companies_by_parent_id_groups: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| companyId | 
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

[**List[CompanyGroup]**](CompanyGroup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of CompanyGroup |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_company_companies_by_parent_id_groups_by_id**
> CompanyGroup get_company_companies_by_parent_id_groups_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get CompanyGroup

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.company_group import CompanyGroup
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
    api_instance = connectwise_psa.CompanyGroupsApi(api_client)
    id = 56 # int | groupId
    parent_id = 56 # int | companyId
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
        # Get CompanyGroup
        api_response = api_instance.get_company_companies_by_parent_id_groups_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of CompanyGroupsApi->get_company_companies_by_parent_id_groups_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompanyGroupsApi->get_company_companies_by_parent_id_groups_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| groupId | 
 **parent_id** | **int**| companyId | 
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

[**CompanyGroup**](CompanyGroup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | CompanyGroup |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_company_companies_by_parent_id_groups_count**
> Count get_company_companies_by_parent_id_groups_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Count of CompanyGroup

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
    api_instance = connectwise_psa.CompanyGroupsApi(api_client)
    parent_id = 56 # int | companyId
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
        # Get Count of CompanyGroup
        api_response = api_instance.get_company_companies_by_parent_id_groups_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of CompanyGroupsApi->get_company_companies_by_parent_id_groups_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompanyGroupsApi->get_company_companies_by_parent_id_groups_count: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| companyId | 
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

# **patch_company_companies_by_parent_id_groups_by_id**
> CompanyGroup patch_company_companies_by_parent_id_groups_by_id(id, parent_id, client_id, patch_operation)

Patch CompanyGroup

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.company_group import CompanyGroup
from connectwise_psa.models.patch_operation import PatchOperation
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
    api_instance = connectwise_psa.CompanyGroupsApi(api_client)
    id = 56 # int | groupId
    parent_id = 56 # int | companyId
    client_id = 'client_id_example' # str | 
    patch_operation = [connectwise_psa.PatchOperation()] # List[PatchOperation] | List of PatchOperation

    try:
        # Patch CompanyGroup
        api_response = api_instance.patch_company_companies_by_parent_id_groups_by_id(id, parent_id, client_id, patch_operation)
        print("The response of CompanyGroupsApi->patch_company_companies_by_parent_id_groups_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompanyGroupsApi->patch_company_companies_by_parent_id_groups_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| groupId | 
 **parent_id** | **int**| companyId | 
 **client_id** | **str**|  | 
 **patch_operation** | [**List[PatchOperation]**](PatchOperation.md)| List of PatchOperation | 

### Return type

[**CompanyGroup**](CompanyGroup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | CompanyGroup |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_company_companies_by_parent_id_groups**
> CompanyGroup post_company_companies_by_parent_id_groups(parent_id, client_id, company_group)

Post CompanyGroup

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.company_group import CompanyGroup
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
    api_instance = connectwise_psa.CompanyGroupsApi(api_client)
    parent_id = 56 # int | companyId
    client_id = 'client_id_example' # str | 
    company_group = connectwise_psa.CompanyGroup() # CompanyGroup | companyGroup

    try:
        # Post CompanyGroup
        api_response = api_instance.post_company_companies_by_parent_id_groups(parent_id, client_id, company_group)
        print("The response of CompanyGroupsApi->post_company_companies_by_parent_id_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompanyGroupsApi->post_company_companies_by_parent_id_groups: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| companyId | 
 **client_id** | **str**|  | 
 **company_group** | [**CompanyGroup**](CompanyGroup.md)| companyGroup | 

### Return type

[**CompanyGroup**](CompanyGroup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | CompanyGroup |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_company_companies_by_parent_id_groups_by_id**
> CompanyGroup put_company_companies_by_parent_id_groups_by_id(id, parent_id, client_id, company_group)

Put CompanyGroup

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.company_group import CompanyGroup
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
    api_instance = connectwise_psa.CompanyGroupsApi(api_client)
    id = 56 # int | groupId
    parent_id = 56 # int | companyId
    client_id = 'client_id_example' # str | 
    company_group = connectwise_psa.CompanyGroup() # CompanyGroup | companyGroup

    try:
        # Put CompanyGroup
        api_response = api_instance.put_company_companies_by_parent_id_groups_by_id(id, parent_id, client_id, company_group)
        print("The response of CompanyGroupsApi->put_company_companies_by_parent_id_groups_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompanyGroupsApi->put_company_companies_by_parent_id_groups_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| groupId | 
 **parent_id** | **int**| companyId | 
 **client_id** | **str**|  | 
 **company_group** | [**CompanyGroup**](CompanyGroup.md)| companyGroup | 

### Return type

[**CompanyGroup**](CompanyGroup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | CompanyGroup |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

