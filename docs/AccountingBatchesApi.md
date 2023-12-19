# connectwise_psa.AccountingBatchesApi

All URIs are relative to *https://api-aus.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_finance_accounting_batches_by_id**](AccountingBatchesApi.md#delete_finance_accounting_batches_by_id) | **DELETE** /finance/accounting/batches/{id} | Delete GLExport
[**get_finance_accounting_batches**](AccountingBatchesApi.md#get_finance_accounting_batches) | **GET** /finance/accounting/batches | Get List of AccountingBatch
[**get_finance_accounting_batches_by_id**](AccountingBatchesApi.md#get_finance_accounting_batches_by_id) | **GET** /finance/accounting/batches/{id} | Get AccountingBatch
[**get_finance_accounting_batches_count**](AccountingBatchesApi.md#get_finance_accounting_batches_count) | **GET** /finance/accounting/batches/count | Get Count of AccountingBatch
[**post_finance_accounting_batches**](AccountingBatchesApi.md#post_finance_accounting_batches) | **POST** /finance/accounting/batches | Post GLExport
[**post_finance_accounting_batches_by_id_export**](AccountingBatchesApi.md#post_finance_accounting_batches_by_id_export) | **POST** /finance/accounting/batches/{id}/export | Post GLExport
[**post_finance_accounting_export**](AccountingBatchesApi.md#post_finance_accounting_export) | **POST** /finance/accounting/export | Post GLExport


# **delete_finance_accounting_batches_by_id**
> delete_finance_accounting_batches_by_id(id, client_id)

Delete GLExport

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
    api_instance = connectwise_psa.AccountingBatchesApi(api_client)
    id = 56 # int | batcheId
    client_id = 'client_id_example' # str | 

    try:
        # Delete GLExport
        api_instance.delete_finance_accounting_batches_by_id(id, client_id)
    except Exception as e:
        print("Exception when calling AccountingBatchesApi->delete_finance_accounting_batches_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| batcheId | 
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

# **get_finance_accounting_batches**
> List[AccountingBatch] get_finance_accounting_batches(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of AccountingBatch

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.accounting_batch import AccountingBatch
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
    api_instance = connectwise_psa.AccountingBatchesApi(api_client)
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
        # Get List of AccountingBatch
        api_response = api_instance.get_finance_accounting_batches(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of AccountingBatchesApi->get_finance_accounting_batches:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountingBatchesApi->get_finance_accounting_batches: %s\n" % e)
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

[**List[AccountingBatch]**](AccountingBatch.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of AccountingBatch |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_finance_accounting_batches_by_id**
> AccountingBatch get_finance_accounting_batches_by_id(id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get AccountingBatch

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.accounting_batch import AccountingBatch
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
    api_instance = connectwise_psa.AccountingBatchesApi(api_client)
    id = 56 # int | batcheId
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
        # Get AccountingBatch
        api_response = api_instance.get_finance_accounting_batches_by_id(id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of AccountingBatchesApi->get_finance_accounting_batches_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountingBatchesApi->get_finance_accounting_batches_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| batcheId | 
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

[**AccountingBatch**](AccountingBatch.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | AccountingBatch |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_finance_accounting_batches_count**
> Count get_finance_accounting_batches_count(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Count of AccountingBatch

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
    api_instance = connectwise_psa.AccountingBatchesApi(api_client)
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
        # Get Count of AccountingBatch
        api_response = api_instance.get_finance_accounting_batches_count(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of AccountingBatchesApi->get_finance_accounting_batches_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountingBatchesApi->get_finance_accounting_batches_count: %s\n" % e)
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

# **post_finance_accounting_batches**
> GLExport post_finance_accounting_batches(client_id, create_accounting_batch_request)

Post GLExport

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.create_accounting_batch_request import CreateAccountingBatchRequest
from connectwise_psa.models.gl_export import GLExport
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
    api_instance = connectwise_psa.AccountingBatchesApi(api_client)
    client_id = 'client_id_example' # str | 
    create_accounting_batch_request = connectwise_psa.CreateAccountingBatchRequest() # CreateAccountingBatchRequest | accountingBatchParameters

    try:
        # Post GLExport
        api_response = api_instance.post_finance_accounting_batches(client_id, create_accounting_batch_request)
        print("The response of AccountingBatchesApi->post_finance_accounting_batches:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountingBatchesApi->post_finance_accounting_batches: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**|  | 
 **create_accounting_batch_request** | [**CreateAccountingBatchRequest**](CreateAccountingBatchRequest.md)| accountingBatchParameters | 

### Return type

[**GLExport**](GLExport.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | GLExport |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_finance_accounting_batches_by_id_export**
> GLExport post_finance_accounting_batches_by_id_export(id, client_id, export_accounting_batch_request)

Post GLExport

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.export_accounting_batch_request import ExportAccountingBatchRequest
from connectwise_psa.models.gl_export import GLExport
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
    api_instance = connectwise_psa.AccountingBatchesApi(api_client)
    id = 56 # int | batcheId
    client_id = 'client_id_example' # str | 
    export_accounting_batch_request = connectwise_psa.ExportAccountingBatchRequest() # ExportAccountingBatchRequest | batchExportParameters

    try:
        # Post GLExport
        api_response = api_instance.post_finance_accounting_batches_by_id_export(id, client_id, export_accounting_batch_request)
        print("The response of AccountingBatchesApi->post_finance_accounting_batches_by_id_export:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountingBatchesApi->post_finance_accounting_batches_by_id_export: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| batcheId | 
 **client_id** | **str**|  | 
 **export_accounting_batch_request** | [**ExportAccountingBatchRequest**](ExportAccountingBatchRequest.md)| batchExportParameters | 

### Return type

[**GLExport**](GLExport.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | GLExport |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_finance_accounting_export**
> GLExport post_finance_accounting_export(client_id, export_accounting_batch_request)

Post GLExport

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.export_accounting_batch_request import ExportAccountingBatchRequest
from connectwise_psa.models.gl_export import GLExport
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
    api_instance = connectwise_psa.AccountingBatchesApi(api_client)
    client_id = 'client_id_example' # str | 
    export_accounting_batch_request = connectwise_psa.ExportAccountingBatchRequest() # ExportAccountingBatchRequest | batchExportParameters

    try:
        # Post GLExport
        api_response = api_instance.post_finance_accounting_export(client_id, export_accounting_batch_request)
        print("The response of AccountingBatchesApi->post_finance_accounting_export:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountingBatchesApi->post_finance_accounting_export: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**|  | 
 **export_accounting_batch_request** | [**ExportAccountingBatchRequest**](ExportAccountingBatchRequest.md)| batchExportParameters | 

### Return type

[**GLExport**](GLExport.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | GLExport |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

