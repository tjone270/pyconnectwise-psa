# connectwise_psa.SsoConfigurationsApi

All URIs are relative to *https://aus-api.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_system_sso_configurations_by_id**](SsoConfigurationsApi.md#delete_system_sso_configurations_by_id) | **DELETE** /system/ssoConfigurations/{id} | Delete SsoConfiguration
[**get_system_sso_configurations**](SsoConfigurationsApi.md#get_system_sso_configurations) | **GET** /system/ssoConfigurations | Get List of SsoConfiguration
[**get_system_sso_configurations_by_id**](SsoConfigurationsApi.md#get_system_sso_configurations_by_id) | **GET** /system/ssoConfigurations/{id} | Get SsoConfiguration
[**get_system_sso_configurations_count**](SsoConfigurationsApi.md#get_system_sso_configurations_count) | **GET** /system/ssoConfigurations/count | Get Count of SsoConfiguration
[**patch_system_sso_configurations_by_id**](SsoConfigurationsApi.md#patch_system_sso_configurations_by_id) | **PATCH** /system/ssoConfigurations/{id} | Patch SsoConfiguration
[**post_system_sso_configurations**](SsoConfigurationsApi.md#post_system_sso_configurations) | **POST** /system/ssoConfigurations | Post SsoConfiguration
[**post_system_sso_configurations_by_id_registertoken**](SsoConfigurationsApi.md#post_system_sso_configurations_by_id_registertoken) | **POST** /system/ssoConfigurations/{id}/registertoken | Post SsoConfiguration
[**post_system_sso_configurations_by_id_submitmembers**](SsoConfigurationsApi.md#post_system_sso_configurations_by_id_submitmembers) | **POST** /system/ssoConfigurations/{id}/submitmembers | Post SsoConfiguration
[**put_system_sso_configurations_by_id**](SsoConfigurationsApi.md#put_system_sso_configurations_by_id) | **PUT** /system/ssoConfigurations/{id} | Put SsoConfiguration


# **delete_system_sso_configurations_by_id**
> delete_system_sso_configurations_by_id(id, client_id)

Delete SsoConfiguration

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
    api_instance = connectwise_psa.SsoConfigurationsApi(api_client)
    id = 56 # int | ssoConfigurationId
    client_id = 'client_id_example' # str | 

    try:
        # Delete SsoConfiguration
        api_instance.delete_system_sso_configurations_by_id(id, client_id)
    except Exception as e:
        print("Exception when calling SsoConfigurationsApi->delete_system_sso_configurations_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ssoConfigurationId | 
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

# **get_system_sso_configurations**
> List[SsoConfiguration] get_system_sso_configurations(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of SsoConfiguration

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.sso_configuration import SsoConfiguration
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
    api_instance = connectwise_psa.SsoConfigurationsApi(api_client)
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
        # Get List of SsoConfiguration
        api_response = api_instance.get_system_sso_configurations(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of SsoConfigurationsApi->get_system_sso_configurations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SsoConfigurationsApi->get_system_sso_configurations: %s\n" % e)
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

[**List[SsoConfiguration]**](SsoConfiguration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of SsoConfiguration |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_system_sso_configurations_by_id**
> SsoConfiguration get_system_sso_configurations_by_id(id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get SsoConfiguration

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.sso_configuration import SsoConfiguration
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
    api_instance = connectwise_psa.SsoConfigurationsApi(api_client)
    id = 56 # int | ssoConfigurationId
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
        # Get SsoConfiguration
        api_response = api_instance.get_system_sso_configurations_by_id(id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of SsoConfigurationsApi->get_system_sso_configurations_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SsoConfigurationsApi->get_system_sso_configurations_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ssoConfigurationId | 
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

[**SsoConfiguration**](SsoConfiguration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | SsoConfiguration |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_system_sso_configurations_count**
> Count get_system_sso_configurations_count(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Count of SsoConfiguration

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
    api_instance = connectwise_psa.SsoConfigurationsApi(api_client)
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
        # Get Count of SsoConfiguration
        api_response = api_instance.get_system_sso_configurations_count(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of SsoConfigurationsApi->get_system_sso_configurations_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SsoConfigurationsApi->get_system_sso_configurations_count: %s\n" % e)
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

# **patch_system_sso_configurations_by_id**
> SsoConfiguration patch_system_sso_configurations_by_id(id, client_id, patch_operation)

Patch SsoConfiguration

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.patch_operation import PatchOperation
from connectwise_psa.models.sso_configuration import SsoConfiguration
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
    api_instance = connectwise_psa.SsoConfigurationsApi(api_client)
    id = 56 # int | ssoConfigurationId
    client_id = 'client_id_example' # str | 
    patch_operation = [connectwise_psa.PatchOperation()] # List[PatchOperation] | List of PatchOperation

    try:
        # Patch SsoConfiguration
        api_response = api_instance.patch_system_sso_configurations_by_id(id, client_id, patch_operation)
        print("The response of SsoConfigurationsApi->patch_system_sso_configurations_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SsoConfigurationsApi->patch_system_sso_configurations_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ssoConfigurationId | 
 **client_id** | **str**|  | 
 **patch_operation** | [**List[PatchOperation]**](PatchOperation.md)| List of PatchOperation | 

### Return type

[**SsoConfiguration**](SsoConfiguration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | SsoConfiguration |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_system_sso_configurations**
> SsoConfiguration post_system_sso_configurations(client_id, sso_configuration)

Post SsoConfiguration

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.sso_configuration import SsoConfiguration
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
    api_instance = connectwise_psa.SsoConfigurationsApi(api_client)
    client_id = 'client_id_example' # str | 
    sso_configuration = connectwise_psa.SsoConfiguration() # SsoConfiguration | ssoConfiguration

    try:
        # Post SsoConfiguration
        api_response = api_instance.post_system_sso_configurations(client_id, sso_configuration)
        print("The response of SsoConfigurationsApi->post_system_sso_configurations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SsoConfigurationsApi->post_system_sso_configurations: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**|  | 
 **sso_configuration** | [**SsoConfiguration**](SsoConfiguration.md)| ssoConfiguration | 

### Return type

[**SsoConfiguration**](SsoConfiguration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | SsoConfiguration |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_system_sso_configurations_by_id_registertoken**
> SsoConfiguration post_system_sso_configurations_by_id_registertoken(id, client_id, sso_configuration)

Post SsoConfiguration

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.sso_configuration import SsoConfiguration
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
    api_instance = connectwise_psa.SsoConfigurationsApi(api_client)
    id = 56 # int | ssoConfigurationId
    client_id = 'client_id_example' # str | 
    sso_configuration = connectwise_psa.SsoConfiguration() # SsoConfiguration | ssoConfiguration

    try:
        # Post SsoConfiguration
        api_response = api_instance.post_system_sso_configurations_by_id_registertoken(id, client_id, sso_configuration)
        print("The response of SsoConfigurationsApi->post_system_sso_configurations_by_id_registertoken:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SsoConfigurationsApi->post_system_sso_configurations_by_id_registertoken: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ssoConfigurationId | 
 **client_id** | **str**|  | 
 **sso_configuration** | [**SsoConfiguration**](SsoConfiguration.md)| ssoConfiguration | 

### Return type

[**SsoConfiguration**](SsoConfiguration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | SsoConfiguration |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_system_sso_configurations_by_id_submitmembers**
> SsoConfiguration post_system_sso_configurations_by_id_submitmembers(id, client_id, sso_configuration)

Post SsoConfiguration

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.sso_configuration import SsoConfiguration
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
    api_instance = connectwise_psa.SsoConfigurationsApi(api_client)
    id = 56 # int | ssoConfigurationId
    client_id = 'client_id_example' # str | 
    sso_configuration = connectwise_psa.SsoConfiguration() # SsoConfiguration | ssoConfiguration

    try:
        # Post SsoConfiguration
        api_response = api_instance.post_system_sso_configurations_by_id_submitmembers(id, client_id, sso_configuration)
        print("The response of SsoConfigurationsApi->post_system_sso_configurations_by_id_submitmembers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SsoConfigurationsApi->post_system_sso_configurations_by_id_submitmembers: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ssoConfigurationId | 
 **client_id** | **str**|  | 
 **sso_configuration** | [**SsoConfiguration**](SsoConfiguration.md)| ssoConfiguration | 

### Return type

[**SsoConfiguration**](SsoConfiguration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | SsoConfiguration |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_system_sso_configurations_by_id**
> SsoConfiguration put_system_sso_configurations_by_id(id, client_id, sso_configuration)

Put SsoConfiguration

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.sso_configuration import SsoConfiguration
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
    api_instance = connectwise_psa.SsoConfigurationsApi(api_client)
    id = 56 # int | ssoConfigurationId
    client_id = 'client_id_example' # str | 
    sso_configuration = connectwise_psa.SsoConfiguration() # SsoConfiguration | ssoConfiguration

    try:
        # Put SsoConfiguration
        api_response = api_instance.put_system_sso_configurations_by_id(id, client_id, sso_configuration)
        print("The response of SsoConfigurationsApi->put_system_sso_configurations_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SsoConfigurationsApi->put_system_sso_configurations_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ssoConfigurationId | 
 **client_id** | **str**|  | 
 **sso_configuration** | [**SsoConfiguration**](SsoConfiguration.md)| ssoConfiguration | 

### Return type

[**SsoConfiguration**](SsoConfiguration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | SsoConfiguration |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

