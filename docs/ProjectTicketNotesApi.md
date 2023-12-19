# connectwise_psa.ProjectTicketNotesApi

All URIs are relative to *https://api-aus.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_project_tickets_by_parent_id_all_notes**](ProjectTicketNotesApi.md#get_project_tickets_by_parent_id_all_notes) | **GET** /project/tickets/{parentId}/allNotes | Get List of ProjectTicketNote
[**post_project_ticket_note_by_id_mark_as**](ProjectTicketNotesApi.md#post_project_ticket_note_by_id_mark_as) | **POST** /project/ticketNote/{id}/markAs/ | Post ProjectTicketNote


# **get_project_tickets_by_parent_id_all_notes**
> List[ProjectTicketNote] get_project_tickets_by_parent_id_all_notes(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of ProjectTicketNote

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.project_ticket_note import ProjectTicketNote
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
    api_instance = connectwise_psa.ProjectTicketNotesApi(api_client)
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
        # Get List of ProjectTicketNote
        api_response = api_instance.get_project_tickets_by_parent_id_all_notes(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of ProjectTicketNotesApi->get_project_tickets_by_parent_id_all_notes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectTicketNotesApi->get_project_tickets_by_parent_id_all_notes: %s\n" % e)
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

[**List[ProjectTicketNote]**](ProjectTicketNote.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of ProjectTicketNote |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_project_ticket_note_by_id_mark_as**
> post_project_ticket_note_by_id_mark_as(id, client_id, project_ticket_note)

Post ProjectTicketNote

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.project_ticket_note import ProjectTicketNote
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
    api_instance = connectwise_psa.ProjectTicketNotesApi(api_client)
    id = 56 # int | ticketNoteId
    client_id = 'client_id_example' # str | 
    project_ticket_note = connectwise_psa.ProjectTicketNote() # ProjectTicketNote | item

    try:
        # Post ProjectTicketNote
        api_instance.post_project_ticket_note_by_id_mark_as(id, client_id, project_ticket_note)
    except Exception as e:
        print("Exception when calling ProjectTicketNotesApi->post_project_ticket_note_by_id_mark_as: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ticketNoteId | 
 **client_id** | **str**|  | 
 **project_ticket_note** | [**ProjectTicketNote**](ProjectTicketNote.md)| item | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Responses cannot be located for this operation. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

