# connectwise_psa.InvoicePaymentsApi

All URIs are relative to *https://aus-api.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_finance_invoices_by_parent_id_payments_by_id**](InvoicePaymentsApi.md#delete_finance_invoices_by_parent_id_payments_by_id) | **DELETE** /finance/invoices/{parentId}/payments/{id} | Delete Payment
[**get_finance_invoices_by_parent_id_payments**](InvoicePaymentsApi.md#get_finance_invoices_by_parent_id_payments) | **GET** /finance/invoices/{parentId}/payments | Get List of Payment
[**get_finance_invoices_by_parent_id_payments_by_id**](InvoicePaymentsApi.md#get_finance_invoices_by_parent_id_payments_by_id) | **GET** /finance/invoices/{parentId}/payments/{id} | Get Payment
[**patch_finance_invoices_by_parent_id_payments_by_id**](InvoicePaymentsApi.md#patch_finance_invoices_by_parent_id_payments_by_id) | **PATCH** /finance/invoices/{parentId}/payments/{id} | Patch Payment
[**post_finance_invoices_by_parent_id_payments**](InvoicePaymentsApi.md#post_finance_invoices_by_parent_id_payments) | **POST** /finance/invoices/{parentId}/payments | Post Payment
[**put_finance_invoices_by_parent_id_payments_by_id**](InvoicePaymentsApi.md#put_finance_invoices_by_parent_id_payments_by_id) | **PUT** /finance/invoices/{parentId}/payments/{id} | Put Payment


# **delete_finance_invoices_by_parent_id_payments_by_id**
> delete_finance_invoices_by_parent_id_payments_by_id(id, parent_id, client_id)

Delete Payment

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
    api_instance = connectwise_psa.InvoicePaymentsApi(api_client)
    id = 56 # int | paymentId
    parent_id = 56 # int | invoiceId
    client_id = 'client_id_example' # str | 

    try:
        # Delete Payment
        api_instance.delete_finance_invoices_by_parent_id_payments_by_id(id, parent_id, client_id)
    except Exception as e:
        print("Exception when calling InvoicePaymentsApi->delete_finance_invoices_by_parent_id_payments_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| paymentId | 
 **parent_id** | **int**| invoiceId | 
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

# **get_finance_invoices_by_parent_id_payments**
> List[InvoicePayment] get_finance_invoices_by_parent_id_payments(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of Payment

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.invoice_payment import InvoicePayment
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
    api_instance = connectwise_psa.InvoicePaymentsApi(api_client)
    parent_id = 56 # int | invoiceId
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
        # Get List of Payment
        api_response = api_instance.get_finance_invoices_by_parent_id_payments(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of InvoicePaymentsApi->get_finance_invoices_by_parent_id_payments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoicePaymentsApi->get_finance_invoices_by_parent_id_payments: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| invoiceId | 
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

[**List[InvoicePayment]**](InvoicePayment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of Payment |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_finance_invoices_by_parent_id_payments_by_id**
> InvoicePayment get_finance_invoices_by_parent_id_payments_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Payment

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.invoice_payment import InvoicePayment
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
    api_instance = connectwise_psa.InvoicePaymentsApi(api_client)
    id = 56 # int | paymentId
    parent_id = 56 # int | invoiceId
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
        # Get Payment
        api_response = api_instance.get_finance_invoices_by_parent_id_payments_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of InvoicePaymentsApi->get_finance_invoices_by_parent_id_payments_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoicePaymentsApi->get_finance_invoices_by_parent_id_payments_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| paymentId | 
 **parent_id** | **int**| invoiceId | 
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

[**InvoicePayment**](InvoicePayment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Payment |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_finance_invoices_by_parent_id_payments_by_id**
> InvoicePayment patch_finance_invoices_by_parent_id_payments_by_id(id, parent_id, client_id, patch_operation)

Patch Payment

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.invoice_payment import InvoicePayment
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
    api_instance = connectwise_psa.InvoicePaymentsApi(api_client)
    id = 56 # int | paymentId
    parent_id = 56 # int | invoiceId
    client_id = 'client_id_example' # str | 
    patch_operation = [connectwise_psa.PatchOperation()] # List[PatchOperation] | List of PatchOperation

    try:
        # Patch Payment
        api_response = api_instance.patch_finance_invoices_by_parent_id_payments_by_id(id, parent_id, client_id, patch_operation)
        print("The response of InvoicePaymentsApi->patch_finance_invoices_by_parent_id_payments_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoicePaymentsApi->patch_finance_invoices_by_parent_id_payments_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| paymentId | 
 **parent_id** | **int**| invoiceId | 
 **client_id** | **str**|  | 
 **patch_operation** | [**List[PatchOperation]**](PatchOperation.md)| List of PatchOperation | 

### Return type

[**InvoicePayment**](InvoicePayment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Payment |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_finance_invoices_by_parent_id_payments**
> InvoicePayment post_finance_invoices_by_parent_id_payments(parent_id, client_id, invoice_payment)

Post Payment

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.invoice_payment import InvoicePayment
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
    api_instance = connectwise_psa.InvoicePaymentsApi(api_client)
    parent_id = 56 # int | invoiceId
    client_id = 'client_id_example' # str | 
    invoice_payment = connectwise_psa.InvoicePayment() # InvoicePayment | payment

    try:
        # Post Payment
        api_response = api_instance.post_finance_invoices_by_parent_id_payments(parent_id, client_id, invoice_payment)
        print("The response of InvoicePaymentsApi->post_finance_invoices_by_parent_id_payments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoicePaymentsApi->post_finance_invoices_by_parent_id_payments: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| invoiceId | 
 **client_id** | **str**|  | 
 **invoice_payment** | [**InvoicePayment**](InvoicePayment.md)| payment | 

### Return type

[**InvoicePayment**](InvoicePayment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Payment |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_finance_invoices_by_parent_id_payments_by_id**
> InvoicePayment put_finance_invoices_by_parent_id_payments_by_id(id, parent_id, client_id, invoice_payment)

Put Payment

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.invoice_payment import InvoicePayment
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
    api_instance = connectwise_psa.InvoicePaymentsApi(api_client)
    id = 56 # int | paymentId
    parent_id = 56 # int | invoiceId
    client_id = 'client_id_example' # str | 
    invoice_payment = connectwise_psa.InvoicePayment() # InvoicePayment | payment

    try:
        # Put Payment
        api_response = api_instance.put_finance_invoices_by_parent_id_payments_by_id(id, parent_id, client_id, invoice_payment)
        print("The response of InvoicePaymentsApi->put_finance_invoices_by_parent_id_payments_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoicePaymentsApi->put_finance_invoices_by_parent_id_payments_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| paymentId | 
 **parent_id** | **int**| invoiceId | 
 **client_id** | **str**|  | 
 **invoice_payment** | [**InvoicePayment**](InvoicePayment.md)| payment | 

### Return type

[**InvoicePayment**](InvoicePayment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Payment |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

