# connectwise_psa.WorkRoleLocationsApi

All URIs are relative to *https://aus-api.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_time_work_roles_by_parent_id_locations_by_id**](WorkRoleLocationsApi.md#delete_time_work_roles_by_parent_id_locations_by_id) | **DELETE** /time/workRoles/{parentId}/locations/{id} | Delete WorkRoleLocation
[**get_time_work_roles_by_parent_id_locations**](WorkRoleLocationsApi.md#get_time_work_roles_by_parent_id_locations) | **GET** /time/workRoles/{parentId}/locations | Get List of WorkRoleLocation
[**get_time_work_roles_by_parent_id_locations_by_id**](WorkRoleLocationsApi.md#get_time_work_roles_by_parent_id_locations_by_id) | **GET** /time/workRoles/{parentId}/locations/{id} | Get WorkRoleLocation
[**get_time_work_roles_by_parent_id_locations_count**](WorkRoleLocationsApi.md#get_time_work_roles_by_parent_id_locations_count) | **GET** /time/workRoles/{parentId}/locations/count | Get Count of WorkRoleLocation
[**patch_time_work_roles_by_parent_id_locations_by_id**](WorkRoleLocationsApi.md#patch_time_work_roles_by_parent_id_locations_by_id) | **PATCH** /time/workRoles/{parentId}/locations/{id} | Patch WorkRoleLocation
[**post_time_work_roles_by_parent_id_locations**](WorkRoleLocationsApi.md#post_time_work_roles_by_parent_id_locations) | **POST** /time/workRoles/{parentId}/locations | Post WorkRoleLocation
[**put_time_work_roles_by_parent_id_locations_by_id**](WorkRoleLocationsApi.md#put_time_work_roles_by_parent_id_locations_by_id) | **PUT** /time/workRoles/{parentId}/locations/{id} | Put WorkRoleLocation


# **delete_time_work_roles_by_parent_id_locations_by_id**
> delete_time_work_roles_by_parent_id_locations_by_id(id, parent_id, client_id)

Delete WorkRoleLocation

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
    api_instance = connectwise_psa.WorkRoleLocationsApi(api_client)
    id = 56 # int | locationId
    parent_id = 56 # int | workRoleId
    client_id = 'client_id_example' # str | 

    try:
        # Delete WorkRoleLocation
        api_instance.delete_time_work_roles_by_parent_id_locations_by_id(id, parent_id, client_id)
    except Exception as e:
        print("Exception when calling WorkRoleLocationsApi->delete_time_work_roles_by_parent_id_locations_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| locationId | 
 **parent_id** | **int**| workRoleId | 
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

# **get_time_work_roles_by_parent_id_locations**
> List[WorkRoleLocation] get_time_work_roles_by_parent_id_locations(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of WorkRoleLocation

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.work_role_location import WorkRoleLocation
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
    api_instance = connectwise_psa.WorkRoleLocationsApi(api_client)
    parent_id = 56 # int | workRoleId
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
        # Get List of WorkRoleLocation
        api_response = api_instance.get_time_work_roles_by_parent_id_locations(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of WorkRoleLocationsApi->get_time_work_roles_by_parent_id_locations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkRoleLocationsApi->get_time_work_roles_by_parent_id_locations: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| workRoleId | 
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

[**List[WorkRoleLocation]**](WorkRoleLocation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of WorkRoleLocation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_time_work_roles_by_parent_id_locations_by_id**
> WorkRoleLocation get_time_work_roles_by_parent_id_locations_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get WorkRoleLocation

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.work_role_location import WorkRoleLocation
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
    api_instance = connectwise_psa.WorkRoleLocationsApi(api_client)
    id = 56 # int | locationId
    parent_id = 56 # int | workRoleId
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
        # Get WorkRoleLocation
        api_response = api_instance.get_time_work_roles_by_parent_id_locations_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of WorkRoleLocationsApi->get_time_work_roles_by_parent_id_locations_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkRoleLocationsApi->get_time_work_roles_by_parent_id_locations_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| locationId | 
 **parent_id** | **int**| workRoleId | 
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

[**WorkRoleLocation**](WorkRoleLocation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | WorkRoleLocation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_time_work_roles_by_parent_id_locations_count**
> Count get_time_work_roles_by_parent_id_locations_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Count of WorkRoleLocation

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
    api_instance = connectwise_psa.WorkRoleLocationsApi(api_client)
    parent_id = 56 # int | workRoleId
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
        # Get Count of WorkRoleLocation
        api_response = api_instance.get_time_work_roles_by_parent_id_locations_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of WorkRoleLocationsApi->get_time_work_roles_by_parent_id_locations_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkRoleLocationsApi->get_time_work_roles_by_parent_id_locations_count: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| workRoleId | 
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

# **patch_time_work_roles_by_parent_id_locations_by_id**
> WorkRoleLocation patch_time_work_roles_by_parent_id_locations_by_id(id, parent_id, client_id, patch_operation)

Patch WorkRoleLocation

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.patch_operation import PatchOperation
from connectwise_psa.models.work_role_location import WorkRoleLocation
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
    api_instance = connectwise_psa.WorkRoleLocationsApi(api_client)
    id = 56 # int | locationId
    parent_id = 56 # int | workRoleId
    client_id = 'client_id_example' # str | 
    patch_operation = [connectwise_psa.PatchOperation()] # List[PatchOperation] | List of PatchOperation

    try:
        # Patch WorkRoleLocation
        api_response = api_instance.patch_time_work_roles_by_parent_id_locations_by_id(id, parent_id, client_id, patch_operation)
        print("The response of WorkRoleLocationsApi->patch_time_work_roles_by_parent_id_locations_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkRoleLocationsApi->patch_time_work_roles_by_parent_id_locations_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| locationId | 
 **parent_id** | **int**| workRoleId | 
 **client_id** | **str**|  | 
 **patch_operation** | [**List[PatchOperation]**](PatchOperation.md)| List of PatchOperation | 

### Return type

[**WorkRoleLocation**](WorkRoleLocation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | WorkRoleLocation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_time_work_roles_by_parent_id_locations**
> WorkRoleLocation post_time_work_roles_by_parent_id_locations(parent_id, client_id, work_role_location)

Post WorkRoleLocation

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.work_role_location import WorkRoleLocation
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
    api_instance = connectwise_psa.WorkRoleLocationsApi(api_client)
    parent_id = 56 # int | workRoleId
    client_id = 'client_id_example' # str | 
    work_role_location = connectwise_psa.WorkRoleLocation() # WorkRoleLocation | workRoleLocation

    try:
        # Post WorkRoleLocation
        api_response = api_instance.post_time_work_roles_by_parent_id_locations(parent_id, client_id, work_role_location)
        print("The response of WorkRoleLocationsApi->post_time_work_roles_by_parent_id_locations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkRoleLocationsApi->post_time_work_roles_by_parent_id_locations: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| workRoleId | 
 **client_id** | **str**|  | 
 **work_role_location** | [**WorkRoleLocation**](WorkRoleLocation.md)| workRoleLocation | 

### Return type

[**WorkRoleLocation**](WorkRoleLocation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | WorkRoleLocation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_time_work_roles_by_parent_id_locations_by_id**
> WorkRoleLocation put_time_work_roles_by_parent_id_locations_by_id(id, parent_id, client_id, work_role_location)

Put WorkRoleLocation

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.work_role_location import WorkRoleLocation
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
    api_instance = connectwise_psa.WorkRoleLocationsApi(api_client)
    id = 56 # int | locationId
    parent_id = 56 # int | workRoleId
    client_id = 'client_id_example' # str | 
    work_role_location = connectwise_psa.WorkRoleLocation() # WorkRoleLocation | workRoleLocation

    try:
        # Put WorkRoleLocation
        api_response = api_instance.put_time_work_roles_by_parent_id_locations_by_id(id, parent_id, client_id, work_role_location)
        print("The response of WorkRoleLocationsApi->put_time_work_roles_by_parent_id_locations_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkRoleLocationsApi->put_time_work_roles_by_parent_id_locations_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| locationId | 
 **parent_id** | **int**| workRoleId | 
 **client_id** | **str**|  | 
 **work_role_location** | [**WorkRoleLocation**](WorkRoleLocation.md)| workRoleLocation | 

### Return type

[**WorkRoleLocation**](WorkRoleLocation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | WorkRoleLocation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

