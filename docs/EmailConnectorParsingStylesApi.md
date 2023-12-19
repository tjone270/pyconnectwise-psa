# connectwise_psa.EmailConnectorParsingStylesApi

All URIs are relative to *https://aus-api.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_system_email_connectors_by_parent_id_parsing_styles_by_id**](EmailConnectorParsingStylesApi.md#delete_system_email_connectors_by_parent_id_parsing_styles_by_id) | **DELETE** /system/emailConnectors/{parentId}/parsingStyles/{id} | Delete EmailConnectorParsingStyle
[**get_system_email_connectors_by_parent_id_parsing_styles**](EmailConnectorParsingStylesApi.md#get_system_email_connectors_by_parent_id_parsing_styles) | **GET** /system/emailConnectors/{parentId}/parsingStyles | Get List of EmailConnectorParsingStyle
[**get_system_email_connectors_by_parent_id_parsing_styles_by_id**](EmailConnectorParsingStylesApi.md#get_system_email_connectors_by_parent_id_parsing_styles_by_id) | **GET** /system/emailConnectors/{parentId}/parsingStyles/{id} | Get EmailConnectorParsingStyle
[**get_system_email_connectors_by_parent_id_parsing_styles_count**](EmailConnectorParsingStylesApi.md#get_system_email_connectors_by_parent_id_parsing_styles_count) | **GET** /system/emailConnectors/{parentId}/parsingStyles/count | Get Count of EmailConnectorParsingStyle
[**patch_system_email_connectors_by_parent_id_parsing_styles_by_id**](EmailConnectorParsingStylesApi.md#patch_system_email_connectors_by_parent_id_parsing_styles_by_id) | **PATCH** /system/emailConnectors/{parentId}/parsingStyles/{id} | Patch EmailConnectorParsingStyle
[**post_system_email_connectors_by_parent_id_parsing_styles**](EmailConnectorParsingStylesApi.md#post_system_email_connectors_by_parent_id_parsing_styles) | **POST** /system/emailConnectors/{parentId}/parsingStyles | Post EmailConnectorParsingStyle
[**put_system_email_connectors_by_parent_id_parsing_styles_by_id**](EmailConnectorParsingStylesApi.md#put_system_email_connectors_by_parent_id_parsing_styles_by_id) | **PUT** /system/emailConnectors/{parentId}/parsingStyles/{id} | Put EmailConnectorParsingStyle


# **delete_system_email_connectors_by_parent_id_parsing_styles_by_id**
> delete_system_email_connectors_by_parent_id_parsing_styles_by_id(id, parent_id, client_id)

Delete EmailConnectorParsingStyle

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
    api_instance = connectwise_psa.EmailConnectorParsingStylesApi(api_client)
    id = 56 # int | parsingStyleId
    parent_id = 56 # int | emailConnectorId
    client_id = 'client_id_example' # str | 

    try:
        # Delete EmailConnectorParsingStyle
        api_instance.delete_system_email_connectors_by_parent_id_parsing_styles_by_id(id, parent_id, client_id)
    except Exception as e:
        print("Exception when calling EmailConnectorParsingStylesApi->delete_system_email_connectors_by_parent_id_parsing_styles_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| parsingStyleId | 
 **parent_id** | **int**| emailConnectorId | 
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

# **get_system_email_connectors_by_parent_id_parsing_styles**
> List[EmailConnectorParsingStyle] get_system_email_connectors_by_parent_id_parsing_styles(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of EmailConnectorParsingStyle

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.email_connector_parsing_style import EmailConnectorParsingStyle
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
    api_instance = connectwise_psa.EmailConnectorParsingStylesApi(api_client)
    parent_id = 56 # int | emailConnectorId
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
        # Get List of EmailConnectorParsingStyle
        api_response = api_instance.get_system_email_connectors_by_parent_id_parsing_styles(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of EmailConnectorParsingStylesApi->get_system_email_connectors_by_parent_id_parsing_styles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailConnectorParsingStylesApi->get_system_email_connectors_by_parent_id_parsing_styles: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| emailConnectorId | 
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

[**List[EmailConnectorParsingStyle]**](EmailConnectorParsingStyle.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of EmailConnectorParsingStyle |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_system_email_connectors_by_parent_id_parsing_styles_by_id**
> EmailConnectorParsingStyle get_system_email_connectors_by_parent_id_parsing_styles_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get EmailConnectorParsingStyle

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.email_connector_parsing_style import EmailConnectorParsingStyle
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
    api_instance = connectwise_psa.EmailConnectorParsingStylesApi(api_client)
    id = 56 # int | parsingStyleId
    parent_id = 56 # int | emailConnectorId
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
        # Get EmailConnectorParsingStyle
        api_response = api_instance.get_system_email_connectors_by_parent_id_parsing_styles_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of EmailConnectorParsingStylesApi->get_system_email_connectors_by_parent_id_parsing_styles_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailConnectorParsingStylesApi->get_system_email_connectors_by_parent_id_parsing_styles_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| parsingStyleId | 
 **parent_id** | **int**| emailConnectorId | 
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

[**EmailConnectorParsingStyle**](EmailConnectorParsingStyle.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | EmailConnectorParsingStyle |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_system_email_connectors_by_parent_id_parsing_styles_count**
> Count get_system_email_connectors_by_parent_id_parsing_styles_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Count of EmailConnectorParsingStyle

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
    api_instance = connectwise_psa.EmailConnectorParsingStylesApi(api_client)
    parent_id = 56 # int | emailConnectorId
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
        # Get Count of EmailConnectorParsingStyle
        api_response = api_instance.get_system_email_connectors_by_parent_id_parsing_styles_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of EmailConnectorParsingStylesApi->get_system_email_connectors_by_parent_id_parsing_styles_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailConnectorParsingStylesApi->get_system_email_connectors_by_parent_id_parsing_styles_count: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| emailConnectorId | 
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

# **patch_system_email_connectors_by_parent_id_parsing_styles_by_id**
> EmailConnectorParsingStyle patch_system_email_connectors_by_parent_id_parsing_styles_by_id(id, parent_id, client_id, patch_operation)

Patch EmailConnectorParsingStyle

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.email_connector_parsing_style import EmailConnectorParsingStyle
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
    api_instance = connectwise_psa.EmailConnectorParsingStylesApi(api_client)
    id = 56 # int | parsingStyleId
    parent_id = 56 # int | emailConnectorId
    client_id = 'client_id_example' # str | 
    patch_operation = [connectwise_psa.PatchOperation()] # List[PatchOperation] | List of PatchOperation

    try:
        # Patch EmailConnectorParsingStyle
        api_response = api_instance.patch_system_email_connectors_by_parent_id_parsing_styles_by_id(id, parent_id, client_id, patch_operation)
        print("The response of EmailConnectorParsingStylesApi->patch_system_email_connectors_by_parent_id_parsing_styles_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailConnectorParsingStylesApi->patch_system_email_connectors_by_parent_id_parsing_styles_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| parsingStyleId | 
 **parent_id** | **int**| emailConnectorId | 
 **client_id** | **str**|  | 
 **patch_operation** | [**List[PatchOperation]**](PatchOperation.md)| List of PatchOperation | 

### Return type

[**EmailConnectorParsingStyle**](EmailConnectorParsingStyle.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | EmailConnectorParsingStyle |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_system_email_connectors_by_parent_id_parsing_styles**
> EmailConnectorParsingStyle post_system_email_connectors_by_parent_id_parsing_styles(parent_id, client_id, email_connector_parsing_style)

Post EmailConnectorParsingStyle

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.email_connector_parsing_style import EmailConnectorParsingStyle
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
    api_instance = connectwise_psa.EmailConnectorParsingStylesApi(api_client)
    parent_id = 56 # int | emailConnectorId
    client_id = 'client_id_example' # str | 
    email_connector_parsing_style = connectwise_psa.EmailConnectorParsingStyle() # EmailConnectorParsingStyle | emailConnectorParsingStyle

    try:
        # Post EmailConnectorParsingStyle
        api_response = api_instance.post_system_email_connectors_by_parent_id_parsing_styles(parent_id, client_id, email_connector_parsing_style)
        print("The response of EmailConnectorParsingStylesApi->post_system_email_connectors_by_parent_id_parsing_styles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailConnectorParsingStylesApi->post_system_email_connectors_by_parent_id_parsing_styles: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| emailConnectorId | 
 **client_id** | **str**|  | 
 **email_connector_parsing_style** | [**EmailConnectorParsingStyle**](EmailConnectorParsingStyle.md)| emailConnectorParsingStyle | 

### Return type

[**EmailConnectorParsingStyle**](EmailConnectorParsingStyle.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | EmailConnectorParsingStyle |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_system_email_connectors_by_parent_id_parsing_styles_by_id**
> EmailConnectorParsingStyle put_system_email_connectors_by_parent_id_parsing_styles_by_id(id, parent_id, client_id, email_connector_parsing_style)

Put EmailConnectorParsingStyle

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.email_connector_parsing_style import EmailConnectorParsingStyle
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
    api_instance = connectwise_psa.EmailConnectorParsingStylesApi(api_client)
    id = 56 # int | parsingStyleId
    parent_id = 56 # int | emailConnectorId
    client_id = 'client_id_example' # str | 
    email_connector_parsing_style = connectwise_psa.EmailConnectorParsingStyle() # EmailConnectorParsingStyle | emailConnectorParsingStyle

    try:
        # Put EmailConnectorParsingStyle
        api_response = api_instance.put_system_email_connectors_by_parent_id_parsing_styles_by_id(id, parent_id, client_id, email_connector_parsing_style)
        print("The response of EmailConnectorParsingStylesApi->put_system_email_connectors_by_parent_id_parsing_styles_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailConnectorParsingStylesApi->put_system_email_connectors_by_parent_id_parsing_styles_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| parsingStyleId | 
 **parent_id** | **int**| emailConnectorId | 
 **client_id** | **str**|  | 
 **email_connector_parsing_style** | [**EmailConnectorParsingStyle**](EmailConnectorParsingStyle.md)| emailConnectorParsingStyle | 

### Return type

[**EmailConnectorParsingStyle**](EmailConnectorParsingStyle.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | EmailConnectorParsingStyle |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

