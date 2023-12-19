# connectwise_psa.ClosedInvoicesApi

All URIs are relative to *https://api-aus.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**patch_finance_closed_invoices_by_id**](ClosedInvoicesApi.md#patch_finance_closed_invoices_by_id) | **PATCH** /finance/closedInvoices/{id} | Patch ClosedInvoice
[**put_finance_closed_invoices_by_id**](ClosedInvoicesApi.md#put_finance_closed_invoices_by_id) | **PUT** /finance/closedInvoices/{id} | Put ClosedInvoice


# **patch_finance_closed_invoices_by_id**
> ClosedInvoice patch_finance_closed_invoices_by_id(id, client_id, patch_operation)

Patch ClosedInvoice

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.closed_invoice import ClosedInvoice
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
    api_instance = connectwise_psa.ClosedInvoicesApi(api_client)
    id = 56 # int | closedInvoiceId
    client_id = 'client_id_example' # str | 
    patch_operation = [connectwise_psa.PatchOperation()] # List[PatchOperation] | List of PatchOperation

    try:
        # Patch ClosedInvoice
        api_response = api_instance.patch_finance_closed_invoices_by_id(id, client_id, patch_operation)
        print("The response of ClosedInvoicesApi->patch_finance_closed_invoices_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClosedInvoicesApi->patch_finance_closed_invoices_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| closedInvoiceId | 
 **client_id** | **str**|  | 
 **patch_operation** | [**List[PatchOperation]**](PatchOperation.md)| List of PatchOperation | 

### Return type

[**ClosedInvoice**](ClosedInvoice.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ClosedInvoice |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_finance_closed_invoices_by_id**
> ClosedInvoice put_finance_closed_invoices_by_id(id, client_id, closed_invoice)

Put ClosedInvoice

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.closed_invoice import ClosedInvoice
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
    api_instance = connectwise_psa.ClosedInvoicesApi(api_client)
    id = 56 # int | closedInvoiceId
    client_id = 'client_id_example' # str | 
    closed_invoice = connectwise_psa.ClosedInvoice() # ClosedInvoice | closedInvoice

    try:
        # Put ClosedInvoice
        api_response = api_instance.put_finance_closed_invoices_by_id(id, client_id, closed_invoice)
        print("The response of ClosedInvoicesApi->put_finance_closed_invoices_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClosedInvoicesApi->put_finance_closed_invoices_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| closedInvoiceId | 
 **client_id** | **str**|  | 
 **closed_invoice** | [**ClosedInvoice**](ClosedInvoice.md)| closedInvoice | 

### Return type

[**ClosedInvoice**](ClosedInvoice.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ClosedInvoice |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

