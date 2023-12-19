# connectwise_psa.ManagementNetworksSecurityApi

All URIs are relative to *https://api-aus.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_system_management_network_securities_by_id**](ManagementNetworksSecurityApi.md#delete_system_management_network_securities_by_id) | **DELETE** /system/managementNetworkSecurities/{id} | Delete ManagementNetworkSecurity
[**get_system_management_network_securities**](ManagementNetworksSecurityApi.md#get_system_management_network_securities) | **GET** /system/managementNetworkSecurities | Get List of ManagementNetworkSecurity
[**get_system_management_network_securities_by_id**](ManagementNetworksSecurityApi.md#get_system_management_network_securities_by_id) | **GET** /system/managementNetworkSecurities/{id} | Get ManagementNetworkSecurity
[**get_system_management_network_securities_by_id_test_credentials**](ManagementNetworksSecurityApi.md#get_system_management_network_securities_by_id_test_credentials) | **GET** /system/managementNetworkSecurities/{id}/testCredentials | Get SuccessResponse
[**get_system_management_network_securities_count**](ManagementNetworksSecurityApi.md#get_system_management_network_securities_count) | **GET** /system/managementNetworkSecurities/count | Get Count of ManagementNetworkSecurity
[**patch_system_management_network_securities_by_id**](ManagementNetworksSecurityApi.md#patch_system_management_network_securities_by_id) | **PATCH** /system/managementNetworkSecurities/{id} | Patch ManagementNetworkSecurity
[**post_system_management_network_securities**](ManagementNetworksSecurityApi.md#post_system_management_network_securities) | **POST** /system/managementNetworkSecurities | Post ManagementNetworkSecurity
[**put_system_management_network_securities_by_id**](ManagementNetworksSecurityApi.md#put_system_management_network_securities_by_id) | **PUT** /system/managementNetworkSecurities/{id} | Put ManagementNetworkSecurity


# **delete_system_management_network_securities_by_id**
> delete_system_management_network_securities_by_id(id, client_id)

Delete ManagementNetworkSecurity

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
    api_instance = connectwise_psa.ManagementNetworksSecurityApi(api_client)
    id = 56 # int | managementNetworkSecurityId
    client_id = 'client_id_example' # str | 

    try:
        # Delete ManagementNetworkSecurity
        api_instance.delete_system_management_network_securities_by_id(id, client_id)
    except Exception as e:
        print("Exception when calling ManagementNetworksSecurityApi->delete_system_management_network_securities_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| managementNetworkSecurityId | 
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

# **get_system_management_network_securities**
> List[ManagementNetworkSecurity] get_system_management_network_securities(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of ManagementNetworkSecurity

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.management_network_security import ManagementNetworkSecurity
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
    api_instance = connectwise_psa.ManagementNetworksSecurityApi(api_client)
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
        # Get List of ManagementNetworkSecurity
        api_response = api_instance.get_system_management_network_securities(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of ManagementNetworksSecurityApi->get_system_management_network_securities:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagementNetworksSecurityApi->get_system_management_network_securities: %s\n" % e)
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

[**List[ManagementNetworkSecurity]**](ManagementNetworkSecurity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of ManagementNetworkSecurity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_system_management_network_securities_by_id**
> ManagementNetworkSecurity get_system_management_network_securities_by_id(id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get ManagementNetworkSecurity

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.management_network_security import ManagementNetworkSecurity
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
    api_instance = connectwise_psa.ManagementNetworksSecurityApi(api_client)
    id = 56 # int | managementNetworkSecurityId
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
        # Get ManagementNetworkSecurity
        api_response = api_instance.get_system_management_network_securities_by_id(id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of ManagementNetworksSecurityApi->get_system_management_network_securities_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagementNetworksSecurityApi->get_system_management_network_securities_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| managementNetworkSecurityId | 
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

[**ManagementNetworkSecurity**](ManagementNetworkSecurity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ManagementNetworkSecurity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_system_management_network_securities_by_id_test_credentials**
> SuccessResponse get_system_management_network_securities_by_id_test_credentials(id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get SuccessResponse

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.success_response import SuccessResponse
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
    api_instance = connectwise_psa.ManagementNetworksSecurityApi(api_client)
    id = 56 # int | managementNetworkSecurityId
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
        api_response = api_instance.get_system_management_network_securities_by_id_test_credentials(id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of ManagementNetworksSecurityApi->get_system_management_network_securities_by_id_test_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagementNetworksSecurityApi->get_system_management_network_securities_by_id_test_credentials: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| managementNetworkSecurityId | 
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

# **get_system_management_network_securities_count**
> Count get_system_management_network_securities_count(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Count of ManagementNetworkSecurity

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
    api_instance = connectwise_psa.ManagementNetworksSecurityApi(api_client)
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
        # Get Count of ManagementNetworkSecurity
        api_response = api_instance.get_system_management_network_securities_count(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of ManagementNetworksSecurityApi->get_system_management_network_securities_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagementNetworksSecurityApi->get_system_management_network_securities_count: %s\n" % e)
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

# **patch_system_management_network_securities_by_id**
> ManagementNetworkSecurity patch_system_management_network_securities_by_id(id, client_id, patch_operation)

Patch ManagementNetworkSecurity

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.management_network_security import ManagementNetworkSecurity
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
    api_instance = connectwise_psa.ManagementNetworksSecurityApi(api_client)
    id = 56 # int | managementNetworkSecurityId
    client_id = 'client_id_example' # str | 
    patch_operation = [connectwise_psa.PatchOperation()] # List[PatchOperation] | List of PatchOperation

    try:
        # Patch ManagementNetworkSecurity
        api_response = api_instance.patch_system_management_network_securities_by_id(id, client_id, patch_operation)
        print("The response of ManagementNetworksSecurityApi->patch_system_management_network_securities_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagementNetworksSecurityApi->patch_system_management_network_securities_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| managementNetworkSecurityId | 
 **client_id** | **str**|  | 
 **patch_operation** | [**List[PatchOperation]**](PatchOperation.md)| List of PatchOperation | 

### Return type

[**ManagementNetworkSecurity**](ManagementNetworkSecurity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ManagementNetworkSecurity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_system_management_network_securities**
> ManagementNetworkSecurity post_system_management_network_securities(client_id, management_network_security)

Post ManagementNetworkSecurity

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.management_network_security import ManagementNetworkSecurity
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
    api_instance = connectwise_psa.ManagementNetworksSecurityApi(api_client)
    client_id = 'client_id_example' # str | 
    management_network_security = connectwise_psa.ManagementNetworkSecurity() # ManagementNetworkSecurity | managementNetworkSecurity

    try:
        # Post ManagementNetworkSecurity
        api_response = api_instance.post_system_management_network_securities(client_id, management_network_security)
        print("The response of ManagementNetworksSecurityApi->post_system_management_network_securities:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagementNetworksSecurityApi->post_system_management_network_securities: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**|  | 
 **management_network_security** | [**ManagementNetworkSecurity**](ManagementNetworkSecurity.md)| managementNetworkSecurity | 

### Return type

[**ManagementNetworkSecurity**](ManagementNetworkSecurity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | ManagementNetworkSecurity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_system_management_network_securities_by_id**
> ManagementNetworkSecurity put_system_management_network_securities_by_id(id, client_id, management_network_security)

Put ManagementNetworkSecurity

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.management_network_security import ManagementNetworkSecurity
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
    api_instance = connectwise_psa.ManagementNetworksSecurityApi(api_client)
    id = 56 # int | managementNetworkSecurityId
    client_id = 'client_id_example' # str | 
    management_network_security = connectwise_psa.ManagementNetworkSecurity() # ManagementNetworkSecurity | managementNetworkSecurity

    try:
        # Put ManagementNetworkSecurity
        api_response = api_instance.put_system_management_network_securities_by_id(id, client_id, management_network_security)
        print("The response of ManagementNetworksSecurityApi->put_system_management_network_securities_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagementNetworksSecurityApi->put_system_management_network_securities_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| managementNetworkSecurityId | 
 **client_id** | **str**|  | 
 **management_network_security** | [**ManagementNetworkSecurity**](ManagementNetworkSecurity.md)| managementNetworkSecurity | 

### Return type

[**ManagementNetworkSecurity**](ManagementNetworkSecurity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ManagementNetworkSecurity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

