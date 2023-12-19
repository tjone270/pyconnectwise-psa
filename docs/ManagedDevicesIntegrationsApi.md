# connectwise_psa.ManagedDevicesIntegrationsApi

All URIs are relative to *https://aus-api.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_company_managed_devices_integrations_by_id**](ManagedDevicesIntegrationsApi.md#delete_company_managed_devices_integrations_by_id) | **DELETE** /company/managedDevicesIntegrations/{id} | Delete ManagedDevicesIntegration
[**get_company_managed_devices_integrations**](ManagedDevicesIntegrationsApi.md#get_company_managed_devices_integrations) | **GET** /company/managedDevicesIntegrations | Get List of ManagedDevicesIntegration
[**get_company_managed_devices_integrations_by_id**](ManagedDevicesIntegrationsApi.md#get_company_managed_devices_integrations_by_id) | **GET** /company/managedDevicesIntegrations/{id} | Get ManagedDevicesIntegration
[**get_company_managed_devices_integrations_by_id_usages**](ManagedDevicesIntegrationsApi.md#get_company_managed_devices_integrations_by_id_usages) | **GET** /company/managedDevicesIntegrations/{id}/usages | Get List of Usage Count
[**get_company_managed_devices_integrations_by_id_usages_list**](ManagedDevicesIntegrationsApi.md#get_company_managed_devices_integrations_by_id_usages_list) | **GET** /company/managedDevicesIntegrations/{id}/usages/list | Get List of Usage
[**get_company_managed_devices_integrations_count**](ManagedDevicesIntegrationsApi.md#get_company_managed_devices_integrations_count) | **GET** /company/managedDevicesIntegrations/count | Get Count of Usage
[**patch_company_managed_devices_integrations_by_id**](ManagedDevicesIntegrationsApi.md#patch_company_managed_devices_integrations_by_id) | **PATCH** /company/managedDevicesIntegrations/{id} | Patch ManagedDevicesIntegration
[**post_company_managed_devices_integrations**](ManagedDevicesIntegrationsApi.md#post_company_managed_devices_integrations) | **POST** /company/managedDevicesIntegrations | Post ManagedDevicesIntegration
[**put_company_managed_devices_integrations_by_id**](ManagedDevicesIntegrationsApi.md#put_company_managed_devices_integrations_by_id) | **PUT** /company/managedDevicesIntegrations/{id} | Put ManagedDevicesIntegration


# **delete_company_managed_devices_integrations_by_id**
> delete_company_managed_devices_integrations_by_id(id, client_id)

Delete ManagedDevicesIntegration

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
    api_instance = connectwise_psa.ManagedDevicesIntegrationsApi(api_client)
    id = 56 # int | managedDevicesIntegrationId
    client_id = 'client_id_example' # str | 

    try:
        # Delete ManagedDevicesIntegration
        api_instance.delete_company_managed_devices_integrations_by_id(id, client_id)
    except Exception as e:
        print("Exception when calling ManagedDevicesIntegrationsApi->delete_company_managed_devices_integrations_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| managedDevicesIntegrationId | 
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

# **get_company_managed_devices_integrations**
> List[ManagedDevicesIntegration] get_company_managed_devices_integrations(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of ManagedDevicesIntegration

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.managed_devices_integration import ManagedDevicesIntegration
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
    api_instance = connectwise_psa.ManagedDevicesIntegrationsApi(api_client)
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
        # Get List of ManagedDevicesIntegration
        api_response = api_instance.get_company_managed_devices_integrations(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of ManagedDevicesIntegrationsApi->get_company_managed_devices_integrations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagedDevicesIntegrationsApi->get_company_managed_devices_integrations: %s\n" % e)
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

[**List[ManagedDevicesIntegration]**](ManagedDevicesIntegration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of ManagedDevicesIntegration |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_company_managed_devices_integrations_by_id**
> ManagedDevicesIntegration get_company_managed_devices_integrations_by_id(id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get ManagedDevicesIntegration

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.managed_devices_integration import ManagedDevicesIntegration
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
    api_instance = connectwise_psa.ManagedDevicesIntegrationsApi(api_client)
    id = 56 # int | managedDevicesIntegrationId
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
        # Get ManagedDevicesIntegration
        api_response = api_instance.get_company_managed_devices_integrations_by_id(id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of ManagedDevicesIntegrationsApi->get_company_managed_devices_integrations_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagedDevicesIntegrationsApi->get_company_managed_devices_integrations_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| managedDevicesIntegrationId | 
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

[**ManagedDevicesIntegration**](ManagedDevicesIntegration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ManagedDevicesIntegration |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_company_managed_devices_integrations_by_id_usages**
> List[Usage] get_company_managed_devices_integrations_by_id_usages(id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of Usage Count

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.usage import Usage
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
    api_instance = connectwise_psa.ManagedDevicesIntegrationsApi(api_client)
    id = 56 # int | managedDevicesIntegrationId
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
        # Get List of Usage Count
        api_response = api_instance.get_company_managed_devices_integrations_by_id_usages(id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of ManagedDevicesIntegrationsApi->get_company_managed_devices_integrations_by_id_usages:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagedDevicesIntegrationsApi->get_company_managed_devices_integrations_by_id_usages: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| managedDevicesIntegrationId | 
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

[**List[Usage]**](Usage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of Usage |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_company_managed_devices_integrations_by_id_usages_list**
> List[Usage] get_company_managed_devices_integrations_by_id_usages_list(id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of Usage

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.usage import Usage
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
    api_instance = connectwise_psa.ManagedDevicesIntegrationsApi(api_client)
    id = 56 # int | managedDevicesIntegrationId
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
        # Get List of Usage
        api_response = api_instance.get_company_managed_devices_integrations_by_id_usages_list(id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of ManagedDevicesIntegrationsApi->get_company_managed_devices_integrations_by_id_usages_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagedDevicesIntegrationsApi->get_company_managed_devices_integrations_by_id_usages_list: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| managedDevicesIntegrationId | 
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

[**List[Usage]**](Usage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of Usage |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_company_managed_devices_integrations_count**
> Count get_company_managed_devices_integrations_count(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Count of Usage

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
    api_instance = connectwise_psa.ManagedDevicesIntegrationsApi(api_client)
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
        # Get Count of Usage
        api_response = api_instance.get_company_managed_devices_integrations_count(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of ManagedDevicesIntegrationsApi->get_company_managed_devices_integrations_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagedDevicesIntegrationsApi->get_company_managed_devices_integrations_count: %s\n" % e)
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

# **patch_company_managed_devices_integrations_by_id**
> ManagedDevicesIntegration patch_company_managed_devices_integrations_by_id(id, client_id, patch_operation)

Patch ManagedDevicesIntegration

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.managed_devices_integration import ManagedDevicesIntegration
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
    api_instance = connectwise_psa.ManagedDevicesIntegrationsApi(api_client)
    id = 56 # int | managedDevicesIntegrationId
    client_id = 'client_id_example' # str | 
    patch_operation = [connectwise_psa.PatchOperation()] # List[PatchOperation] | List of PatchOperation

    try:
        # Patch ManagedDevicesIntegration
        api_response = api_instance.patch_company_managed_devices_integrations_by_id(id, client_id, patch_operation)
        print("The response of ManagedDevicesIntegrationsApi->patch_company_managed_devices_integrations_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagedDevicesIntegrationsApi->patch_company_managed_devices_integrations_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| managedDevicesIntegrationId | 
 **client_id** | **str**|  | 
 **patch_operation** | [**List[PatchOperation]**](PatchOperation.md)| List of PatchOperation | 

### Return type

[**ManagedDevicesIntegration**](ManagedDevicesIntegration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ManagedDevicesIntegration |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_company_managed_devices_integrations**
> ManagedDevicesIntegration post_company_managed_devices_integrations(client_id, managed_devices_integration)

Post ManagedDevicesIntegration

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.managed_devices_integration import ManagedDevicesIntegration
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
    api_instance = connectwise_psa.ManagedDevicesIntegrationsApi(api_client)
    client_id = 'client_id_example' # str | 
    managed_devices_integration = connectwise_psa.ManagedDevicesIntegration() # ManagedDevicesIntegration | managedDevicesIntegration

    try:
        # Post ManagedDevicesIntegration
        api_response = api_instance.post_company_managed_devices_integrations(client_id, managed_devices_integration)
        print("The response of ManagedDevicesIntegrationsApi->post_company_managed_devices_integrations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagedDevicesIntegrationsApi->post_company_managed_devices_integrations: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**|  | 
 **managed_devices_integration** | [**ManagedDevicesIntegration**](ManagedDevicesIntegration.md)| managedDevicesIntegration | 

### Return type

[**ManagedDevicesIntegration**](ManagedDevicesIntegration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | ManagedDevicesIntegration |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_company_managed_devices_integrations_by_id**
> ManagedDevicesIntegration put_company_managed_devices_integrations_by_id(id, client_id, managed_devices_integration)

Put ManagedDevicesIntegration

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.managed_devices_integration import ManagedDevicesIntegration
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
    api_instance = connectwise_psa.ManagedDevicesIntegrationsApi(api_client)
    id = 56 # int | managedDevicesIntegrationId
    client_id = 'client_id_example' # str | 
    managed_devices_integration = connectwise_psa.ManagedDevicesIntegration() # ManagedDevicesIntegration | managedDevicesIntegration

    try:
        # Put ManagedDevicesIntegration
        api_response = api_instance.put_company_managed_devices_integrations_by_id(id, client_id, managed_devices_integration)
        print("The response of ManagedDevicesIntegrationsApi->put_company_managed_devices_integrations_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagedDevicesIntegrationsApi->put_company_managed_devices_integrations_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| managedDevicesIntegrationId | 
 **client_id** | **str**|  | 
 **managed_devices_integration** | [**ManagedDevicesIntegration**](ManagedDevicesIntegration.md)| managedDevicesIntegration | 

### Return type

[**ManagedDevicesIntegration**](ManagedDevicesIntegration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ManagedDevicesIntegration |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

