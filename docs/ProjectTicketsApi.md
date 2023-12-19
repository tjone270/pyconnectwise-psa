# connectwise_psa.ProjectTicketsApi

All URIs are relative to *https://aus-api.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_project_tickets_by_id**](ProjectTicketsApi.md#delete_project_tickets_by_id) | **DELETE** /project/tickets/{id} | Delete ProjectTicket
[**delete_project_tickets_by_parent_id_configurations_by_id**](ProjectTicketsApi.md#delete_project_tickets_by_parent_id_configurations_by_id) | **DELETE** /project/tickets/{parentId}/configurations/{id} | Delete ConfigurationReference
[**get_project_tickets**](ProjectTicketsApi.md#get_project_tickets) | **GET** /project/tickets | Get List of ProjectTicket
[**get_project_tickets_by_id**](ProjectTicketsApi.md#get_project_tickets_by_id) | **GET** /project/tickets/{id} | Get ProjectTicket
[**get_project_tickets_by_parent_id_activities**](ProjectTicketsApi.md#get_project_tickets_by_parent_id_activities) | **GET** /project/tickets/{parentId}/activities | Get List of ActivityReference              Gets activities associated to the ticket              Please use the /sales/activities?conditions&#x3D;ticket/id&#x3D;{id} endpoint
[**get_project_tickets_by_parent_id_activities_count**](ProjectTicketsApi.md#get_project_tickets_by_parent_id_activities_count) | **GET** /project/tickets/{parentId}/activities/count | Get Count of ActivityReference              Gets count of activities associated to the ticket              Please use the /sales/activities/count?conditions&#x3D;ticket/id&#x3D;{id} endpoint
[**get_project_tickets_by_parent_id_configurations**](ProjectTicketsApi.md#get_project_tickets_by_parent_id_configurations) | **GET** /project/tickets/{parentId}/configurations | Get List of ConfigurationReference
[**get_project_tickets_by_parent_id_configurations_by_id**](ProjectTicketsApi.md#get_project_tickets_by_parent_id_configurations_by_id) | **GET** /project/tickets/{parentId}/configurations/{id} | Get ConfigurationReference
[**get_project_tickets_by_parent_id_configurations_count**](ProjectTicketsApi.md#get_project_tickets_by_parent_id_configurations_count) | **GET** /project/tickets/{parentId}/configurations/count | Get Count of ConfigurationReference
[**get_project_tickets_by_parent_id_documents**](ProjectTicketsApi.md#get_project_tickets_by_parent_id_documents) | **GET** /project/tickets/{parentId}/documents | Get List of DocumentReference              Gets the documents associated to the ticket              Please use the /system/documents?recordType&#x3D;Ticket&amp;amp;recordId&#x3D;{id} endpoint
[**get_project_tickets_by_parent_id_documents_count**](ProjectTicketsApi.md#get_project_tickets_by_parent_id_documents_count) | **GET** /project/tickets/{parentId}/documents/count | Get Count of DocumentReference
[**get_project_tickets_by_parent_id_products**](ProjectTicketsApi.md#get_project_tickets_by_parent_id_products) | **GET** /project/tickets/{parentId}/products | Get List of ProductReference              Gets the products associated to the ticket              Please use the /procurement/products?conditions&#x3D;chargeToType&#x3D;&#39;Ticket&#39; AND chargeToId&#x3D;{id} endpoint
[**get_project_tickets_by_parent_id_products_count**](ProjectTicketsApi.md#get_project_tickets_by_parent_id_products_count) | **GET** /project/tickets/{parentId}/products/count | Get Count of ProductReference              Gets the products associated to the ticket              Please use the /procurement/products/count?conditions&#x3D;chargeToType&#x3D;&#39;Ticket&#39; AND chargeToId&#x3D;{id} endpoint
[**get_project_tickets_by_parent_id_scheduleentries**](ProjectTicketsApi.md#get_project_tickets_by_parent_id_scheduleentries) | **GET** /project/tickets/{parentId}/scheduleentries | Get List of ScheduleEntryReference              Gets the schedule entries associated to the ticket              Please use the /schedule/entries?conditions&#x3D;type/id&#x3D;4 AND objectId&#x3D;{id} endpoint
[**get_project_tickets_by_parent_id_scheduleentries_count**](ProjectTicketsApi.md#get_project_tickets_by_parent_id_scheduleentries_count) | **GET** /project/tickets/{parentId}/scheduleentries/count | Get Count of ScheduleEntryReference              Gets the schedule entries count associated to the ticket              Please use the /schedule/entries/count?conditions&#x3D;type/id&#x3D;4 AND objectId&#x3D;{id} endpoint
[**get_project_tickets_by_parent_id_timeentries**](ProjectTicketsApi.md#get_project_tickets_by_parent_id_timeentries) | **GET** /project/tickets/{parentId}/timeentries | Get List of TimeEntryReference              Gets time entries associated to the ticket              Please use the /time/entries?conditions&#x3D;(chargeToType&#x3D;\&quot;ServiceTicket\&quot; OR chargeToType&#x3D;\&quot;ProjectTicket\&quot;) AND chargeToId&#x3D;{id} endpoint
[**get_project_tickets_by_parent_id_timeentries_count**](ProjectTicketsApi.md#get_project_tickets_by_parent_id_timeentries_count) | **GET** /project/tickets/{parentId}/timeentries/count | Get Count of TimeEntryReference              Gets time entries count associated to the ticket              Please use the /time/entries/count?conditions&#x3D;(chargeToType&#x3D;\&quot;ServiceTicket\&quot; OR chargeToType&#x3D;\&quot;ProjectTicket\&quot;) AND chargeToId&#x3D;{id} endpoint
[**get_project_tickets_count**](ProjectTicketsApi.md#get_project_tickets_count) | **GET** /project/tickets/count | Get Count of ProjectTicket
[**patch_project_tickets_by_id**](ProjectTicketsApi.md#patch_project_tickets_by_id) | **PATCH** /project/tickets/{id} | Patch ProjectTicket
[**post_project_tickets**](ProjectTicketsApi.md#post_project_tickets) | **POST** /project/tickets | Post ProjectTicket
[**post_project_tickets_by_parent_id_configurations**](ProjectTicketsApi.md#post_project_tickets_by_parent_id_configurations) | **POST** /project/tickets/{parentId}/configurations | Post ConfigurationReference
[**post_project_tickets_by_parent_id_convert**](ProjectTicketsApi.md#post_project_tickets_by_parent_id_convert) | **POST** /project/tickets/{parentId}/convert | Post SuccessResponse
[**post_project_tickets_search**](ProjectTicketsApi.md#post_project_tickets_search) | **POST** /project/tickets/search | Post List of ProjectTicket
[**put_project_tickets_by_id**](ProjectTicketsApi.md#put_project_tickets_by_id) | **PUT** /project/tickets/{id} | Put ProjectTicket


# **delete_project_tickets_by_id**
> delete_project_tickets_by_id(id, client_id)

Delete ProjectTicket

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
    api_instance = connectwise_psa.ProjectTicketsApi(api_client)
    id = 56 # int | ticketId
    client_id = 'client_id_example' # str | 

    try:
        # Delete ProjectTicket
        api_instance.delete_project_tickets_by_id(id, client_id)
    except Exception as e:
        print("Exception when calling ProjectTicketsApi->delete_project_tickets_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ticketId | 
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

# **delete_project_tickets_by_parent_id_configurations_by_id**
> delete_project_tickets_by_parent_id_configurations_by_id(id, parent_id, client_id)

Delete ConfigurationReference

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
    api_instance = connectwise_psa.ProjectTicketsApi(api_client)
    id = 56 # int | configurationId
    parent_id = 56 # int | ticketId
    client_id = 'client_id_example' # str | 

    try:
        # Delete ConfigurationReference
        api_instance.delete_project_tickets_by_parent_id_configurations_by_id(id, parent_id, client_id)
    except Exception as e:
        print("Exception when calling ProjectTicketsApi->delete_project_tickets_by_parent_id_configurations_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| configurationId | 
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

# **get_project_tickets**
> List[ProjectTicket] get_project_tickets(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of ProjectTicket

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.project_ticket import ProjectTicket
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
    api_instance = connectwise_psa.ProjectTicketsApi(api_client)
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
        # Get List of ProjectTicket
        api_response = api_instance.get_project_tickets(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of ProjectTicketsApi->get_project_tickets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectTicketsApi->get_project_tickets: %s\n" % e)
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

[**List[ProjectTicket]**](ProjectTicket.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of ProjectTicket |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_tickets_by_id**
> ProjectTicket get_project_tickets_by_id(id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get ProjectTicket

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.project_ticket import ProjectTicket
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
    api_instance = connectwise_psa.ProjectTicketsApi(api_client)
    id = 56 # int | ticketId
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
        # Get ProjectTicket
        api_response = api_instance.get_project_tickets_by_id(id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of ProjectTicketsApi->get_project_tickets_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectTicketsApi->get_project_tickets_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ticketId | 
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

[**ProjectTicket**](ProjectTicket.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ProjectTicket |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_tickets_by_parent_id_activities**
> List[ActivityReference] get_project_tickets_by_parent_id_activities(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of ActivityReference              Gets activities associated to the ticket              Please use the /sales/activities?conditions=ticket/id={id} endpoint

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.activity_reference import ActivityReference
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
    api_instance = connectwise_psa.ProjectTicketsApi(api_client)
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
        # Get List of ActivityReference              Gets activities associated to the ticket              Please use the /sales/activities?conditions=ticket/id={id} endpoint
        api_response = api_instance.get_project_tickets_by_parent_id_activities(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of ProjectTicketsApi->get_project_tickets_by_parent_id_activities:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectTicketsApi->get_project_tickets_by_parent_id_activities: %s\n" % e)
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

[**List[ActivityReference]**](ActivityReference.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of ActivityReference |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_tickets_by_parent_id_activities_count**
> Count get_project_tickets_by_parent_id_activities_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Count of ActivityReference              Gets count of activities associated to the ticket              Please use the /sales/activities/count?conditions=ticket/id={id} endpoint

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
    api_instance = connectwise_psa.ProjectTicketsApi(api_client)
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
        # Get Count of ActivityReference              Gets count of activities associated to the ticket              Please use the /sales/activities/count?conditions=ticket/id={id} endpoint
        api_response = api_instance.get_project_tickets_by_parent_id_activities_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of ProjectTicketsApi->get_project_tickets_by_parent_id_activities_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectTicketsApi->get_project_tickets_by_parent_id_activities_count: %s\n" % e)
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

# **get_project_tickets_by_parent_id_configurations**
> List[ConfigurationReference] get_project_tickets_by_parent_id_configurations(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of ConfigurationReference

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.configuration_reference import ConfigurationReference
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
    api_instance = connectwise_psa.ProjectTicketsApi(api_client)
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
        # Get List of ConfigurationReference
        api_response = api_instance.get_project_tickets_by_parent_id_configurations(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of ProjectTicketsApi->get_project_tickets_by_parent_id_configurations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectTicketsApi->get_project_tickets_by_parent_id_configurations: %s\n" % e)
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

[**List[ConfigurationReference]**](ConfigurationReference.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of ConfigurationReference |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_tickets_by_parent_id_configurations_by_id**
> ConfigurationReference get_project_tickets_by_parent_id_configurations_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get ConfigurationReference

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.configuration_reference import ConfigurationReference
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
    api_instance = connectwise_psa.ProjectTicketsApi(api_client)
    id = 56 # int | configurationId
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
        # Get ConfigurationReference
        api_response = api_instance.get_project_tickets_by_parent_id_configurations_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of ProjectTicketsApi->get_project_tickets_by_parent_id_configurations_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectTicketsApi->get_project_tickets_by_parent_id_configurations_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| configurationId | 
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

[**ConfigurationReference**](ConfigurationReference.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ConfigurationReference |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_tickets_by_parent_id_configurations_count**
> Count get_project_tickets_by_parent_id_configurations_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Count of ConfigurationReference

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
    api_instance = connectwise_psa.ProjectTicketsApi(api_client)
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
        # Get Count of ConfigurationReference
        api_response = api_instance.get_project_tickets_by_parent_id_configurations_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of ProjectTicketsApi->get_project_tickets_by_parent_id_configurations_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectTicketsApi->get_project_tickets_by_parent_id_configurations_count: %s\n" % e)
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

# **get_project_tickets_by_parent_id_documents**
> List[DocumentReference] get_project_tickets_by_parent_id_documents(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of DocumentReference              Gets the documents associated to the ticket              Please use the /system/documents?recordType=Ticket&amp;recordId={id} endpoint

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.document_reference import DocumentReference
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
    api_instance = connectwise_psa.ProjectTicketsApi(api_client)
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
        # Get List of DocumentReference              Gets the documents associated to the ticket              Please use the /system/documents?recordType=Ticket&amp;recordId={id} endpoint
        api_response = api_instance.get_project_tickets_by_parent_id_documents(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of ProjectTicketsApi->get_project_tickets_by_parent_id_documents:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectTicketsApi->get_project_tickets_by_parent_id_documents: %s\n" % e)
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

[**List[DocumentReference]**](DocumentReference.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of DocumentReference |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_tickets_by_parent_id_documents_count**
> Count get_project_tickets_by_parent_id_documents_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Count of DocumentReference

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
    api_instance = connectwise_psa.ProjectTicketsApi(api_client)
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
        # Get Count of DocumentReference
        api_response = api_instance.get_project_tickets_by_parent_id_documents_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of ProjectTicketsApi->get_project_tickets_by_parent_id_documents_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectTicketsApi->get_project_tickets_by_parent_id_documents_count: %s\n" % e)
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

# **get_project_tickets_by_parent_id_products**
> List[ProductReference] get_project_tickets_by_parent_id_products(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of ProductReference              Gets the products associated to the ticket              Please use the /procurement/products?conditions=chargeToType='Ticket' AND chargeToId={id} endpoint

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.product_reference import ProductReference
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
    api_instance = connectwise_psa.ProjectTicketsApi(api_client)
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
        # Get List of ProductReference              Gets the products associated to the ticket              Please use the /procurement/products?conditions=chargeToType='Ticket' AND chargeToId={id} endpoint
        api_response = api_instance.get_project_tickets_by_parent_id_products(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of ProjectTicketsApi->get_project_tickets_by_parent_id_products:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectTicketsApi->get_project_tickets_by_parent_id_products: %s\n" % e)
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

[**List[ProductReference]**](ProductReference.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of ProductReference |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_tickets_by_parent_id_products_count**
> Count get_project_tickets_by_parent_id_products_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Count of ProductReference              Gets the products associated to the ticket              Please use the /procurement/products/count?conditions=chargeToType='Ticket' AND chargeToId={id} endpoint

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
    api_instance = connectwise_psa.ProjectTicketsApi(api_client)
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
        # Get Count of ProductReference              Gets the products associated to the ticket              Please use the /procurement/products/count?conditions=chargeToType='Ticket' AND chargeToId={id} endpoint
        api_response = api_instance.get_project_tickets_by_parent_id_products_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of ProjectTicketsApi->get_project_tickets_by_parent_id_products_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectTicketsApi->get_project_tickets_by_parent_id_products_count: %s\n" % e)
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

# **get_project_tickets_by_parent_id_scheduleentries**
> List[ScheduleEntryReference] get_project_tickets_by_parent_id_scheduleentries(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of ScheduleEntryReference              Gets the schedule entries associated to the ticket              Please use the /schedule/entries?conditions=type/id=4 AND objectId={id} endpoint

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.schedule_entry_reference import ScheduleEntryReference
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
    api_instance = connectwise_psa.ProjectTicketsApi(api_client)
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
        # Get List of ScheduleEntryReference              Gets the schedule entries associated to the ticket              Please use the /schedule/entries?conditions=type/id=4 AND objectId={id} endpoint
        api_response = api_instance.get_project_tickets_by_parent_id_scheduleentries(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of ProjectTicketsApi->get_project_tickets_by_parent_id_scheduleentries:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectTicketsApi->get_project_tickets_by_parent_id_scheduleentries: %s\n" % e)
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

[**List[ScheduleEntryReference]**](ScheduleEntryReference.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of ScheduleEntryReference |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_tickets_by_parent_id_scheduleentries_count**
> Count get_project_tickets_by_parent_id_scheduleentries_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Count of ScheduleEntryReference              Gets the schedule entries count associated to the ticket              Please use the /schedule/entries/count?conditions=type/id=4 AND objectId={id} endpoint

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
    api_instance = connectwise_psa.ProjectTicketsApi(api_client)
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
        # Get Count of ScheduleEntryReference              Gets the schedule entries count associated to the ticket              Please use the /schedule/entries/count?conditions=type/id=4 AND objectId={id} endpoint
        api_response = api_instance.get_project_tickets_by_parent_id_scheduleentries_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of ProjectTicketsApi->get_project_tickets_by_parent_id_scheduleentries_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectTicketsApi->get_project_tickets_by_parent_id_scheduleentries_count: %s\n" % e)
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

# **get_project_tickets_by_parent_id_timeentries**
> List[TimeEntryReference] get_project_tickets_by_parent_id_timeentries(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of TimeEntryReference              Gets time entries associated to the ticket              Please use the /time/entries?conditions=(chargeToType=\"ServiceTicket\" OR chargeToType=\"ProjectTicket\") AND chargeToId={id} endpoint

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.time_entry_reference import TimeEntryReference
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
    api_instance = connectwise_psa.ProjectTicketsApi(api_client)
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
        # Get List of TimeEntryReference              Gets time entries associated to the ticket              Please use the /time/entries?conditions=(chargeToType=\"ServiceTicket\" OR chargeToType=\"ProjectTicket\") AND chargeToId={id} endpoint
        api_response = api_instance.get_project_tickets_by_parent_id_timeentries(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of ProjectTicketsApi->get_project_tickets_by_parent_id_timeentries:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectTicketsApi->get_project_tickets_by_parent_id_timeentries: %s\n" % e)
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

[**List[TimeEntryReference]**](TimeEntryReference.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of TimeEntryReference |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_tickets_by_parent_id_timeentries_count**
> Count get_project_tickets_by_parent_id_timeentries_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Count of TimeEntryReference              Gets time entries count associated to the ticket              Please use the /time/entries/count?conditions=(chargeToType=\"ServiceTicket\" OR chargeToType=\"ProjectTicket\") AND chargeToId={id} endpoint

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
    api_instance = connectwise_psa.ProjectTicketsApi(api_client)
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
        # Get Count of TimeEntryReference              Gets time entries count associated to the ticket              Please use the /time/entries/count?conditions=(chargeToType=\"ServiceTicket\" OR chargeToType=\"ProjectTicket\") AND chargeToId={id} endpoint
        api_response = api_instance.get_project_tickets_by_parent_id_timeentries_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of ProjectTicketsApi->get_project_tickets_by_parent_id_timeentries_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectTicketsApi->get_project_tickets_by_parent_id_timeentries_count: %s\n" % e)
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

# **get_project_tickets_count**
> Count get_project_tickets_count(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Count of ProjectTicket

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
    api_instance = connectwise_psa.ProjectTicketsApi(api_client)
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
        # Get Count of ProjectTicket
        api_response = api_instance.get_project_tickets_count(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of ProjectTicketsApi->get_project_tickets_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectTicketsApi->get_project_tickets_count: %s\n" % e)
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

# **patch_project_tickets_by_id**
> ProjectTicket patch_project_tickets_by_id(id, client_id, patch_operation)

Patch ProjectTicket

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.patch_operation import PatchOperation
from connectwise_psa.models.project_ticket import ProjectTicket
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
    api_instance = connectwise_psa.ProjectTicketsApi(api_client)
    id = 56 # int | ticketId
    client_id = 'client_id_example' # str | 
    patch_operation = [connectwise_psa.PatchOperation()] # List[PatchOperation] | List of PatchOperation

    try:
        # Patch ProjectTicket
        api_response = api_instance.patch_project_tickets_by_id(id, client_id, patch_operation)
        print("The response of ProjectTicketsApi->patch_project_tickets_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectTicketsApi->patch_project_tickets_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ticketId | 
 **client_id** | **str**|  | 
 **patch_operation** | [**List[PatchOperation]**](PatchOperation.md)| List of PatchOperation | 

### Return type

[**ProjectTicket**](ProjectTicket.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ProjectTicket |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_project_tickets**
> ProjectTicket post_project_tickets(client_id, project_ticket)

Post ProjectTicket

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.project_ticket import ProjectTicket
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
    api_instance = connectwise_psa.ProjectTicketsApi(api_client)
    client_id = 'client_id_example' # str | 
    project_ticket = connectwise_psa.ProjectTicket() # ProjectTicket | ticket

    try:
        # Post ProjectTicket
        api_response = api_instance.post_project_tickets(client_id, project_ticket)
        print("The response of ProjectTicketsApi->post_project_tickets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectTicketsApi->post_project_tickets: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**|  | 
 **project_ticket** | [**ProjectTicket**](ProjectTicket.md)| ticket | 

### Return type

[**ProjectTicket**](ProjectTicket.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | ProjectTicket |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_project_tickets_by_parent_id_configurations**
> ConfigurationReference post_project_tickets_by_parent_id_configurations(parent_id, client_id, configuration_reference)

Post ConfigurationReference

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.configuration_reference import ConfigurationReference
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
    api_instance = connectwise_psa.ProjectTicketsApi(api_client)
    parent_id = 56 # int | ticketId
    client_id = 'client_id_example' # str | 
    configuration_reference = connectwise_psa.ConfigurationReference() # ConfigurationReference | configuration

    try:
        # Post ConfigurationReference
        api_response = api_instance.post_project_tickets_by_parent_id_configurations(parent_id, client_id, configuration_reference)
        print("The response of ProjectTicketsApi->post_project_tickets_by_parent_id_configurations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectTicketsApi->post_project_tickets_by_parent_id_configurations: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| ticketId | 
 **client_id** | **str**|  | 
 **configuration_reference** | [**ConfigurationReference**](ConfigurationReference.md)| configuration | 

### Return type

[**ConfigurationReference**](ConfigurationReference.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | ConfigurationReference |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_project_tickets_by_parent_id_convert**
> SuccessResponse post_project_tickets_by_parent_id_convert(parent_id, client_id, convert_item)

Post SuccessResponse

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.convert_item import ConvertItem
from connectwise_psa.models.success_response import SuccessResponse
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
    api_instance = connectwise_psa.ProjectTicketsApi(api_client)
    parent_id = 56 # int | ticketId
    client_id = 'client_id_example' # str | 
    convert_item = connectwise_psa.ConvertItem() # ConvertItem | item

    try:
        # Post SuccessResponse
        api_response = api_instance.post_project_tickets_by_parent_id_convert(parent_id, client_id, convert_item)
        print("The response of ProjectTicketsApi->post_project_tickets_by_parent_id_convert:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectTicketsApi->post_project_tickets_by_parent_id_convert: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| ticketId | 
 **client_id** | **str**|  | 
 **convert_item** | [**ConvertItem**](ConvertItem.md)| item | 

### Return type

[**SuccessResponse**](SuccessResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | SuccessResponse |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_project_tickets_search**
> List[ProjectTicket] post_project_tickets_search(client_id, filter_values)

Post List of ProjectTicket

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.filter_values import FilterValues
from connectwise_psa.models.project_ticket import ProjectTicket
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
    api_instance = connectwise_psa.ProjectTicketsApi(api_client)
    client_id = 'client_id_example' # str | 
    filter_values = connectwise_psa.FilterValues() # FilterValues | filterValues

    try:
        # Post List of ProjectTicket
        api_response = api_instance.post_project_tickets_search(client_id, filter_values)
        print("The response of ProjectTicketsApi->post_project_tickets_search:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectTicketsApi->post_project_tickets_search: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**|  | 
 **filter_values** | [**FilterValues**](FilterValues.md)| filterValues | 

### Return type

[**List[ProjectTicket]**](ProjectTicket.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of ProjectTicket |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_project_tickets_by_id**
> ProjectTicket put_project_tickets_by_id(id, client_id, project_ticket)

Put ProjectTicket

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.project_ticket import ProjectTicket
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
    api_instance = connectwise_psa.ProjectTicketsApi(api_client)
    id = 56 # int | ticketId
    client_id = 'client_id_example' # str | 
    project_ticket = connectwise_psa.ProjectTicket() # ProjectTicket | ticket

    try:
        # Put ProjectTicket
        api_response = api_instance.put_project_tickets_by_id(id, client_id, project_ticket)
        print("The response of ProjectTicketsApi->put_project_tickets_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectTicketsApi->put_project_tickets_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ticketId | 
 **client_id** | **str**|  | 
 **project_ticket** | [**ProjectTicket**](ProjectTicket.md)| ticket | 

### Return type

[**ProjectTicket**](ProjectTicket.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ProjectTicket |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

