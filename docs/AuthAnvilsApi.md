# connectwise_psa.AuthAnvilsApi

All URIs are relative to *https://aus-api.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_system_auth_anvils**](AuthAnvilsApi.md#get_system_auth_anvils) | **GET** /system/authAnvils | Get List of ConnectWise.Apis.v3_0.v2015_3.System.AuthAnvil.AuthAnvil
[**get_system_auth_anvils_by_id**](AuthAnvilsApi.md#get_system_auth_anvils_by_id) | **GET** /system/authAnvils/{id} | Get ConnectWise.Apis.v3_0.v2015_3.System.AuthAnvil.AuthAnvil
[**get_system_auth_anvils_count**](AuthAnvilsApi.md#get_system_auth_anvils_count) | **GET** /system/authAnvils/count | Get Count of SuccessResponse
[**get_system_auth_anvils_test_connection**](AuthAnvilsApi.md#get_system_auth_anvils_test_connection) | **GET** /system/authAnvils/testConnection | Get SuccessResponse
[**patch_system_auth_anvils_by_id**](AuthAnvilsApi.md#patch_system_auth_anvils_by_id) | **PATCH** /system/authAnvils/{id} | Patch ConnectWise.Apis.v3_0.v2015_3.System.AuthAnvil.AuthAnvil
[**put_system_auth_anvils_by_id**](AuthAnvilsApi.md#put_system_auth_anvils_by_id) | **PUT** /system/authAnvils/{id} | Put ConnectWise.Apis.v3_0.v2015_3.System.AuthAnvil.AuthAnvil


# **get_system_auth_anvils**
> List[AuthAnvil] get_system_auth_anvils(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of ConnectWise.Apis.v3_0.v2015_3.System.AuthAnvil.AuthAnvil

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.auth_anvil import AuthAnvil
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
    api_instance = connectwise_psa.AuthAnvilsApi(api_client)
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
        # Get List of ConnectWise.Apis.v3_0.v2015_3.System.AuthAnvil.AuthAnvil
        api_response = api_instance.get_system_auth_anvils(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of AuthAnvilsApi->get_system_auth_anvils:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthAnvilsApi->get_system_auth_anvils: %s\n" % e)
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

[**List[AuthAnvil]**](AuthAnvil.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of ConnectWise.Apis.v3_0.v2015_3.System.AuthAnvil.AuthAnvil |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_system_auth_anvils_by_id**
> AuthAnvil get_system_auth_anvils_by_id(id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get ConnectWise.Apis.v3_0.v2015_3.System.AuthAnvil.AuthAnvil

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.auth_anvil import AuthAnvil
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
    api_instance = connectwise_psa.AuthAnvilsApi(api_client)
    id = 56 # int | authAnvilId
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
        # Get ConnectWise.Apis.v3_0.v2015_3.System.AuthAnvil.AuthAnvil
        api_response = api_instance.get_system_auth_anvils_by_id(id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of AuthAnvilsApi->get_system_auth_anvils_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthAnvilsApi->get_system_auth_anvils_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| authAnvilId | 
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

[**AuthAnvil**](AuthAnvil.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ConnectWise.Apis.v3_0.v2015_3.System.AuthAnvil.AuthAnvil |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_system_auth_anvils_count**
> Count get_system_auth_anvils_count(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Count of SuccessResponse

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.count import Count
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
    api_instance = connectwise_psa.AuthAnvilsApi(api_client)
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
        # Get Count of SuccessResponse
        api_response = api_instance.get_system_auth_anvils_count(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of AuthAnvilsApi->get_system_auth_anvils_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthAnvilsApi->get_system_auth_anvils_count: %s\n" % e)
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

# **get_system_auth_anvils_test_connection**
> SuccessResponse get_system_auth_anvils_test_connection(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get SuccessResponse

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.success_response import SuccessResponse
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
    api_instance = connectwise_psa.AuthAnvilsApi(api_client)
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
        # Get SuccessResponse
        api_response = api_instance.get_system_auth_anvils_test_connection(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of AuthAnvilsApi->get_system_auth_anvils_test_connection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthAnvilsApi->get_system_auth_anvils_test_connection: %s\n" % e)
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

[**SuccessResponse**](SuccessResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | SuccessResponse |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_system_auth_anvils_by_id**
> AuthAnvil patch_system_auth_anvils_by_id(id, client_id, patch_operation)

Patch ConnectWise.Apis.v3_0.v2015_3.System.AuthAnvil.AuthAnvil

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.auth_anvil import AuthAnvil
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
    api_instance = connectwise_psa.AuthAnvilsApi(api_client)
    id = 56 # int | authAnvilId
    client_id = 'client_id_example' # str | 
    patch_operation = [connectwise_psa.PatchOperation()] # List[PatchOperation] | List of PatchOperation

    try:
        # Patch ConnectWise.Apis.v3_0.v2015_3.System.AuthAnvil.AuthAnvil
        api_response = api_instance.patch_system_auth_anvils_by_id(id, client_id, patch_operation)
        print("The response of AuthAnvilsApi->patch_system_auth_anvils_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthAnvilsApi->patch_system_auth_anvils_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| authAnvilId | 
 **client_id** | **str**|  | 
 **patch_operation** | [**List[PatchOperation]**](PatchOperation.md)| List of PatchOperation | 

### Return type

[**AuthAnvil**](AuthAnvil.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ConnectWise.Apis.v3_0.v2015_3.System.AuthAnvil.AuthAnvil |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_system_auth_anvils_by_id**
> AuthAnvil put_system_auth_anvils_by_id(id, client_id, auth_anvil)

Put ConnectWise.Apis.v3_0.v2015_3.System.AuthAnvil.AuthAnvil

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.auth_anvil import AuthAnvil
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
    api_instance = connectwise_psa.AuthAnvilsApi(api_client)
    id = 56 # int | authAnvilId
    client_id = 'client_id_example' # str | 
    auth_anvil = connectwise_psa.AuthAnvil() # AuthAnvil | authAnvil

    try:
        # Put ConnectWise.Apis.v3_0.v2015_3.System.AuthAnvil.AuthAnvil
        api_response = api_instance.put_system_auth_anvils_by_id(id, client_id, auth_anvil)
        print("The response of AuthAnvilsApi->put_system_auth_anvils_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthAnvilsApi->put_system_auth_anvils_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| authAnvilId | 
 **client_id** | **str**|  | 
 **auth_anvil** | [**AuthAnvil**](AuthAnvil.md)| authAnvil | 

### Return type

[**AuthAnvil**](AuthAnvil.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ConnectWise.Apis.v3_0.v2015_3.System.AuthAnvil.AuthAnvil |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

