# connectwise_psa.TaxCodeExpenseTypeExemptionsApi

All URIs are relative to *https://api-aus.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_finance_tax_codes_by_parent_id_expense_type_exemptions_by_id**](TaxCodeExpenseTypeExemptionsApi.md#delete_finance_tax_codes_by_parent_id_expense_type_exemptions_by_id) | **DELETE** /finance/taxCodes/{parentId}/expenseTypeExemptions/{id} | Delete ExpenseTypeExemption
[**get_finance_tax_codes_by_parent_id_expense_type_exemptions**](TaxCodeExpenseTypeExemptionsApi.md#get_finance_tax_codes_by_parent_id_expense_type_exemptions) | **GET** /finance/taxCodes/{parentId}/expenseTypeExemptions | Get List of ExpenseTypeExemption
[**get_finance_tax_codes_by_parent_id_expense_type_exemptions_by_id**](TaxCodeExpenseTypeExemptionsApi.md#get_finance_tax_codes_by_parent_id_expense_type_exemptions_by_id) | **GET** /finance/taxCodes/{parentId}/expenseTypeExemptions/{id} | Get ExpenseTypeExemption
[**get_finance_tax_codes_by_parent_id_expense_type_exemptions_count**](TaxCodeExpenseTypeExemptionsApi.md#get_finance_tax_codes_by_parent_id_expense_type_exemptions_count) | **GET** /finance/taxCodes/{parentId}/expenseTypeExemptions/count | Get Count of ExpenseTypeExemption
[**patch_finance_tax_codes_by_parent_id_expense_type_exemptions_by_id**](TaxCodeExpenseTypeExemptionsApi.md#patch_finance_tax_codes_by_parent_id_expense_type_exemptions_by_id) | **PATCH** /finance/taxCodes/{parentId}/expenseTypeExemptions/{id} | Patch ExpenseTypeExemption
[**post_finance_tax_codes_by_parent_id_expense_type_exemptions**](TaxCodeExpenseTypeExemptionsApi.md#post_finance_tax_codes_by_parent_id_expense_type_exemptions) | **POST** /finance/taxCodes/{parentId}/expenseTypeExemptions | Post ExpenseTypeExemption
[**put_finance_tax_codes_by_parent_id_expense_type_exemptions_by_id**](TaxCodeExpenseTypeExemptionsApi.md#put_finance_tax_codes_by_parent_id_expense_type_exemptions_by_id) | **PUT** /finance/taxCodes/{parentId}/expenseTypeExemptions/{id} | Put ExpenseTypeExemption


# **delete_finance_tax_codes_by_parent_id_expense_type_exemptions_by_id**
> delete_finance_tax_codes_by_parent_id_expense_type_exemptions_by_id(id, parent_id, client_id)

Delete ExpenseTypeExemption

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
    api_instance = connectwise_psa.TaxCodeExpenseTypeExemptionsApi(api_client)
    id = 56 # int | expenseTypeExemptionId
    parent_id = 56 # int | taxCodeId
    client_id = 'client_id_example' # str | 

    try:
        # Delete ExpenseTypeExemption
        api_instance.delete_finance_tax_codes_by_parent_id_expense_type_exemptions_by_id(id, parent_id, client_id)
    except Exception as e:
        print("Exception when calling TaxCodeExpenseTypeExemptionsApi->delete_finance_tax_codes_by_parent_id_expense_type_exemptions_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| expenseTypeExemptionId | 
 **parent_id** | **int**| taxCodeId | 
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

# **get_finance_tax_codes_by_parent_id_expense_type_exemptions**
> List[ExpenseTypeExemption] get_finance_tax_codes_by_parent_id_expense_type_exemptions(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of ExpenseTypeExemption

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.expense_type_exemption import ExpenseTypeExemption
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
    api_instance = connectwise_psa.TaxCodeExpenseTypeExemptionsApi(api_client)
    parent_id = 56 # int | taxCodeId
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
        # Get List of ExpenseTypeExemption
        api_response = api_instance.get_finance_tax_codes_by_parent_id_expense_type_exemptions(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of TaxCodeExpenseTypeExemptionsApi->get_finance_tax_codes_by_parent_id_expense_type_exemptions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaxCodeExpenseTypeExemptionsApi->get_finance_tax_codes_by_parent_id_expense_type_exemptions: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| taxCodeId | 
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

[**List[ExpenseTypeExemption]**](ExpenseTypeExemption.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of ExpenseTypeExemption |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_finance_tax_codes_by_parent_id_expense_type_exemptions_by_id**
> ExpenseTypeExemption get_finance_tax_codes_by_parent_id_expense_type_exemptions_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get ExpenseTypeExemption

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.expense_type_exemption import ExpenseTypeExemption
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
    api_instance = connectwise_psa.TaxCodeExpenseTypeExemptionsApi(api_client)
    id = 56 # int | expenseTypeExemptionId
    parent_id = 56 # int | taxCodeId
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
        # Get ExpenseTypeExemption
        api_response = api_instance.get_finance_tax_codes_by_parent_id_expense_type_exemptions_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of TaxCodeExpenseTypeExemptionsApi->get_finance_tax_codes_by_parent_id_expense_type_exemptions_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaxCodeExpenseTypeExemptionsApi->get_finance_tax_codes_by_parent_id_expense_type_exemptions_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| expenseTypeExemptionId | 
 **parent_id** | **int**| taxCodeId | 
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

[**ExpenseTypeExemption**](ExpenseTypeExemption.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ExpenseTypeExemption |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_finance_tax_codes_by_parent_id_expense_type_exemptions_count**
> Count get_finance_tax_codes_by_parent_id_expense_type_exemptions_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Count of ExpenseTypeExemption

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
    api_instance = connectwise_psa.TaxCodeExpenseTypeExemptionsApi(api_client)
    parent_id = 56 # int | taxCodeId
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
        # Get Count of ExpenseTypeExemption
        api_response = api_instance.get_finance_tax_codes_by_parent_id_expense_type_exemptions_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of TaxCodeExpenseTypeExemptionsApi->get_finance_tax_codes_by_parent_id_expense_type_exemptions_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaxCodeExpenseTypeExemptionsApi->get_finance_tax_codes_by_parent_id_expense_type_exemptions_count: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| taxCodeId | 
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

# **patch_finance_tax_codes_by_parent_id_expense_type_exemptions_by_id**
> ExpenseTypeExemption patch_finance_tax_codes_by_parent_id_expense_type_exemptions_by_id(id, parent_id, client_id, patch_operation)

Patch ExpenseTypeExemption

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.expense_type_exemption import ExpenseTypeExemption
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
    api_instance = connectwise_psa.TaxCodeExpenseTypeExemptionsApi(api_client)
    id = 56 # int | expenseTypeExemptionId
    parent_id = 56 # int | taxCodeId
    client_id = 'client_id_example' # str | 
    patch_operation = [connectwise_psa.PatchOperation()] # List[PatchOperation] | List of PatchOperation

    try:
        # Patch ExpenseTypeExemption
        api_response = api_instance.patch_finance_tax_codes_by_parent_id_expense_type_exemptions_by_id(id, parent_id, client_id, patch_operation)
        print("The response of TaxCodeExpenseTypeExemptionsApi->patch_finance_tax_codes_by_parent_id_expense_type_exemptions_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaxCodeExpenseTypeExemptionsApi->patch_finance_tax_codes_by_parent_id_expense_type_exemptions_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| expenseTypeExemptionId | 
 **parent_id** | **int**| taxCodeId | 
 **client_id** | **str**|  | 
 **patch_operation** | [**List[PatchOperation]**](PatchOperation.md)| List of PatchOperation | 

### Return type

[**ExpenseTypeExemption**](ExpenseTypeExemption.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ExpenseTypeExemption |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_finance_tax_codes_by_parent_id_expense_type_exemptions**
> ExpenseTypeExemption post_finance_tax_codes_by_parent_id_expense_type_exemptions(parent_id, client_id, expense_type_exemption)

Post ExpenseTypeExemption

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.expense_type_exemption import ExpenseTypeExemption
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
    api_instance = connectwise_psa.TaxCodeExpenseTypeExemptionsApi(api_client)
    parent_id = 56 # int | taxCodeId
    client_id = 'client_id_example' # str | 
    expense_type_exemption = connectwise_psa.ExpenseTypeExemption() # ExpenseTypeExemption | expenseTypeExemption

    try:
        # Post ExpenseTypeExemption
        api_response = api_instance.post_finance_tax_codes_by_parent_id_expense_type_exemptions(parent_id, client_id, expense_type_exemption)
        print("The response of TaxCodeExpenseTypeExemptionsApi->post_finance_tax_codes_by_parent_id_expense_type_exemptions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaxCodeExpenseTypeExemptionsApi->post_finance_tax_codes_by_parent_id_expense_type_exemptions: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| taxCodeId | 
 **client_id** | **str**|  | 
 **expense_type_exemption** | [**ExpenseTypeExemption**](ExpenseTypeExemption.md)| expenseTypeExemption | 

### Return type

[**ExpenseTypeExemption**](ExpenseTypeExemption.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | ExpenseTypeExemption |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_finance_tax_codes_by_parent_id_expense_type_exemptions_by_id**
> ExpenseTypeExemption put_finance_tax_codes_by_parent_id_expense_type_exemptions_by_id(id, parent_id, client_id, expense_type_exemption)

Put ExpenseTypeExemption

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.expense_type_exemption import ExpenseTypeExemption
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
    api_instance = connectwise_psa.TaxCodeExpenseTypeExemptionsApi(api_client)
    id = 56 # int | expenseTypeExemptionId
    parent_id = 56 # int | taxCodeId
    client_id = 'client_id_example' # str | 
    expense_type_exemption = connectwise_psa.ExpenseTypeExemption() # ExpenseTypeExemption | expenseTypeExemption

    try:
        # Put ExpenseTypeExemption
        api_response = api_instance.put_finance_tax_codes_by_parent_id_expense_type_exemptions_by_id(id, parent_id, client_id, expense_type_exemption)
        print("The response of TaxCodeExpenseTypeExemptionsApi->put_finance_tax_codes_by_parent_id_expense_type_exemptions_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaxCodeExpenseTypeExemptionsApi->put_finance_tax_codes_by_parent_id_expense_type_exemptions_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| expenseTypeExemptionId | 
 **parent_id** | **int**| taxCodeId | 
 **client_id** | **str**|  | 
 **expense_type_exemption** | [**ExpenseTypeExemption**](ExpenseTypeExemption.md)| expenseTypeExemption | 

### Return type

[**ExpenseTypeExemption**](ExpenseTypeExemption.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ExpenseTypeExemption |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

