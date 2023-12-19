# connectwise_psa.ContactGroupsApi

All URIs are relative to *https://aus-api.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_company_contacts_by_parent_id_groups_by_id**](ContactGroupsApi.md#delete_company_contacts_by_parent_id_groups_by_id) | **DELETE** /company/contacts/{parentId}/groups/{id} | Delete ContactGroup
[**get_company_contacts_by_parent_id_groups**](ContactGroupsApi.md#get_company_contacts_by_parent_id_groups) | **GET** /company/contacts/{parentId}/groups | Get List of ContactGroup
[**get_company_contacts_by_parent_id_groups_by_id**](ContactGroupsApi.md#get_company_contacts_by_parent_id_groups_by_id) | **GET** /company/contacts/{parentId}/groups/{id} | Get ContactGroup
[**get_company_contacts_by_parent_id_groups_count**](ContactGroupsApi.md#get_company_contacts_by_parent_id_groups_count) | **GET** /company/contacts/{parentId}/groups/count | Get Count of ContactGroup
[**patch_company_contacts_by_parent_id_groups_by_id**](ContactGroupsApi.md#patch_company_contacts_by_parent_id_groups_by_id) | **PATCH** /company/contacts/{parentId}/groups/{id} | Patch ContactGroup
[**post_company_contacts_by_parent_id_groups**](ContactGroupsApi.md#post_company_contacts_by_parent_id_groups) | **POST** /company/contacts/{parentId}/groups | Post ContactGroup
[**put_company_contacts_by_parent_id_groups_by_id**](ContactGroupsApi.md#put_company_contacts_by_parent_id_groups_by_id) | **PUT** /company/contacts/{parentId}/groups/{id} | Put ContactGroup


# **delete_company_contacts_by_parent_id_groups_by_id**
> delete_company_contacts_by_parent_id_groups_by_id(id, parent_id, client_id)

Delete ContactGroup

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
    api_instance = connectwise_psa.ContactGroupsApi(api_client)
    id = 56 # int | groupId
    parent_id = 56 # int | contactId
    client_id = 'client_id_example' # str | 

    try:
        # Delete ContactGroup
        api_instance.delete_company_contacts_by_parent_id_groups_by_id(id, parent_id, client_id)
    except Exception as e:
        print("Exception when calling ContactGroupsApi->delete_company_contacts_by_parent_id_groups_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| groupId | 
 **parent_id** | **int**| contactId | 
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

# **get_company_contacts_by_parent_id_groups**
> List[ContactGroup] get_company_contacts_by_parent_id_groups(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of ContactGroup

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.contact_group import ContactGroup
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
    api_instance = connectwise_psa.ContactGroupsApi(api_client)
    parent_id = 56 # int | contactId
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
        # Get List of ContactGroup
        api_response = api_instance.get_company_contacts_by_parent_id_groups(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of ContactGroupsApi->get_company_contacts_by_parent_id_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactGroupsApi->get_company_contacts_by_parent_id_groups: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| contactId | 
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

[**List[ContactGroup]**](ContactGroup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of ContactGroup |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_company_contacts_by_parent_id_groups_by_id**
> ContactGroup get_company_contacts_by_parent_id_groups_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get ContactGroup

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.contact_group import ContactGroup
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
    api_instance = connectwise_psa.ContactGroupsApi(api_client)
    id = 56 # int | groupId
    parent_id = 56 # int | contactId
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
        # Get ContactGroup
        api_response = api_instance.get_company_contacts_by_parent_id_groups_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of ContactGroupsApi->get_company_contacts_by_parent_id_groups_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactGroupsApi->get_company_contacts_by_parent_id_groups_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| groupId | 
 **parent_id** | **int**| contactId | 
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

[**ContactGroup**](ContactGroup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ContactGroup |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_company_contacts_by_parent_id_groups_count**
> Count get_company_contacts_by_parent_id_groups_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Count of ContactGroup

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
    api_instance = connectwise_psa.ContactGroupsApi(api_client)
    parent_id = 56 # int | contactId
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
        # Get Count of ContactGroup
        api_response = api_instance.get_company_contacts_by_parent_id_groups_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of ContactGroupsApi->get_company_contacts_by_parent_id_groups_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactGroupsApi->get_company_contacts_by_parent_id_groups_count: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| contactId | 
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

# **patch_company_contacts_by_parent_id_groups_by_id**
> ContactGroup patch_company_contacts_by_parent_id_groups_by_id(id, parent_id, client_id, patch_operation)

Patch ContactGroup

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.contact_group import ContactGroup
from connectwise_psa.models.patch_operation import PatchOperation
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
    api_instance = connectwise_psa.ContactGroupsApi(api_client)
    id = 56 # int | groupId
    parent_id = 56 # int | contactId
    client_id = 'client_id_example' # str | 
    patch_operation = [connectwise_psa.PatchOperation()] # List[PatchOperation] | List of PatchOperation

    try:
        # Patch ContactGroup
        api_response = api_instance.patch_company_contacts_by_parent_id_groups_by_id(id, parent_id, client_id, patch_operation)
        print("The response of ContactGroupsApi->patch_company_contacts_by_parent_id_groups_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactGroupsApi->patch_company_contacts_by_parent_id_groups_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| groupId | 
 **parent_id** | **int**| contactId | 
 **client_id** | **str**|  | 
 **patch_operation** | [**List[PatchOperation]**](PatchOperation.md)| List of PatchOperation | 

### Return type

[**ContactGroup**](ContactGroup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ContactGroup |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_company_contacts_by_parent_id_groups**
> ContactGroup post_company_contacts_by_parent_id_groups(parent_id, client_id, contact_group)

Post ContactGroup

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.contact_group import ContactGroup
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
    api_instance = connectwise_psa.ContactGroupsApi(api_client)
    parent_id = 56 # int | contactId
    client_id = 'client_id_example' # str | 
    contact_group = connectwise_psa.ContactGroup() # ContactGroup | contactGroup

    try:
        # Post ContactGroup
        api_response = api_instance.post_company_contacts_by_parent_id_groups(parent_id, client_id, contact_group)
        print("The response of ContactGroupsApi->post_company_contacts_by_parent_id_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactGroupsApi->post_company_contacts_by_parent_id_groups: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| contactId | 
 **client_id** | **str**|  | 
 **contact_group** | [**ContactGroup**](ContactGroup.md)| contactGroup | 

### Return type

[**ContactGroup**](ContactGroup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | ContactGroup |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_company_contacts_by_parent_id_groups_by_id**
> ContactGroup put_company_contacts_by_parent_id_groups_by_id(id, parent_id, client_id, contact_group)

Put ContactGroup

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.contact_group import ContactGroup
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
    api_instance = connectwise_psa.ContactGroupsApi(api_client)
    id = 56 # int | groupId
    parent_id = 56 # int | contactId
    client_id = 'client_id_example' # str | 
    contact_group = connectwise_psa.ContactGroup() # ContactGroup | contactGroup

    try:
        # Put ContactGroup
        api_response = api_instance.put_company_contacts_by_parent_id_groups_by_id(id, parent_id, client_id, contact_group)
        print("The response of ContactGroupsApi->put_company_contacts_by_parent_id_groups_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactGroupsApi->put_company_contacts_by_parent_id_groups_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| groupId | 
 **parent_id** | **int**| contactId | 
 **client_id** | **str**|  | 
 **contact_group** | [**ContactGroup**](ContactGroup.md)| contactGroup | 

### Return type

[**ContactGroup**](ContactGroup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ContactGroup |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

