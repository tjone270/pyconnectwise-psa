# connectwise_psa.UserDefinedFieldsApi

All URIs are relative to *https://aus-api.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_system_user_defined_fields_by_id**](UserDefinedFieldsApi.md#delete_system_user_defined_fields_by_id) | **DELETE** /system/userDefinedFields/{id} | Delete UserDefinedField
[**get_system_user_defined_fields**](UserDefinedFieldsApi.md#get_system_user_defined_fields) | **GET** /system/userDefinedFields | Get List of UserDefinedField
[**get_system_user_defined_fields_by_id**](UserDefinedFieldsApi.md#get_system_user_defined_fields_by_id) | **GET** /system/userDefinedFields/{id} | Get UserDefinedField
[**get_system_user_defined_fields_count**](UserDefinedFieldsApi.md#get_system_user_defined_fields_count) | **GET** /system/userDefinedFields/count | Get Count of UserDefinedField
[**patch_system_user_defined_fields_by_id**](UserDefinedFieldsApi.md#patch_system_user_defined_fields_by_id) | **PATCH** /system/userDefinedFields/{id} | Patch UserDefinedField
[**post_system_user_defined_fields**](UserDefinedFieldsApi.md#post_system_user_defined_fields) | **POST** /system/userDefinedFields | Post UserDefinedField
[**put_system_user_defined_fields_by_id**](UserDefinedFieldsApi.md#put_system_user_defined_fields_by_id) | **PUT** /system/userDefinedFields/{id} | Put UserDefinedField


# **delete_system_user_defined_fields_by_id**
> delete_system_user_defined_fields_by_id(id, client_id)

Delete UserDefinedField

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
    api_instance = connectwise_psa.UserDefinedFieldsApi(api_client)
    id = 56 # int | userDefinedFieldId
    client_id = 'client_id_example' # str | 

    try:
        # Delete UserDefinedField
        api_instance.delete_system_user_defined_fields_by_id(id, client_id)
    except Exception as e:
        print("Exception when calling UserDefinedFieldsApi->delete_system_user_defined_fields_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| userDefinedFieldId | 
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

# **get_system_user_defined_fields**
> List[UserDefinedField] get_system_user_defined_fields(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of UserDefinedField

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.user_defined_field import UserDefinedField
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
    api_instance = connectwise_psa.UserDefinedFieldsApi(api_client)
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
        # Get List of UserDefinedField
        api_response = api_instance.get_system_user_defined_fields(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of UserDefinedFieldsApi->get_system_user_defined_fields:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserDefinedFieldsApi->get_system_user_defined_fields: %s\n" % e)
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

[**List[UserDefinedField]**](UserDefinedField.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of UserDefinedField |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_system_user_defined_fields_by_id**
> UserDefinedField get_system_user_defined_fields_by_id(id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get UserDefinedField

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.user_defined_field import UserDefinedField
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
    api_instance = connectwise_psa.UserDefinedFieldsApi(api_client)
    id = 56 # int | userDefinedFieldId
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
        # Get UserDefinedField
        api_response = api_instance.get_system_user_defined_fields_by_id(id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of UserDefinedFieldsApi->get_system_user_defined_fields_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserDefinedFieldsApi->get_system_user_defined_fields_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| userDefinedFieldId | 
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

[**UserDefinedField**](UserDefinedField.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | UserDefinedField |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_system_user_defined_fields_count**
> Count get_system_user_defined_fields_count(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Count of UserDefinedField

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
    api_instance = connectwise_psa.UserDefinedFieldsApi(api_client)
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
        # Get Count of UserDefinedField
        api_response = api_instance.get_system_user_defined_fields_count(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of UserDefinedFieldsApi->get_system_user_defined_fields_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserDefinedFieldsApi->get_system_user_defined_fields_count: %s\n" % e)
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

# **patch_system_user_defined_fields_by_id**
> UserDefinedField patch_system_user_defined_fields_by_id(id, client_id, patch_operation)

Patch UserDefinedField

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.patch_operation import PatchOperation
from connectwise_psa.models.user_defined_field import UserDefinedField
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
    api_instance = connectwise_psa.UserDefinedFieldsApi(api_client)
    id = 56 # int | userDefinedFieldId
    client_id = 'client_id_example' # str | 
    patch_operation = [connectwise_psa.PatchOperation()] # List[PatchOperation] | List of PatchOperation

    try:
        # Patch UserDefinedField
        api_response = api_instance.patch_system_user_defined_fields_by_id(id, client_id, patch_operation)
        print("The response of UserDefinedFieldsApi->patch_system_user_defined_fields_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserDefinedFieldsApi->patch_system_user_defined_fields_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| userDefinedFieldId | 
 **client_id** | **str**|  | 
 **patch_operation** | [**List[PatchOperation]**](PatchOperation.md)| List of PatchOperation | 

### Return type

[**UserDefinedField**](UserDefinedField.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | UserDefinedField |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_system_user_defined_fields**
> UserDefinedField post_system_user_defined_fields(client_id, user_defined_field)

Post UserDefinedField

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.user_defined_field import UserDefinedField
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
    api_instance = connectwise_psa.UserDefinedFieldsApi(api_client)
    client_id = 'client_id_example' # str | 
    user_defined_field = connectwise_psa.UserDefinedField() # UserDefinedField | userDefinedField

    try:
        # Post UserDefinedField
        api_response = api_instance.post_system_user_defined_fields(client_id, user_defined_field)
        print("The response of UserDefinedFieldsApi->post_system_user_defined_fields:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserDefinedFieldsApi->post_system_user_defined_fields: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**|  | 
 **user_defined_field** | [**UserDefinedField**](UserDefinedField.md)| userDefinedField | 

### Return type

[**UserDefinedField**](UserDefinedField.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | UserDefinedField |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_system_user_defined_fields_by_id**
> UserDefinedField put_system_user_defined_fields_by_id(id, client_id, user_defined_field)

Put UserDefinedField

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.user_defined_field import UserDefinedField
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
    api_instance = connectwise_psa.UserDefinedFieldsApi(api_client)
    id = 56 # int | userDefinedFieldId
    client_id = 'client_id_example' # str | 
    user_defined_field = connectwise_psa.UserDefinedField() # UserDefinedField | userDefinedField

    try:
        # Put UserDefinedField
        api_response = api_instance.put_system_user_defined_fields_by_id(id, client_id, user_defined_field)
        print("The response of UserDefinedFieldsApi->put_system_user_defined_fields_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserDefinedFieldsApi->put_system_user_defined_fields_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| userDefinedFieldId | 
 **client_id** | **str**|  | 
 **user_defined_field** | [**UserDefinedField**](UserDefinedField.md)| userDefinedField | 

### Return type

[**UserDefinedField**](UserDefinedField.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | UserDefinedField |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

