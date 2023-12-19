# connectwise_psa.ProjectTemplateTicketsApi

All URIs are relative to *https://aus-api.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_project_project_templates_by_parent_id_project_template_tickets_by_id**](ProjectTemplateTicketsApi.md#delete_project_project_templates_by_parent_id_project_template_tickets_by_id) | **DELETE** /project/projectTemplates/{parentId}/projectTemplateTickets/{id} | Delete ProjectTemplateTickets
[**get_project_project_templates_by_parent_id_project_template_tickets**](ProjectTemplateTicketsApi.md#get_project_project_templates_by_parent_id_project_template_tickets) | **GET** /project/projectTemplates/{parentId}/projectTemplateTickets | Get List of ProjectTemplateTickets
[**get_project_project_templates_by_parent_id_project_template_tickets_by_id**](ProjectTemplateTicketsApi.md#get_project_project_templates_by_parent_id_project_template_tickets_by_id) | **GET** /project/projectTemplates/{parentId}/projectTemplateTickets/{id} | Get ProjectTemplateTickets
[**get_project_project_templates_by_parent_id_project_template_tickets_count**](ProjectTemplateTicketsApi.md#get_project_project_templates_by_parent_id_project_template_tickets_count) | **GET** /project/projectTemplates/{parentId}/projectTemplateTickets/count | Get Count of ProjectTemplateTickets
[**patch_project_project_templates_by_parent_id_project_template_tickets_by_id**](ProjectTemplateTicketsApi.md#patch_project_project_templates_by_parent_id_project_template_tickets_by_id) | **PATCH** /project/projectTemplates/{parentId}/projectTemplateTickets/{id} | Patch ProjectTemplateTickets
[**post_project_project_templates_by_parent_id_project_template_tickets**](ProjectTemplateTicketsApi.md#post_project_project_templates_by_parent_id_project_template_tickets) | **POST** /project/projectTemplates/{parentId}/projectTemplateTickets | Post ProjectTemplateTickets
[**put_project_project_templates_by_parent_id_project_template_tickets_by_id**](ProjectTemplateTicketsApi.md#put_project_project_templates_by_parent_id_project_template_tickets_by_id) | **PUT** /project/projectTemplates/{parentId}/projectTemplateTickets/{id} | Put ProjectTemplateTickets


# **delete_project_project_templates_by_parent_id_project_template_tickets_by_id**
> delete_project_project_templates_by_parent_id_project_template_tickets_by_id(id, parent_id, client_id)

Delete ProjectTemplateTickets

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
    api_instance = connectwise_psa.ProjectTemplateTicketsApi(api_client)
    id = 56 # int | ProjectTemplateTicketId
    parent_id = 56 # int | projectTemplateId
    client_id = 'client_id_example' # str | 

    try:
        # Delete ProjectTemplateTickets
        api_instance.delete_project_project_templates_by_parent_id_project_template_tickets_by_id(id, parent_id, client_id)
    except Exception as e:
        print("Exception when calling ProjectTemplateTicketsApi->delete_project_project_templates_by_parent_id_project_template_tickets_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ProjectTemplateTicketId | 
 **parent_id** | **int**| projectTemplateId | 
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

# **get_project_project_templates_by_parent_id_project_template_tickets**
> List[ProjectTemplateTicket] get_project_project_templates_by_parent_id_project_template_tickets(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of ProjectTemplateTickets

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.project_template_ticket import ProjectTemplateTicket
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
    api_instance = connectwise_psa.ProjectTemplateTicketsApi(api_client)
    parent_id = 56 # int | projectTemplateId
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
        # Get List of ProjectTemplateTickets
        api_response = api_instance.get_project_project_templates_by_parent_id_project_template_tickets(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of ProjectTemplateTicketsApi->get_project_project_templates_by_parent_id_project_template_tickets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectTemplateTicketsApi->get_project_project_templates_by_parent_id_project_template_tickets: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| projectTemplateId | 
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

[**List[ProjectTemplateTicket]**](ProjectTemplateTicket.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of projectTemplateTickets |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_project_templates_by_parent_id_project_template_tickets_by_id**
> ProjectTemplateTicket get_project_project_templates_by_parent_id_project_template_tickets_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get ProjectTemplateTickets

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.project_template_ticket import ProjectTemplateTicket
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
    api_instance = connectwise_psa.ProjectTemplateTicketsApi(api_client)
    id = 56 # int | ProjectTemplateTicketId
    parent_id = 56 # int | projectTemplateId
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
        # Get ProjectTemplateTickets
        api_response = api_instance.get_project_project_templates_by_parent_id_project_template_tickets_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of ProjectTemplateTicketsApi->get_project_project_templates_by_parent_id_project_template_tickets_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectTemplateTicketsApi->get_project_project_templates_by_parent_id_project_template_tickets_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ProjectTemplateTicketId | 
 **parent_id** | **int**| projectTemplateId | 
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

[**ProjectTemplateTicket**](ProjectTemplateTicket.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ProjectTemplateTicket |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_project_templates_by_parent_id_project_template_tickets_count**
> Count get_project_project_templates_by_parent_id_project_template_tickets_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Count of ProjectTemplateTickets

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
    api_instance = connectwise_psa.ProjectTemplateTicketsApi(api_client)
    parent_id = 56 # int | projectTemplateId
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
        # Get Count of ProjectTemplateTickets
        api_response = api_instance.get_project_project_templates_by_parent_id_project_template_tickets_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of ProjectTemplateTicketsApi->get_project_project_templates_by_parent_id_project_template_tickets_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectTemplateTicketsApi->get_project_project_templates_by_parent_id_project_template_tickets_count: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| projectTemplateId | 
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

# **patch_project_project_templates_by_parent_id_project_template_tickets_by_id**
> ProjectTemplateTicket patch_project_project_templates_by_parent_id_project_template_tickets_by_id(id, parent_id, client_id, patch_operation)

Patch ProjectTemplateTickets

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.patch_operation import PatchOperation
from connectwise_psa.models.project_template_ticket import ProjectTemplateTicket
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
    api_instance = connectwise_psa.ProjectTemplateTicketsApi(api_client)
    id = 56 # int | ProjectTemplateTicketId
    parent_id = 56 # int | projectTemplateId
    client_id = 'client_id_example' # str | 
    patch_operation = [connectwise_psa.PatchOperation()] # List[PatchOperation] | List of PatchOperation

    try:
        # Patch ProjectTemplateTickets
        api_response = api_instance.patch_project_project_templates_by_parent_id_project_template_tickets_by_id(id, parent_id, client_id, patch_operation)
        print("The response of ProjectTemplateTicketsApi->patch_project_project_templates_by_parent_id_project_template_tickets_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectTemplateTicketsApi->patch_project_project_templates_by_parent_id_project_template_tickets_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ProjectTemplateTicketId | 
 **parent_id** | **int**| projectTemplateId | 
 **client_id** | **str**|  | 
 **patch_operation** | [**List[PatchOperation]**](PatchOperation.md)| List of PatchOperation | 

### Return type

[**ProjectTemplateTicket**](ProjectTemplateTicket.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ProjectTemplateTicket |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_project_project_templates_by_parent_id_project_template_tickets**
> ProjectTemplateTicket post_project_project_templates_by_parent_id_project_template_tickets(parent_id, client_id, project_template_ticket)

Post ProjectTemplateTickets

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.project_template_ticket import ProjectTemplateTicket
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
    api_instance = connectwise_psa.ProjectTemplateTicketsApi(api_client)
    parent_id = 56 # int | projectTemplateId
    client_id = 'client_id_example' # str | 
    project_template_ticket = connectwise_psa.ProjectTemplateTicket() # ProjectTemplateTicket | ProjectTemplateTicket

    try:
        # Post ProjectTemplateTickets
        api_response = api_instance.post_project_project_templates_by_parent_id_project_template_tickets(parent_id, client_id, project_template_ticket)
        print("The response of ProjectTemplateTicketsApi->post_project_project_templates_by_parent_id_project_template_tickets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectTemplateTicketsApi->post_project_project_templates_by_parent_id_project_template_tickets: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| projectTemplateId | 
 **client_id** | **str**|  | 
 **project_template_ticket** | [**ProjectTemplateTicket**](ProjectTemplateTicket.md)| ProjectTemplateTicket | 

### Return type

[**ProjectTemplateTicket**](ProjectTemplateTicket.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | ProjectTemplateTicket |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_project_project_templates_by_parent_id_project_template_tickets_by_id**
> ProjectTemplateTicket put_project_project_templates_by_parent_id_project_template_tickets_by_id(id, parent_id, client_id, project_template_ticket)

Put ProjectTemplateTickets

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.project_template_ticket import ProjectTemplateTicket
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
    api_instance = connectwise_psa.ProjectTemplateTicketsApi(api_client)
    id = 56 # int | ProjectTemplateTicketId
    parent_id = 56 # int | projectTemplateId
    client_id = 'client_id_example' # str | 
    project_template_ticket = connectwise_psa.ProjectTemplateTicket() # ProjectTemplateTicket | companyTypeAssociation

    try:
        # Put ProjectTemplateTickets
        api_response = api_instance.put_project_project_templates_by_parent_id_project_template_tickets_by_id(id, parent_id, client_id, project_template_ticket)
        print("The response of ProjectTemplateTicketsApi->put_project_project_templates_by_parent_id_project_template_tickets_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectTemplateTicketsApi->put_project_project_templates_by_parent_id_project_template_tickets_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ProjectTemplateTicketId | 
 **parent_id** | **int**| projectTemplateId | 
 **client_id** | **str**|  | 
 **project_template_ticket** | [**ProjectTemplateTicket**](ProjectTemplateTicket.md)| companyTypeAssociation | 

### Return type

[**ProjectTemplateTicket**](ProjectTemplateTicket.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ProjectTemplateTicket |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

