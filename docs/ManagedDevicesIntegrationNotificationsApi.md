# connectwise_psa.ManagedDevicesIntegrationNotificationsApi

All URIs are relative to *https://api-aus.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_company_managed_devices_integrations_by_parent_id_notifications_by_id**](ManagedDevicesIntegrationNotificationsApi.md#delete_company_managed_devices_integrations_by_parent_id_notifications_by_id) | **DELETE** /company/managedDevicesIntegrations/{parentId}/notifications/{id} | Delete ManagedDevicesIntegrationNotification
[**get_company_managed_devices_integrations_by_parent_id_notifications**](ManagedDevicesIntegrationNotificationsApi.md#get_company_managed_devices_integrations_by_parent_id_notifications) | **GET** /company/managedDevicesIntegrations/{parentId}/notifications | Get List of ManagedDevicesIntegrationNotification
[**get_company_managed_devices_integrations_by_parent_id_notifications_by_id**](ManagedDevicesIntegrationNotificationsApi.md#get_company_managed_devices_integrations_by_parent_id_notifications_by_id) | **GET** /company/managedDevicesIntegrations/{parentId}/notifications/{id} | Get ManagedDevicesIntegrationNotification
[**get_company_managed_devices_integrations_by_parent_id_notifications_count**](ManagedDevicesIntegrationNotificationsApi.md#get_company_managed_devices_integrations_by_parent_id_notifications_count) | **GET** /company/managedDevicesIntegrations/{parentId}/notifications/count | Get Count of ManagedDevicesIntegrationNotification
[**patch_company_managed_devices_integrations_by_parent_id_notifications_by_id**](ManagedDevicesIntegrationNotificationsApi.md#patch_company_managed_devices_integrations_by_parent_id_notifications_by_id) | **PATCH** /company/managedDevicesIntegrations/{parentId}/notifications/{id} | Patch ManagedDevicesIntegrationNotification
[**post_company_managed_devices_integrations_by_parent_id_notifications**](ManagedDevicesIntegrationNotificationsApi.md#post_company_managed_devices_integrations_by_parent_id_notifications) | **POST** /company/managedDevicesIntegrations/{parentId}/notifications | Post ManagedDevicesIntegrationNotification
[**put_company_managed_devices_integrations_by_parent_id_notifications_by_id**](ManagedDevicesIntegrationNotificationsApi.md#put_company_managed_devices_integrations_by_parent_id_notifications_by_id) | **PUT** /company/managedDevicesIntegrations/{parentId}/notifications/{id} | Put ManagedDevicesIntegrationNotification


# **delete_company_managed_devices_integrations_by_parent_id_notifications_by_id**
> ManagedDevicesIntegrationNotification delete_company_managed_devices_integrations_by_parent_id_notifications_by_id(id, parent_id, client_id)

Delete ManagedDevicesIntegrationNotification

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.managed_devices_integration_notification import ManagedDevicesIntegrationNotification
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
    api_instance = connectwise_psa.ManagedDevicesIntegrationNotificationsApi(api_client)
    id = 56 # int | notificationId
    parent_id = 56 # int | managedDevicesIntegrationId
    client_id = 'client_id_example' # str | 

    try:
        # Delete ManagedDevicesIntegrationNotification
        api_response = api_instance.delete_company_managed_devices_integrations_by_parent_id_notifications_by_id(id, parent_id, client_id)
        print("The response of ManagedDevicesIntegrationNotificationsApi->delete_company_managed_devices_integrations_by_parent_id_notifications_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagedDevicesIntegrationNotificationsApi->delete_company_managed_devices_integrations_by_parent_id_notifications_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| notificationId | 
 **parent_id** | **int**| managedDevicesIntegrationId | 
 **client_id** | **str**|  | 

### Return type

[**ManagedDevicesIntegrationNotification**](ManagedDevicesIntegrationNotification.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ManagedDevicesIntegrationNotification |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_company_managed_devices_integrations_by_parent_id_notifications**
> List[ManagedDevicesIntegrationNotification] get_company_managed_devices_integrations_by_parent_id_notifications(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of ManagedDevicesIntegrationNotification

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.managed_devices_integration_notification import ManagedDevicesIntegrationNotification
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
    api_instance = connectwise_psa.ManagedDevicesIntegrationNotificationsApi(api_client)
    parent_id = 56 # int | managedDevicesIntegrationId
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
        # Get List of ManagedDevicesIntegrationNotification
        api_response = api_instance.get_company_managed_devices_integrations_by_parent_id_notifications(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of ManagedDevicesIntegrationNotificationsApi->get_company_managed_devices_integrations_by_parent_id_notifications:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagedDevicesIntegrationNotificationsApi->get_company_managed_devices_integrations_by_parent_id_notifications: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| managedDevicesIntegrationId | 
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

[**List[ManagedDevicesIntegrationNotification]**](ManagedDevicesIntegrationNotification.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of ManagedDevicesIntegrationNotification |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_company_managed_devices_integrations_by_parent_id_notifications_by_id**
> ManagedDevicesIntegrationNotification get_company_managed_devices_integrations_by_parent_id_notifications_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get ManagedDevicesIntegrationNotification

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.managed_devices_integration_notification import ManagedDevicesIntegrationNotification
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
    api_instance = connectwise_psa.ManagedDevicesIntegrationNotificationsApi(api_client)
    id = 56 # int | notificationId
    parent_id = 56 # int | managedDevicesIntegrationId
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
        # Get ManagedDevicesIntegrationNotification
        api_response = api_instance.get_company_managed_devices_integrations_by_parent_id_notifications_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of ManagedDevicesIntegrationNotificationsApi->get_company_managed_devices_integrations_by_parent_id_notifications_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagedDevicesIntegrationNotificationsApi->get_company_managed_devices_integrations_by_parent_id_notifications_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| notificationId | 
 **parent_id** | **int**| managedDevicesIntegrationId | 
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

[**ManagedDevicesIntegrationNotification**](ManagedDevicesIntegrationNotification.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ManagedDevicesIntegrationNotification |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_company_managed_devices_integrations_by_parent_id_notifications_count**
> Count get_company_managed_devices_integrations_by_parent_id_notifications_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Count of ManagedDevicesIntegrationNotification

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
    api_instance = connectwise_psa.ManagedDevicesIntegrationNotificationsApi(api_client)
    parent_id = 56 # int | managedDevicesIntegrationId
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
        # Get Count of ManagedDevicesIntegrationNotification
        api_response = api_instance.get_company_managed_devices_integrations_by_parent_id_notifications_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of ManagedDevicesIntegrationNotificationsApi->get_company_managed_devices_integrations_by_parent_id_notifications_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagedDevicesIntegrationNotificationsApi->get_company_managed_devices_integrations_by_parent_id_notifications_count: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| managedDevicesIntegrationId | 
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

# **patch_company_managed_devices_integrations_by_parent_id_notifications_by_id**
> ManagedDevicesIntegrationNotification patch_company_managed_devices_integrations_by_parent_id_notifications_by_id(id, parent_id, client_id, patch_operation)

Patch ManagedDevicesIntegrationNotification

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.managed_devices_integration_notification import ManagedDevicesIntegrationNotification
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
    api_instance = connectwise_psa.ManagedDevicesIntegrationNotificationsApi(api_client)
    id = 56 # int | notificationId
    parent_id = 56 # int | managedDevicesIntegrationId
    client_id = 'client_id_example' # str | 
    patch_operation = [connectwise_psa.PatchOperation()] # List[PatchOperation] | List of PatchOperation

    try:
        # Patch ManagedDevicesIntegrationNotification
        api_response = api_instance.patch_company_managed_devices_integrations_by_parent_id_notifications_by_id(id, parent_id, client_id, patch_operation)
        print("The response of ManagedDevicesIntegrationNotificationsApi->patch_company_managed_devices_integrations_by_parent_id_notifications_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagedDevicesIntegrationNotificationsApi->patch_company_managed_devices_integrations_by_parent_id_notifications_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| notificationId | 
 **parent_id** | **int**| managedDevicesIntegrationId | 
 **client_id** | **str**|  | 
 **patch_operation** | [**List[PatchOperation]**](PatchOperation.md)| List of PatchOperation | 

### Return type

[**ManagedDevicesIntegrationNotification**](ManagedDevicesIntegrationNotification.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ManagedDevicesIntegrationNotification |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_company_managed_devices_integrations_by_parent_id_notifications**
> ManagedDevicesIntegrationNotification post_company_managed_devices_integrations_by_parent_id_notifications(parent_id, client_id, managed_devices_integration_notification)

Post ManagedDevicesIntegrationNotification

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.managed_devices_integration_notification import ManagedDevicesIntegrationNotification
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
    api_instance = connectwise_psa.ManagedDevicesIntegrationNotificationsApi(api_client)
    parent_id = 56 # int | managedDevicesIntegrationId
    client_id = 'client_id_example' # str | 
    managed_devices_integration_notification = connectwise_psa.ManagedDevicesIntegrationNotification() # ManagedDevicesIntegrationNotification | notification

    try:
        # Post ManagedDevicesIntegrationNotification
        api_response = api_instance.post_company_managed_devices_integrations_by_parent_id_notifications(parent_id, client_id, managed_devices_integration_notification)
        print("The response of ManagedDevicesIntegrationNotificationsApi->post_company_managed_devices_integrations_by_parent_id_notifications:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagedDevicesIntegrationNotificationsApi->post_company_managed_devices_integrations_by_parent_id_notifications: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| managedDevicesIntegrationId | 
 **client_id** | **str**|  | 
 **managed_devices_integration_notification** | [**ManagedDevicesIntegrationNotification**](ManagedDevicesIntegrationNotification.md)| notification | 

### Return type

[**ManagedDevicesIntegrationNotification**](ManagedDevicesIntegrationNotification.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ManagedDevicesIntegrationNotification |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_company_managed_devices_integrations_by_parent_id_notifications_by_id**
> ManagedDevicesIntegrationNotification put_company_managed_devices_integrations_by_parent_id_notifications_by_id(id, parent_id, client_id, managed_devices_integration_notification)

Put ManagedDevicesIntegrationNotification

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.managed_devices_integration_notification import ManagedDevicesIntegrationNotification
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
    api_instance = connectwise_psa.ManagedDevicesIntegrationNotificationsApi(api_client)
    id = 56 # int | notificationId
    parent_id = 56 # int | managedDevicesIntegrationId
    client_id = 'client_id_example' # str | 
    managed_devices_integration_notification = connectwise_psa.ManagedDevicesIntegrationNotification() # ManagedDevicesIntegrationNotification | notification

    try:
        # Put ManagedDevicesIntegrationNotification
        api_response = api_instance.put_company_managed_devices_integrations_by_parent_id_notifications_by_id(id, parent_id, client_id, managed_devices_integration_notification)
        print("The response of ManagedDevicesIntegrationNotificationsApi->put_company_managed_devices_integrations_by_parent_id_notifications_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagedDevicesIntegrationNotificationsApi->put_company_managed_devices_integrations_by_parent_id_notifications_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| notificationId | 
 **parent_id** | **int**| managedDevicesIntegrationId | 
 **client_id** | **str**|  | 
 **managed_devices_integration_notification** | [**ManagedDevicesIntegrationNotification**](ManagedDevicesIntegrationNotification.md)| notification | 

### Return type

[**ManagedDevicesIntegrationNotification**](ManagedDevicesIntegrationNotification.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ManagedDevicesIntegrationNotification |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

