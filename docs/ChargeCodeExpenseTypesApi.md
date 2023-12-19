# connectwise_psa.ChargeCodeExpenseTypesApi

All URIs are relative to *https://api-aus.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_time_charge_codes_by_parent_id_expense_types_by_id**](ChargeCodeExpenseTypesApi.md#delete_time_charge_codes_by_parent_id_expense_types_by_id) | **DELETE** /time/chargeCodes/{parentId}/expenseTypes/{id} | Delete ChargeCodeExpenseType
[**get_time_charge_codes_by_parent_id_expense_types**](ChargeCodeExpenseTypesApi.md#get_time_charge_codes_by_parent_id_expense_types) | **GET** /time/chargeCodes/{parentId}/expenseTypes | Get List of ChargeCodeExpenseType
[**get_time_charge_codes_by_parent_id_expense_types_by_id**](ChargeCodeExpenseTypesApi.md#get_time_charge_codes_by_parent_id_expense_types_by_id) | **GET** /time/chargeCodes/{parentId}/expenseTypes/{id} | Get ChargeCodeExpenseType
[**get_time_charge_codes_by_parent_id_expense_types_count**](ChargeCodeExpenseTypesApi.md#get_time_charge_codes_by_parent_id_expense_types_count) | **GET** /time/chargeCodes/{parentId}/expenseTypes/count | Get Count of ChargeCodeExpenseType
[**patch_time_charge_codes_by_parent_id_expense_types_by_id**](ChargeCodeExpenseTypesApi.md#patch_time_charge_codes_by_parent_id_expense_types_by_id) | **PATCH** /time/chargeCodes/{parentId}/expenseTypes/{id} | Patch ChargeCodeExpenseType
[**post_time_charge_codes_by_parent_id_expense_types**](ChargeCodeExpenseTypesApi.md#post_time_charge_codes_by_parent_id_expense_types) | **POST** /time/chargeCodes/{parentId}/expenseTypes | Post ChargeCodeExpenseType
[**put_time_charge_codes_by_parent_id_expense_types_by_id**](ChargeCodeExpenseTypesApi.md#put_time_charge_codes_by_parent_id_expense_types_by_id) | **PUT** /time/chargeCodes/{parentId}/expenseTypes/{id} | Put ChargeCodeExpenseType


# **delete_time_charge_codes_by_parent_id_expense_types_by_id**
> delete_time_charge_codes_by_parent_id_expense_types_by_id(id, parent_id, client_id)

Delete ChargeCodeExpenseType

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
    api_instance = connectwise_psa.ChargeCodeExpenseTypesApi(api_client)
    id = 56 # int | expenseTypeId
    parent_id = 56 # int | chargeCodeId
    client_id = 'client_id_example' # str | 

    try:
        # Delete ChargeCodeExpenseType
        api_instance.delete_time_charge_codes_by_parent_id_expense_types_by_id(id, parent_id, client_id)
    except Exception as e:
        print("Exception when calling ChargeCodeExpenseTypesApi->delete_time_charge_codes_by_parent_id_expense_types_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| expenseTypeId | 
 **parent_id** | **int**| chargeCodeId | 
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

# **get_time_charge_codes_by_parent_id_expense_types**
> List[ChargeCodeExpenseType] get_time_charge_codes_by_parent_id_expense_types(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of ChargeCodeExpenseType

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.charge_code_expense_type import ChargeCodeExpenseType
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
    api_instance = connectwise_psa.ChargeCodeExpenseTypesApi(api_client)
    parent_id = 56 # int | chargeCodeId
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
        # Get List of ChargeCodeExpenseType
        api_response = api_instance.get_time_charge_codes_by_parent_id_expense_types(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of ChargeCodeExpenseTypesApi->get_time_charge_codes_by_parent_id_expense_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChargeCodeExpenseTypesApi->get_time_charge_codes_by_parent_id_expense_types: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| chargeCodeId | 
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

[**List[ChargeCodeExpenseType]**](ChargeCodeExpenseType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of ChargeCodeExpenseType |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_time_charge_codes_by_parent_id_expense_types_by_id**
> ChargeCodeExpenseType get_time_charge_codes_by_parent_id_expense_types_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get ChargeCodeExpenseType

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.charge_code_expense_type import ChargeCodeExpenseType
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
    api_instance = connectwise_psa.ChargeCodeExpenseTypesApi(api_client)
    id = 56 # int | expenseTypeId
    parent_id = 56 # int | chargeCodeId
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
        # Get ChargeCodeExpenseType
        api_response = api_instance.get_time_charge_codes_by_parent_id_expense_types_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of ChargeCodeExpenseTypesApi->get_time_charge_codes_by_parent_id_expense_types_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChargeCodeExpenseTypesApi->get_time_charge_codes_by_parent_id_expense_types_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| expenseTypeId | 
 **parent_id** | **int**| chargeCodeId | 
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

[**ChargeCodeExpenseType**](ChargeCodeExpenseType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ChargeCodeExpenseType |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_time_charge_codes_by_parent_id_expense_types_count**
> Count get_time_charge_codes_by_parent_id_expense_types_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Count of ChargeCodeExpenseType

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
    api_instance = connectwise_psa.ChargeCodeExpenseTypesApi(api_client)
    parent_id = 56 # int | chargeCodeId
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
        # Get Count of ChargeCodeExpenseType
        api_response = api_instance.get_time_charge_codes_by_parent_id_expense_types_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of ChargeCodeExpenseTypesApi->get_time_charge_codes_by_parent_id_expense_types_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChargeCodeExpenseTypesApi->get_time_charge_codes_by_parent_id_expense_types_count: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| chargeCodeId | 
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

# **patch_time_charge_codes_by_parent_id_expense_types_by_id**
> ChargeCodeExpenseType patch_time_charge_codes_by_parent_id_expense_types_by_id(id, parent_id, client_id, patch_operation)

Patch ChargeCodeExpenseType

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.charge_code_expense_type import ChargeCodeExpenseType
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
    api_instance = connectwise_psa.ChargeCodeExpenseTypesApi(api_client)
    id = 56 # int | expenseTypeId
    parent_id = 56 # int | chargeCodeId
    client_id = 'client_id_example' # str | 
    patch_operation = [connectwise_psa.PatchOperation()] # List[PatchOperation] | List of PatchOperation

    try:
        # Patch ChargeCodeExpenseType
        api_response = api_instance.patch_time_charge_codes_by_parent_id_expense_types_by_id(id, parent_id, client_id, patch_operation)
        print("The response of ChargeCodeExpenseTypesApi->patch_time_charge_codes_by_parent_id_expense_types_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChargeCodeExpenseTypesApi->patch_time_charge_codes_by_parent_id_expense_types_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| expenseTypeId | 
 **parent_id** | **int**| chargeCodeId | 
 **client_id** | **str**|  | 
 **patch_operation** | [**List[PatchOperation]**](PatchOperation.md)| List of PatchOperation | 

### Return type

[**ChargeCodeExpenseType**](ChargeCodeExpenseType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ChargeCodeExpenseType |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_time_charge_codes_by_parent_id_expense_types**
> ChargeCodeExpenseType post_time_charge_codes_by_parent_id_expense_types(parent_id, client_id, charge_code_expense_type)

Post ChargeCodeExpenseType

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.charge_code_expense_type import ChargeCodeExpenseType
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
    api_instance = connectwise_psa.ChargeCodeExpenseTypesApi(api_client)
    parent_id = 56 # int | chargeCodeId
    client_id = 'client_id_example' # str | 
    charge_code_expense_type = connectwise_psa.ChargeCodeExpenseType() # ChargeCodeExpenseType | chargeCodeExpenseType

    try:
        # Post ChargeCodeExpenseType
        api_response = api_instance.post_time_charge_codes_by_parent_id_expense_types(parent_id, client_id, charge_code_expense_type)
        print("The response of ChargeCodeExpenseTypesApi->post_time_charge_codes_by_parent_id_expense_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChargeCodeExpenseTypesApi->post_time_charge_codes_by_parent_id_expense_types: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| chargeCodeId | 
 **client_id** | **str**|  | 
 **charge_code_expense_type** | [**ChargeCodeExpenseType**](ChargeCodeExpenseType.md)| chargeCodeExpenseType | 

### Return type

[**ChargeCodeExpenseType**](ChargeCodeExpenseType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | ChargeCodeExpenseType |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_time_charge_codes_by_parent_id_expense_types_by_id**
> ChargeCodeExpenseType put_time_charge_codes_by_parent_id_expense_types_by_id(id, parent_id, client_id, charge_code_expense_type)

Put ChargeCodeExpenseType

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.charge_code_expense_type import ChargeCodeExpenseType
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
    api_instance = connectwise_psa.ChargeCodeExpenseTypesApi(api_client)
    id = 56 # int | expenseTypeId
    parent_id = 56 # int | chargeCodeId
    client_id = 'client_id_example' # str | 
    charge_code_expense_type = connectwise_psa.ChargeCodeExpenseType() # ChargeCodeExpenseType | chargeCodeExpenseType

    try:
        # Put ChargeCodeExpenseType
        api_response = api_instance.put_time_charge_codes_by_parent_id_expense_types_by_id(id, parent_id, client_id, charge_code_expense_type)
        print("The response of ChargeCodeExpenseTypesApi->put_time_charge_codes_by_parent_id_expense_types_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChargeCodeExpenseTypesApi->put_time_charge_codes_by_parent_id_expense_types_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| expenseTypeId | 
 **parent_id** | **int**| chargeCodeId | 
 **client_id** | **str**|  | 
 **charge_code_expense_type** | [**ChargeCodeExpenseType**](ChargeCodeExpenseType.md)| chargeCodeExpenseType | 

### Return type

[**ChargeCodeExpenseType**](ChargeCodeExpenseType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ChargeCodeExpenseType |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

