# connectwise_psa.ServiceSignoffCustomFieldApi

All URIs are relative to *https://api-aus.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_service_service_signoff_by_parent_id_signoffcustomfields_by_id**](ServiceSignoffCustomFieldApi.md#delete_service_service_signoff_by_parent_id_signoffcustomfields_by_id) | **DELETE** /service/serviceSignoff/{parentId}/signoffcustomfields/{id} | Delete ServiceSignoffCustomField
[**get_service_service_signoff_by_parent_id_signoffcustomfields**](ServiceSignoffCustomFieldApi.md#get_service_service_signoff_by_parent_id_signoffcustomfields) | **GET** /service/serviceSignoff/{parentId}/signoffcustomfields | Get List of ServiceSignoffCustomField
[**get_service_service_signoff_by_parent_id_signoffcustomfields_by_id**](ServiceSignoffCustomFieldApi.md#get_service_service_signoff_by_parent_id_signoffcustomfields_by_id) | **GET** /service/serviceSignoff/{parentId}/signoffcustomfields/{id} | Get ServiceSignoffCustomField
[**get_service_service_signoff_by_parent_id_signoffcustomfields_count**](ServiceSignoffCustomFieldApi.md#get_service_service_signoff_by_parent_id_signoffcustomfields_count) | **GET** /service/serviceSignoff/{parentId}/signoffcustomfields/count | Get Count of ServiceSignoffCustomField
[**patch_service_service_signoff_by_parent_id_signoffcustomfields_by_id**](ServiceSignoffCustomFieldApi.md#patch_service_service_signoff_by_parent_id_signoffcustomfields_by_id) | **PATCH** /service/serviceSignoff/{parentId}/signoffcustomfields/{id} | Patch ServiceSignoffCustomField
[**post_service_service_signoff_by_parent_id_signoffcustomfields**](ServiceSignoffCustomFieldApi.md#post_service_service_signoff_by_parent_id_signoffcustomfields) | **POST** /service/serviceSignoff/{parentId}/signoffcustomfields | Post ServiceSignoffCustomField
[**put_service_service_signoff_by_parent_id_signoffcustomfields_by_id**](ServiceSignoffCustomFieldApi.md#put_service_service_signoff_by_parent_id_signoffcustomfields_by_id) | **PUT** /service/serviceSignoff/{parentId}/signoffcustomfields/{id} | Put ServiceSignoffCustomField


# **delete_service_service_signoff_by_parent_id_signoffcustomfields_by_id**
> delete_service_service_signoff_by_parent_id_signoffcustomfields_by_id(id, parent_id, client_id)

Delete ServiceSignoffCustomField

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
    api_instance = connectwise_psa.ServiceSignoffCustomFieldApi(api_client)
    id = 56 # int | ServiceSignoffCustomFieldId
    parent_id = 56 # int | serviceSignoffId
    client_id = 'client_id_example' # str | 

    try:
        # Delete ServiceSignoffCustomField
        api_instance.delete_service_service_signoff_by_parent_id_signoffcustomfields_by_id(id, parent_id, client_id)
    except Exception as e:
        print("Exception when calling ServiceSignoffCustomFieldApi->delete_service_service_signoff_by_parent_id_signoffcustomfields_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ServiceSignoffCustomFieldId | 
 **parent_id** | **int**| serviceSignoffId | 
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

# **get_service_service_signoff_by_parent_id_signoffcustomfields**
> List[ServiceSignoffCustomField] get_service_service_signoff_by_parent_id_signoffcustomfields(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of ServiceSignoffCustomField

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.service_signoff_custom_field import ServiceSignoffCustomField
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
    api_instance = connectwise_psa.ServiceSignoffCustomFieldApi(api_client)
    parent_id = 56 # int | serviceSignoffId
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
        # Get List of ServiceSignoffCustomField
        api_response = api_instance.get_service_service_signoff_by_parent_id_signoffcustomfields(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of ServiceSignoffCustomFieldApi->get_service_service_signoff_by_parent_id_signoffcustomfields:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceSignoffCustomFieldApi->get_service_service_signoff_by_parent_id_signoffcustomfields: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| serviceSignoffId | 
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

[**List[ServiceSignoffCustomField]**](ServiceSignoffCustomField.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of ServiceSignoffCustomField |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_service_service_signoff_by_parent_id_signoffcustomfields_by_id**
> ServiceSignoffCustomField get_service_service_signoff_by_parent_id_signoffcustomfields_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get ServiceSignoffCustomField

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.service_signoff_custom_field import ServiceSignoffCustomField
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
    api_instance = connectwise_psa.ServiceSignoffCustomFieldApi(api_client)
    id = 56 # int | ServiceSignoffCustomFieldId
    parent_id = 56 # int | serviceSignoffId
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
        # Get ServiceSignoffCustomField
        api_response = api_instance.get_service_service_signoff_by_parent_id_signoffcustomfields_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of ServiceSignoffCustomFieldApi->get_service_service_signoff_by_parent_id_signoffcustomfields_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceSignoffCustomFieldApi->get_service_service_signoff_by_parent_id_signoffcustomfields_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ServiceSignoffCustomFieldId | 
 **parent_id** | **int**| serviceSignoffId | 
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

[**ServiceSignoffCustomField**](ServiceSignoffCustomField.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ServiceSignoffCustomField |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_service_service_signoff_by_parent_id_signoffcustomfields_count**
> Count get_service_service_signoff_by_parent_id_signoffcustomfields_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Count of ServiceSignoffCustomField

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
    api_instance = connectwise_psa.ServiceSignoffCustomFieldApi(api_client)
    parent_id = 56 # int | serviceSignoffId
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
        # Get Count of ServiceSignoffCustomField
        api_response = api_instance.get_service_service_signoff_by_parent_id_signoffcustomfields_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of ServiceSignoffCustomFieldApi->get_service_service_signoff_by_parent_id_signoffcustomfields_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceSignoffCustomFieldApi->get_service_service_signoff_by_parent_id_signoffcustomfields_count: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| serviceSignoffId | 
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

# **patch_service_service_signoff_by_parent_id_signoffcustomfields_by_id**
> ServiceSignoffCustomField patch_service_service_signoff_by_parent_id_signoffcustomfields_by_id(id, parent_id, client_id, patch_operation)

Patch ServiceSignoffCustomField

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.patch_operation import PatchOperation
from connectwise_psa.models.service_signoff_custom_field import ServiceSignoffCustomField
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
    api_instance = connectwise_psa.ServiceSignoffCustomFieldApi(api_client)
    id = 56 # int | ServiceSignoffCustomFieldId
    parent_id = 56 # int | serviceSignoffId
    client_id = 'client_id_example' # str | 
    patch_operation = [connectwise_psa.PatchOperation()] # List[PatchOperation] | List of PatchOperation

    try:
        # Patch ServiceSignoffCustomField
        api_response = api_instance.patch_service_service_signoff_by_parent_id_signoffcustomfields_by_id(id, parent_id, client_id, patch_operation)
        print("The response of ServiceSignoffCustomFieldApi->patch_service_service_signoff_by_parent_id_signoffcustomfields_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceSignoffCustomFieldApi->patch_service_service_signoff_by_parent_id_signoffcustomfields_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ServiceSignoffCustomFieldId | 
 **parent_id** | **int**| serviceSignoffId | 
 **client_id** | **str**|  | 
 **patch_operation** | [**List[PatchOperation]**](PatchOperation.md)| List of PatchOperation | 

### Return type

[**ServiceSignoffCustomField**](ServiceSignoffCustomField.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ServiceSignoff |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_service_service_signoff_by_parent_id_signoffcustomfields**
> ServiceSignoffCustomField post_service_service_signoff_by_parent_id_signoffcustomfields(parent_id, client_id, service_signoff_custom_field)

Post ServiceSignoffCustomField

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.service_signoff_custom_field import ServiceSignoffCustomField
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
    api_instance = connectwise_psa.ServiceSignoffCustomFieldApi(api_client)
    parent_id = 56 # int | serviceSignoffId
    client_id = 'client_id_example' # str | 
    service_signoff_custom_field = connectwise_psa.ServiceSignoffCustomField() # ServiceSignoffCustomField | serviceSignoff

    try:
        # Post ServiceSignoffCustomField
        api_response = api_instance.post_service_service_signoff_by_parent_id_signoffcustomfields(parent_id, client_id, service_signoff_custom_field)
        print("The response of ServiceSignoffCustomFieldApi->post_service_service_signoff_by_parent_id_signoffcustomfields:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceSignoffCustomFieldApi->post_service_service_signoff_by_parent_id_signoffcustomfields: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| serviceSignoffId | 
 **client_id** | **str**|  | 
 **service_signoff_custom_field** | [**ServiceSignoffCustomField**](ServiceSignoffCustomField.md)| serviceSignoff | 

### Return type

[**ServiceSignoffCustomField**](ServiceSignoffCustomField.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | ServiceSignoffCustomField |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_service_service_signoff_by_parent_id_signoffcustomfields_by_id**
> ServiceSignoffCustomField put_service_service_signoff_by_parent_id_signoffcustomfields_by_id(id, parent_id, client_id, service_signoff_custom_field)

Put ServiceSignoffCustomField

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.service_signoff_custom_field import ServiceSignoffCustomField
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
    api_instance = connectwise_psa.ServiceSignoffCustomFieldApi(api_client)
    id = 56 # int | ServiceSignoffCustomFieldId
    parent_id = 56 # int | serviceSignoffId
    client_id = 'client_id_example' # str | 
    service_signoff_custom_field = connectwise_psa.ServiceSignoffCustomField() # ServiceSignoffCustomField | ServiceSignoffCustomField

    try:
        # Put ServiceSignoffCustomField
        api_response = api_instance.put_service_service_signoff_by_parent_id_signoffcustomfields_by_id(id, parent_id, client_id, service_signoff_custom_field)
        print("The response of ServiceSignoffCustomFieldApi->put_service_service_signoff_by_parent_id_signoffcustomfields_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceSignoffCustomFieldApi->put_service_service_signoff_by_parent_id_signoffcustomfields_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ServiceSignoffCustomFieldId | 
 **parent_id** | **int**| serviceSignoffId | 
 **client_id** | **str**|  | 
 **service_signoff_custom_field** | [**ServiceSignoffCustomField**](ServiceSignoffCustomField.md)| ServiceSignoffCustomField | 

### Return type

[**ServiceSignoffCustomField**](ServiceSignoffCustomField.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ServiceSignoffCustomField |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

