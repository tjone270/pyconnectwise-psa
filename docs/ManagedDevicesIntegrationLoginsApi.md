# connectwise_psa.ManagedDevicesIntegrationLoginsApi

All URIs are relative to *https://aus-api.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_company_managed_devices_integrations_by_parent_id_logins_by_id**](ManagedDevicesIntegrationLoginsApi.md#delete_company_managed_devices_integrations_by_parent_id_logins_by_id) | **DELETE** /company/managedDevicesIntegrations/{parentId}/logins/{id} | Delete ManagedDevicesIntegrationLogin
[**get_company_managed_devices_integrations_by_parent_id_logins**](ManagedDevicesIntegrationLoginsApi.md#get_company_managed_devices_integrations_by_parent_id_logins) | **GET** /company/managedDevicesIntegrations/{parentId}/logins | Get List of ManagedDevicesIntegrationLogin
[**get_company_managed_devices_integrations_by_parent_id_logins_by_id**](ManagedDevicesIntegrationLoginsApi.md#get_company_managed_devices_integrations_by_parent_id_logins_by_id) | **GET** /company/managedDevicesIntegrations/{parentId}/logins/{id} | Get ManagedDevicesIntegrationLogin
[**get_company_managed_devices_integrations_by_parent_id_logins_count**](ManagedDevicesIntegrationLoginsApi.md#get_company_managed_devices_integrations_by_parent_id_logins_count) | **GET** /company/managedDevicesIntegrations/{parentId}/logins/count | Get Count of ManagedDevicesIntegrationLogin
[**patch_company_managed_devices_integrations_by_parent_id_logins_by_id**](ManagedDevicesIntegrationLoginsApi.md#patch_company_managed_devices_integrations_by_parent_id_logins_by_id) | **PATCH** /company/managedDevicesIntegrations/{parentId}/logins/{id} | Patch ManagedDevicesIntegrationLogin
[**post_company_managed_devices_integrations_by_parent_id_logins**](ManagedDevicesIntegrationLoginsApi.md#post_company_managed_devices_integrations_by_parent_id_logins) | **POST** /company/managedDevicesIntegrations/{parentId}/logins | Post ManagedDevicesIntegrationLogin
[**put_company_managed_devices_integrations_by_parent_id_logins_by_id**](ManagedDevicesIntegrationLoginsApi.md#put_company_managed_devices_integrations_by_parent_id_logins_by_id) | **PUT** /company/managedDevicesIntegrations/{parentId}/logins/{id} | Put ManagedDevicesIntegrationLogin


# **delete_company_managed_devices_integrations_by_parent_id_logins_by_id**
> ManagedDevicesIntegrationLogin delete_company_managed_devices_integrations_by_parent_id_logins_by_id(id, parent_id, client_id)

Delete ManagedDevicesIntegrationLogin

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.managed_devices_integration_login import ManagedDevicesIntegrationLogin
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
    api_instance = connectwise_psa.ManagedDevicesIntegrationLoginsApi(api_client)
    id = 56 # int | loginId
    parent_id = 56 # int | managedDevicesIntegrationId
    client_id = 'client_id_example' # str | 

    try:
        # Delete ManagedDevicesIntegrationLogin
        api_response = api_instance.delete_company_managed_devices_integrations_by_parent_id_logins_by_id(id, parent_id, client_id)
        print("The response of ManagedDevicesIntegrationLoginsApi->delete_company_managed_devices_integrations_by_parent_id_logins_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagedDevicesIntegrationLoginsApi->delete_company_managed_devices_integrations_by_parent_id_logins_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| loginId | 
 **parent_id** | **int**| managedDevicesIntegrationId | 
 **client_id** | **str**|  | 

### Return type

[**ManagedDevicesIntegrationLogin**](ManagedDevicesIntegrationLogin.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ManagedDevicesIntegrationLogin |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_company_managed_devices_integrations_by_parent_id_logins**
> List[ManagedDevicesIntegrationLogin] get_company_managed_devices_integrations_by_parent_id_logins(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of ManagedDevicesIntegrationLogin

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.managed_devices_integration_login import ManagedDevicesIntegrationLogin
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
    api_instance = connectwise_psa.ManagedDevicesIntegrationLoginsApi(api_client)
    parent_id = 56 # int | managedDevicesIntegrationId
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
        # Get List of ManagedDevicesIntegrationLogin
        api_response = api_instance.get_company_managed_devices_integrations_by_parent_id_logins(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of ManagedDevicesIntegrationLoginsApi->get_company_managed_devices_integrations_by_parent_id_logins:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagedDevicesIntegrationLoginsApi->get_company_managed_devices_integrations_by_parent_id_logins: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| managedDevicesIntegrationId | 
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

[**List[ManagedDevicesIntegrationLogin]**](ManagedDevicesIntegrationLogin.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of ManagedDevicesIntegrationLogin |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_company_managed_devices_integrations_by_parent_id_logins_by_id**
> ManagedDevicesIntegrationLogin get_company_managed_devices_integrations_by_parent_id_logins_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get ManagedDevicesIntegrationLogin

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.managed_devices_integration_login import ManagedDevicesIntegrationLogin
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
    api_instance = connectwise_psa.ManagedDevicesIntegrationLoginsApi(api_client)
    id = 56 # int | loginId
    parent_id = 56 # int | managedDevicesIntegrationId
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
        # Get ManagedDevicesIntegrationLogin
        api_response = api_instance.get_company_managed_devices_integrations_by_parent_id_logins_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of ManagedDevicesIntegrationLoginsApi->get_company_managed_devices_integrations_by_parent_id_logins_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagedDevicesIntegrationLoginsApi->get_company_managed_devices_integrations_by_parent_id_logins_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| loginId | 
 **parent_id** | **int**| managedDevicesIntegrationId | 
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

[**ManagedDevicesIntegrationLogin**](ManagedDevicesIntegrationLogin.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ManagedDevicesIntegrationLogin |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_company_managed_devices_integrations_by_parent_id_logins_count**
> Count get_company_managed_devices_integrations_by_parent_id_logins_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Count of ManagedDevicesIntegrationLogin

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
    api_instance = connectwise_psa.ManagedDevicesIntegrationLoginsApi(api_client)
    parent_id = 56 # int | managedDevicesIntegrationId
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
        # Get Count of ManagedDevicesIntegrationLogin
        api_response = api_instance.get_company_managed_devices_integrations_by_parent_id_logins_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of ManagedDevicesIntegrationLoginsApi->get_company_managed_devices_integrations_by_parent_id_logins_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagedDevicesIntegrationLoginsApi->get_company_managed_devices_integrations_by_parent_id_logins_count: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| managedDevicesIntegrationId | 
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

# **patch_company_managed_devices_integrations_by_parent_id_logins_by_id**
> ManagedDevicesIntegrationLogin patch_company_managed_devices_integrations_by_parent_id_logins_by_id(id, parent_id, client_id, patch_operation)

Patch ManagedDevicesIntegrationLogin

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.managed_devices_integration_login import ManagedDevicesIntegrationLogin
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
    api_instance = connectwise_psa.ManagedDevicesIntegrationLoginsApi(api_client)
    id = 56 # int | loginId
    parent_id = 56 # int | managedDevicesIntegrationId
    client_id = 'client_id_example' # str | 
    patch_operation = [connectwise_psa.PatchOperation()] # List[PatchOperation] | List of PatchOperation

    try:
        # Patch ManagedDevicesIntegrationLogin
        api_response = api_instance.patch_company_managed_devices_integrations_by_parent_id_logins_by_id(id, parent_id, client_id, patch_operation)
        print("The response of ManagedDevicesIntegrationLoginsApi->patch_company_managed_devices_integrations_by_parent_id_logins_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagedDevicesIntegrationLoginsApi->patch_company_managed_devices_integrations_by_parent_id_logins_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| loginId | 
 **parent_id** | **int**| managedDevicesIntegrationId | 
 **client_id** | **str**|  | 
 **patch_operation** | [**List[PatchOperation]**](PatchOperation.md)| List of PatchOperation | 

### Return type

[**ManagedDevicesIntegrationLogin**](ManagedDevicesIntegrationLogin.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ManagedDevicesIntegrationLogin |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_company_managed_devices_integrations_by_parent_id_logins**
> ManagedDevicesIntegrationLogin post_company_managed_devices_integrations_by_parent_id_logins(parent_id, client_id, managed_devices_integration_login)

Post ManagedDevicesIntegrationLogin

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.managed_devices_integration_login import ManagedDevicesIntegrationLogin
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
    api_instance = connectwise_psa.ManagedDevicesIntegrationLoginsApi(api_client)
    parent_id = 56 # int | managedDevicesIntegrationId
    client_id = 'client_id_example' # str | 
    managed_devices_integration_login = connectwise_psa.ManagedDevicesIntegrationLogin() # ManagedDevicesIntegrationLogin | login

    try:
        # Post ManagedDevicesIntegrationLogin
        api_response = api_instance.post_company_managed_devices_integrations_by_parent_id_logins(parent_id, client_id, managed_devices_integration_login)
        print("The response of ManagedDevicesIntegrationLoginsApi->post_company_managed_devices_integrations_by_parent_id_logins:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagedDevicesIntegrationLoginsApi->post_company_managed_devices_integrations_by_parent_id_logins: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| managedDevicesIntegrationId | 
 **client_id** | **str**|  | 
 **managed_devices_integration_login** | [**ManagedDevicesIntegrationLogin**](ManagedDevicesIntegrationLogin.md)| login | 

### Return type

[**ManagedDevicesIntegrationLogin**](ManagedDevicesIntegrationLogin.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ManagedDevicesIntegrationLogin |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_company_managed_devices_integrations_by_parent_id_logins_by_id**
> ManagedDevicesIntegrationLogin put_company_managed_devices_integrations_by_parent_id_logins_by_id(id, parent_id, client_id, managed_devices_integration_login)

Put ManagedDevicesIntegrationLogin

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.managed_devices_integration_login import ManagedDevicesIntegrationLogin
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
    api_instance = connectwise_psa.ManagedDevicesIntegrationLoginsApi(api_client)
    id = 56 # int | loginId
    parent_id = 56 # int | managedDevicesIntegrationId
    client_id = 'client_id_example' # str | 
    managed_devices_integration_login = connectwise_psa.ManagedDevicesIntegrationLogin() # ManagedDevicesIntegrationLogin | login

    try:
        # Put ManagedDevicesIntegrationLogin
        api_response = api_instance.put_company_managed_devices_integrations_by_parent_id_logins_by_id(id, parent_id, client_id, managed_devices_integration_login)
        print("The response of ManagedDevicesIntegrationLoginsApi->put_company_managed_devices_integrations_by_parent_id_logins_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagedDevicesIntegrationLoginsApi->put_company_managed_devices_integrations_by_parent_id_logins_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| loginId | 
 **parent_id** | **int**| managedDevicesIntegrationId | 
 **client_id** | **str**|  | 
 **managed_devices_integration_login** | [**ManagedDevicesIntegrationLogin**](ManagedDevicesIntegrationLogin.md)| login | 

### Return type

[**ManagedDevicesIntegrationLogin**](ManagedDevicesIntegrationLogin.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ManagedDevicesIntegrationLogin |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

