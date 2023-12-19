# connectwise_psa.PortalConfigurationsApi

All URIs are relative to *https://api-aus.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_company_portal_configurations_by_id**](PortalConfigurationsApi.md#delete_company_portal_configurations_by_id) | **DELETE** /company/portalConfigurations/{id} | Delete PortalConfiguration
[**get_company_portal_configurations**](PortalConfigurationsApi.md#get_company_portal_configurations) | **GET** /company/portalConfigurations | Get List of PortalConfiguration
[**get_company_portal_configurations_by_id**](PortalConfigurationsApi.md#get_company_portal_configurations_by_id) | **GET** /company/portalConfigurations/{id} | Get PortalConfiguration
[**get_company_portal_configurations_count**](PortalConfigurationsApi.md#get_company_portal_configurations_count) | **GET** /company/portalConfigurations/count | Get Count of PortalConfiguration
[**patch_company_portal_configurations_by_id**](PortalConfigurationsApi.md#patch_company_portal_configurations_by_id) | **PATCH** /company/portalConfigurations/{id} | Patch PortalConfiguration
[**post_company_portal_configurations**](PortalConfigurationsApi.md#post_company_portal_configurations) | **POST** /company/portalConfigurations | Post PortalConfiguration
[**post_company_portal_configurations_copy**](PortalConfigurationsApi.md#post_company_portal_configurations_copy) | **POST** /company/portalConfigurations/copy | Post PortalConfiguration
[**put_company_portal_configurations_by_id**](PortalConfigurationsApi.md#put_company_portal_configurations_by_id) | **PUT** /company/portalConfigurations/{id} | Put PortalConfiguration


# **delete_company_portal_configurations_by_id**
> delete_company_portal_configurations_by_id(id, client_id)

Delete PortalConfiguration

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
    api_instance = connectwise_psa.PortalConfigurationsApi(api_client)
    id = 56 # int | portalConfigurationId
    client_id = 'client_id_example' # str | 

    try:
        # Delete PortalConfiguration
        api_instance.delete_company_portal_configurations_by_id(id, client_id)
    except Exception as e:
        print("Exception when calling PortalConfigurationsApi->delete_company_portal_configurations_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| portalConfigurationId | 
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

# **get_company_portal_configurations**
> List[PortalConfiguration] get_company_portal_configurations(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of PortalConfiguration

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.portal_configuration import PortalConfiguration
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
    api_instance = connectwise_psa.PortalConfigurationsApi(api_client)
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
        # Get List of PortalConfiguration
        api_response = api_instance.get_company_portal_configurations(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of PortalConfigurationsApi->get_company_portal_configurations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortalConfigurationsApi->get_company_portal_configurations: %s\n" % e)
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

[**List[PortalConfiguration]**](PortalConfiguration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of PortalConfiguration |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_company_portal_configurations_by_id**
> PortalConfiguration get_company_portal_configurations_by_id(id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get PortalConfiguration

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.portal_configuration import PortalConfiguration
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
    api_instance = connectwise_psa.PortalConfigurationsApi(api_client)
    id = 56 # int | portalConfigurationId
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
        # Get PortalConfiguration
        api_response = api_instance.get_company_portal_configurations_by_id(id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of PortalConfigurationsApi->get_company_portal_configurations_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortalConfigurationsApi->get_company_portal_configurations_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| portalConfigurationId | 
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

[**PortalConfiguration**](PortalConfiguration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | PortalConfiguration |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_company_portal_configurations_count**
> Count get_company_portal_configurations_count(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Count of PortalConfiguration

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
    api_instance = connectwise_psa.PortalConfigurationsApi(api_client)
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
        # Get Count of PortalConfiguration
        api_response = api_instance.get_company_portal_configurations_count(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of PortalConfigurationsApi->get_company_portal_configurations_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortalConfigurationsApi->get_company_portal_configurations_count: %s\n" % e)
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

# **patch_company_portal_configurations_by_id**
> PortalConfiguration patch_company_portal_configurations_by_id(id, client_id, patch_operation)

Patch PortalConfiguration

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.patch_operation import PatchOperation
from connectwise_psa.models.portal_configuration import PortalConfiguration
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
    api_instance = connectwise_psa.PortalConfigurationsApi(api_client)
    id = 56 # int | portalConfigurationId
    client_id = 'client_id_example' # str | 
    patch_operation = [connectwise_psa.PatchOperation()] # List[PatchOperation] | List of PatchOperation

    try:
        # Patch PortalConfiguration
        api_response = api_instance.patch_company_portal_configurations_by_id(id, client_id, patch_operation)
        print("The response of PortalConfigurationsApi->patch_company_portal_configurations_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortalConfigurationsApi->patch_company_portal_configurations_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| portalConfigurationId | 
 **client_id** | **str**|  | 
 **patch_operation** | [**List[PatchOperation]**](PatchOperation.md)| List of PatchOperation | 

### Return type

[**PortalConfiguration**](PortalConfiguration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | PortalConfiguration |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_company_portal_configurations**
> PortalConfiguration post_company_portal_configurations(client_id, portal_configuration)

Post PortalConfiguration

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.portal_configuration import PortalConfiguration
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
    api_instance = connectwise_psa.PortalConfigurationsApi(api_client)
    client_id = 'client_id_example' # str | 
    portal_configuration = connectwise_psa.PortalConfiguration() # PortalConfiguration | portalConfiguration

    try:
        # Post PortalConfiguration
        api_response = api_instance.post_company_portal_configurations(client_id, portal_configuration)
        print("The response of PortalConfigurationsApi->post_company_portal_configurations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortalConfigurationsApi->post_company_portal_configurations: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**|  | 
 **portal_configuration** | [**PortalConfiguration**](PortalConfiguration.md)| portalConfiguration | 

### Return type

[**PortalConfiguration**](PortalConfiguration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | PortalConfiguration |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_company_portal_configurations_copy**
> PortalConfiguration post_company_portal_configurations_copy(client_id, portal_configuration)

Post PortalConfiguration

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.portal_configuration import PortalConfiguration
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
    api_instance = connectwise_psa.PortalConfigurationsApi(api_client)
    client_id = 'client_id_example' # str | 
    portal_configuration = connectwise_psa.PortalConfiguration() # PortalConfiguration | copy

    try:
        # Post PortalConfiguration
        api_response = api_instance.post_company_portal_configurations_copy(client_id, portal_configuration)
        print("The response of PortalConfigurationsApi->post_company_portal_configurations_copy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortalConfigurationsApi->post_company_portal_configurations_copy: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**|  | 
 **portal_configuration** | [**PortalConfiguration**](PortalConfiguration.md)| copy | 

### Return type

[**PortalConfiguration**](PortalConfiguration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | PortalConfiguration |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_company_portal_configurations_by_id**
> PortalConfiguration put_company_portal_configurations_by_id(id, client_id, portal_configuration)

Put PortalConfiguration

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.portal_configuration import PortalConfiguration
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
    api_instance = connectwise_psa.PortalConfigurationsApi(api_client)
    id = 56 # int | portalConfigurationId
    client_id = 'client_id_example' # str | 
    portal_configuration = connectwise_psa.PortalConfiguration() # PortalConfiguration | portalConfiguration

    try:
        # Put PortalConfiguration
        api_response = api_instance.put_company_portal_configurations_by_id(id, client_id, portal_configuration)
        print("The response of PortalConfigurationsApi->put_company_portal_configurations_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortalConfigurationsApi->put_company_portal_configurations_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| portalConfigurationId | 
 **client_id** | **str**|  | 
 **portal_configuration** | [**PortalConfiguration**](PortalConfiguration.md)| portalConfiguration | 

### Return type

[**PortalConfiguration**](PortalConfiguration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | PortalConfiguration |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

