# connectwise_psa.M365ContactSyncsApi

All URIs are relative to *https://api-aus.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_system_m365contactsync_by_id**](M365ContactSyncsApi.md#delete_system_m365contactsync_by_id) | **DELETE** /system/m365contactsync/{id}/ | Delete M365ContactSync
[**get_system_m365contactsync_authorize**](M365ContactSyncsApi.md#get_system_m365contactsync_authorize) | **GET** /system/m365contactsync/authorize/ | Initiate Application ConsentAsync
[**get_system_m365contactsync_by_id**](M365ContactSyncsApi.md#get_system_m365contactsync_by_id) | **GET** /system/m365contactsync/{id}/ | Get ContactSync By Id
[**get_system_m365contactsync_by_id_test**](M365ContactSyncsApi.md#get_system_m365contactsync_by_id_test) | **GET** /system/m365contactsync/{id}/test/ | Test Consent Async
[**get_system_m365contactsync_by_id_viewauth**](M365ContactSyncsApi.md#get_system_m365contactsync_by_id_viewauth) | **GET** /system/m365contactsync/{id}/viewauth/ | Get AuthInfo Async
[**patch_system_m365contactsync_by_id**](M365ContactSyncsApi.md#patch_system_m365contactsync_by_id) | **PATCH** /system/m365contactsync/{id}/ | Update ContactSync Async
[**post_system_m365contactsync**](M365ContactSyncsApi.md#post_system_m365contactsync) | **POST** /system/m365contactsync/ | Create Async


# **delete_system_m365contactsync_by_id**
> M365ContactSync delete_system_m365contactsync_by_id(id, client_id)

Delete M365ContactSync

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.m365_contact_sync import M365ContactSync
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
    api_instance = connectwise_psa.M365ContactSyncsApi(api_client)
    id = 56 # int | M365ContactSyncId
    client_id = 'client_id_example' # str | 

    try:
        # Delete M365ContactSync
        api_response = api_instance.delete_system_m365contactsync_by_id(id, client_id)
        print("The response of M365ContactSyncsApi->delete_system_m365contactsync_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling M365ContactSyncsApi->delete_system_m365contactsync_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| M365ContactSyncId | 
 **client_id** | **str**|  | 

### Return type

[**M365ContactSync**](M365ContactSync.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | M365ContactSync |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_system_m365contactsync_authorize**
> SuccessResponse get_system_m365contactsync_authorize(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Initiate Application ConsentAsync

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.success_response import SuccessResponse
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
    api_instance = connectwise_psa.M365ContactSyncsApi(api_client)
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
        # Initiate Application ConsentAsync
        api_response = api_instance.get_system_m365contactsync_authorize(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of M365ContactSyncsApi->get_system_m365contactsync_authorize:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling M365ContactSyncsApi->get_system_m365contactsync_authorize: %s\n" % e)
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

[**SuccessResponse**](SuccessResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | SuccessResponse |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_system_m365contactsync_by_id**
> M365ContactSync get_system_m365contactsync_by_id(id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get ContactSync By Id

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.m365_contact_sync import M365ContactSync
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
    api_instance = connectwise_psa.M365ContactSyncsApi(api_client)
    id = 56 # int | M365ContactSyncId
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
        # Get ContactSync By Id
        api_response = api_instance.get_system_m365contactsync_by_id(id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of M365ContactSyncsApi->get_system_m365contactsync_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling M365ContactSyncsApi->get_system_m365contactsync_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| M365ContactSyncId | 
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

[**M365ContactSync**](M365ContactSync.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | M365ContactSync |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_system_m365contactsync_by_id_test**
> SuccessResponse get_system_m365contactsync_by_id_test(id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Test Consent Async

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.success_response import SuccessResponse
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
    api_instance = connectwise_psa.M365ContactSyncsApi(api_client)
    id = 56 # int | M365ContactSyncId
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
        # Test Consent Async
        api_response = api_instance.get_system_m365contactsync_by_id_test(id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of M365ContactSyncsApi->get_system_m365contactsync_by_id_test:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling M365ContactSyncsApi->get_system_m365contactsync_by_id_test: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| M365ContactSyncId | 
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

[**SuccessResponse**](SuccessResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | SuccessResponse |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_system_m365contactsync_by_id_viewauth**
> M365ContactSync get_system_m365contactsync_by_id_viewauth(id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get AuthInfo Async

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.m365_contact_sync import M365ContactSync
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
    api_instance = connectwise_psa.M365ContactSyncsApi(api_client)
    id = 56 # int | M365ContactSyncId
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
        # Get AuthInfo Async
        api_response = api_instance.get_system_m365contactsync_by_id_viewauth(id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of M365ContactSyncsApi->get_system_m365contactsync_by_id_viewauth:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling M365ContactSyncsApi->get_system_m365contactsync_by_id_viewauth: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| M365ContactSyncId | 
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

[**M365ContactSync**](M365ContactSync.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | M365ContactSync |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_system_m365contactsync_by_id**
> M365ContactSync patch_system_m365contactsync_by_id(id, client_id)

Update ContactSync Async

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.m365_contact_sync import M365ContactSync
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
    api_instance = connectwise_psa.M365ContactSyncsApi(api_client)
    id = 56 # int | M365ContactSyncId
    client_id = 'client_id_example' # str | 

    try:
        # Update ContactSync Async
        api_response = api_instance.patch_system_m365contactsync_by_id(id, client_id)
        print("The response of M365ContactSyncsApi->patch_system_m365contactsync_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling M365ContactSyncsApi->patch_system_m365contactsync_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| M365ContactSyncId | 
 **client_id** | **str**|  | 

### Return type

[**M365ContactSync**](M365ContactSync.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | M365ContactSync |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_system_m365contactsync**
> M365ContactSync post_system_m365contactsync(client_id)

Create Async

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.m365_contact_sync import M365ContactSync
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
    api_instance = connectwise_psa.M365ContactSyncsApi(api_client)
    client_id = 'client_id_example' # str | 

    try:
        # Create Async
        api_response = api_instance.post_system_m365contactsync(client_id)
        print("The response of M365ContactSyncsApi->post_system_m365contactsync:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling M365ContactSyncsApi->post_system_m365contactsync: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**|  | 

### Return type

[**M365ContactSync**](M365ContactSync.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | M365ContactSync |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

