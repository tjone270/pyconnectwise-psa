# connectwise_psa.EPayConfigurationsApi

All URIs are relative to *https://api-aus.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_system_e_pay_configurations_by_id**](EPayConfigurationsApi.md#delete_system_e_pay_configurations_by_id) | **DELETE** /system/ePayConfigurations/{id} | Delete EPayConfiguration
[**get_system_e_pay_configurations**](EPayConfigurationsApi.md#get_system_e_pay_configurations) | **GET** /system/ePayConfigurations | Get List of EPayConfiguration
[**get_system_e_pay_configurations_by_id**](EPayConfigurationsApi.md#get_system_e_pay_configurations_by_id) | **GET** /system/ePayConfigurations/{id} | Get EPayConfiguration
[**get_system_e_pay_configurations_count**](EPayConfigurationsApi.md#get_system_e_pay_configurations_count) | **GET** /system/ePayConfigurations/count | Get Count of EPayConfiguration
[**patch_system_e_pay_configurations_by_id**](EPayConfigurationsApi.md#patch_system_e_pay_configurations_by_id) | **PATCH** /system/ePayConfigurations/{id} | Patch EPayConfiguration
[**post_system_e_pay_configurations**](EPayConfigurationsApi.md#post_system_e_pay_configurations) | **POST** /system/ePayConfigurations | Post EPayConfiguration
[**put_system_e_pay_configurations_by_id**](EPayConfigurationsApi.md#put_system_e_pay_configurations_by_id) | **PUT** /system/ePayConfigurations/{id} | Put EPayConfiguration


# **delete_system_e_pay_configurations_by_id**
> delete_system_e_pay_configurations_by_id(id, client_id)

Delete EPayConfiguration

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
    api_instance = connectwise_psa.EPayConfigurationsApi(api_client)
    id = 56 # int | ePayConfigurationId
    client_id = 'client_id_example' # str | 

    try:
        # Delete EPayConfiguration
        api_instance.delete_system_e_pay_configurations_by_id(id, client_id)
    except Exception as e:
        print("Exception when calling EPayConfigurationsApi->delete_system_e_pay_configurations_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ePayConfigurationId | 
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

# **get_system_e_pay_configurations**
> List[EPayConfiguration] get_system_e_pay_configurations(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of EPayConfiguration

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.e_pay_configuration import EPayConfiguration
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
    api_instance = connectwise_psa.EPayConfigurationsApi(api_client)
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
        # Get List of EPayConfiguration
        api_response = api_instance.get_system_e_pay_configurations(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of EPayConfigurationsApi->get_system_e_pay_configurations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EPayConfigurationsApi->get_system_e_pay_configurations: %s\n" % e)
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

[**List[EPayConfiguration]**](EPayConfiguration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of EPayConfiguration |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_system_e_pay_configurations_by_id**
> EPayConfiguration get_system_e_pay_configurations_by_id(id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get EPayConfiguration

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.e_pay_configuration import EPayConfiguration
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
    api_instance = connectwise_psa.EPayConfigurationsApi(api_client)
    id = 56 # int | ePayConfigurationId
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
        # Get EPayConfiguration
        api_response = api_instance.get_system_e_pay_configurations_by_id(id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of EPayConfigurationsApi->get_system_e_pay_configurations_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EPayConfigurationsApi->get_system_e_pay_configurations_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ePayConfigurationId | 
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

[**EPayConfiguration**](EPayConfiguration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | EPayConfiguration |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_system_e_pay_configurations_count**
> Count get_system_e_pay_configurations_count(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Count of EPayConfiguration

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
    api_instance = connectwise_psa.EPayConfigurationsApi(api_client)
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
        # Get Count of EPayConfiguration
        api_response = api_instance.get_system_e_pay_configurations_count(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of EPayConfigurationsApi->get_system_e_pay_configurations_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EPayConfigurationsApi->get_system_e_pay_configurations_count: %s\n" % e)
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

# **patch_system_e_pay_configurations_by_id**
> EPayConfiguration patch_system_e_pay_configurations_by_id(id, client_id, patch_operation)

Patch EPayConfiguration

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.e_pay_configuration import EPayConfiguration
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
    api_instance = connectwise_psa.EPayConfigurationsApi(api_client)
    id = 56 # int | ePayConfigurationId
    client_id = 'client_id_example' # str | 
    patch_operation = [connectwise_psa.PatchOperation()] # List[PatchOperation] | List of PatchOperation

    try:
        # Patch EPayConfiguration
        api_response = api_instance.patch_system_e_pay_configurations_by_id(id, client_id, patch_operation)
        print("The response of EPayConfigurationsApi->patch_system_e_pay_configurations_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EPayConfigurationsApi->patch_system_e_pay_configurations_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ePayConfigurationId | 
 **client_id** | **str**|  | 
 **patch_operation** | [**List[PatchOperation]**](PatchOperation.md)| List of PatchOperation | 

### Return type

[**EPayConfiguration**](EPayConfiguration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | EPayConfiguration |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_system_e_pay_configurations**
> EPayConfiguration post_system_e_pay_configurations(client_id, e_pay_configuration)

Post EPayConfiguration

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.e_pay_configuration import EPayConfiguration
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
    api_instance = connectwise_psa.EPayConfigurationsApi(api_client)
    client_id = 'client_id_example' # str | 
    e_pay_configuration = connectwise_psa.EPayConfiguration() # EPayConfiguration | ePayConfiguration

    try:
        # Post EPayConfiguration
        api_response = api_instance.post_system_e_pay_configurations(client_id, e_pay_configuration)
        print("The response of EPayConfigurationsApi->post_system_e_pay_configurations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EPayConfigurationsApi->post_system_e_pay_configurations: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**|  | 
 **e_pay_configuration** | [**EPayConfiguration**](EPayConfiguration.md)| ePayConfiguration | 

### Return type

[**EPayConfiguration**](EPayConfiguration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | EPayConfiguration |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_system_e_pay_configurations_by_id**
> EPayConfiguration put_system_e_pay_configurations_by_id(id, client_id, e_pay_configuration)

Put EPayConfiguration

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.e_pay_configuration import EPayConfiguration
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
    api_instance = connectwise_psa.EPayConfigurationsApi(api_client)
    id = 56 # int | ePayConfigurationId
    client_id = 'client_id_example' # str | 
    e_pay_configuration = connectwise_psa.EPayConfiguration() # EPayConfiguration | ePayConfiguration

    try:
        # Put EPayConfiguration
        api_response = api_instance.put_system_e_pay_configurations_by_id(id, client_id, e_pay_configuration)
        print("The response of EPayConfigurationsApi->put_system_e_pay_configurations_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EPayConfigurationsApi->put_system_e_pay_configurations_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ePayConfigurationId | 
 **client_id** | **str**|  | 
 **e_pay_configuration** | [**EPayConfiguration**](EPayConfiguration.md)| ePayConfiguration | 

### Return type

[**EPayConfiguration**](EPayConfiguration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | EPayConfiguration |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

