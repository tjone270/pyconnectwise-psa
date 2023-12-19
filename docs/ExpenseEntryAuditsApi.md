# connectwise_psa.ExpenseEntryAuditsApi

All URIs are relative to *https://aus-api.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_expense_entries_by_parent_id_audits**](ExpenseEntryAuditsApi.md#get_expense_entries_by_parent_id_audits) | **GET** /expense/entries/{parentId}/audits | Get List of ExpenseEntryAudit
[**get_expense_entries_by_parent_id_audits_by_id**](ExpenseEntryAuditsApi.md#get_expense_entries_by_parent_id_audits_by_id) | **GET** /expense/entries/{parentId}/audits/{id} | Get ExpenseEntryAudit
[**get_expense_entries_by_parent_id_audits_count**](ExpenseEntryAuditsApi.md#get_expense_entries_by_parent_id_audits_count) | **GET** /expense/entries/{parentId}/audits/count | Get Count of ExpenseEntryAudit


# **get_expense_entries_by_parent_id_audits**
> List[ExpenseEntryAudit] get_expense_entries_by_parent_id_audits(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of ExpenseEntryAudit

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.expense_entry_audit import ExpenseEntryAudit
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
    api_instance = connectwise_psa.ExpenseEntryAuditsApi(api_client)
    parent_id = 56 # int | entryId
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
        # Get List of ExpenseEntryAudit
        api_response = api_instance.get_expense_entries_by_parent_id_audits(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of ExpenseEntryAuditsApi->get_expense_entries_by_parent_id_audits:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExpenseEntryAuditsApi->get_expense_entries_by_parent_id_audits: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| entryId | 
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

[**List[ExpenseEntryAudit]**](ExpenseEntryAudit.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of ExpenseEntryAudit |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_expense_entries_by_parent_id_audits_by_id**
> ExpenseEntryAudit get_expense_entries_by_parent_id_audits_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get ExpenseEntryAudit

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.expense_entry_audit import ExpenseEntryAudit
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
    api_instance = connectwise_psa.ExpenseEntryAuditsApi(api_client)
    id = 56 # int | auditId
    parent_id = 56 # int | entryId
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
        # Get ExpenseEntryAudit
        api_response = api_instance.get_expense_entries_by_parent_id_audits_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of ExpenseEntryAuditsApi->get_expense_entries_by_parent_id_audits_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExpenseEntryAuditsApi->get_expense_entries_by_parent_id_audits_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| auditId | 
 **parent_id** | **int**| entryId | 
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

[**ExpenseEntryAudit**](ExpenseEntryAudit.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ExpenseEntryAudit |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_expense_entries_by_parent_id_audits_count**
> Count get_expense_entries_by_parent_id_audits_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Count of ExpenseEntryAudit

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
    api_instance = connectwise_psa.ExpenseEntryAuditsApi(api_client)
    parent_id = 56 # int | entryId
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
        # Get Count of ExpenseEntryAudit
        api_response = api_instance.get_expense_entries_by_parent_id_audits_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of ExpenseEntryAuditsApi->get_expense_entries_by_parent_id_audits_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExpenseEntryAuditsApi->get_expense_entries_by_parent_id_audits_count: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| entryId | 
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

