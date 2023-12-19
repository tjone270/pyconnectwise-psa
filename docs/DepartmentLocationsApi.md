# connectwise_psa.DepartmentLocationsApi

All URIs are relative to *https://aus-api.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_system_departments_by_parent_id_locations_by_id**](DepartmentLocationsApi.md#delete_system_departments_by_parent_id_locations_by_id) | **DELETE** /system/departments/{parentId}/locations/{id} | Delete DepartmentLocation
[**get_system_departments_by_parent_id_locations**](DepartmentLocationsApi.md#get_system_departments_by_parent_id_locations) | **GET** /system/departments/{parentId}/locations | Get List of DepartmentLocation
[**get_system_departments_by_parent_id_locations_by_id**](DepartmentLocationsApi.md#get_system_departments_by_parent_id_locations_by_id) | **GET** /system/departments/{parentId}/locations/{id} | Get DepartmentLocation
[**get_system_departments_by_parent_id_locations_count**](DepartmentLocationsApi.md#get_system_departments_by_parent_id_locations_count) | **GET** /system/departments/{parentId}/locations/count | Get Count of DepartmentLocation
[**patch_system_departments_by_parent_id_locations_by_id**](DepartmentLocationsApi.md#patch_system_departments_by_parent_id_locations_by_id) | **PATCH** /system/departments/{parentId}/locations/{id} | Patch DepartmentLocation
[**post_system_departments_by_parent_id_locations**](DepartmentLocationsApi.md#post_system_departments_by_parent_id_locations) | **POST** /system/departments/{parentId}/locations | Post DepartmentLocation
[**put_system_departments_by_parent_id_locations_by_id**](DepartmentLocationsApi.md#put_system_departments_by_parent_id_locations_by_id) | **PUT** /system/departments/{parentId}/locations/{id} | Put DepartmentLocation


# **delete_system_departments_by_parent_id_locations_by_id**
> delete_system_departments_by_parent_id_locations_by_id(id, parent_id, client_id)

Delete DepartmentLocation

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
    api_instance = connectwise_psa.DepartmentLocationsApi(api_client)
    id = 56 # int | locationId
    parent_id = 56 # int | departmentId
    client_id = 'client_id_example' # str | 

    try:
        # Delete DepartmentLocation
        api_instance.delete_system_departments_by_parent_id_locations_by_id(id, parent_id, client_id)
    except Exception as e:
        print("Exception when calling DepartmentLocationsApi->delete_system_departments_by_parent_id_locations_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| locationId | 
 **parent_id** | **int**| departmentId | 
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

# **get_system_departments_by_parent_id_locations**
> List[DepartmentLocation] get_system_departments_by_parent_id_locations(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of DepartmentLocation

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.department_location import DepartmentLocation
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
    api_instance = connectwise_psa.DepartmentLocationsApi(api_client)
    parent_id = 56 # int | departmentId
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
        # Get List of DepartmentLocation
        api_response = api_instance.get_system_departments_by_parent_id_locations(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of DepartmentLocationsApi->get_system_departments_by_parent_id_locations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DepartmentLocationsApi->get_system_departments_by_parent_id_locations: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| departmentId | 
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

[**List[DepartmentLocation]**](DepartmentLocation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of DepartmentLocation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_system_departments_by_parent_id_locations_by_id**
> DepartmentLocation get_system_departments_by_parent_id_locations_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get DepartmentLocation

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.department_location import DepartmentLocation
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
    api_instance = connectwise_psa.DepartmentLocationsApi(api_client)
    id = 56 # int | locationId
    parent_id = 56 # int | departmentId
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
        # Get DepartmentLocation
        api_response = api_instance.get_system_departments_by_parent_id_locations_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of DepartmentLocationsApi->get_system_departments_by_parent_id_locations_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DepartmentLocationsApi->get_system_departments_by_parent_id_locations_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| locationId | 
 **parent_id** | **int**| departmentId | 
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

[**DepartmentLocation**](DepartmentLocation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | DepartmentLocation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_system_departments_by_parent_id_locations_count**
> Count get_system_departments_by_parent_id_locations_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Count of DepartmentLocation

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
    api_instance = connectwise_psa.DepartmentLocationsApi(api_client)
    parent_id = 56 # int | departmentId
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
        # Get Count of DepartmentLocation
        api_response = api_instance.get_system_departments_by_parent_id_locations_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of DepartmentLocationsApi->get_system_departments_by_parent_id_locations_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DepartmentLocationsApi->get_system_departments_by_parent_id_locations_count: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| departmentId | 
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

# **patch_system_departments_by_parent_id_locations_by_id**
> DepartmentLocation patch_system_departments_by_parent_id_locations_by_id(id, parent_id, client_id, patch_operation)

Patch DepartmentLocation

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.department_location import DepartmentLocation
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
    api_instance = connectwise_psa.DepartmentLocationsApi(api_client)
    id = 56 # int | locationId
    parent_id = 56 # int | departmentId
    client_id = 'client_id_example' # str | 
    patch_operation = [connectwise_psa.PatchOperation()] # List[PatchOperation] | List of PatchOperation

    try:
        # Patch DepartmentLocation
        api_response = api_instance.patch_system_departments_by_parent_id_locations_by_id(id, parent_id, client_id, patch_operation)
        print("The response of DepartmentLocationsApi->patch_system_departments_by_parent_id_locations_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DepartmentLocationsApi->patch_system_departments_by_parent_id_locations_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| locationId | 
 **parent_id** | **int**| departmentId | 
 **client_id** | **str**|  | 
 **patch_operation** | [**List[PatchOperation]**](PatchOperation.md)| List of PatchOperation | 

### Return type

[**DepartmentLocation**](DepartmentLocation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | DepartmentLocation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_system_departments_by_parent_id_locations**
> DepartmentLocation post_system_departments_by_parent_id_locations(parent_id, client_id, department_location)

Post DepartmentLocation

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.department_location import DepartmentLocation
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
    api_instance = connectwise_psa.DepartmentLocationsApi(api_client)
    parent_id = 56 # int | departmentId
    client_id = 'client_id_example' # str | 
    department_location = connectwise_psa.DepartmentLocation() # DepartmentLocation | departmentLocation

    try:
        # Post DepartmentLocation
        api_response = api_instance.post_system_departments_by_parent_id_locations(parent_id, client_id, department_location)
        print("The response of DepartmentLocationsApi->post_system_departments_by_parent_id_locations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DepartmentLocationsApi->post_system_departments_by_parent_id_locations: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| departmentId | 
 **client_id** | **str**|  | 
 **department_location** | [**DepartmentLocation**](DepartmentLocation.md)| departmentLocation | 

### Return type

[**DepartmentLocation**](DepartmentLocation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | DepartmentLocation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_system_departments_by_parent_id_locations_by_id**
> DepartmentLocation put_system_departments_by_parent_id_locations_by_id(id, parent_id, client_id, department_location)

Put DepartmentLocation

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.department_location import DepartmentLocation
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
    api_instance = connectwise_psa.DepartmentLocationsApi(api_client)
    id = 56 # int | locationId
    parent_id = 56 # int | departmentId
    client_id = 'client_id_example' # str | 
    department_location = connectwise_psa.DepartmentLocation() # DepartmentLocation | departmentLocation

    try:
        # Put DepartmentLocation
        api_response = api_instance.put_system_departments_by_parent_id_locations_by_id(id, parent_id, client_id, department_location)
        print("The response of DepartmentLocationsApi->put_system_departments_by_parent_id_locations_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DepartmentLocationsApi->put_system_departments_by_parent_id_locations_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| locationId | 
 **parent_id** | **int**| departmentId | 
 **client_id** | **str**|  | 
 **department_location** | [**DepartmentLocation**](DepartmentLocation.md)| departmentLocation | 

### Return type

[**DepartmentLocation**](DepartmentLocation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | DepartmentLocation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

