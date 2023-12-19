# connectwise_psa.ConnectWiseHostedSetupsApi

All URIs are relative to *https://api-aus.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_system_connectwisehostedsetups_by_id**](ConnectWiseHostedSetupsApi.md#delete_system_connectwisehostedsetups_by_id) | **DELETE** /system/connectwisehostedsetups/{id} | Delete ConnectWiseHostedSetup
[**get_system_connectwisehostedsetups**](ConnectWiseHostedSetupsApi.md#get_system_connectwisehostedsetups) | **GET** /system/connectwisehostedsetups | Get List of ConnectWiseHostedSetup
[**get_system_connectwisehostedsetups_by_id**](ConnectWiseHostedSetupsApi.md#get_system_connectwisehostedsetups_by_id) | **GET** /system/connectwisehostedsetups/{id} | Get ConnectWiseHostedSetup
[**get_system_connectwisehostedsetups_count**](ConnectWiseHostedSetupsApi.md#get_system_connectwisehostedsetups_count) | **GET** /system/connectwisehostedsetups/count | Get Count of ConnectWiseHostedSetup
[**patch_system_connectwisehostedsetups_by_id**](ConnectWiseHostedSetupsApi.md#patch_system_connectwisehostedsetups_by_id) | **PATCH** /system/connectwisehostedsetups/{id} | Patch ConnectWiseHostedSetup
[**post_system_connectwisehostedsetups**](ConnectWiseHostedSetupsApi.md#post_system_connectwisehostedsetups) | **POST** /system/connectwisehostedsetups | Post ConnectWiseHostedSetup
[**put_system_connectwisehostedsetups_by_id**](ConnectWiseHostedSetupsApi.md#put_system_connectwisehostedsetups_by_id) | **PUT** /system/connectwisehostedsetups/{id} | Put ConnectWiseHostedSetup


# **delete_system_connectwisehostedsetups_by_id**
> delete_system_connectwisehostedsetups_by_id(id, client_id)

Delete ConnectWiseHostedSetup

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
    api_instance = connectwise_psa.ConnectWiseHostedSetupsApi(api_client)
    id = 56 # int | connectwisehostedsetupId
    client_id = 'client_id_example' # str | 

    try:
        # Delete ConnectWiseHostedSetup
        api_instance.delete_system_connectwisehostedsetups_by_id(id, client_id)
    except Exception as e:
        print("Exception when calling ConnectWiseHostedSetupsApi->delete_system_connectwisehostedsetups_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| connectwisehostedsetupId | 
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

# **get_system_connectwisehostedsetups**
> List[ConnectWiseHostedSetup] get_system_connectwisehostedsetups(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of ConnectWiseHostedSetup

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.connect_wise_hosted_setup import ConnectWiseHostedSetup
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
    api_instance = connectwise_psa.ConnectWiseHostedSetupsApi(api_client)
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
        # Get List of ConnectWiseHostedSetup
        api_response = api_instance.get_system_connectwisehostedsetups(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of ConnectWiseHostedSetupsApi->get_system_connectwisehostedsetups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectWiseHostedSetupsApi->get_system_connectwisehostedsetups: %s\n" % e)
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

[**List[ConnectWiseHostedSetup]**](ConnectWiseHostedSetup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of ConnectWiseHostedSetup |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_system_connectwisehostedsetups_by_id**
> ConnectWiseHostedSetup get_system_connectwisehostedsetups_by_id(id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get ConnectWiseHostedSetup

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.connect_wise_hosted_setup import ConnectWiseHostedSetup
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
    api_instance = connectwise_psa.ConnectWiseHostedSetupsApi(api_client)
    id = 56 # int | connectwisehostedsetupId
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
        # Get ConnectWiseHostedSetup
        api_response = api_instance.get_system_connectwisehostedsetups_by_id(id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of ConnectWiseHostedSetupsApi->get_system_connectwisehostedsetups_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectWiseHostedSetupsApi->get_system_connectwisehostedsetups_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| connectwisehostedsetupId | 
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

[**ConnectWiseHostedSetup**](ConnectWiseHostedSetup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ConnectWiseHostedSetup |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_system_connectwisehostedsetups_count**
> Count get_system_connectwisehostedsetups_count(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Count of ConnectWiseHostedSetup

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
    api_instance = connectwise_psa.ConnectWiseHostedSetupsApi(api_client)
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
        # Get Count of ConnectWiseHostedSetup
        api_response = api_instance.get_system_connectwisehostedsetups_count(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of ConnectWiseHostedSetupsApi->get_system_connectwisehostedsetups_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectWiseHostedSetupsApi->get_system_connectwisehostedsetups_count: %s\n" % e)
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

# **patch_system_connectwisehostedsetups_by_id**
> ConnectWiseHostedSetup patch_system_connectwisehostedsetups_by_id(id, client_id, patch_operation)

Patch ConnectWiseHostedSetup

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.connect_wise_hosted_setup import ConnectWiseHostedSetup
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
    api_instance = connectwise_psa.ConnectWiseHostedSetupsApi(api_client)
    id = 56 # int | connectwisehostedsetupId
    client_id = 'client_id_example' # str | 
    patch_operation = [connectwise_psa.PatchOperation()] # List[PatchOperation] | List of PatchOperation

    try:
        # Patch ConnectWiseHostedSetup
        api_response = api_instance.patch_system_connectwisehostedsetups_by_id(id, client_id, patch_operation)
        print("The response of ConnectWiseHostedSetupsApi->patch_system_connectwisehostedsetups_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectWiseHostedSetupsApi->patch_system_connectwisehostedsetups_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| connectwisehostedsetupId | 
 **client_id** | **str**|  | 
 **patch_operation** | [**List[PatchOperation]**](PatchOperation.md)| List of PatchOperation | 

### Return type

[**ConnectWiseHostedSetup**](ConnectWiseHostedSetup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ConnectWiseHostedSetup |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_system_connectwisehostedsetups**
> ConnectWiseHostedSetup post_system_connectwisehostedsetups(client_id, connect_wise_hosted_setup)

Post ConnectWiseHostedSetup

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.connect_wise_hosted_setup import ConnectWiseHostedSetup
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
    api_instance = connectwise_psa.ConnectWiseHostedSetupsApi(api_client)
    client_id = 'client_id_example' # str | 
    connect_wise_hosted_setup = connectwise_psa.ConnectWiseHostedSetup() # ConnectWiseHostedSetup | connectWiseHostedSetup

    try:
        # Post ConnectWiseHostedSetup
        api_response = api_instance.post_system_connectwisehostedsetups(client_id, connect_wise_hosted_setup)
        print("The response of ConnectWiseHostedSetupsApi->post_system_connectwisehostedsetups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectWiseHostedSetupsApi->post_system_connectwisehostedsetups: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**|  | 
 **connect_wise_hosted_setup** | [**ConnectWiseHostedSetup**](ConnectWiseHostedSetup.md)| connectWiseHostedSetup | 

### Return type

[**ConnectWiseHostedSetup**](ConnectWiseHostedSetup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | ConnectWiseHostedSetup |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_system_connectwisehostedsetups_by_id**
> ConnectWiseHostedSetup put_system_connectwisehostedsetups_by_id(id, client_id, connect_wise_hosted_setup)

Put ConnectWiseHostedSetup

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.connect_wise_hosted_setup import ConnectWiseHostedSetup
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
    api_instance = connectwise_psa.ConnectWiseHostedSetupsApi(api_client)
    id = 56 # int | connectwisehostedsetupId
    client_id = 'client_id_example' # str | 
    connect_wise_hosted_setup = connectwise_psa.ConnectWiseHostedSetup() # ConnectWiseHostedSetup | connectWiseHostedSetup

    try:
        # Put ConnectWiseHostedSetup
        api_response = api_instance.put_system_connectwisehostedsetups_by_id(id, client_id, connect_wise_hosted_setup)
        print("The response of ConnectWiseHostedSetupsApi->put_system_connectwisehostedsetups_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectWiseHostedSetupsApi->put_system_connectwisehostedsetups_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| connectwisehostedsetupId | 
 **client_id** | **str**|  | 
 **connect_wise_hosted_setup** | [**ConnectWiseHostedSetup**](ConnectWiseHostedSetup.md)| connectWiseHostedSetup | 

### Return type

[**ConnectWiseHostedSetup**](ConnectWiseHostedSetup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ConnectWiseHostedSetup |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

