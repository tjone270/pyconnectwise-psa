# connectwise_psa.TicketNotesApi

All URIs are relative to *https://aus-api.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_project_tickets_by_parent_id_notes_by_id**](TicketNotesApi.md#delete_project_tickets_by_parent_id_notes_by_id) | **DELETE** /project/tickets/{parentId}/notes/{id} | Delete TicketNote
[**delete_service_tickets_by_parent_id_notes_by_id**](TicketNotesApi.md#delete_service_tickets_by_parent_id_notes_by_id) | **DELETE** /service/tickets/{parentId}/notes/{id} | Delete ServiceNote
[**get_project_tickets_by_parent_id_notes**](TicketNotesApi.md#get_project_tickets_by_parent_id_notes) | **GET** /project/tickets/{parentId}/notes | Get List of TicketNote
[**get_project_tickets_by_parent_id_notes_by_id**](TicketNotesApi.md#get_project_tickets_by_parent_id_notes_by_id) | **GET** /project/tickets/{parentId}/notes/{id} | Get TicketNote
[**get_project_tickets_by_parent_id_notes_count**](TicketNotesApi.md#get_project_tickets_by_parent_id_notes_count) | **GET** /project/tickets/{parentId}/notes/count | Get Count of TicketNote
[**get_service_tickets_by_parent_id_notes**](TicketNotesApi.md#get_service_tickets_by_parent_id_notes) | **GET** /service/tickets/{parentId}/notes | Get List of ServiceNote
[**get_service_tickets_by_parent_id_notes_by_id**](TicketNotesApi.md#get_service_tickets_by_parent_id_notes_by_id) | **GET** /service/tickets/{parentId}/notes/{id} | Get ServiceNote
[**get_service_tickets_by_parent_id_notes_count**](TicketNotesApi.md#get_service_tickets_by_parent_id_notes_count) | **GET** /service/tickets/{parentId}/notes/count | Get Count of ServiceNote
[**patch_project_tickets_by_parent_id_notes_by_id**](TicketNotesApi.md#patch_project_tickets_by_parent_id_notes_by_id) | **PATCH** /project/tickets/{parentId}/notes/{id} | Patch TicketNote
[**patch_service_tickets_by_parent_id_notes_by_id**](TicketNotesApi.md#patch_service_tickets_by_parent_id_notes_by_id) | **PATCH** /service/tickets/{parentId}/notes/{id} | Patch ServiceNote
[**post_project_tickets_by_parent_id_notes**](TicketNotesApi.md#post_project_tickets_by_parent_id_notes) | **POST** /project/tickets/{parentId}/notes | Post TicketNote
[**post_service_tickets_by_parent_id_notes**](TicketNotesApi.md#post_service_tickets_by_parent_id_notes) | **POST** /service/tickets/{parentId}/notes | Post ServiceNote
[**put_project_tickets_by_parent_id_notes_by_id**](TicketNotesApi.md#put_project_tickets_by_parent_id_notes_by_id) | **PUT** /project/tickets/{parentId}/notes/{id} | Put TicketNote
[**put_service_tickets_by_parent_id_notes_by_id**](TicketNotesApi.md#put_service_tickets_by_parent_id_notes_by_id) | **PUT** /service/tickets/{parentId}/notes/{id} | Put ServiceNote


# **delete_project_tickets_by_parent_id_notes_by_id**
> delete_project_tickets_by_parent_id_notes_by_id(id, parent_id, client_id)

Delete TicketNote

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
    api_instance = connectwise_psa.TicketNotesApi(api_client)
    id = 56 # int | noteId
    parent_id = 56 # int | ticketId
    client_id = 'client_id_example' # str | 

    try:
        # Delete TicketNote
        api_instance.delete_project_tickets_by_parent_id_notes_by_id(id, parent_id, client_id)
    except Exception as e:
        print("Exception when calling TicketNotesApi->delete_project_tickets_by_parent_id_notes_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| noteId | 
 **parent_id** | **int**| ticketId | 
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

# **delete_service_tickets_by_parent_id_notes_by_id**
> delete_service_tickets_by_parent_id_notes_by_id(id, parent_id, client_id)

Delete ServiceNote

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
    api_instance = connectwise_psa.TicketNotesApi(api_client)
    id = 56 # int | noteId
    parent_id = 56 # int | ticketId
    client_id = 'client_id_example' # str | 

    try:
        # Delete ServiceNote
        api_instance.delete_service_tickets_by_parent_id_notes_by_id(id, parent_id, client_id)
    except Exception as e:
        print("Exception when calling TicketNotesApi->delete_service_tickets_by_parent_id_notes_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| noteId | 
 **parent_id** | **int**| ticketId | 
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

# **get_project_tickets_by_parent_id_notes**
> List[TicketNote] get_project_tickets_by_parent_id_notes(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of TicketNote

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.ticket_note import TicketNote
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
    api_instance = connectwise_psa.TicketNotesApi(api_client)
    parent_id = 56 # int | ticketId
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
        # Get List of TicketNote
        api_response = api_instance.get_project_tickets_by_parent_id_notes(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of TicketNotesApi->get_project_tickets_by_parent_id_notes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TicketNotesApi->get_project_tickets_by_parent_id_notes: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| ticketId | 
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

[**List[TicketNote]**](TicketNote.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of TicketNote |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_tickets_by_parent_id_notes_by_id**
> TicketNote get_project_tickets_by_parent_id_notes_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get TicketNote

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.ticket_note import TicketNote
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
    api_instance = connectwise_psa.TicketNotesApi(api_client)
    id = 56 # int | noteId
    parent_id = 56 # int | ticketId
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
        # Get TicketNote
        api_response = api_instance.get_project_tickets_by_parent_id_notes_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of TicketNotesApi->get_project_tickets_by_parent_id_notes_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TicketNotesApi->get_project_tickets_by_parent_id_notes_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| noteId | 
 **parent_id** | **int**| ticketId | 
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

[**TicketNote**](TicketNote.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | TicketNote |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_tickets_by_parent_id_notes_count**
> Count get_project_tickets_by_parent_id_notes_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Count of TicketNote

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
    api_instance = connectwise_psa.TicketNotesApi(api_client)
    parent_id = 56 # int | ticketId
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
        # Get Count of TicketNote
        api_response = api_instance.get_project_tickets_by_parent_id_notes_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of TicketNotesApi->get_project_tickets_by_parent_id_notes_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TicketNotesApi->get_project_tickets_by_parent_id_notes_count: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| ticketId | 
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

# **get_service_tickets_by_parent_id_notes**
> List[ServiceNote] get_service_tickets_by_parent_id_notes(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of ServiceNote

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.service_note import ServiceNote
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
    api_instance = connectwise_psa.TicketNotesApi(api_client)
    parent_id = 56 # int | ticketId
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
        # Get List of ServiceNote
        api_response = api_instance.get_service_tickets_by_parent_id_notes(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of TicketNotesApi->get_service_tickets_by_parent_id_notes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TicketNotesApi->get_service_tickets_by_parent_id_notes: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| ticketId | 
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

[**List[ServiceNote]**](ServiceNote.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of ServiceNote |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_service_tickets_by_parent_id_notes_by_id**
> ServiceNote get_service_tickets_by_parent_id_notes_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get ServiceNote

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.service_note import ServiceNote
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
    api_instance = connectwise_psa.TicketNotesApi(api_client)
    id = 56 # int | noteId
    parent_id = 56 # int | ticketId
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
        # Get ServiceNote
        api_response = api_instance.get_service_tickets_by_parent_id_notes_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of TicketNotesApi->get_service_tickets_by_parent_id_notes_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TicketNotesApi->get_service_tickets_by_parent_id_notes_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| noteId | 
 **parent_id** | **int**| ticketId | 
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

[**ServiceNote**](ServiceNote.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ServiceNote |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_service_tickets_by_parent_id_notes_count**
> Count get_service_tickets_by_parent_id_notes_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Count of ServiceNote

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
    api_instance = connectwise_psa.TicketNotesApi(api_client)
    parent_id = 56 # int | ticketId
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
        # Get Count of ServiceNote
        api_response = api_instance.get_service_tickets_by_parent_id_notes_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of TicketNotesApi->get_service_tickets_by_parent_id_notes_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TicketNotesApi->get_service_tickets_by_parent_id_notes_count: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| ticketId | 
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

# **patch_project_tickets_by_parent_id_notes_by_id**
> TicketNote patch_project_tickets_by_parent_id_notes_by_id(id, parent_id, client_id, patch_operation)

Patch TicketNote

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.patch_operation import PatchOperation
from connectwise_psa.models.ticket_note import TicketNote
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
    api_instance = connectwise_psa.TicketNotesApi(api_client)
    id = 56 # int | noteId
    parent_id = 56 # int | ticketId
    client_id = 'client_id_example' # str | 
    patch_operation = [connectwise_psa.PatchOperation()] # List[PatchOperation] | List of PatchOperation

    try:
        # Patch TicketNote
        api_response = api_instance.patch_project_tickets_by_parent_id_notes_by_id(id, parent_id, client_id, patch_operation)
        print("The response of TicketNotesApi->patch_project_tickets_by_parent_id_notes_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TicketNotesApi->patch_project_tickets_by_parent_id_notes_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| noteId | 
 **parent_id** | **int**| ticketId | 
 **client_id** | **str**|  | 
 **patch_operation** | [**List[PatchOperation]**](PatchOperation.md)| List of PatchOperation | 

### Return type

[**TicketNote**](TicketNote.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | TicketNote |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_service_tickets_by_parent_id_notes_by_id**
> ServiceNote patch_service_tickets_by_parent_id_notes_by_id(id, parent_id, client_id, patch_operation)

Patch ServiceNote

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.patch_operation import PatchOperation
from connectwise_psa.models.service_note import ServiceNote
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
    api_instance = connectwise_psa.TicketNotesApi(api_client)
    id = 56 # int | noteId
    parent_id = 56 # int | ticketId
    client_id = 'client_id_example' # str | 
    patch_operation = [connectwise_psa.PatchOperation()] # List[PatchOperation] | List of PatchOperation

    try:
        # Patch ServiceNote
        api_response = api_instance.patch_service_tickets_by_parent_id_notes_by_id(id, parent_id, client_id, patch_operation)
        print("The response of TicketNotesApi->patch_service_tickets_by_parent_id_notes_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TicketNotesApi->patch_service_tickets_by_parent_id_notes_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| noteId | 
 **parent_id** | **int**| ticketId | 
 **client_id** | **str**|  | 
 **patch_operation** | [**List[PatchOperation]**](PatchOperation.md)| List of PatchOperation | 

### Return type

[**ServiceNote**](ServiceNote.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ServiceNote |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_project_tickets_by_parent_id_notes**
> TicketNote post_project_tickets_by_parent_id_notes(parent_id, client_id, ticket_note)

Post TicketNote

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.ticket_note import TicketNote
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
    api_instance = connectwise_psa.TicketNotesApi(api_client)
    parent_id = 56 # int | ticketId
    client_id = 'client_id_example' # str | 
    ticket_note = connectwise_psa.TicketNote() # TicketNote | ticketNote

    try:
        # Post TicketNote
        api_response = api_instance.post_project_tickets_by_parent_id_notes(parent_id, client_id, ticket_note)
        print("The response of TicketNotesApi->post_project_tickets_by_parent_id_notes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TicketNotesApi->post_project_tickets_by_parent_id_notes: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| ticketId | 
 **client_id** | **str**|  | 
 **ticket_note** | [**TicketNote**](TicketNote.md)| ticketNote | 

### Return type

[**TicketNote**](TicketNote.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | TicketNote |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_service_tickets_by_parent_id_notes**
> ServiceNote post_service_tickets_by_parent_id_notes(parent_id, client_id, service_note)

Post ServiceNote

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.service_note import ServiceNote
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
    api_instance = connectwise_psa.TicketNotesApi(api_client)
    parent_id = 56 # int | ticketId
    client_id = 'client_id_example' # str | 
    service_note = connectwise_psa.ServiceNote() # ServiceNote | serviceNote

    try:
        # Post ServiceNote
        api_response = api_instance.post_service_tickets_by_parent_id_notes(parent_id, client_id, service_note)
        print("The response of TicketNotesApi->post_service_tickets_by_parent_id_notes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TicketNotesApi->post_service_tickets_by_parent_id_notes: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| ticketId | 
 **client_id** | **str**|  | 
 **service_note** | [**ServiceNote**](ServiceNote.md)| serviceNote | 

### Return type

[**ServiceNote**](ServiceNote.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | ServiceNote |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_project_tickets_by_parent_id_notes_by_id**
> TicketNote put_project_tickets_by_parent_id_notes_by_id(id, parent_id, client_id, ticket_note)

Put TicketNote

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.ticket_note import TicketNote
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
    api_instance = connectwise_psa.TicketNotesApi(api_client)
    id = 56 # int | noteId
    parent_id = 56 # int | ticketId
    client_id = 'client_id_example' # str | 
    ticket_note = connectwise_psa.TicketNote() # TicketNote | ticketNote

    try:
        # Put TicketNote
        api_response = api_instance.put_project_tickets_by_parent_id_notes_by_id(id, parent_id, client_id, ticket_note)
        print("The response of TicketNotesApi->put_project_tickets_by_parent_id_notes_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TicketNotesApi->put_project_tickets_by_parent_id_notes_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| noteId | 
 **parent_id** | **int**| ticketId | 
 **client_id** | **str**|  | 
 **ticket_note** | [**TicketNote**](TicketNote.md)| ticketNote | 

### Return type

[**TicketNote**](TicketNote.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | TicketNote |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_service_tickets_by_parent_id_notes_by_id**
> ServiceNote put_service_tickets_by_parent_id_notes_by_id(id, parent_id, client_id, service_note)

Put ServiceNote

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.service_note import ServiceNote
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
    api_instance = connectwise_psa.TicketNotesApi(api_client)
    id = 56 # int | noteId
    parent_id = 56 # int | ticketId
    client_id = 'client_id_example' # str | 
    service_note = connectwise_psa.ServiceNote() # ServiceNote | serviceNote

    try:
        # Put ServiceNote
        api_response = api_instance.put_service_tickets_by_parent_id_notes_by_id(id, parent_id, client_id, service_note)
        print("The response of TicketNotesApi->put_service_tickets_by_parent_id_notes_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TicketNotesApi->put_service_tickets_by_parent_id_notes_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| noteId | 
 **parent_id** | **int**| ticketId | 
 **client_id** | **str**|  | 
 **service_note** | [**ServiceNote**](ServiceNote.md)| serviceNote | 

### Return type

[**ServiceNote**](ServiceNote.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ServiceNote |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

