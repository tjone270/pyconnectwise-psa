# connectwise_psa.EmailConnectorsApi

All URIs are relative to *https://aus-api.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_system_email_connectors_by_id**](EmailConnectorsApi.md#delete_system_email_connectors_by_id) | **DELETE** /system/emailConnectors/{id} | Delete EmailConnector
[**get_system_email_connectors**](EmailConnectorsApi.md#get_system_email_connectors) | **GET** /system/emailConnectors | Get List of EmailConnector
[**get_system_email_connectors_by_id**](EmailConnectorsApi.md#get_system_email_connectors_by_id) | **GET** /system/emailConnectors/{id} | Get EmailConnector
[**get_system_email_connectors_count**](EmailConnectorsApi.md#get_system_email_connectors_count) | **GET** /system/emailConnectors/count | Get Count of EmailConnector
[**patch_system_email_connectors_by_id**](EmailConnectorsApi.md#patch_system_email_connectors_by_id) | **PATCH** /system/emailConnectors/{id} | Patch EmailConnector
[**post_system_email_connectors**](EmailConnectorsApi.md#post_system_email_connectors) | **POST** /system/emailConnectors | Post EmailConnector
[**put_system_email_connectors_by_id**](EmailConnectorsApi.md#put_system_email_connectors_by_id) | **PUT** /system/emailConnectors/{id} | Put EmailConnector


# **delete_system_email_connectors_by_id**
> delete_system_email_connectors_by_id(id, client_id)

Delete EmailConnector

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
    api_instance = connectwise_psa.EmailConnectorsApi(api_client)
    id = 56 # int | emailConnectorId
    client_id = 'client_id_example' # str | 

    try:
        # Delete EmailConnector
        api_instance.delete_system_email_connectors_by_id(id, client_id)
    except Exception as e:
        print("Exception when calling EmailConnectorsApi->delete_system_email_connectors_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| emailConnectorId | 
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

# **get_system_email_connectors**
> List[EmailConnector] get_system_email_connectors(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of EmailConnector

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.email_connector import EmailConnector
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
    api_instance = connectwise_psa.EmailConnectorsApi(api_client)
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
        # Get List of EmailConnector
        api_response = api_instance.get_system_email_connectors(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of EmailConnectorsApi->get_system_email_connectors:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailConnectorsApi->get_system_email_connectors: %s\n" % e)
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

[**List[EmailConnector]**](EmailConnector.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of EmailConnector |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_system_email_connectors_by_id**
> EmailConnector get_system_email_connectors_by_id(id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get EmailConnector

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.email_connector import EmailConnector
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
    api_instance = connectwise_psa.EmailConnectorsApi(api_client)
    id = 56 # int | emailConnectorId
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
        # Get EmailConnector
        api_response = api_instance.get_system_email_connectors_by_id(id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of EmailConnectorsApi->get_system_email_connectors_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailConnectorsApi->get_system_email_connectors_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| emailConnectorId | 
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

[**EmailConnector**](EmailConnector.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | EmailConnector |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_system_email_connectors_count**
> Count get_system_email_connectors_count(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Count of EmailConnector

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
    api_instance = connectwise_psa.EmailConnectorsApi(api_client)
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
        # Get Count of EmailConnector
        api_response = api_instance.get_system_email_connectors_count(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of EmailConnectorsApi->get_system_email_connectors_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailConnectorsApi->get_system_email_connectors_count: %s\n" % e)
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

# **patch_system_email_connectors_by_id**
> EmailConnector patch_system_email_connectors_by_id(id, client_id, patch_operation)

Patch EmailConnector

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.email_connector import EmailConnector
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
    api_instance = connectwise_psa.EmailConnectorsApi(api_client)
    id = 56 # int | emailConnectorId
    client_id = 'client_id_example' # str | 
    patch_operation = [connectwise_psa.PatchOperation()] # List[PatchOperation] | List of PatchOperation

    try:
        # Patch EmailConnector
        api_response = api_instance.patch_system_email_connectors_by_id(id, client_id, patch_operation)
        print("The response of EmailConnectorsApi->patch_system_email_connectors_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailConnectorsApi->patch_system_email_connectors_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| emailConnectorId | 
 **client_id** | **str**|  | 
 **patch_operation** | [**List[PatchOperation]**](PatchOperation.md)| List of PatchOperation | 

### Return type

[**EmailConnector**](EmailConnector.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | EmailConnector |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_system_email_connectors**
> EmailConnector post_system_email_connectors(client_id, email_connector)

Post EmailConnector

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.email_connector import EmailConnector
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
    api_instance = connectwise_psa.EmailConnectorsApi(api_client)
    client_id = 'client_id_example' # str | 
    email_connector = connectwise_psa.EmailConnector() # EmailConnector | emailConnector

    try:
        # Post EmailConnector
        api_response = api_instance.post_system_email_connectors(client_id, email_connector)
        print("The response of EmailConnectorsApi->post_system_email_connectors:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailConnectorsApi->post_system_email_connectors: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**|  | 
 **email_connector** | [**EmailConnector**](EmailConnector.md)| emailConnector | 

### Return type

[**EmailConnector**](EmailConnector.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | EmailConnector |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_system_email_connectors_by_id**
> EmailConnector put_system_email_connectors_by_id(id, client_id, email_connector)

Put EmailConnector

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.email_connector import EmailConnector
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
    api_instance = connectwise_psa.EmailConnectorsApi(api_client)
    id = 56 # int | emailConnectorId
    client_id = 'client_id_example' # str | 
    email_connector = connectwise_psa.EmailConnector() # EmailConnector | emailConnector

    try:
        # Put EmailConnector
        api_response = api_instance.put_system_email_connectors_by_id(id, client_id, email_connector)
        print("The response of EmailConnectorsApi->put_system_email_connectors_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailConnectorsApi->put_system_email_connectors_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| emailConnectorId | 
 **client_id** | **str**|  | 
 **email_connector** | [**EmailConnector**](EmailConnector.md)| emailConnector | 

### Return type

[**EmailConnector**](EmailConnector.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | EmailConnector |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

