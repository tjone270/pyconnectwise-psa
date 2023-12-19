# connectwise_psa.ContactNotesApi

All URIs are relative to *https://api-aus.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_company_contacts_by_parent_id_notes_by_id**](ContactNotesApi.md#delete_company_contacts_by_parent_id_notes_by_id) | **DELETE** /company/contacts/{parentId}/notes/{id} | Delete ContactNote
[**get_company_contacts_by_parent_id_notes**](ContactNotesApi.md#get_company_contacts_by_parent_id_notes) | **GET** /company/contacts/{parentId}/notes | Get List of ContactNote
[**get_company_contacts_by_parent_id_notes_by_id**](ContactNotesApi.md#get_company_contacts_by_parent_id_notes_by_id) | **GET** /company/contacts/{parentId}/notes/{id} | Get ContactNote
[**get_company_contacts_by_parent_id_notes_count**](ContactNotesApi.md#get_company_contacts_by_parent_id_notes_count) | **GET** /company/contacts/{parentId}/notes/count | Get Count of ContactNote
[**patch_company_contacts_by_parent_id_notes_by_id**](ContactNotesApi.md#patch_company_contacts_by_parent_id_notes_by_id) | **PATCH** /company/contacts/{parentId}/notes/{id} | Patch ContactNote
[**post_company_contacts_by_parent_id_notes**](ContactNotesApi.md#post_company_contacts_by_parent_id_notes) | **POST** /company/contacts/{parentId}/notes | Post ContactNote
[**put_company_contacts_by_parent_id_notes_by_id**](ContactNotesApi.md#put_company_contacts_by_parent_id_notes_by_id) | **PUT** /company/contacts/{parentId}/notes/{id} | Put ContactNote


# **delete_company_contacts_by_parent_id_notes_by_id**
> delete_company_contacts_by_parent_id_notes_by_id(id, parent_id, client_id)

Delete ContactNote

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
    api_instance = connectwise_psa.ContactNotesApi(api_client)
    id = 56 # int | noteId
    parent_id = 56 # int | contactId
    client_id = 'client_id_example' # str | 

    try:
        # Delete ContactNote
        api_instance.delete_company_contacts_by_parent_id_notes_by_id(id, parent_id, client_id)
    except Exception as e:
        print("Exception when calling ContactNotesApi->delete_company_contacts_by_parent_id_notes_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| noteId | 
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

# **get_company_contacts_by_parent_id_notes**
> List[ContactNote] get_company_contacts_by_parent_id_notes(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of ContactNote

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.contact_note import ContactNote
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
    api_instance = connectwise_psa.ContactNotesApi(api_client)
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
        # Get List of ContactNote
        api_response = api_instance.get_company_contacts_by_parent_id_notes(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of ContactNotesApi->get_company_contacts_by_parent_id_notes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactNotesApi->get_company_contacts_by_parent_id_notes: %s\n" % e)
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

[**List[ContactNote]**](ContactNote.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of ContactNote |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_company_contacts_by_parent_id_notes_by_id**
> ContactNote get_company_contacts_by_parent_id_notes_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get ContactNote

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.contact_note import ContactNote
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
    api_instance = connectwise_psa.ContactNotesApi(api_client)
    id = 56 # int | noteId
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
        # Get ContactNote
        api_response = api_instance.get_company_contacts_by_parent_id_notes_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of ContactNotesApi->get_company_contacts_by_parent_id_notes_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactNotesApi->get_company_contacts_by_parent_id_notes_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| noteId | 
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

[**ContactNote**](ContactNote.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ContactNote |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_company_contacts_by_parent_id_notes_count**
> Count get_company_contacts_by_parent_id_notes_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Count of ContactNote

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
    api_instance = connectwise_psa.ContactNotesApi(api_client)
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
        # Get Count of ContactNote
        api_response = api_instance.get_company_contacts_by_parent_id_notes_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of ContactNotesApi->get_company_contacts_by_parent_id_notes_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactNotesApi->get_company_contacts_by_parent_id_notes_count: %s\n" % e)
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

# **patch_company_contacts_by_parent_id_notes_by_id**
> ContactNote patch_company_contacts_by_parent_id_notes_by_id(id, parent_id, client_id, patch_operation)

Patch ContactNote

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.contact_note import ContactNote
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
    api_instance = connectwise_psa.ContactNotesApi(api_client)
    id = 56 # int | noteId
    parent_id = 56 # int | contactId
    client_id = 'client_id_example' # str | 
    patch_operation = [connectwise_psa.PatchOperation()] # List[PatchOperation] | List of PatchOperation

    try:
        # Patch ContactNote
        api_response = api_instance.patch_company_contacts_by_parent_id_notes_by_id(id, parent_id, client_id, patch_operation)
        print("The response of ContactNotesApi->patch_company_contacts_by_parent_id_notes_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactNotesApi->patch_company_contacts_by_parent_id_notes_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| noteId | 
 **parent_id** | **int**| contactId | 
 **client_id** | **str**|  | 
 **patch_operation** | [**List[PatchOperation]**](PatchOperation.md)| List of PatchOperation | 

### Return type

[**ContactNote**](ContactNote.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ContactNote |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_company_contacts_by_parent_id_notes**
> ContactNote post_company_contacts_by_parent_id_notes(parent_id, client_id, contact_note)

Post ContactNote

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.contact_note import ContactNote
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
    api_instance = connectwise_psa.ContactNotesApi(api_client)
    parent_id = 56 # int | contactId
    client_id = 'client_id_example' # str | 
    contact_note = connectwise_psa.ContactNote() # ContactNote | contactNote

    try:
        # Post ContactNote
        api_response = api_instance.post_company_contacts_by_parent_id_notes(parent_id, client_id, contact_note)
        print("The response of ContactNotesApi->post_company_contacts_by_parent_id_notes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactNotesApi->post_company_contacts_by_parent_id_notes: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| contactId | 
 **client_id** | **str**|  | 
 **contact_note** | [**ContactNote**](ContactNote.md)| contactNote | 

### Return type

[**ContactNote**](ContactNote.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | ContactNote |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_company_contacts_by_parent_id_notes_by_id**
> ContactNote put_company_contacts_by_parent_id_notes_by_id(id, parent_id, client_id, contact_note)

Put ContactNote

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.contact_note import ContactNote
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
    api_instance = connectwise_psa.ContactNotesApi(api_client)
    id = 56 # int | noteId
    parent_id = 56 # int | contactId
    client_id = 'client_id_example' # str | 
    contact_note = connectwise_psa.ContactNote() # ContactNote | contactNote

    try:
        # Put ContactNote
        api_response = api_instance.put_company_contacts_by_parent_id_notes_by_id(id, parent_id, client_id, contact_note)
        print("The response of ContactNotesApi->put_company_contacts_by_parent_id_notes_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactNotesApi->put_company_contacts_by_parent_id_notes_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| noteId | 
 **parent_id** | **int**| contactId | 
 **client_id** | **str**|  | 
 **contact_note** | [**ContactNote**](ContactNote.md)| contactNote | 

### Return type

[**ContactNote**](ContactNote.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ContactNote |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

