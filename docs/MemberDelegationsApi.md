# connectwise_psa.MemberDelegationsApi

All URIs are relative to *https://api-aus.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_system_members_by_parent_id_delegations_by_id**](MemberDelegationsApi.md#delete_system_members_by_parent_id_delegations_by_id) | **DELETE** /system/members/{parentId}/delegations/{id} | Delete MemberDelegation
[**delete_system_my_account_by_parent_id_delegations_by_id**](MemberDelegationsApi.md#delete_system_my_account_by_parent_id_delegations_by_id) | **DELETE** /system/myAccount/{parentId}/delegations/{id} | Delete MemberDelegation
[**get_system_members_by_parent_id_delegations**](MemberDelegationsApi.md#get_system_members_by_parent_id_delegations) | **GET** /system/members/{parentId}/delegations | Get List of MemberDelegation
[**get_system_members_by_parent_id_delegations_by_id**](MemberDelegationsApi.md#get_system_members_by_parent_id_delegations_by_id) | **GET** /system/members/{parentId}/delegations/{id} | Get MemberDelegation
[**get_system_members_by_parent_id_delegations_count**](MemberDelegationsApi.md#get_system_members_by_parent_id_delegations_count) | **GET** /system/members/{parentId}/delegations/count | Get Count of MemberDelegation
[**get_system_my_account_by_parent_id_delegations**](MemberDelegationsApi.md#get_system_my_account_by_parent_id_delegations) | **GET** /system/myAccount/{parentId}/delegations | Get List of MemberDelegation
[**get_system_my_account_by_parent_id_delegations_by_id**](MemberDelegationsApi.md#get_system_my_account_by_parent_id_delegations_by_id) | **GET** /system/myAccount/{parentId}/delegations/{id} | Get MemberDelegation
[**get_system_my_account_by_parent_id_delegations_count**](MemberDelegationsApi.md#get_system_my_account_by_parent_id_delegations_count) | **GET** /system/myAccount/{parentId}/delegations/count | Get Count of MemberDelegation
[**patch_system_members_by_parent_id_delegations_by_id**](MemberDelegationsApi.md#patch_system_members_by_parent_id_delegations_by_id) | **PATCH** /system/members/{parentId}/delegations/{id} | Patch MemberDelegation
[**patch_system_my_account_by_parent_id_delegations_by_id**](MemberDelegationsApi.md#patch_system_my_account_by_parent_id_delegations_by_id) | **PATCH** /system/myAccount/{parentId}/delegations/{id} | Patch MemberDelegation
[**post_system_members_by_parent_id_delegations**](MemberDelegationsApi.md#post_system_members_by_parent_id_delegations) | **POST** /system/members/{parentId}/delegations | Post MemberDelegation
[**post_system_my_account_by_parent_id_delegations**](MemberDelegationsApi.md#post_system_my_account_by_parent_id_delegations) | **POST** /system/myAccount/{parentId}/delegations | Post MemberDelegation
[**put_system_members_by_parent_id_delegations_by_id**](MemberDelegationsApi.md#put_system_members_by_parent_id_delegations_by_id) | **PUT** /system/members/{parentId}/delegations/{id} | Put MemberDelegation
[**put_system_my_account_by_parent_id_delegations_by_id**](MemberDelegationsApi.md#put_system_my_account_by_parent_id_delegations_by_id) | **PUT** /system/myAccount/{parentId}/delegations/{id} | Put MemberDelegation


# **delete_system_members_by_parent_id_delegations_by_id**
> delete_system_members_by_parent_id_delegations_by_id(id, parent_id, client_id)

Delete MemberDelegation

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
    api_instance = connectwise_psa.MemberDelegationsApi(api_client)
    id = 56 # int | delegationId
    parent_id = 56 # int | memberId
    client_id = 'client_id_example' # str | 

    try:
        # Delete MemberDelegation
        api_instance.delete_system_members_by_parent_id_delegations_by_id(id, parent_id, client_id)
    except Exception as e:
        print("Exception when calling MemberDelegationsApi->delete_system_members_by_parent_id_delegations_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| delegationId | 
 **parent_id** | **int**| memberId | 
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

# **delete_system_my_account_by_parent_id_delegations_by_id**
> delete_system_my_account_by_parent_id_delegations_by_id(id, parent_id, client_id)

Delete MemberDelegation

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
    api_instance = connectwise_psa.MemberDelegationsApi(api_client)
    id = 56 # int | delegationId
    parent_id = 56 # int | memberId
    client_id = 'client_id_example' # str | 

    try:
        # Delete MemberDelegation
        api_instance.delete_system_my_account_by_parent_id_delegations_by_id(id, parent_id, client_id)
    except Exception as e:
        print("Exception when calling MemberDelegationsApi->delete_system_my_account_by_parent_id_delegations_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| delegationId | 
 **parent_id** | **int**| memberId | 
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

# **get_system_members_by_parent_id_delegations**
> List[MemberDelegation] get_system_members_by_parent_id_delegations(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of MemberDelegation

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.member_delegation import MemberDelegation
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
    api_instance = connectwise_psa.MemberDelegationsApi(api_client)
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
        # Get List of MemberDelegation
        api_response = api_instance.get_system_members_by_parent_id_delegations(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of MemberDelegationsApi->get_system_members_by_parent_id_delegations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MemberDelegationsApi->get_system_members_by_parent_id_delegations: %s\n" % e)
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

[**List[MemberDelegation]**](MemberDelegation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of MemberDelegation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_system_members_by_parent_id_delegations_by_id**
> MemberDelegation get_system_members_by_parent_id_delegations_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get MemberDelegation

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.member_delegation import MemberDelegation
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
    api_instance = connectwise_psa.MemberDelegationsApi(api_client)
    id = 56 # int | delegationId
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
        # Get MemberDelegation
        api_response = api_instance.get_system_members_by_parent_id_delegations_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of MemberDelegationsApi->get_system_members_by_parent_id_delegations_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MemberDelegationsApi->get_system_members_by_parent_id_delegations_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| delegationId | 
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

[**MemberDelegation**](MemberDelegation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | MemberDelegation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_system_members_by_parent_id_delegations_count**
> Count get_system_members_by_parent_id_delegations_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Count of MemberDelegation

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
    api_instance = connectwise_psa.MemberDelegationsApi(api_client)
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
        # Get Count of MemberDelegation
        api_response = api_instance.get_system_members_by_parent_id_delegations_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of MemberDelegationsApi->get_system_members_by_parent_id_delegations_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MemberDelegationsApi->get_system_members_by_parent_id_delegations_count: %s\n" % e)
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

# **get_system_my_account_by_parent_id_delegations**
> List[MemberDelegation] get_system_my_account_by_parent_id_delegations(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of MemberDelegation

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.member_delegation import MemberDelegation
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
    api_instance = connectwise_psa.MemberDelegationsApi(api_client)
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
        # Get List of MemberDelegation
        api_response = api_instance.get_system_my_account_by_parent_id_delegations(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of MemberDelegationsApi->get_system_my_account_by_parent_id_delegations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MemberDelegationsApi->get_system_my_account_by_parent_id_delegations: %s\n" % e)
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

[**List[MemberDelegation]**](MemberDelegation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of MemberDelegation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_system_my_account_by_parent_id_delegations_by_id**
> MemberDelegation get_system_my_account_by_parent_id_delegations_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get MemberDelegation

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.member_delegation import MemberDelegation
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
    api_instance = connectwise_psa.MemberDelegationsApi(api_client)
    id = 56 # int | delegationId
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
        # Get MemberDelegation
        api_response = api_instance.get_system_my_account_by_parent_id_delegations_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of MemberDelegationsApi->get_system_my_account_by_parent_id_delegations_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MemberDelegationsApi->get_system_my_account_by_parent_id_delegations_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| delegationId | 
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

[**MemberDelegation**](MemberDelegation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | MemberDelegation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_system_my_account_by_parent_id_delegations_count**
> Count get_system_my_account_by_parent_id_delegations_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Count of MemberDelegation

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
    api_instance = connectwise_psa.MemberDelegationsApi(api_client)
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
        # Get Count of MemberDelegation
        api_response = api_instance.get_system_my_account_by_parent_id_delegations_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of MemberDelegationsApi->get_system_my_account_by_parent_id_delegations_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MemberDelegationsApi->get_system_my_account_by_parent_id_delegations_count: %s\n" % e)
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

# **patch_system_members_by_parent_id_delegations_by_id**
> MemberDelegation patch_system_members_by_parent_id_delegations_by_id(id, parent_id, client_id, patch_operation)

Patch MemberDelegation

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.member_delegation import MemberDelegation
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
    api_instance = connectwise_psa.MemberDelegationsApi(api_client)
    id = 56 # int | delegationId
    parent_id = 56 # int | memberId
    client_id = 'client_id_example' # str | 
    patch_operation = [connectwise_psa.PatchOperation()] # List[PatchOperation] | List of PatchOperation

    try:
        # Patch MemberDelegation
        api_response = api_instance.patch_system_members_by_parent_id_delegations_by_id(id, parent_id, client_id, patch_operation)
        print("The response of MemberDelegationsApi->patch_system_members_by_parent_id_delegations_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MemberDelegationsApi->patch_system_members_by_parent_id_delegations_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| delegationId | 
 **parent_id** | **int**| memberId | 
 **client_id** | **str**|  | 
 **patch_operation** | [**List[PatchOperation]**](PatchOperation.md)| List of PatchOperation | 

### Return type

[**MemberDelegation**](MemberDelegation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | MemberDelegation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_system_my_account_by_parent_id_delegations_by_id**
> MemberDelegation patch_system_my_account_by_parent_id_delegations_by_id(id, parent_id, client_id, patch_operation)

Patch MemberDelegation

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.member_delegation import MemberDelegation
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
    api_instance = connectwise_psa.MemberDelegationsApi(api_client)
    id = 56 # int | delegationId
    parent_id = 56 # int | memberId
    client_id = 'client_id_example' # str | 
    patch_operation = [connectwise_psa.PatchOperation()] # List[PatchOperation] | List of PatchOperation

    try:
        # Patch MemberDelegation
        api_response = api_instance.patch_system_my_account_by_parent_id_delegations_by_id(id, parent_id, client_id, patch_operation)
        print("The response of MemberDelegationsApi->patch_system_my_account_by_parent_id_delegations_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MemberDelegationsApi->patch_system_my_account_by_parent_id_delegations_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| delegationId | 
 **parent_id** | **int**| memberId | 
 **client_id** | **str**|  | 
 **patch_operation** | [**List[PatchOperation]**](PatchOperation.md)| List of PatchOperation | 

### Return type

[**MemberDelegation**](MemberDelegation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | MemberDelegation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_system_members_by_parent_id_delegations**
> MemberDelegation post_system_members_by_parent_id_delegations(parent_id, client_id, member_delegation)

Post MemberDelegation

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.member_delegation import MemberDelegation
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
    api_instance = connectwise_psa.MemberDelegationsApi(api_client)
    parent_id = 56 # int | memberId
    client_id = 'client_id_example' # str | 
    member_delegation = connectwise_psa.MemberDelegation() # MemberDelegation | memberDelegation

    try:
        # Post MemberDelegation
        api_response = api_instance.post_system_members_by_parent_id_delegations(parent_id, client_id, member_delegation)
        print("The response of MemberDelegationsApi->post_system_members_by_parent_id_delegations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MemberDelegationsApi->post_system_members_by_parent_id_delegations: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| memberId | 
 **client_id** | **str**|  | 
 **member_delegation** | [**MemberDelegation**](MemberDelegation.md)| memberDelegation | 

### Return type

[**MemberDelegation**](MemberDelegation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | MemberDelegation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_system_my_account_by_parent_id_delegations**
> MemberDelegation post_system_my_account_by_parent_id_delegations(parent_id, client_id, member_delegation)

Post MemberDelegation

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.member_delegation import MemberDelegation
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
    api_instance = connectwise_psa.MemberDelegationsApi(api_client)
    parent_id = 56 # int | memberId
    client_id = 'client_id_example' # str | 
    member_delegation = connectwise_psa.MemberDelegation() # MemberDelegation | memberDelegation

    try:
        # Post MemberDelegation
        api_response = api_instance.post_system_my_account_by_parent_id_delegations(parent_id, client_id, member_delegation)
        print("The response of MemberDelegationsApi->post_system_my_account_by_parent_id_delegations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MemberDelegationsApi->post_system_my_account_by_parent_id_delegations: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| memberId | 
 **client_id** | **str**|  | 
 **member_delegation** | [**MemberDelegation**](MemberDelegation.md)| memberDelegation | 

### Return type

[**MemberDelegation**](MemberDelegation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | MemberDelegation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_system_members_by_parent_id_delegations_by_id**
> MemberDelegation put_system_members_by_parent_id_delegations_by_id(id, parent_id, client_id, member_delegation)

Put MemberDelegation

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.member_delegation import MemberDelegation
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
    api_instance = connectwise_psa.MemberDelegationsApi(api_client)
    id = 56 # int | delegationId
    parent_id = 56 # int | memberId
    client_id = 'client_id_example' # str | 
    member_delegation = connectwise_psa.MemberDelegation() # MemberDelegation | memberDelegation

    try:
        # Put MemberDelegation
        api_response = api_instance.put_system_members_by_parent_id_delegations_by_id(id, parent_id, client_id, member_delegation)
        print("The response of MemberDelegationsApi->put_system_members_by_parent_id_delegations_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MemberDelegationsApi->put_system_members_by_parent_id_delegations_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| delegationId | 
 **parent_id** | **int**| memberId | 
 **client_id** | **str**|  | 
 **member_delegation** | [**MemberDelegation**](MemberDelegation.md)| memberDelegation | 

### Return type

[**MemberDelegation**](MemberDelegation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | MemberDelegation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_system_my_account_by_parent_id_delegations_by_id**
> MemberDelegation put_system_my_account_by_parent_id_delegations_by_id(id, parent_id, client_id, member_delegation)

Put MemberDelegation

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.member_delegation import MemberDelegation
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
    api_instance = connectwise_psa.MemberDelegationsApi(api_client)
    id = 56 # int | delegationId
    parent_id = 56 # int | memberId
    client_id = 'client_id_example' # str | 
    member_delegation = connectwise_psa.MemberDelegation() # MemberDelegation | memberDelegation

    try:
        # Put MemberDelegation
        api_response = api_instance.put_system_my_account_by_parent_id_delegations_by_id(id, parent_id, client_id, member_delegation)
        print("The response of MemberDelegationsApi->put_system_my_account_by_parent_id_delegations_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MemberDelegationsApi->put_system_my_account_by_parent_id_delegations_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| delegationId | 
 **parent_id** | **int**| memberId | 
 **client_id** | **str**|  | 
 **member_delegation** | [**MemberDelegation**](MemberDelegation.md)| memberDelegation | 

### Return type

[**MemberDelegation**](MemberDelegation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | MemberDelegation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

