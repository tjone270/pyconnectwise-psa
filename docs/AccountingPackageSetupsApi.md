# connectwise_psa.AccountingPackageSetupsApi

All URIs are relative to *https://api-aus.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_finance_accounting_package_setup**](AccountingPackageSetupsApi.md#get_finance_accounting_package_setup) | **GET** /finance/accountingPackageSetup | Get List of AccountingPackageSetup
[**get_finance_accounting_package_setup_by_id**](AccountingPackageSetupsApi.md#get_finance_accounting_package_setup_by_id) | **GET** /finance/accountingPackageSetup/{id} | Get AccountingPackageSetup
[**get_finance_accounting_package_setup_count**](AccountingPackageSetupsApi.md#get_finance_accounting_package_setup_count) | **GET** /finance/accountingPackageSetup/count | Get Count of AccountingPackageSetup
[**patch_finance_accounting_package_setup_by_id**](AccountingPackageSetupsApi.md#patch_finance_accounting_package_setup_by_id) | **PATCH** /finance/accountingPackageSetup/{id} | Patch AccountingPackageSetup
[**put_finance_accounting_package_setup_by_id**](AccountingPackageSetupsApi.md#put_finance_accounting_package_setup_by_id) | **PUT** /finance/accountingPackageSetup/{id} | Put AccountingPackageSetup


# **get_finance_accounting_package_setup**
> List[AccountingPackageSetup] get_finance_accounting_package_setup(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of AccountingPackageSetup

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.accounting_package_setup import AccountingPackageSetup
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
    api_instance = connectwise_psa.AccountingPackageSetupsApi(api_client)
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
        # Get List of AccountingPackageSetup
        api_response = api_instance.get_finance_accounting_package_setup(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of AccountingPackageSetupsApi->get_finance_accounting_package_setup:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountingPackageSetupsApi->get_finance_accounting_package_setup: %s\n" % e)
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

[**List[AccountingPackageSetup]**](AccountingPackageSetup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of AccountingPackageSetup |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_finance_accounting_package_setup_by_id**
> AccountingPackageSetup get_finance_accounting_package_setup_by_id(id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get AccountingPackageSetup

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.accounting_package_setup import AccountingPackageSetup
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
    api_instance = connectwise_psa.AccountingPackageSetupsApi(api_client)
    id = 56 # int | accountingPackageSetupId
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
        # Get AccountingPackageSetup
        api_response = api_instance.get_finance_accounting_package_setup_by_id(id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of AccountingPackageSetupsApi->get_finance_accounting_package_setup_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountingPackageSetupsApi->get_finance_accounting_package_setup_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| accountingPackageSetupId | 
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

[**AccountingPackageSetup**](AccountingPackageSetup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | AccountingPackageSetup |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_finance_accounting_package_setup_count**
> Count get_finance_accounting_package_setup_count(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Count of AccountingPackageSetup

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
    api_instance = connectwise_psa.AccountingPackageSetupsApi(api_client)
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
        # Get Count of AccountingPackageSetup
        api_response = api_instance.get_finance_accounting_package_setup_count(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of AccountingPackageSetupsApi->get_finance_accounting_package_setup_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountingPackageSetupsApi->get_finance_accounting_package_setup_count: %s\n" % e)
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

# **patch_finance_accounting_package_setup_by_id**
> AccountingPackageSetup patch_finance_accounting_package_setup_by_id(id, client_id, patch_operation)

Patch AccountingPackageSetup

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.accounting_package_setup import AccountingPackageSetup
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
    api_instance = connectwise_psa.AccountingPackageSetupsApi(api_client)
    id = 56 # int | accountingPackageSetupId
    client_id = 'client_id_example' # str | 
    patch_operation = [connectwise_psa.PatchOperation()] # List[PatchOperation] | List of PatchOperation

    try:
        # Patch AccountingPackageSetup
        api_response = api_instance.patch_finance_accounting_package_setup_by_id(id, client_id, patch_operation)
        print("The response of AccountingPackageSetupsApi->patch_finance_accounting_package_setup_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountingPackageSetupsApi->patch_finance_accounting_package_setup_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| accountingPackageSetupId | 
 **client_id** | **str**|  | 
 **patch_operation** | [**List[PatchOperation]**](PatchOperation.md)| List of PatchOperation | 

### Return type

[**AccountingPackageSetup**](AccountingPackageSetup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | AccountingPackageSetup |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_finance_accounting_package_setup_by_id**
> AccountingPackageSetup put_finance_accounting_package_setup_by_id(id, client_id, accounting_package_setup)

Put AccountingPackageSetup

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.accounting_package_setup import AccountingPackageSetup
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
    api_instance = connectwise_psa.AccountingPackageSetupsApi(api_client)
    id = 56 # int | accountingPackageSetupId
    client_id = 'client_id_example' # str | 
    accounting_package_setup = connectwise_psa.AccountingPackageSetup() # AccountingPackageSetup | accountingPackageSetup

    try:
        # Put AccountingPackageSetup
        api_response = api_instance.put_finance_accounting_package_setup_by_id(id, client_id, accounting_package_setup)
        print("The response of AccountingPackageSetupsApi->put_finance_accounting_package_setup_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountingPackageSetupsApi->put_finance_accounting_package_setup_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| accountingPackageSetupId | 
 **client_id** | **str**|  | 
 **accounting_package_setup** | [**AccountingPackageSetup**](AccountingPackageSetup.md)| accountingPackageSetup | 

### Return type

[**AccountingPackageSetup**](AccountingPackageSetup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | AccountingPackageSetup |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

