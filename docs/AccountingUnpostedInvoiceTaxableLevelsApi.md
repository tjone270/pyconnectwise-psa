# connectwise_psa.AccountingUnpostedInvoiceTaxableLevelsApi

All URIs are relative to *https://api-aus.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_finance_accounting_unpostedinvoices_by_parent_id_taxable_levels**](AccountingUnpostedInvoiceTaxableLevelsApi.md#get_finance_accounting_unpostedinvoices_by_parent_id_taxable_levels) | **GET** /finance/accounting/unpostedinvoices/{parentId}/taxableLevels | Get List of UnpostedInvoiceTaxableLevel
[**get_finance_accounting_unpostedinvoices_by_parent_id_taxable_levels_by_id**](AccountingUnpostedInvoiceTaxableLevelsApi.md#get_finance_accounting_unpostedinvoices_by_parent_id_taxable_levels_by_id) | **GET** /finance/accounting/unpostedinvoices/{parentId}/taxableLevels/{id} | Get UnpostedInvoiceTaxableLevel
[**get_finance_accounting_unpostedinvoices_by_parent_id_taxable_levels_count**](AccountingUnpostedInvoiceTaxableLevelsApi.md#get_finance_accounting_unpostedinvoices_by_parent_id_taxable_levels_count) | **GET** /finance/accounting/unpostedinvoices/{parentId}/taxableLevels/count | Get Count of UnpostedInvoiceTaxableLevel


# **get_finance_accounting_unpostedinvoices_by_parent_id_taxable_levels**
> List[UnpostedInvoiceTaxableLevel] get_finance_accounting_unpostedinvoices_by_parent_id_taxable_levels(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of UnpostedInvoiceTaxableLevel

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.unposted_invoice_taxable_level import UnpostedInvoiceTaxableLevel
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
    api_instance = connectwise_psa.AccountingUnpostedInvoiceTaxableLevelsApi(api_client)
    parent_id = 56 # int | unpostedinvoiceId
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
        # Get List of UnpostedInvoiceTaxableLevel
        api_response = api_instance.get_finance_accounting_unpostedinvoices_by_parent_id_taxable_levels(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of AccountingUnpostedInvoiceTaxableLevelsApi->get_finance_accounting_unpostedinvoices_by_parent_id_taxable_levels:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountingUnpostedInvoiceTaxableLevelsApi->get_finance_accounting_unpostedinvoices_by_parent_id_taxable_levels: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| unpostedinvoiceId | 
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

[**List[UnpostedInvoiceTaxableLevel]**](UnpostedInvoiceTaxableLevel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of UnpostedInvoiceTaxableLevel |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_finance_accounting_unpostedinvoices_by_parent_id_taxable_levels_by_id**
> UnpostedInvoiceTaxableLevel get_finance_accounting_unpostedinvoices_by_parent_id_taxable_levels_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get UnpostedInvoiceTaxableLevel

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.unposted_invoice_taxable_level import UnpostedInvoiceTaxableLevel
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
    api_instance = connectwise_psa.AccountingUnpostedInvoiceTaxableLevelsApi(api_client)
    id = 56 # int | taxableLevelId
    parent_id = 56 # int | unpostedinvoiceId
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
        # Get UnpostedInvoiceTaxableLevel
        api_response = api_instance.get_finance_accounting_unpostedinvoices_by_parent_id_taxable_levels_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of AccountingUnpostedInvoiceTaxableLevelsApi->get_finance_accounting_unpostedinvoices_by_parent_id_taxable_levels_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountingUnpostedInvoiceTaxableLevelsApi->get_finance_accounting_unpostedinvoices_by_parent_id_taxable_levels_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| taxableLevelId | 
 **parent_id** | **int**| unpostedinvoiceId | 
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

[**UnpostedInvoiceTaxableLevel**](UnpostedInvoiceTaxableLevel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | UnpostedInvoiceTaxableLevel |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_finance_accounting_unpostedinvoices_by_parent_id_taxable_levels_count**
> Count get_finance_accounting_unpostedinvoices_by_parent_id_taxable_levels_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Count of UnpostedInvoiceTaxableLevel

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
    api_instance = connectwise_psa.AccountingUnpostedInvoiceTaxableLevelsApi(api_client)
    parent_id = 56 # int | unpostedinvoiceId
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
        # Get Count of UnpostedInvoiceTaxableLevel
        api_response = api_instance.get_finance_accounting_unpostedinvoices_by_parent_id_taxable_levels_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of AccountingUnpostedInvoiceTaxableLevelsApi->get_finance_accounting_unpostedinvoices_by_parent_id_taxable_levels_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountingUnpostedInvoiceTaxableLevelsApi->get_finance_accounting_unpostedinvoices_by_parent_id_taxable_levels_count: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| unpostedinvoiceId | 
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

