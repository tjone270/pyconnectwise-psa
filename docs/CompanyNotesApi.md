# connectwise_psa.CompanyNotesApi

All URIs are relative to *https://api-aus.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_company_companies_by_parent_id_notes_by_id**](CompanyNotesApi.md#delete_company_companies_by_parent_id_notes_by_id) | **DELETE** /company/companies/{parentId}/notes/{id} | Delete CompanyNote
[**get_company_companies_by_parent_id_notes**](CompanyNotesApi.md#get_company_companies_by_parent_id_notes) | **GET** /company/companies/{parentId}/notes | Get List of CompanyNote
[**get_company_companies_by_parent_id_notes_by_id**](CompanyNotesApi.md#get_company_companies_by_parent_id_notes_by_id) | **GET** /company/companies/{parentId}/notes/{id} | Get CompanyNote
[**get_company_companies_by_parent_id_notes_count**](CompanyNotesApi.md#get_company_companies_by_parent_id_notes_count) | **GET** /company/companies/{parentId}/notes/count | Get Count of CompanyNote
[**patch_company_companies_by_parent_id_notes_by_id**](CompanyNotesApi.md#patch_company_companies_by_parent_id_notes_by_id) | **PATCH** /company/companies/{parentId}/notes/{id} | Patch CompanyNote
[**post_company_companies_by_parent_id_notes**](CompanyNotesApi.md#post_company_companies_by_parent_id_notes) | **POST** /company/companies/{parentId}/notes | Post CompanyNote
[**put_company_companies_by_parent_id_notes_by_id**](CompanyNotesApi.md#put_company_companies_by_parent_id_notes_by_id) | **PUT** /company/companies/{parentId}/notes/{id} | Put CompanyNote


# **delete_company_companies_by_parent_id_notes_by_id**
> delete_company_companies_by_parent_id_notes_by_id(id, parent_id, client_id)

Delete CompanyNote

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
    api_instance = connectwise_psa.CompanyNotesApi(api_client)
    id = 56 # int | noteId
    parent_id = 56 # int | companyId
    client_id = 'client_id_example' # str | 

    try:
        # Delete CompanyNote
        api_instance.delete_company_companies_by_parent_id_notes_by_id(id, parent_id, client_id)
    except Exception as e:
        print("Exception when calling CompanyNotesApi->delete_company_companies_by_parent_id_notes_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| noteId | 
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

# **get_company_companies_by_parent_id_notes**
> List[CompanyNote] get_company_companies_by_parent_id_notes(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of CompanyNote

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.company_note import CompanyNote
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
    api_instance = connectwise_psa.CompanyNotesApi(api_client)
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
        # Get List of CompanyNote
        api_response = api_instance.get_company_companies_by_parent_id_notes(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of CompanyNotesApi->get_company_companies_by_parent_id_notes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompanyNotesApi->get_company_companies_by_parent_id_notes: %s\n" % e)
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

[**List[CompanyNote]**](CompanyNote.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of CompanyNote |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_company_companies_by_parent_id_notes_by_id**
> CompanyNote get_company_companies_by_parent_id_notes_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get CompanyNote

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.company_note import CompanyNote
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
    api_instance = connectwise_psa.CompanyNotesApi(api_client)
    id = 56 # int | noteId
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
        # Get CompanyNote
        api_response = api_instance.get_company_companies_by_parent_id_notes_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of CompanyNotesApi->get_company_companies_by_parent_id_notes_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompanyNotesApi->get_company_companies_by_parent_id_notes_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| noteId | 
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

[**CompanyNote**](CompanyNote.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | CompanyNote |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_company_companies_by_parent_id_notes_count**
> Count get_company_companies_by_parent_id_notes_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Count of CompanyNote

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
    api_instance = connectwise_psa.CompanyNotesApi(api_client)
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
        # Get Count of CompanyNote
        api_response = api_instance.get_company_companies_by_parent_id_notes_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of CompanyNotesApi->get_company_companies_by_parent_id_notes_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompanyNotesApi->get_company_companies_by_parent_id_notes_count: %s\n" % e)
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

# **patch_company_companies_by_parent_id_notes_by_id**
> CompanyNote patch_company_companies_by_parent_id_notes_by_id(id, parent_id, client_id, patch_operation)

Patch CompanyNote

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.company_note import CompanyNote
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
    api_instance = connectwise_psa.CompanyNotesApi(api_client)
    id = 56 # int | noteId
    parent_id = 56 # int | companyId
    client_id = 'client_id_example' # str | 
    patch_operation = [connectwise_psa.PatchOperation()] # List[PatchOperation] | List of PatchOperation

    try:
        # Patch CompanyNote
        api_response = api_instance.patch_company_companies_by_parent_id_notes_by_id(id, parent_id, client_id, patch_operation)
        print("The response of CompanyNotesApi->patch_company_companies_by_parent_id_notes_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompanyNotesApi->patch_company_companies_by_parent_id_notes_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| noteId | 
 **parent_id** | **int**| companyId | 
 **client_id** | **str**|  | 
 **patch_operation** | [**List[PatchOperation]**](PatchOperation.md)| List of PatchOperation | 

### Return type

[**CompanyNote**](CompanyNote.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | CompanyNote |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_company_companies_by_parent_id_notes**
> CompanyNote post_company_companies_by_parent_id_notes(parent_id, client_id, company_note)

Post CompanyNote

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.company_note import CompanyNote
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
    api_instance = connectwise_psa.CompanyNotesApi(api_client)
    parent_id = 56 # int | companyId
    client_id = 'client_id_example' # str | 
    company_note = connectwise_psa.CompanyNote() # CompanyNote | companyNote

    try:
        # Post CompanyNote
        api_response = api_instance.post_company_companies_by_parent_id_notes(parent_id, client_id, company_note)
        print("The response of CompanyNotesApi->post_company_companies_by_parent_id_notes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompanyNotesApi->post_company_companies_by_parent_id_notes: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| companyId | 
 **client_id** | **str**|  | 
 **company_note** | [**CompanyNote**](CompanyNote.md)| companyNote | 

### Return type

[**CompanyNote**](CompanyNote.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | CompanyNote |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_company_companies_by_parent_id_notes_by_id**
> CompanyNote put_company_companies_by_parent_id_notes_by_id(id, parent_id, client_id, company_note)

Put CompanyNote

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.company_note import CompanyNote
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
    api_instance = connectwise_psa.CompanyNotesApi(api_client)
    id = 56 # int | noteId
    parent_id = 56 # int | companyId
    client_id = 'client_id_example' # str | 
    company_note = connectwise_psa.CompanyNote() # CompanyNote | companyNote

    try:
        # Put CompanyNote
        api_response = api_instance.put_company_companies_by_parent_id_notes_by_id(id, parent_id, client_id, company_note)
        print("The response of CompanyNotesApi->put_company_companies_by_parent_id_notes_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompanyNotesApi->put_company_companies_by_parent_id_notes_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| noteId | 
 **parent_id** | **int**| companyId | 
 **client_id** | **str**|  | 
 **company_note** | [**CompanyNote**](CompanyNote.md)| companyNote | 

### Return type

[**CompanyNote**](CompanyNote.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | CompanyNote |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

