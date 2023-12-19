# connectwise_psa.ConfigurationStatusesApi

All URIs are relative to *https://aus-api.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_company_configurations_statuses_by_id**](ConfigurationStatusesApi.md#delete_company_configurations_statuses_by_id) | **DELETE** /company/configurations/statuses/{id} | Delete ConfigurationStatus
[**get_company_configurations_statuses**](ConfigurationStatusesApi.md#get_company_configurations_statuses) | **GET** /company/configurations/statuses | Get List of ConfigurationStatus
[**get_company_configurations_statuses_by_id**](ConfigurationStatusesApi.md#get_company_configurations_statuses_by_id) | **GET** /company/configurations/statuses/{id} | Get ConfigurationStatus
[**get_company_configurations_statuses_by_id_usages**](ConfigurationStatusesApi.md#get_company_configurations_statuses_by_id_usages) | **GET** /company/configurations/statuses/{id}/usages | Get List of Usage Count
[**get_company_configurations_statuses_by_id_usages_list**](ConfigurationStatusesApi.md#get_company_configurations_statuses_by_id_usages_list) | **GET** /company/configurations/statuses/{id}/usages/list | Get List of Usage
[**get_company_configurations_statuses_count**](ConfigurationStatusesApi.md#get_company_configurations_statuses_count) | **GET** /company/configurations/statuses/count | Get Count of ConfigurationStatus
[**patch_company_configurations_statuses_by_id**](ConfigurationStatusesApi.md#patch_company_configurations_statuses_by_id) | **PATCH** /company/configurations/statuses/{id} | Patch ConfigurationStatus
[**post_company_configurations_statuses**](ConfigurationStatusesApi.md#post_company_configurations_statuses) | **POST** /company/configurations/statuses | Post ConfigurationStatus
[**put_company_configurations_statuses_by_id**](ConfigurationStatusesApi.md#put_company_configurations_statuses_by_id) | **PUT** /company/configurations/statuses/{id} | Put ConfigurationStatus


# **delete_company_configurations_statuses_by_id**
> delete_company_configurations_statuses_by_id(id, client_id)

Delete ConfigurationStatus

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
    api_instance = connectwise_psa.ConfigurationStatusesApi(api_client)
    id = 56 # int | statusId
    client_id = 'client_id_example' # str | 

    try:
        # Delete ConfigurationStatus
        api_instance.delete_company_configurations_statuses_by_id(id, client_id)
    except Exception as e:
        print("Exception when calling ConfigurationStatusesApi->delete_company_configurations_statuses_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| statusId | 
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

# **get_company_configurations_statuses**
> List[ConfigurationStatus] get_company_configurations_statuses(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of ConfigurationStatus

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.configuration_status import ConfigurationStatus
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
    api_instance = connectwise_psa.ConfigurationStatusesApi(api_client)
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
        # Get List of ConfigurationStatus
        api_response = api_instance.get_company_configurations_statuses(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of ConfigurationStatusesApi->get_company_configurations_statuses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationStatusesApi->get_company_configurations_statuses: %s\n" % e)
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

[**List[ConfigurationStatus]**](ConfigurationStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of ConfigurationStatus |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_company_configurations_statuses_by_id**
> ConfigurationStatus get_company_configurations_statuses_by_id(id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get ConfigurationStatus

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.configuration_status import ConfigurationStatus
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
    api_instance = connectwise_psa.ConfigurationStatusesApi(api_client)
    id = 56 # int | statusId
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
        # Get ConfigurationStatus
        api_response = api_instance.get_company_configurations_statuses_by_id(id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of ConfigurationStatusesApi->get_company_configurations_statuses_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationStatusesApi->get_company_configurations_statuses_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| statusId | 
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

[**ConfigurationStatus**](ConfigurationStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ConfigurationStatus |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_company_configurations_statuses_by_id_usages**
> List[Usage] get_company_configurations_statuses_by_id_usages(id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

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
    api_instance = connectwise_psa.ConfigurationStatusesApi(api_client)
    id = 56 # int | statusId
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
        api_response = api_instance.get_company_configurations_statuses_by_id_usages(id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of ConfigurationStatusesApi->get_company_configurations_statuses_by_id_usages:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationStatusesApi->get_company_configurations_statuses_by_id_usages: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| statusId | 
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

# **get_company_configurations_statuses_by_id_usages_list**
> List[Usage] get_company_configurations_statuses_by_id_usages_list(id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

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
    api_instance = connectwise_psa.ConfigurationStatusesApi(api_client)
    id = 56 # int | statusId
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
        api_response = api_instance.get_company_configurations_statuses_by_id_usages_list(id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of ConfigurationStatusesApi->get_company_configurations_statuses_by_id_usages_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationStatusesApi->get_company_configurations_statuses_by_id_usages_list: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| statusId | 
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

# **get_company_configurations_statuses_count**
> Count get_company_configurations_statuses_count(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Count of ConfigurationStatus

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
    api_instance = connectwise_psa.ConfigurationStatusesApi(api_client)
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
        # Get Count of ConfigurationStatus
        api_response = api_instance.get_company_configurations_statuses_count(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of ConfigurationStatusesApi->get_company_configurations_statuses_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationStatusesApi->get_company_configurations_statuses_count: %s\n" % e)
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

# **patch_company_configurations_statuses_by_id**
> ConfigurationStatus patch_company_configurations_statuses_by_id(id, client_id, patch_operation)

Patch ConfigurationStatus

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.configuration_status import ConfigurationStatus
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
    api_instance = connectwise_psa.ConfigurationStatusesApi(api_client)
    id = 56 # int | statusId
    client_id = 'client_id_example' # str | 
    patch_operation = [connectwise_psa.PatchOperation()] # List[PatchOperation] | List of PatchOperation

    try:
        # Patch ConfigurationStatus
        api_response = api_instance.patch_company_configurations_statuses_by_id(id, client_id, patch_operation)
        print("The response of ConfigurationStatusesApi->patch_company_configurations_statuses_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationStatusesApi->patch_company_configurations_statuses_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| statusId | 
 **client_id** | **str**|  | 
 **patch_operation** | [**List[PatchOperation]**](PatchOperation.md)| List of PatchOperation | 

### Return type

[**ConfigurationStatus**](ConfigurationStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ConfigurationStatus |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_company_configurations_statuses**
> ConfigurationStatus post_company_configurations_statuses(client_id, configuration_status)

Post ConfigurationStatus

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.configuration_status import ConfigurationStatus
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
    api_instance = connectwise_psa.ConfigurationStatusesApi(api_client)
    client_id = 'client_id_example' # str | 
    configuration_status = connectwise_psa.ConfigurationStatus() # ConfigurationStatus | configurationStatus

    try:
        # Post ConfigurationStatus
        api_response = api_instance.post_company_configurations_statuses(client_id, configuration_status)
        print("The response of ConfigurationStatusesApi->post_company_configurations_statuses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationStatusesApi->post_company_configurations_statuses: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**|  | 
 **configuration_status** | [**ConfigurationStatus**](ConfigurationStatus.md)| configurationStatus | 

### Return type

[**ConfigurationStatus**](ConfigurationStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | ConfigurationStatus |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_company_configurations_statuses_by_id**
> ConfigurationStatus put_company_configurations_statuses_by_id(id, client_id, configuration_status)

Put ConfigurationStatus

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.configuration_status import ConfigurationStatus
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
    api_instance = connectwise_psa.ConfigurationStatusesApi(api_client)
    id = 56 # int | statusId
    client_id = 'client_id_example' # str | 
    configuration_status = connectwise_psa.ConfigurationStatus() # ConfigurationStatus | configurationStatus

    try:
        # Put ConfigurationStatus
        api_response = api_instance.put_company_configurations_statuses_by_id(id, client_id, configuration_status)
        print("The response of ConfigurationStatusesApi->put_company_configurations_statuses_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationStatusesApi->put_company_configurations_statuses_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| statusId | 
 **client_id** | **str**|  | 
 **configuration_status** | [**ConfigurationStatus**](ConfigurationStatus.md)| configurationStatus | 

### Return type

[**ConfigurationStatus**](ConfigurationStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ConfigurationStatus |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

