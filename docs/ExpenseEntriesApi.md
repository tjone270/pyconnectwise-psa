# connectwise_psa.ExpenseEntriesApi

All URIs are relative to *https://aus-api.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_expense_entries_by_id**](ExpenseEntriesApi.md#delete_expense_entries_by_id) | **DELETE** /expense/entries/{id} | Delete ExpenseEntry
[**get_expense_entries**](ExpenseEntriesApi.md#get_expense_entries) | **GET** /expense/entries | Get List of ExpenseEntry
[**get_expense_entries_by_id**](ExpenseEntriesApi.md#get_expense_entries_by_id) | **GET** /expense/entries/{id} | Get ExpenseEntry
[**get_expense_entries_count**](ExpenseEntriesApi.md#get_expense_entries_count) | **GET** /expense/entries/count | Get Count of ExpenseEntry
[**patch_expense_entries_by_id**](ExpenseEntriesApi.md#patch_expense_entries_by_id) | **PATCH** /expense/entries/{id} | Patch ExpenseEntry
[**post_expense_entries**](ExpenseEntriesApi.md#post_expense_entries) | **POST** /expense/entries | Post ExpenseEntry
[**put_expense_entries_by_id**](ExpenseEntriesApi.md#put_expense_entries_by_id) | **PUT** /expense/entries/{id} | Put ExpenseEntry


# **delete_expense_entries_by_id**
> delete_expense_entries_by_id(id, client_id)

Delete ExpenseEntry

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
    api_instance = connectwise_psa.ExpenseEntriesApi(api_client)
    id = 56 # int | entryId
    client_id = 'client_id_example' # str | 

    try:
        # Delete ExpenseEntry
        api_instance.delete_expense_entries_by_id(id, client_id)
    except Exception as e:
        print("Exception when calling ExpenseEntriesApi->delete_expense_entries_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| entryId | 
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

# **get_expense_entries**
> List[ExpenseEntry] get_expense_entries(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of ExpenseEntry

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.expense_entry import ExpenseEntry
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
    api_instance = connectwise_psa.ExpenseEntriesApi(api_client)
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
        # Get List of ExpenseEntry
        api_response = api_instance.get_expense_entries(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of ExpenseEntriesApi->get_expense_entries:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExpenseEntriesApi->get_expense_entries: %s\n" % e)
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

[**List[ExpenseEntry]**](ExpenseEntry.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of ExpenseEntry |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_expense_entries_by_id**
> ExpenseEntry get_expense_entries_by_id(id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get ExpenseEntry

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.expense_entry import ExpenseEntry
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
    api_instance = connectwise_psa.ExpenseEntriesApi(api_client)
    id = 56 # int | entryId
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
        # Get ExpenseEntry
        api_response = api_instance.get_expense_entries_by_id(id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of ExpenseEntriesApi->get_expense_entries_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExpenseEntriesApi->get_expense_entries_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| entryId | 
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

[**ExpenseEntry**](ExpenseEntry.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ExpenseEntry |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_expense_entries_count**
> Count get_expense_entries_count(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Count of ExpenseEntry

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
    api_instance = connectwise_psa.ExpenseEntriesApi(api_client)
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
        # Get Count of ExpenseEntry
        api_response = api_instance.get_expense_entries_count(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of ExpenseEntriesApi->get_expense_entries_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExpenseEntriesApi->get_expense_entries_count: %s\n" % e)
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

# **patch_expense_entries_by_id**
> ExpenseEntry patch_expense_entries_by_id(id, client_id, patch_operation)

Patch ExpenseEntry

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.expense_entry import ExpenseEntry
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
    api_instance = connectwise_psa.ExpenseEntriesApi(api_client)
    id = 56 # int | entryId
    client_id = 'client_id_example' # str | 
    patch_operation = [connectwise_psa.PatchOperation()] # List[PatchOperation] | List of PatchOperation

    try:
        # Patch ExpenseEntry
        api_response = api_instance.patch_expense_entries_by_id(id, client_id, patch_operation)
        print("The response of ExpenseEntriesApi->patch_expense_entries_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExpenseEntriesApi->patch_expense_entries_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| entryId | 
 **client_id** | **str**|  | 
 **patch_operation** | [**List[PatchOperation]**](PatchOperation.md)| List of PatchOperation | 

### Return type

[**ExpenseEntry**](ExpenseEntry.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ExpenseEntry |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_expense_entries**
> ExpenseEntry post_expense_entries(client_id, expense_entry)

Post ExpenseEntry

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.expense_entry import ExpenseEntry
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
    api_instance = connectwise_psa.ExpenseEntriesApi(api_client)
    client_id = 'client_id_example' # str | 
    expense_entry = connectwise_psa.ExpenseEntry() # ExpenseEntry | expenseEntry

    try:
        # Post ExpenseEntry
        api_response = api_instance.post_expense_entries(client_id, expense_entry)
        print("The response of ExpenseEntriesApi->post_expense_entries:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExpenseEntriesApi->post_expense_entries: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**|  | 
 **expense_entry** | [**ExpenseEntry**](ExpenseEntry.md)| expenseEntry | 

### Return type

[**ExpenseEntry**](ExpenseEntry.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | ExpenseEntry |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_expense_entries_by_id**
> ExpenseEntry put_expense_entries_by_id(id, client_id, expense_entry)

Put ExpenseEntry

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.expense_entry import ExpenseEntry
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
    api_instance = connectwise_psa.ExpenseEntriesApi(api_client)
    id = 56 # int | entryId
    client_id = 'client_id_example' # str | 
    expense_entry = connectwise_psa.ExpenseEntry() # ExpenseEntry | expenseEntry

    try:
        # Put ExpenseEntry
        api_response = api_instance.put_expense_entries_by_id(id, client_id, expense_entry)
        print("The response of ExpenseEntriesApi->put_expense_entries_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExpenseEntriesApi->put_expense_entries_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| entryId | 
 **client_id** | **str**|  | 
 **expense_entry** | [**ExpenseEntry**](ExpenseEntry.md)| expenseEntry | 

### Return type

[**ExpenseEntry**](ExpenseEntry.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ExpenseEntry |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

