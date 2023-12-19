# connectwise_psa.ManagedDeviceAccountsApi

All URIs are relative to *https://aus-api.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_system_members_by_parent_id_managed_device_accounts_bulk**](ManagedDeviceAccountsApi.md#delete_system_members_by_parent_id_managed_device_accounts_bulk) | **DELETE** /system/members/{parentId}/managedDeviceAccounts/bulk | Delete BulkResult
[**get_system_members_by_parent_id_managed_device_accounts**](ManagedDeviceAccountsApi.md#get_system_members_by_parent_id_managed_device_accounts) | **GET** /system/members/{parentId}/managedDeviceAccounts | Get List of ManagedDeviceAccount
[**put_system_members_by_parent_id_managed_device_accounts_bulk**](ManagedDeviceAccountsApi.md#put_system_members_by_parent_id_managed_device_accounts_bulk) | **PUT** /system/members/{parentId}/managedDeviceAccounts/bulk | Put BulkResult


# **delete_system_members_by_parent_id_managed_device_accounts_bulk**
> BulkResult delete_system_members_by_parent_id_managed_device_accounts_bulk(parent_id, client_id, id_collection)

Delete BulkResult

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.bulk_result import BulkResult
from connectwise_psa.models.id_collection import IdCollection
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
    api_instance = connectwise_psa.ManagedDeviceAccountsApi(api_client)
    parent_id = 56 # int | memberId
    client_id = 'client_id_example' # str | 
    id_collection = connectwise_psa.IdCollection() # IdCollection | managedDeviceAccounts

    try:
        # Delete BulkResult
        api_response = api_instance.delete_system_members_by_parent_id_managed_device_accounts_bulk(parent_id, client_id, id_collection)
        print("The response of ManagedDeviceAccountsApi->delete_system_members_by_parent_id_managed_device_accounts_bulk:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagedDeviceAccountsApi->delete_system_members_by_parent_id_managed_device_accounts_bulk: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| memberId | 
 **client_id** | **str**|  | 
 **id_collection** | [**IdCollection**](IdCollection.md)| managedDeviceAccounts | 

### Return type

[**BulkResult**](BulkResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**207** | BulkResult |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_system_members_by_parent_id_managed_device_accounts**
> List[ManagedDeviceAccount] get_system_members_by_parent_id_managed_device_accounts(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of ManagedDeviceAccount

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.managed_device_account import ManagedDeviceAccount
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
    api_instance = connectwise_psa.ManagedDeviceAccountsApi(api_client)
    parent_id = 56 # int | memberId
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
        # Get List of ManagedDeviceAccount
        api_response = api_instance.get_system_members_by_parent_id_managed_device_accounts(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of ManagedDeviceAccountsApi->get_system_members_by_parent_id_managed_device_accounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagedDeviceAccountsApi->get_system_members_by_parent_id_managed_device_accounts: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| memberId | 
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

[**List[ManagedDeviceAccount]**](ManagedDeviceAccount.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of ManagedDeviceAccount |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_system_members_by_parent_id_managed_device_accounts_bulk**
> BulkResult put_system_members_by_parent_id_managed_device_accounts_bulk(parent_id, client_id, managed_device_account)

Put BulkResult

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.bulk_result import BulkResult
from connectwise_psa.models.managed_device_account import ManagedDeviceAccount
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
    api_instance = connectwise_psa.ManagedDeviceAccountsApi(api_client)
    parent_id = 56 # int | memberId
    client_id = 'client_id_example' # str | 
    managed_device_account = [connectwise_psa.ManagedDeviceAccount()] # List[ManagedDeviceAccount] | List of ManagedDeviceAccount

    try:
        # Put BulkResult
        api_response = api_instance.put_system_members_by_parent_id_managed_device_accounts_bulk(parent_id, client_id, managed_device_account)
        print("The response of ManagedDeviceAccountsApi->put_system_members_by_parent_id_managed_device_accounts_bulk:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagedDeviceAccountsApi->put_system_members_by_parent_id_managed_device_accounts_bulk: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| memberId | 
 **client_id** | **str**|  | 
 **managed_device_account** | [**List[ManagedDeviceAccount]**](ManagedDeviceAccount.md)| List of ManagedDeviceAccount | 

### Return type

[**BulkResult**](BulkResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**207** | BulkResult |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

