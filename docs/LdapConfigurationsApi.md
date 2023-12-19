# connectwise_psa.LdapConfigurationsApi

All URIs are relative to *https://aus-api.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_system_ldap_configurations_by_id**](LdapConfigurationsApi.md#delete_system_ldap_configurations_by_id) | **DELETE** /system/ldapConfigurations/{id} | Delete LdapConfiguration
[**get_system_ldap_configurations**](LdapConfigurationsApi.md#get_system_ldap_configurations) | **GET** /system/ldapConfigurations | Get List of LdapConfiguration
[**get_system_ldap_configurations_by_id**](LdapConfigurationsApi.md#get_system_ldap_configurations_by_id) | **GET** /system/ldapConfigurations/{id} | Get LdapConfiguration
[**get_system_ldap_configurations_count**](LdapConfigurationsApi.md#get_system_ldap_configurations_count) | **GET** /system/ldapConfigurations/count | Get Count of LdapConfiguration
[**patch_system_ldap_configurations_by_id**](LdapConfigurationsApi.md#patch_system_ldap_configurations_by_id) | **PATCH** /system/ldapConfigurations/{id} | Patch LdapConfiguration
[**post_system_ldap_configurations**](LdapConfigurationsApi.md#post_system_ldap_configurations) | **POST** /system/ldapConfigurations | Post LdapConfiguration
[**post_system_ldap_configurations_test_link**](LdapConfigurationsApi.md#post_system_ldap_configurations_test_link) | **POST** /system/ldapConfigurations/testLink | Post SuccessResponse
[**put_system_ldap_configurations_by_id**](LdapConfigurationsApi.md#put_system_ldap_configurations_by_id) | **PUT** /system/ldapConfigurations/{id} | Put LdapConfiguration


# **delete_system_ldap_configurations_by_id**
> delete_system_ldap_configurations_by_id(id, client_id)

Delete LdapConfiguration

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
    api_instance = connectwise_psa.LdapConfigurationsApi(api_client)
    id = 56 # int | ldapConfigurationId
    client_id = 'client_id_example' # str | 

    try:
        # Delete LdapConfiguration
        api_instance.delete_system_ldap_configurations_by_id(id, client_id)
    except Exception as e:
        print("Exception when calling LdapConfigurationsApi->delete_system_ldap_configurations_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ldapConfigurationId | 
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

# **get_system_ldap_configurations**
> List[LdapConfiguration] get_system_ldap_configurations(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of LdapConfiguration

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.ldap_configuration import LdapConfiguration
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
    api_instance = connectwise_psa.LdapConfigurationsApi(api_client)
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
        # Get List of LdapConfiguration
        api_response = api_instance.get_system_ldap_configurations(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of LdapConfigurationsApi->get_system_ldap_configurations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LdapConfigurationsApi->get_system_ldap_configurations: %s\n" % e)
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

[**List[LdapConfiguration]**](LdapConfiguration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of LdapConfiguration |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_system_ldap_configurations_by_id**
> LdapConfiguration get_system_ldap_configurations_by_id(id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get LdapConfiguration

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.ldap_configuration import LdapConfiguration
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
    api_instance = connectwise_psa.LdapConfigurationsApi(api_client)
    id = 56 # int | ldapConfigurationId
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
        # Get LdapConfiguration
        api_response = api_instance.get_system_ldap_configurations_by_id(id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of LdapConfigurationsApi->get_system_ldap_configurations_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LdapConfigurationsApi->get_system_ldap_configurations_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ldapConfigurationId | 
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

[**LdapConfiguration**](LdapConfiguration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | LdapConfiguration |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_system_ldap_configurations_count**
> Count get_system_ldap_configurations_count(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Count of LdapConfiguration

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
    api_instance = connectwise_psa.LdapConfigurationsApi(api_client)
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
        # Get Count of LdapConfiguration
        api_response = api_instance.get_system_ldap_configurations_count(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of LdapConfigurationsApi->get_system_ldap_configurations_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LdapConfigurationsApi->get_system_ldap_configurations_count: %s\n" % e)
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

# **patch_system_ldap_configurations_by_id**
> LdapConfiguration patch_system_ldap_configurations_by_id(id, client_id, patch_operation)

Patch LdapConfiguration

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.ldap_configuration import LdapConfiguration
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
    api_instance = connectwise_psa.LdapConfigurationsApi(api_client)
    id = 56 # int | ldapConfigurationId
    client_id = 'client_id_example' # str | 
    patch_operation = [connectwise_psa.PatchOperation()] # List[PatchOperation] | List of PatchOperation

    try:
        # Patch LdapConfiguration
        api_response = api_instance.patch_system_ldap_configurations_by_id(id, client_id, patch_operation)
        print("The response of LdapConfigurationsApi->patch_system_ldap_configurations_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LdapConfigurationsApi->patch_system_ldap_configurations_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ldapConfigurationId | 
 **client_id** | **str**|  | 
 **patch_operation** | [**List[PatchOperation]**](PatchOperation.md)| List of PatchOperation | 

### Return type

[**LdapConfiguration**](LdapConfiguration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | LdapConfiguration |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_system_ldap_configurations**
> LdapConfiguration post_system_ldap_configurations(client_id, ldap_configuration)

Post LdapConfiguration

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.ldap_configuration import LdapConfiguration
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
    api_instance = connectwise_psa.LdapConfigurationsApi(api_client)
    client_id = 'client_id_example' # str | 
    ldap_configuration = connectwise_psa.LdapConfiguration() # LdapConfiguration | ldapConfiguration

    try:
        # Post LdapConfiguration
        api_response = api_instance.post_system_ldap_configurations(client_id, ldap_configuration)
        print("The response of LdapConfigurationsApi->post_system_ldap_configurations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LdapConfigurationsApi->post_system_ldap_configurations: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**|  | 
 **ldap_configuration** | [**LdapConfiguration**](LdapConfiguration.md)| ldapConfiguration | 

### Return type

[**LdapConfiguration**](LdapConfiguration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | LdapConfiguration |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_system_ldap_configurations_test_link**
> SuccessResponse post_system_ldap_configurations_test_link(client_id, ldap_configuration_test_link)

Post SuccessResponse

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.ldap_configuration_test_link import LdapConfigurationTestLink
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
    api_instance = connectwise_psa.LdapConfigurationsApi(api_client)
    client_id = 'client_id_example' # str | 
    ldap_configuration_test_link = connectwise_psa.LdapConfigurationTestLink() # LdapConfigurationTestLink | server

    try:
        # Post SuccessResponse
        api_response = api_instance.post_system_ldap_configurations_test_link(client_id, ldap_configuration_test_link)
        print("The response of LdapConfigurationsApi->post_system_ldap_configurations_test_link:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LdapConfigurationsApi->post_system_ldap_configurations_test_link: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**|  | 
 **ldap_configuration_test_link** | [**LdapConfigurationTestLink**](LdapConfigurationTestLink.md)| server | 

### Return type

[**SuccessResponse**](SuccessResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | SuccessResponse |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_system_ldap_configurations_by_id**
> LdapConfiguration put_system_ldap_configurations_by_id(id, client_id, ldap_configuration)

Put LdapConfiguration

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.ldap_configuration import LdapConfiguration
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
    api_instance = connectwise_psa.LdapConfigurationsApi(api_client)
    id = 56 # int | ldapConfigurationId
    client_id = 'client_id_example' # str | 
    ldap_configuration = connectwise_psa.LdapConfiguration() # LdapConfiguration | ldapConfiguration

    try:
        # Put LdapConfiguration
        api_response = api_instance.put_system_ldap_configurations_by_id(id, client_id, ldap_configuration)
        print("The response of LdapConfigurationsApi->put_system_ldap_configurations_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LdapConfigurationsApi->put_system_ldap_configurations_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ldapConfigurationId | 
 **client_id** | **str**|  | 
 **ldap_configuration** | [**LdapConfiguration**](LdapConfiguration.md)| ldapConfiguration | 

### Return type

[**LdapConfiguration**](LdapConfiguration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | LdapConfiguration |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

