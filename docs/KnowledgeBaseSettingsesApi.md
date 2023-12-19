# connectwise_psa.KnowledgeBaseSettingsesApi

All URIs are relative to *https://aus-api.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_service_knowledgebasesettings**](KnowledgeBaseSettingsesApi.md#get_service_knowledgebasesettings) | **GET** /service/knowledgebasesettings | Get KnowledgeBaseSettings
[**get_service_knowledgebasesettings_by_id**](KnowledgeBaseSettingsesApi.md#get_service_knowledgebasesettings_by_id) | **GET** /service/knowledgebasesettings/{id} | Get KnowledgeBaseSettings
[**patch_service_knowledgebasesettings_by_id**](KnowledgeBaseSettingsesApi.md#patch_service_knowledgebasesettings_by_id) | **PATCH** /service/knowledgebasesettings/{id} | Patch KnowledgeBaseSettings
[**post_service_knowledgebasesettings**](KnowledgeBaseSettingsesApi.md#post_service_knowledgebasesettings) | **POST** /service/knowledgebasesettings | Post KnowledgeBaseSettings
[**put_service_knowledgebasesettings_by_id**](KnowledgeBaseSettingsesApi.md#put_service_knowledgebasesettings_by_id) | **PUT** /service/knowledgebasesettings/{id} | Put KnowledgeBaseSettings


# **get_service_knowledgebasesettings**
> KnowledgeBaseSettings get_service_knowledgebasesettings(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get KnowledgeBaseSettings

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.knowledge_base_settings import KnowledgeBaseSettings
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
    api_instance = connectwise_psa.KnowledgeBaseSettingsesApi(api_client)
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
        # Get KnowledgeBaseSettings
        api_response = api_instance.get_service_knowledgebasesettings(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of KnowledgeBaseSettingsesApi->get_service_knowledgebasesettings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KnowledgeBaseSettingsesApi->get_service_knowledgebasesettings: %s\n" % e)
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

[**KnowledgeBaseSettings**](KnowledgeBaseSettings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | KnowledgeBaseSettings |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_service_knowledgebasesettings_by_id**
> KnowledgeBaseSettings get_service_knowledgebasesettings_by_id(id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get KnowledgeBaseSettings

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.knowledge_base_settings import KnowledgeBaseSettings
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
    api_instance = connectwise_psa.KnowledgeBaseSettingsesApi(api_client)
    id = 56 # int | knowledgebasesettingId
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
        # Get KnowledgeBaseSettings
        api_response = api_instance.get_service_knowledgebasesettings_by_id(id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of KnowledgeBaseSettingsesApi->get_service_knowledgebasesettings_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KnowledgeBaseSettingsesApi->get_service_knowledgebasesettings_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| knowledgebasesettingId | 
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

[**KnowledgeBaseSettings**](KnowledgeBaseSettings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | KnowledgeBaseSettings |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_service_knowledgebasesettings_by_id**
> KnowledgeBaseSettings patch_service_knowledgebasesettings_by_id(id, client_id, patch_operation)

Patch KnowledgeBaseSettings

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.knowledge_base_settings import KnowledgeBaseSettings
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
    api_instance = connectwise_psa.KnowledgeBaseSettingsesApi(api_client)
    id = 56 # int | knowledgebasesettingId
    client_id = 'client_id_example' # str | 
    patch_operation = [connectwise_psa.PatchOperation()] # List[PatchOperation] | List of PatchOperation

    try:
        # Patch KnowledgeBaseSettings
        api_response = api_instance.patch_service_knowledgebasesettings_by_id(id, client_id, patch_operation)
        print("The response of KnowledgeBaseSettingsesApi->patch_service_knowledgebasesettings_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KnowledgeBaseSettingsesApi->patch_service_knowledgebasesettings_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| knowledgebasesettingId | 
 **client_id** | **str**|  | 
 **patch_operation** | [**List[PatchOperation]**](PatchOperation.md)| List of PatchOperation | 

### Return type

[**KnowledgeBaseSettings**](KnowledgeBaseSettings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | KnowledgeBaseSettings |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_service_knowledgebasesettings**
> KnowledgeBaseSettings post_service_knowledgebasesettings(client_id, knowledge_base_settings)

Post KnowledgeBaseSettings

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.knowledge_base_settings import KnowledgeBaseSettings
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
    api_instance = connectwise_psa.KnowledgeBaseSettingsesApi(api_client)
    client_id = 'client_id_example' # str | 
    knowledge_base_settings = connectwise_psa.KnowledgeBaseSettings() # KnowledgeBaseSettings | knowledgeBaseSettings

    try:
        # Post KnowledgeBaseSettings
        api_response = api_instance.post_service_knowledgebasesettings(client_id, knowledge_base_settings)
        print("The response of KnowledgeBaseSettingsesApi->post_service_knowledgebasesettings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KnowledgeBaseSettingsesApi->post_service_knowledgebasesettings: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**|  | 
 **knowledge_base_settings** | [**KnowledgeBaseSettings**](KnowledgeBaseSettings.md)| knowledgeBaseSettings | 

### Return type

[**KnowledgeBaseSettings**](KnowledgeBaseSettings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | KnowledgeBaseSettings |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_service_knowledgebasesettings_by_id**
> KnowledgeBaseSettings put_service_knowledgebasesettings_by_id(id, client_id, knowledge_base_settings)

Put KnowledgeBaseSettings

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.knowledge_base_settings import KnowledgeBaseSettings
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
    api_instance = connectwise_psa.KnowledgeBaseSettingsesApi(api_client)
    id = 56 # int | knowledgebasesettingId
    client_id = 'client_id_example' # str | 
    knowledge_base_settings = connectwise_psa.KnowledgeBaseSettings() # KnowledgeBaseSettings | knowledgeBaseSettings

    try:
        # Put KnowledgeBaseSettings
        api_response = api_instance.put_service_knowledgebasesettings_by_id(id, client_id, knowledge_base_settings)
        print("The response of KnowledgeBaseSettingsesApi->put_service_knowledgebasesettings_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KnowledgeBaseSettingsesApi->put_service_knowledgebasesettings_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| knowledgebasesettingId | 
 **client_id** | **str**|  | 
 **knowledge_base_settings** | [**KnowledgeBaseSettings**](KnowledgeBaseSettings.md)| knowledgeBaseSettings | 

### Return type

[**KnowledgeBaseSettings**](KnowledgeBaseSettings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | KnowledgeBaseSettings |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

