# connectwise_psa.MyAccountsApi

All URIs are relative to *https://api-aus.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_system_my_account_by_id**](MyAccountsApi.md#get_system_my_account_by_id) | **GET** /system/myAccount/{id} | Get MyAccount
[**patch_system_my_account_by_id**](MyAccountsApi.md#patch_system_my_account_by_id) | **PATCH** /system/myAccount/{id} | Patch MyAccount
[**put_system_my_account_by_id**](MyAccountsApi.md#put_system_my_account_by_id) | **PUT** /system/myAccount/{id} | Put MyAccount


# **get_system_my_account_by_id**
> MyAccount get_system_my_account_by_id(id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get MyAccount

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.my_account import MyAccount
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
    api_instance = connectwise_psa.MyAccountsApi(api_client)
    id = 56 # int | memberId
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
        # Get MyAccount
        api_response = api_instance.get_system_my_account_by_id(id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of MyAccountsApi->get_system_my_account_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MyAccountsApi->get_system_my_account_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| memberId | 
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

[**MyAccount**](MyAccount.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | MyAccount |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_system_my_account_by_id**
> MyAccount patch_system_my_account_by_id(id, client_id, patch_operation)

Patch MyAccount

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.my_account import MyAccount
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
    api_instance = connectwise_psa.MyAccountsApi(api_client)
    id = 56 # int | memberId
    client_id = 'client_id_example' # str | 
    patch_operation = [connectwise_psa.PatchOperation()] # List[PatchOperation] | List of PatchOperation

    try:
        # Patch MyAccount
        api_response = api_instance.patch_system_my_account_by_id(id, client_id, patch_operation)
        print("The response of MyAccountsApi->patch_system_my_account_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MyAccountsApi->patch_system_my_account_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| memberId | 
 **client_id** | **str**|  | 
 **patch_operation** | [**List[PatchOperation]**](PatchOperation.md)| List of PatchOperation | 

### Return type

[**MyAccount**](MyAccount.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | MyAccount |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_system_my_account_by_id**
> MyAccount put_system_my_account_by_id(id, client_id, my_account)

Put MyAccount

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.my_account import MyAccount
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
    api_instance = connectwise_psa.MyAccountsApi(api_client)
    id = 56 # int | memberId
    client_id = 'client_id_example' # str | 
    my_account = connectwise_psa.MyAccount() # MyAccount | myAccount

    try:
        # Put MyAccount
        api_response = api_instance.put_system_my_account_by_id(id, client_id, my_account)
        print("The response of MyAccountsApi->put_system_my_account_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MyAccountsApi->put_system_my_account_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| memberId | 
 **client_id** | **str**|  | 
 **my_account** | [**MyAccount**](MyAccount.md)| myAccount | 

### Return type

[**MyAccount**](MyAccount.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | MyAccount |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

