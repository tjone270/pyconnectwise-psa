# connectwise_psa.CustomReportParametersApi

All URIs are relative to *https://api-aus.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_system_custom_reports_by_parent_id_parameters_by_id**](CustomReportParametersApi.md#delete_system_custom_reports_by_parent_id_parameters_by_id) | **DELETE** /system/customReports/{parentId}/parameters/{id} | Delete CustomReportParameter
[**get_system_custom_reports_by_parent_id_parameters**](CustomReportParametersApi.md#get_system_custom_reports_by_parent_id_parameters) | **GET** /system/customReports/{parentId}/parameters | Get List of CustomReportParameter
[**get_system_custom_reports_by_parent_id_parameters_by_id**](CustomReportParametersApi.md#get_system_custom_reports_by_parent_id_parameters_by_id) | **GET** /system/customReports/{parentId}/parameters/{id} | Get CustomReportParameter
[**get_system_custom_reports_by_parent_id_parameters_count**](CustomReportParametersApi.md#get_system_custom_reports_by_parent_id_parameters_count) | **GET** /system/customReports/{parentId}/parameters/count | Get Count of CustomReportParameter
[**patch_system_custom_reports_by_parent_id_parameters_by_id**](CustomReportParametersApi.md#patch_system_custom_reports_by_parent_id_parameters_by_id) | **PATCH** /system/customReports/{parentId}/parameters/{id} | Patch CustomReportParameter
[**post_system_custom_reports_by_parent_id_parameters**](CustomReportParametersApi.md#post_system_custom_reports_by_parent_id_parameters) | **POST** /system/customReports/{parentId}/parameters | Post CustomReportParameter
[**put_system_custom_reports_by_parent_id_parameters_by_id**](CustomReportParametersApi.md#put_system_custom_reports_by_parent_id_parameters_by_id) | **PUT** /system/customReports/{parentId}/parameters/{id} | Put CustomReportParameter


# **delete_system_custom_reports_by_parent_id_parameters_by_id**
> delete_system_custom_reports_by_parent_id_parameters_by_id(id, parent_id, client_id)

Delete CustomReportParameter

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
    api_instance = connectwise_psa.CustomReportParametersApi(api_client)
    id = 56 # int | parameterId
    parent_id = 56 # int | customReportId
    client_id = 'client_id_example' # str | 

    try:
        # Delete CustomReportParameter
        api_instance.delete_system_custom_reports_by_parent_id_parameters_by_id(id, parent_id, client_id)
    except Exception as e:
        print("Exception when calling CustomReportParametersApi->delete_system_custom_reports_by_parent_id_parameters_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| parameterId | 
 **parent_id** | **int**| customReportId | 
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

# **get_system_custom_reports_by_parent_id_parameters**
> List[CustomReportParameter] get_system_custom_reports_by_parent_id_parameters(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of CustomReportParameter

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.custom_report_parameter import CustomReportParameter
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
    api_instance = connectwise_psa.CustomReportParametersApi(api_client)
    parent_id = 56 # int | customReportId
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
        # Get List of CustomReportParameter
        api_response = api_instance.get_system_custom_reports_by_parent_id_parameters(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of CustomReportParametersApi->get_system_custom_reports_by_parent_id_parameters:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomReportParametersApi->get_system_custom_reports_by_parent_id_parameters: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| customReportId | 
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

[**List[CustomReportParameter]**](CustomReportParameter.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of CustomReportParameter |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_system_custom_reports_by_parent_id_parameters_by_id**
> CustomReportParameter get_system_custom_reports_by_parent_id_parameters_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get CustomReportParameter

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.custom_report_parameter import CustomReportParameter
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
    api_instance = connectwise_psa.CustomReportParametersApi(api_client)
    id = 56 # int | parameterId
    parent_id = 56 # int | customReportId
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
        # Get CustomReportParameter
        api_response = api_instance.get_system_custom_reports_by_parent_id_parameters_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of CustomReportParametersApi->get_system_custom_reports_by_parent_id_parameters_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomReportParametersApi->get_system_custom_reports_by_parent_id_parameters_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| parameterId | 
 **parent_id** | **int**| customReportId | 
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

[**CustomReportParameter**](CustomReportParameter.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | CustomReportParameter |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_system_custom_reports_by_parent_id_parameters_count**
> Count get_system_custom_reports_by_parent_id_parameters_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Count of CustomReportParameter

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
    api_instance = connectwise_psa.CustomReportParametersApi(api_client)
    parent_id = 56 # int | customReportId
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
        # Get Count of CustomReportParameter
        api_response = api_instance.get_system_custom_reports_by_parent_id_parameters_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of CustomReportParametersApi->get_system_custom_reports_by_parent_id_parameters_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomReportParametersApi->get_system_custom_reports_by_parent_id_parameters_count: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| customReportId | 
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

# **patch_system_custom_reports_by_parent_id_parameters_by_id**
> CustomReportParameter patch_system_custom_reports_by_parent_id_parameters_by_id(id, parent_id, client_id, patch_operation)

Patch CustomReportParameter

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.custom_report_parameter import CustomReportParameter
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
    api_instance = connectwise_psa.CustomReportParametersApi(api_client)
    id = 56 # int | parameterId
    parent_id = 56 # int | customReportId
    client_id = 'client_id_example' # str | 
    patch_operation = [connectwise_psa.PatchOperation()] # List[PatchOperation] | List of PatchOperation

    try:
        # Patch CustomReportParameter
        api_response = api_instance.patch_system_custom_reports_by_parent_id_parameters_by_id(id, parent_id, client_id, patch_operation)
        print("The response of CustomReportParametersApi->patch_system_custom_reports_by_parent_id_parameters_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomReportParametersApi->patch_system_custom_reports_by_parent_id_parameters_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| parameterId | 
 **parent_id** | **int**| customReportId | 
 **client_id** | **str**|  | 
 **patch_operation** | [**List[PatchOperation]**](PatchOperation.md)| List of PatchOperation | 

### Return type

[**CustomReportParameter**](CustomReportParameter.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | CustomReportParameter |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_system_custom_reports_by_parent_id_parameters**
> CustomReportParameter post_system_custom_reports_by_parent_id_parameters(parent_id, client_id, custom_report_parameter)

Post CustomReportParameter

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.custom_report_parameter import CustomReportParameter
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
    api_instance = connectwise_psa.CustomReportParametersApi(api_client)
    parent_id = 56 # int | customReportId
    client_id = 'client_id_example' # str | 
    custom_report_parameter = connectwise_psa.CustomReportParameter() # CustomReportParameter | customReportParameter

    try:
        # Post CustomReportParameter
        api_response = api_instance.post_system_custom_reports_by_parent_id_parameters(parent_id, client_id, custom_report_parameter)
        print("The response of CustomReportParametersApi->post_system_custom_reports_by_parent_id_parameters:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomReportParametersApi->post_system_custom_reports_by_parent_id_parameters: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| customReportId | 
 **client_id** | **str**|  | 
 **custom_report_parameter** | [**CustomReportParameter**](CustomReportParameter.md)| customReportParameter | 

### Return type

[**CustomReportParameter**](CustomReportParameter.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | CustomReportParameter |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_system_custom_reports_by_parent_id_parameters_by_id**
> CustomReportParameter put_system_custom_reports_by_parent_id_parameters_by_id(id, parent_id, client_id, custom_report_parameter)

Put CustomReportParameter

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.custom_report_parameter import CustomReportParameter
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
    api_instance = connectwise_psa.CustomReportParametersApi(api_client)
    id = 56 # int | parameterId
    parent_id = 56 # int | customReportId
    client_id = 'client_id_example' # str | 
    custom_report_parameter = connectwise_psa.CustomReportParameter() # CustomReportParameter | customReportParameter

    try:
        # Put CustomReportParameter
        api_response = api_instance.put_system_custom_reports_by_parent_id_parameters_by_id(id, parent_id, client_id, custom_report_parameter)
        print("The response of CustomReportParametersApi->put_system_custom_reports_by_parent_id_parameters_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomReportParametersApi->put_system_custom_reports_by_parent_id_parameters_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| parameterId | 
 **parent_id** | **int**| customReportId | 
 **client_id** | **str**|  | 
 **custom_report_parameter** | [**CustomReportParameter**](CustomReportParameter.md)| customReportParameter | 

### Return type

[**CustomReportParameter**](CustomReportParameter.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | CustomReportParameter |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

