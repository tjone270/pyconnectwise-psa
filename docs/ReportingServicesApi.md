# connectwise_psa.ReportingServicesApi

All URIs are relative to *https://api-aus.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_system_mycompany_reporting_services**](ReportingServicesApi.md#get_system_mycompany_reporting_services) | **GET** /system/mycompany/reportingServices | Get List of ReportingService
[**get_system_mycompany_reporting_services_by_id**](ReportingServicesApi.md#get_system_mycompany_reporting_services_by_id) | **GET** /system/mycompany/reportingServices/{id} | Get ReportingService
[**patch_system_mycompany_reporting_services_by_id**](ReportingServicesApi.md#patch_system_mycompany_reporting_services_by_id) | **PATCH** /system/mycompany/reportingServices/{id} | Patch ReportingService
[**post_system_mycompany_reporting_services_by_id_test_connection**](ReportingServicesApi.md#post_system_mycompany_reporting_services_by_id_test_connection) | **POST** /system/mycompany/reportingServices/{id}/testConnection | Post SuccessResponse
[**put_system_mycompany_reporting_services_by_id**](ReportingServicesApi.md#put_system_mycompany_reporting_services_by_id) | **PUT** /system/mycompany/reportingServices/{id} | Put ReportingService


# **get_system_mycompany_reporting_services**
> List[ReportingService] get_system_mycompany_reporting_services(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of ReportingService

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.reporting_service import ReportingService
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
    api_instance = connectwise_psa.ReportingServicesApi(api_client)
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
        # Get List of ReportingService
        api_response = api_instance.get_system_mycompany_reporting_services(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of ReportingServicesApi->get_system_mycompany_reporting_services:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportingServicesApi->get_system_mycompany_reporting_services: %s\n" % e)
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

[**List[ReportingService]**](ReportingService.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of ReportingService |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_system_mycompany_reporting_services_by_id**
> ReportingService get_system_mycompany_reporting_services_by_id(id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get ReportingService

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.reporting_service import ReportingService
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
    api_instance = connectwise_psa.ReportingServicesApi(api_client)
    id = 56 # int | reportingServiceId
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
        # Get ReportingService
        api_response = api_instance.get_system_mycompany_reporting_services_by_id(id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of ReportingServicesApi->get_system_mycompany_reporting_services_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportingServicesApi->get_system_mycompany_reporting_services_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| reportingServiceId | 
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

[**ReportingService**](ReportingService.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ReportingService |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_system_mycompany_reporting_services_by_id**
> ReportingService patch_system_mycompany_reporting_services_by_id(id, client_id, patch_operation)

Patch ReportingService

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.patch_operation import PatchOperation
from connectwise_psa.models.reporting_service import ReportingService
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
    api_instance = connectwise_psa.ReportingServicesApi(api_client)
    id = 56 # int | reportingServiceId
    client_id = 'client_id_example' # str | 
    patch_operation = [connectwise_psa.PatchOperation()] # List[PatchOperation] | List of PatchOperation

    try:
        # Patch ReportingService
        api_response = api_instance.patch_system_mycompany_reporting_services_by_id(id, client_id, patch_operation)
        print("The response of ReportingServicesApi->patch_system_mycompany_reporting_services_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportingServicesApi->patch_system_mycompany_reporting_services_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| reportingServiceId | 
 **client_id** | **str**|  | 
 **patch_operation** | [**List[PatchOperation]**](PatchOperation.md)| List of PatchOperation | 

### Return type

[**ReportingService**](ReportingService.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ReportingService |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_system_mycompany_reporting_services_by_id_test_connection**
> SuccessResponse post_system_mycompany_reporting_services_by_id_test_connection(id, client_id)

Post SuccessResponse

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
    api_instance = connectwise_psa.ReportingServicesApi(api_client)
    id = 56 # int | reportingServiceId
    client_id = 'client_id_example' # str | 

    try:
        # Post SuccessResponse
        api_response = api_instance.post_system_mycompany_reporting_services_by_id_test_connection(id, client_id)
        print("The response of ReportingServicesApi->post_system_mycompany_reporting_services_by_id_test_connection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportingServicesApi->post_system_mycompany_reporting_services_by_id_test_connection: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| reportingServiceId | 
 **client_id** | **str**|  | 

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

# **put_system_mycompany_reporting_services_by_id**
> ReportingService put_system_mycompany_reporting_services_by_id(id, client_id, reporting_service)

Put ReportingService

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.reporting_service import ReportingService
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
    api_instance = connectwise_psa.ReportingServicesApi(api_client)
    id = 56 # int | reportingServiceId
    client_id = 'client_id_example' # str | 
    reporting_service = connectwise_psa.ReportingService() # ReportingService | service

    try:
        # Put ReportingService
        api_response = api_instance.put_system_mycompany_reporting_services_by_id(id, client_id, reporting_service)
        print("The response of ReportingServicesApi->put_system_mycompany_reporting_services_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportingServicesApi->put_system_mycompany_reporting_services_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| reportingServiceId | 
 **client_id** | **str**|  | 
 **reporting_service** | [**ReportingService**](ReportingService.md)| service | 

### Return type

[**ReportingService**](ReportingService.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ReportingService |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

