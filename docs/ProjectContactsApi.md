# connectwise_psa.ProjectContactsApi

All URIs are relative to *https://api-aus.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_project_projects_by_parent_id_contacts_by_id**](ProjectContactsApi.md#delete_project_projects_by_parent_id_contacts_by_id) | **DELETE** /project/projects/{parentId}/contacts/{id} | Delete ProjectContact
[**get_project_projects_by_parent_id_contacts**](ProjectContactsApi.md#get_project_projects_by_parent_id_contacts) | **GET** /project/projects/{parentId}/contacts | Get List of ProjectContact
[**get_project_projects_by_parent_id_contacts_by_id**](ProjectContactsApi.md#get_project_projects_by_parent_id_contacts_by_id) | **GET** /project/projects/{parentId}/contacts/{id} | Get ProjectContact
[**post_project_projects_by_parent_id_contacts**](ProjectContactsApi.md#post_project_projects_by_parent_id_contacts) | **POST** /project/projects/{parentId}/contacts | Post ProjectContact


# **delete_project_projects_by_parent_id_contacts_by_id**
> delete_project_projects_by_parent_id_contacts_by_id(id, parent_id, client_id)

Delete ProjectContact

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
    api_instance = connectwise_psa.ProjectContactsApi(api_client)
    id = 56 # int | contactId
    parent_id = 56 # int | projectId
    client_id = 'client_id_example' # str | 

    try:
        # Delete ProjectContact
        api_instance.delete_project_projects_by_parent_id_contacts_by_id(id, parent_id, client_id)
    except Exception as e:
        print("Exception when calling ProjectContactsApi->delete_project_projects_by_parent_id_contacts_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| contactId | 
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

# **get_project_projects_by_parent_id_contacts**
> List[ProjectContact] get_project_projects_by_parent_id_contacts(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of ProjectContact

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.project_contact import ProjectContact
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
    api_instance = connectwise_psa.ProjectContactsApi(api_client)
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
        # Get List of ProjectContact
        api_response = api_instance.get_project_projects_by_parent_id_contacts(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of ProjectContactsApi->get_project_projects_by_parent_id_contacts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectContactsApi->get_project_projects_by_parent_id_contacts: %s\n" % e)
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

[**List[ProjectContact]**](ProjectContact.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of ProjectContact |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_projects_by_parent_id_contacts_by_id**
> ProjectContact get_project_projects_by_parent_id_contacts_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get ProjectContact

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.project_contact import ProjectContact
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
    api_instance = connectwise_psa.ProjectContactsApi(api_client)
    id = 56 # int | contactId
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
        # Get ProjectContact
        api_response = api_instance.get_project_projects_by_parent_id_contacts_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of ProjectContactsApi->get_project_projects_by_parent_id_contacts_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectContactsApi->get_project_projects_by_parent_id_contacts_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| contactId | 
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

[**ProjectContact**](ProjectContact.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ProjectContact |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_project_projects_by_parent_id_contacts**
> ProjectContact post_project_projects_by_parent_id_contacts(parent_id, client_id, project_contact)

Post ProjectContact

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.project_contact import ProjectContact
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
    api_instance = connectwise_psa.ProjectContactsApi(api_client)
    parent_id = 56 # int | projectId
    client_id = 'client_id_example' # str | 
    project_contact = connectwise_psa.ProjectContact() # ProjectContact | contact

    try:
        # Post ProjectContact
        api_response = api_instance.post_project_projects_by_parent_id_contacts(parent_id, client_id, project_contact)
        print("The response of ProjectContactsApi->post_project_projects_by_parent_id_contacts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectContactsApi->post_project_projects_by_parent_id_contacts: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| projectId | 
 **client_id** | **str**|  | 
 **project_contact** | [**ProjectContact**](ProjectContact.md)| contact | 

### Return type

[**ProjectContact**](ProjectContact.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | ProjectContact |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

