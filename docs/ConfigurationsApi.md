# connectwise_psa.ConfigurationsApi

All URIs are relative to *https://api-aus.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_company_configurations_bulk**](ConfigurationsApi.md#delete_company_configurations_bulk) | **DELETE** /company/configurations/bulk | Delete BulkResult
[**delete_company_configurations_by_id**](ConfigurationsApi.md#delete_company_configurations_by_id) | **DELETE** /company/configurations/{id} | Delete Configuration
[**get_company_configurations**](ConfigurationsApi.md#get_company_configurations) | **GET** /company/configurations | Get List of Configuration
[**get_company_configurations_by_id**](ConfigurationsApi.md#get_company_configurations_by_id) | **GET** /company/configurations/{id} | Get Configuration
[**get_company_configurations_count**](ConfigurationsApi.md#get_company_configurations_count) | **GET** /company/configurations/count | Get Count of Configuration
[**patch_company_configurations_by_id**](ConfigurationsApi.md#patch_company_configurations_by_id) | **PATCH** /company/configurations/{id} | Patch Configuration
[**patch_company_configurations_by_id_change_type**](ConfigurationsApi.md#patch_company_configurations_by_id_change_type) | **PATCH** /company/configurations/{id}/changeType | Patch Configuration
[**post_company_configurations**](ConfigurationsApi.md#post_company_configurations) | **POST** /company/configurations | Post Configuration
[**post_company_configurations_bulk**](ConfigurationsApi.md#post_company_configurations_bulk) | **POST** /company/configurations/bulk | Post Configuration
[**put_company_configurations_bulk**](ConfigurationsApi.md#put_company_configurations_bulk) | **PUT** /company/configurations/bulk | Put Configuration
[**put_company_configurations_by_id**](ConfigurationsApi.md#put_company_configurations_by_id) | **PUT** /company/configurations/{id} | Put Configuration


# **delete_company_configurations_bulk**
> BulkResult delete_company_configurations_bulk(client_id)

Delete BulkResult

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.bulk_result import BulkResult
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
    api_instance = connectwise_psa.ConfigurationsApi(api_client)
    client_id = 'client_id_example' # str | 

    try:
        # Delete BulkResult
        api_response = api_instance.delete_company_configurations_bulk(client_id)
        print("The response of ConfigurationsApi->delete_company_configurations_bulk:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationsApi->delete_company_configurations_bulk: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**|  | 

### Return type

[**BulkResult**](BulkResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**207** | BulkResult |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_company_configurations_by_id**
> delete_company_configurations_by_id(id, client_id)

Delete Configuration

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
    api_instance = connectwise_psa.ConfigurationsApi(api_client)
    id = 56 # int | configurationId
    client_id = 'client_id_example' # str | 

    try:
        # Delete Configuration
        api_instance.delete_company_configurations_by_id(id, client_id)
    except Exception as e:
        print("Exception when calling ConfigurationsApi->delete_company_configurations_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| configurationId | 
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

# **get_company_configurations**
> List[CompanyConfiguration] get_company_configurations(client_id, managed_identifier, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of Configuration

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.company_configuration import CompanyConfiguration
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
    api_instance = connectwise_psa.ConfigurationsApi(api_client)
    client_id = 'client_id_example' # str | 
    managed_identifier = 'managed_identifier_example' # str | managedIdentifier
    conditions = 'conditions_example' # str |  (optional)
    child_conditions = 'child_conditions_example' # str |  (optional)
    custom_field_conditions = 'custom_field_conditions_example' # str |  (optional)
    order_by = 'order_by_example' # str |  (optional)
    fields = 'fields_example' # str |  (optional)
    page = 56 # int |  (optional)
    page_size = 56 # int |  (optional)
    page_id = 56 # int |  (optional)

    try:
        # Get List of Configuration
        api_response = api_instance.get_company_configurations(client_id, managed_identifier, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of ConfigurationsApi->get_company_configurations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationsApi->get_company_configurations: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**|  | 
 **managed_identifier** | **str**| managedIdentifier | 
 **conditions** | **str**|  | [optional] 
 **child_conditions** | **str**|  | [optional] 
 **custom_field_conditions** | **str**|  | [optional] 
 **order_by** | **str**|  | [optional] 
 **fields** | **str**|  | [optional] 
 **page** | **int**|  | [optional] 
 **page_size** | **int**|  | [optional] 
 **page_id** | **int**|  | [optional] 

### Return type

[**List[CompanyConfiguration]**](CompanyConfiguration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of Configuration |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_company_configurations_by_id**
> CompanyConfiguration get_company_configurations_by_id(id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Configuration

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.company_configuration import CompanyConfiguration
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
    api_instance = connectwise_psa.ConfigurationsApi(api_client)
    id = 56 # int | configurationId
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
        # Get Configuration
        api_response = api_instance.get_company_configurations_by_id(id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of ConfigurationsApi->get_company_configurations_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationsApi->get_company_configurations_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| configurationId | 
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

[**CompanyConfiguration**](CompanyConfiguration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Configuration |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_company_configurations_count**
> Count get_company_configurations_count(client_id, managed_identifier, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Count of Configuration

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
    api_instance = connectwise_psa.ConfigurationsApi(api_client)
    client_id = 'client_id_example' # str | 
    managed_identifier = 'managed_identifier_example' # str | managedIdentifier
    conditions = 'conditions_example' # str |  (optional)
    child_conditions = 'child_conditions_example' # str |  (optional)
    custom_field_conditions = 'custom_field_conditions_example' # str |  (optional)
    order_by = 'order_by_example' # str |  (optional)
    fields = 'fields_example' # str |  (optional)
    page = 56 # int |  (optional)
    page_size = 56 # int |  (optional)
    page_id = 56 # int |  (optional)

    try:
        # Get Count of Configuration
        api_response = api_instance.get_company_configurations_count(client_id, managed_identifier, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of ConfigurationsApi->get_company_configurations_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationsApi->get_company_configurations_count: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**|  | 
 **managed_identifier** | **str**| managedIdentifier | 
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

# **patch_company_configurations_by_id**
> CompanyConfiguration patch_company_configurations_by_id(id, client_id, patch_operation, managed_information=managed_information)

Patch Configuration

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.company_configuration import CompanyConfiguration
from connectwise_psa.models.managed_information import ManagedInformation
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
    api_instance = connectwise_psa.ConfigurationsApi(api_client)
    id = 56 # int | configurationId
    client_id = 'client_id_example' # str | 
    patch_operation = [connectwise_psa.PatchOperation()] # List[PatchOperation] | List of PatchOperation
    managed_information = connectwise_psa.ManagedInformation() # ManagedInformation | managedInformation (optional)

    try:
        # Patch Configuration
        api_response = api_instance.patch_company_configurations_by_id(id, client_id, patch_operation, managed_information=managed_information)
        print("The response of ConfigurationsApi->patch_company_configurations_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationsApi->patch_company_configurations_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| configurationId | 
 **client_id** | **str**|  | 
 **patch_operation** | [**List[PatchOperation]**](PatchOperation.md)| List of PatchOperation | 
 **managed_information** | [**ManagedInformation**](.md)| managedInformation | [optional] 

### Return type

[**CompanyConfiguration**](CompanyConfiguration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Configuration |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_company_configurations_by_id_change_type**
> CompanyConfiguration patch_company_configurations_by_id_change_type(id, client_id, patch_operation)

Patch Configuration

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.company_configuration import CompanyConfiguration
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
    api_instance = connectwise_psa.ConfigurationsApi(api_client)
    id = 56 # int | configurationId
    client_id = 'client_id_example' # str | 
    patch_operation = [connectwise_psa.PatchOperation()] # List[PatchOperation] | List of PatchOperation

    try:
        # Patch Configuration
        api_response = api_instance.patch_company_configurations_by_id_change_type(id, client_id, patch_operation)
        print("The response of ConfigurationsApi->patch_company_configurations_by_id_change_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationsApi->patch_company_configurations_by_id_change_type: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| configurationId | 
 **client_id** | **str**|  | 
 **patch_operation** | [**List[PatchOperation]**](PatchOperation.md)| List of PatchOperation | 

### Return type

[**CompanyConfiguration**](CompanyConfiguration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Configuration |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_company_configurations**
> CompanyConfiguration post_company_configurations(client_id, company_configuration, managed_information=managed_information)

Post Configuration

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.company_configuration import CompanyConfiguration
from connectwise_psa.models.managed_information import ManagedInformation
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
    api_instance = connectwise_psa.ConfigurationsApi(api_client)
    client_id = 'client_id_example' # str | 
    company_configuration = connectwise_psa.CompanyConfiguration() # CompanyConfiguration | configuration
    managed_information = connectwise_psa.ManagedInformation() # ManagedInformation | managedInformation (optional)

    try:
        # Post Configuration
        api_response = api_instance.post_company_configurations(client_id, company_configuration, managed_information=managed_information)
        print("The response of ConfigurationsApi->post_company_configurations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationsApi->post_company_configurations: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**|  | 
 **company_configuration** | [**CompanyConfiguration**](CompanyConfiguration.md)| configuration | 
 **managed_information** | [**ManagedInformation**](.md)| managedInformation | [optional] 

### Return type

[**CompanyConfiguration**](CompanyConfiguration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Configuration |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_company_configurations_bulk**
> CompanyConfiguration post_company_configurations_bulk(client_id, company_configuration)

Post Configuration

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.company_configuration import CompanyConfiguration
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
    api_instance = connectwise_psa.ConfigurationsApi(api_client)
    client_id = 'client_id_example' # str | 
    company_configuration = [connectwise_psa.CompanyConfiguration()] # List[CompanyConfiguration] | List of Configuration

    try:
        # Post Configuration
        api_response = api_instance.post_company_configurations_bulk(client_id, company_configuration)
        print("The response of ConfigurationsApi->post_company_configurations_bulk:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationsApi->post_company_configurations_bulk: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**|  | 
 **company_configuration** | [**List[CompanyConfiguration]**](CompanyConfiguration.md)| List of Configuration | 

### Return type

[**CompanyConfiguration**](CompanyConfiguration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**207** | Configuration |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_company_configurations_bulk**
> CompanyConfiguration put_company_configurations_bulk(client_id, company_configuration)

Put Configuration

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.company_configuration import CompanyConfiguration
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
    api_instance = connectwise_psa.ConfigurationsApi(api_client)
    client_id = 'client_id_example' # str | 
    company_configuration = [connectwise_psa.CompanyConfiguration()] # List[CompanyConfiguration] | List of Configuration

    try:
        # Put Configuration
        api_response = api_instance.put_company_configurations_bulk(client_id, company_configuration)
        print("The response of ConfigurationsApi->put_company_configurations_bulk:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationsApi->put_company_configurations_bulk: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**|  | 
 **company_configuration** | [**List[CompanyConfiguration]**](CompanyConfiguration.md)| List of Configuration | 

### Return type

[**CompanyConfiguration**](CompanyConfiguration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**207** | Configuration |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_company_configurations_by_id**
> CompanyConfiguration put_company_configurations_by_id(id, client_id, company_configuration, managed_information=managed_information)

Put Configuration

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.company_configuration import CompanyConfiguration
from connectwise_psa.models.managed_information import ManagedInformation
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
    api_instance = connectwise_psa.ConfigurationsApi(api_client)
    id = 56 # int | configurationId
    client_id = 'client_id_example' # str | 
    company_configuration = connectwise_psa.CompanyConfiguration() # CompanyConfiguration | configuration
    managed_information = connectwise_psa.ManagedInformation() # ManagedInformation | managedInformation (optional)

    try:
        # Put Configuration
        api_response = api_instance.put_company_configurations_by_id(id, client_id, company_configuration, managed_information=managed_information)
        print("The response of ConfigurationsApi->put_company_configurations_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationsApi->put_company_configurations_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| configurationId | 
 **client_id** | **str**|  | 
 **company_configuration** | [**CompanyConfiguration**](CompanyConfiguration.md)| configuration | 
 **managed_information** | [**ManagedInformation**](.md)| managedInformation | [optional] 

### Return type

[**CompanyConfiguration**](CompanyConfiguration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Configuration |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

