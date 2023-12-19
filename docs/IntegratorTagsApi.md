# connectwise_psa.IntegratorTagsApi

All URIs are relative to *https://aus-api.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_system_integrator_tags_by_id**](IntegratorTagsApi.md#delete_system_integrator_tags_by_id) | **DELETE** /system/integratorTags/{id} | Delete IntegratorTag
[**get_system_integrator_tags**](IntegratorTagsApi.md#get_system_integrator_tags) | **GET** /system/integratorTags | Get List of IntegratorTag
[**get_system_integrator_tags_by_id**](IntegratorTagsApi.md#get_system_integrator_tags_by_id) | **GET** /system/integratorTags/{id} | Get IntegratorTag
[**get_system_integrator_tags_count**](IntegratorTagsApi.md#get_system_integrator_tags_count) | **GET** /system/integratorTags/count | Get Count of IntegratorTag
[**patch_system_integrator_tags_by_id**](IntegratorTagsApi.md#patch_system_integrator_tags_by_id) | **PATCH** /system/integratorTags/{id} | Patch IntegratorTag
[**post_system_integrator_tags**](IntegratorTagsApi.md#post_system_integrator_tags) | **POST** /system/integratorTags | Post IntegratorTag
[**put_system_integrator_tags_by_id**](IntegratorTagsApi.md#put_system_integrator_tags_by_id) | **PUT** /system/integratorTags/{id} | Put IntegratorTag


# **delete_system_integrator_tags_by_id**
> delete_system_integrator_tags_by_id(id, client_id)

Delete IntegratorTag

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
    api_instance = connectwise_psa.IntegratorTagsApi(api_client)
    id = 56 # int | integratorTagId
    client_id = 'client_id_example' # str | 

    try:
        # Delete IntegratorTag
        api_instance.delete_system_integrator_tags_by_id(id, client_id)
    except Exception as e:
        print("Exception when calling IntegratorTagsApi->delete_system_integrator_tags_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| integratorTagId | 
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

# **get_system_integrator_tags**
> List[IntegratorTag] get_system_integrator_tags(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of IntegratorTag

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.integrator_tag import IntegratorTag
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
    api_instance = connectwise_psa.IntegratorTagsApi(api_client)
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
        # Get List of IntegratorTag
        api_response = api_instance.get_system_integrator_tags(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of IntegratorTagsApi->get_system_integrator_tags:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegratorTagsApi->get_system_integrator_tags: %s\n" % e)
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

[**List[IntegratorTag]**](IntegratorTag.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of IntegratorTag |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_system_integrator_tags_by_id**
> IntegratorTag get_system_integrator_tags_by_id(id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get IntegratorTag

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.integrator_tag import IntegratorTag
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
    api_instance = connectwise_psa.IntegratorTagsApi(api_client)
    id = 56 # int | integratorTagId
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
        # Get IntegratorTag
        api_response = api_instance.get_system_integrator_tags_by_id(id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of IntegratorTagsApi->get_system_integrator_tags_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegratorTagsApi->get_system_integrator_tags_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| integratorTagId | 
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

[**IntegratorTag**](IntegratorTag.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | IntegratorTag |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_system_integrator_tags_count**
> Count get_system_integrator_tags_count(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Count of IntegratorTag

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
    api_instance = connectwise_psa.IntegratorTagsApi(api_client)
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
        # Get Count of IntegratorTag
        api_response = api_instance.get_system_integrator_tags_count(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of IntegratorTagsApi->get_system_integrator_tags_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegratorTagsApi->get_system_integrator_tags_count: %s\n" % e)
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

# **patch_system_integrator_tags_by_id**
> IntegratorTag patch_system_integrator_tags_by_id(id, client_id, patch_operation)

Patch IntegratorTag

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.integrator_tag import IntegratorTag
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
    api_instance = connectwise_psa.IntegratorTagsApi(api_client)
    id = 56 # int | integratorTagId
    client_id = 'client_id_example' # str | 
    patch_operation = [connectwise_psa.PatchOperation()] # List[PatchOperation] | List of PatchOperation

    try:
        # Patch IntegratorTag
        api_response = api_instance.patch_system_integrator_tags_by_id(id, client_id, patch_operation)
        print("The response of IntegratorTagsApi->patch_system_integrator_tags_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegratorTagsApi->patch_system_integrator_tags_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| integratorTagId | 
 **client_id** | **str**|  | 
 **patch_operation** | [**List[PatchOperation]**](PatchOperation.md)| List of PatchOperation | 

### Return type

[**IntegratorTag**](IntegratorTag.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | IntegratorTag |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_system_integrator_tags**
> IntegratorTag post_system_integrator_tags(client_id, integrator_tag)

Post IntegratorTag

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.integrator_tag import IntegratorTag
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
    api_instance = connectwise_psa.IntegratorTagsApi(api_client)
    client_id = 'client_id_example' # str | 
    integrator_tag = connectwise_psa.IntegratorTag() # IntegratorTag | tag

    try:
        # Post IntegratorTag
        api_response = api_instance.post_system_integrator_tags(client_id, integrator_tag)
        print("The response of IntegratorTagsApi->post_system_integrator_tags:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegratorTagsApi->post_system_integrator_tags: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**|  | 
 **integrator_tag** | [**IntegratorTag**](IntegratorTag.md)| tag | 

### Return type

[**IntegratorTag**](IntegratorTag.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | IntegratorTag |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_system_integrator_tags_by_id**
> IntegratorTag put_system_integrator_tags_by_id(id, client_id, integrator_tag)

Put IntegratorTag

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.integrator_tag import IntegratorTag
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
    api_instance = connectwise_psa.IntegratorTagsApi(api_client)
    id = 56 # int | integratorTagId
    client_id = 'client_id_example' # str | 
    integrator_tag = connectwise_psa.IntegratorTag() # IntegratorTag | tag

    try:
        # Put IntegratorTag
        api_response = api_instance.put_system_integrator_tags_by_id(id, client_id, integrator_tag)
        print("The response of IntegratorTagsApi->put_system_integrator_tags_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegratorTagsApi->put_system_integrator_tags_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| integratorTagId | 
 **client_id** | **str**|  | 
 **integrator_tag** | [**IntegratorTag**](IntegratorTag.md)| tag | 

### Return type

[**IntegratorTag**](IntegratorTag.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | IntegratorTag |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

