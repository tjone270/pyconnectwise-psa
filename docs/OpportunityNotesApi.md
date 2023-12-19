# connectwise_psa.OpportunityNotesApi

All URIs are relative to *https://api-aus.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_sales_opportunities_by_parent_id_notes_by_id**](OpportunityNotesApi.md#delete_sales_opportunities_by_parent_id_notes_by_id) | **DELETE** /sales/opportunities/{parentId}/notes/{id} | Delete OpportunityNote
[**get_sales_opportunities_by_parent_id_notes**](OpportunityNotesApi.md#get_sales_opportunities_by_parent_id_notes) | **GET** /sales/opportunities/{parentId}/notes | Get List of OpportunityNote
[**get_sales_opportunities_by_parent_id_notes_by_id**](OpportunityNotesApi.md#get_sales_opportunities_by_parent_id_notes_by_id) | **GET** /sales/opportunities/{parentId}/notes/{id} | Get OpportunityNote
[**get_sales_opportunities_by_parent_id_notes_count**](OpportunityNotesApi.md#get_sales_opportunities_by_parent_id_notes_count) | **GET** /sales/opportunities/{parentId}/notes/count | Get List of OpportunityNote
[**patch_sales_opportunities_by_parent_id_notes_by_id**](OpportunityNotesApi.md#patch_sales_opportunities_by_parent_id_notes_by_id) | **PATCH** /sales/opportunities/{parentId}/notes/{id} | Patch OpportunityNote
[**post_sales_opportunities_by_parent_id_notes**](OpportunityNotesApi.md#post_sales_opportunities_by_parent_id_notes) | **POST** /sales/opportunities/{parentId}/notes | Post OpportunityNote
[**put_sales_opportunities_by_parent_id_notes_by_id**](OpportunityNotesApi.md#put_sales_opportunities_by_parent_id_notes_by_id) | **PUT** /sales/opportunities/{parentId}/notes/{id} | Put OpportunityNote


# **delete_sales_opportunities_by_parent_id_notes_by_id**
> delete_sales_opportunities_by_parent_id_notes_by_id(id, parent_id, client_id)

Delete OpportunityNote

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
    api_instance = connectwise_psa.OpportunityNotesApi(api_client)
    id = 56 # int | noteId
    parent_id = 56 # int | opportunityId
    client_id = 'client_id_example' # str | 

    try:
        # Delete OpportunityNote
        api_instance.delete_sales_opportunities_by_parent_id_notes_by_id(id, parent_id, client_id)
    except Exception as e:
        print("Exception when calling OpportunityNotesApi->delete_sales_opportunities_by_parent_id_notes_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| noteId | 
 **parent_id** | **int**| opportunityId | 
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

# **get_sales_opportunities_by_parent_id_notes**
> List[OpportunityNote] get_sales_opportunities_by_parent_id_notes(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of OpportunityNote

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.opportunity_note import OpportunityNote
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
    api_instance = connectwise_psa.OpportunityNotesApi(api_client)
    parent_id = 56 # int | opportunityId
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
        # Get List of OpportunityNote
        api_response = api_instance.get_sales_opportunities_by_parent_id_notes(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of OpportunityNotesApi->get_sales_opportunities_by_parent_id_notes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpportunityNotesApi->get_sales_opportunities_by_parent_id_notes: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| opportunityId | 
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

[**List[OpportunityNote]**](OpportunityNote.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of OpportunityNote |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sales_opportunities_by_parent_id_notes_by_id**
> OpportunityNote get_sales_opportunities_by_parent_id_notes_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get OpportunityNote

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.opportunity_note import OpportunityNote
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
    api_instance = connectwise_psa.OpportunityNotesApi(api_client)
    id = 56 # int | noteId
    parent_id = 56 # int | opportunityId
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
        # Get OpportunityNote
        api_response = api_instance.get_sales_opportunities_by_parent_id_notes_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of OpportunityNotesApi->get_sales_opportunities_by_parent_id_notes_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpportunityNotesApi->get_sales_opportunities_by_parent_id_notes_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| noteId | 
 **parent_id** | **int**| opportunityId | 
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

[**OpportunityNote**](OpportunityNote.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OpportunityNote |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sales_opportunities_by_parent_id_notes_count**
> List[OpportunityNote] get_sales_opportunities_by_parent_id_notes_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of OpportunityNote

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.opportunity_note import OpportunityNote
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
    api_instance = connectwise_psa.OpportunityNotesApi(api_client)
    parent_id = 56 # int | opportunityId
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
        # Get List of OpportunityNote
        api_response = api_instance.get_sales_opportunities_by_parent_id_notes_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of OpportunityNotesApi->get_sales_opportunities_by_parent_id_notes_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpportunityNotesApi->get_sales_opportunities_by_parent_id_notes_count: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| opportunityId | 
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

[**List[OpportunityNote]**](OpportunityNote.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of OpportunityNote |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_sales_opportunities_by_parent_id_notes_by_id**
> OpportunityNote patch_sales_opportunities_by_parent_id_notes_by_id(id, parent_id, client_id, patch_operation)

Patch OpportunityNote

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.opportunity_note import OpportunityNote
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
    api_instance = connectwise_psa.OpportunityNotesApi(api_client)
    id = 56 # int | noteId
    parent_id = 56 # int | opportunityId
    client_id = 'client_id_example' # str | 
    patch_operation = [connectwise_psa.PatchOperation()] # List[PatchOperation] | List of PatchOperation

    try:
        # Patch OpportunityNote
        api_response = api_instance.patch_sales_opportunities_by_parent_id_notes_by_id(id, parent_id, client_id, patch_operation)
        print("The response of OpportunityNotesApi->patch_sales_opportunities_by_parent_id_notes_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpportunityNotesApi->patch_sales_opportunities_by_parent_id_notes_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| noteId | 
 **parent_id** | **int**| opportunityId | 
 **client_id** | **str**|  | 
 **patch_operation** | [**List[PatchOperation]**](PatchOperation.md)| List of PatchOperation | 

### Return type

[**OpportunityNote**](OpportunityNote.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OpportunityNote |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_sales_opportunities_by_parent_id_notes**
> OpportunityNote post_sales_opportunities_by_parent_id_notes(parent_id, client_id, opportunity_note)

Post OpportunityNote

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.opportunity_note import OpportunityNote
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
    api_instance = connectwise_psa.OpportunityNotesApi(api_client)
    parent_id = 56 # int | opportunityId
    client_id = 'client_id_example' # str | 
    opportunity_note = connectwise_psa.OpportunityNote() # OpportunityNote | note

    try:
        # Post OpportunityNote
        api_response = api_instance.post_sales_opportunities_by_parent_id_notes(parent_id, client_id, opportunity_note)
        print("The response of OpportunityNotesApi->post_sales_opportunities_by_parent_id_notes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpportunityNotesApi->post_sales_opportunities_by_parent_id_notes: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| opportunityId | 
 **client_id** | **str**|  | 
 **opportunity_note** | [**OpportunityNote**](OpportunityNote.md)| note | 

### Return type

[**OpportunityNote**](OpportunityNote.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | OpportunityNote |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_sales_opportunities_by_parent_id_notes_by_id**
> OpportunityNote put_sales_opportunities_by_parent_id_notes_by_id(id, parent_id, client_id, opportunity_note)

Put OpportunityNote

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.opportunity_note import OpportunityNote
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
    api_instance = connectwise_psa.OpportunityNotesApi(api_client)
    id = 56 # int | noteId
    parent_id = 56 # int | opportunityId
    client_id = 'client_id_example' # str | 
    opportunity_note = connectwise_psa.OpportunityNote() # OpportunityNote | note

    try:
        # Put OpportunityNote
        api_response = api_instance.put_sales_opportunities_by_parent_id_notes_by_id(id, parent_id, client_id, opportunity_note)
        print("The response of OpportunityNotesApi->put_sales_opportunities_by_parent_id_notes_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpportunityNotesApi->put_sales_opportunities_by_parent_id_notes_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| noteId | 
 **parent_id** | **int**| opportunityId | 
 **client_id** | **str**|  | 
 **opportunity_note** | [**OpportunityNote**](OpportunityNote.md)| note | 

### Return type

[**OpportunityNote**](OpportunityNote.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OpportunityNote |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

