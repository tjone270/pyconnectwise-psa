# connectwise_psa.AllowedFileTypeApi

All URIs are relative to *https://aus-api.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_system_allowedfiletypes_by_id**](AllowedFileTypeApi.md#delete_system_allowedfiletypes_by_id) | **DELETE** /system/allowedfiletypes/{id} | Delete AllowedFileType
[**get_system_allowedfiletypes**](AllowedFileTypeApi.md#get_system_allowedfiletypes) | **GET** /system/allowedfiletypes/ | Get List of AllowedFileType
[**get_system_allowedfiletypes_by_id**](AllowedFileTypeApi.md#get_system_allowedfiletypes_by_id) | **GET** /system/allowedfiletypes/{id} | Get AllowedFileType
[**get_system_allowedfiletypes_count**](AllowedFileTypeApi.md#get_system_allowedfiletypes_count) | **GET** /system/allowedfiletypes/count | Get Count of AllowedFileType
[**patch_system_allowedfiletypes_by_id**](AllowedFileTypeApi.md#patch_system_allowedfiletypes_by_id) | **PATCH** /system/allowedfiletypes/{id} | Patch AllowedFileType
[**post_system_allowed_file_types**](AllowedFileTypeApi.md#post_system_allowed_file_types) | **POST** /system/AllowedFileTypes/ | Post AllowedFileType
[**put_system_allowedfiletypes_by_id**](AllowedFileTypeApi.md#put_system_allowedfiletypes_by_id) | **PUT** /system/allowedfiletypes/{id} | Put AllowedFileType


# **delete_system_allowedfiletypes_by_id**
> delete_system_allowedfiletypes_by_id(id, client_id)

Delete AllowedFileType

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
    api_instance = connectwise_psa.AllowedFileTypeApi(api_client)
    id = 56 # int | allowedfiletypeId
    client_id = 'client_id_example' # str | 

    try:
        # Delete AllowedFileType
        api_instance.delete_system_allowedfiletypes_by_id(id, client_id)
    except Exception as e:
        print("Exception when calling AllowedFileTypeApi->delete_system_allowedfiletypes_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| allowedfiletypeId | 
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

# **get_system_allowedfiletypes**
> List[AllowedFileType] get_system_allowedfiletypes(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of AllowedFileType

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.allowed_file_type import AllowedFileType
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
    api_instance = connectwise_psa.AllowedFileTypeApi(api_client)
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
        # Get List of AllowedFileType
        api_response = api_instance.get_system_allowedfiletypes(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of AllowedFileTypeApi->get_system_allowedfiletypes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AllowedFileTypeApi->get_system_allowedfiletypes: %s\n" % e)
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

[**List[AllowedFileType]**](AllowedFileType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of AllowedFileType |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_system_allowedfiletypes_by_id**
> AllowedFileType get_system_allowedfiletypes_by_id(id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get AllowedFileType

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.allowed_file_type import AllowedFileType
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
    api_instance = connectwise_psa.AllowedFileTypeApi(api_client)
    id = 56 # int | allowedfiletypeId
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
        # Get AllowedFileType
        api_response = api_instance.get_system_allowedfiletypes_by_id(id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of AllowedFileTypeApi->get_system_allowedfiletypes_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AllowedFileTypeApi->get_system_allowedfiletypes_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| allowedfiletypeId | 
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

[**AllowedFileType**](AllowedFileType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | AllowedFileType |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_system_allowedfiletypes_count**
> Count get_system_allowedfiletypes_count(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Count of AllowedFileType

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
    api_instance = connectwise_psa.AllowedFileTypeApi(api_client)
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
        # Get Count of AllowedFileType
        api_response = api_instance.get_system_allowedfiletypes_count(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of AllowedFileTypeApi->get_system_allowedfiletypes_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AllowedFileTypeApi->get_system_allowedfiletypes_count: %s\n" % e)
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

# **patch_system_allowedfiletypes_by_id**
> AllowedFileType patch_system_allowedfiletypes_by_id(id, client_id, patch_operation)

Patch AllowedFileType

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.allowed_file_type import AllowedFileType
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
    api_instance = connectwise_psa.AllowedFileTypeApi(api_client)
    id = 56 # int | allowedFileTypesId
    client_id = 'client_id_example' # str | 
    patch_operation = [connectwise_psa.PatchOperation()] # List[PatchOperation] | List of PatchOperation

    try:
        # Patch AllowedFileType
        api_response = api_instance.patch_system_allowedfiletypes_by_id(id, client_id, patch_operation)
        print("The response of AllowedFileTypeApi->patch_system_allowedfiletypes_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AllowedFileTypeApi->patch_system_allowedfiletypes_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| allowedFileTypesId | 
 **client_id** | **str**|  | 
 **patch_operation** | [**List[PatchOperation]**](PatchOperation.md)| List of PatchOperation | 

### Return type

[**AllowedFileType**](AllowedFileType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | AllowedFileType |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_system_allowed_file_types**
> AllowedFileType post_system_allowed_file_types(client_id, allowed_file_type)

Post AllowedFileType

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.allowed_file_type import AllowedFileType
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
    api_instance = connectwise_psa.AllowedFileTypeApi(api_client)
    client_id = 'client_id_example' # str | 
    allowed_file_type = connectwise_psa.AllowedFileType() # AllowedFileType | allowedFileType

    try:
        # Post AllowedFileType
        api_response = api_instance.post_system_allowed_file_types(client_id, allowed_file_type)
        print("The response of AllowedFileTypeApi->post_system_allowed_file_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AllowedFileTypeApi->post_system_allowed_file_types: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**|  | 
 **allowed_file_type** | [**AllowedFileType**](AllowedFileType.md)| allowedFileType | 

### Return type

[**AllowedFileType**](AllowedFileType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | AllowedFileType |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_system_allowedfiletypes_by_id**
> AllowedFileType put_system_allowedfiletypes_by_id(id, client_id, allowed_file_type)

Put AllowedFileType

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.allowed_file_type import AllowedFileType
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
    api_instance = connectwise_psa.AllowedFileTypeApi(api_client)
    id = 56 # int | allowedFileTypeId
    client_id = 'client_id_example' # str | 
    allowed_file_type = connectwise_psa.AllowedFileType() # AllowedFileType | AllowedFileType

    try:
        # Put AllowedFileType
        api_response = api_instance.put_system_allowedfiletypes_by_id(id, client_id, allowed_file_type)
        print("The response of AllowedFileTypeApi->put_system_allowedfiletypes_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AllowedFileTypeApi->put_system_allowedfiletypes_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| allowedFileTypeId | 
 **client_id** | **str**|  | 
 **allowed_file_type** | [**AllowedFileType**](AllowedFileType.md)| AllowedFileType | 

### Return type

[**AllowedFileType**](AllowedFileType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | allowedFileType |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

