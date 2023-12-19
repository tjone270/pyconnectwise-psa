# connectwise_psa.M365ContactSyncApi

All URIs are relative to *https://aus-api.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**post_system_m365contactsync_checkvalidsync**](M365ContactSyncApi.md#post_system_m365contactsync_checkvalidsync) | **POST** /system/m365contactsync/checkvalidsync | Checks if the M365 Tenant is currently associated with a company
[**post_system_m365contactsync_notifydeactivation**](M365ContactSyncApi.md#post_system_m365contactsync_notifydeactivation) | **POST** /system/m365contactsync/notifydeactivation | Notify about a company primary user deactivation on M365
[**post_system_m365contactsync_notifyerror**](M365ContactSyncApi.md#post_system_m365contactsync_notifyerror) | **POST** /system/m365contactsync/notifyerror | Notify about an error connecting to a tenant


# **post_system_m365contactsync_checkvalidsync**
> SuccessResponse post_system_m365contactsync_checkvalidsync(client_id)

Checks if the M365 Tenant is currently associated with a company

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.success_response import SuccessResponse
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
    api_instance = connectwise_psa.M365ContactSyncApi(api_client)
    client_id = 'client_id_example' # str | 

    try:
        # Checks if the M365 Tenant is currently associated with a company
        api_response = api_instance.post_system_m365contactsync_checkvalidsync(client_id)
        print("The response of M365ContactSyncApi->post_system_m365contactsync_checkvalidsync:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling M365ContactSyncApi->post_system_m365contactsync_checkvalidsync: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**|  | 

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
**201** | SuccessResponse |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_system_m365contactsync_notifydeactivation**
> SuccessResponse post_system_m365contactsync_notifydeactivation(client_id, m365_contact_sync_monitoring_notification_info)

Notify about a company primary user deactivation on M365

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.m365_contact_sync_monitoring_notification_info import M365ContactSyncMonitoringNotificationInfo
from connectwise_psa.models.success_response import SuccessResponse
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
    api_instance = connectwise_psa.M365ContactSyncApi(api_client)
    client_id = 'client_id_example' # str | 
    m365_contact_sync_monitoring_notification_info = connectwise_psa.M365ContactSyncMonitoringNotificationInfo() # M365ContactSyncMonitoringNotificationInfo | monitoring

    try:
        # Notify about a company primary user deactivation on M365
        api_response = api_instance.post_system_m365contactsync_notifydeactivation(client_id, m365_contact_sync_monitoring_notification_info)
        print("The response of M365ContactSyncApi->post_system_m365contactsync_notifydeactivation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling M365ContactSyncApi->post_system_m365contactsync_notifydeactivation: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**|  | 
 **m365_contact_sync_monitoring_notification_info** | [**M365ContactSyncMonitoringNotificationInfo**](M365ContactSyncMonitoringNotificationInfo.md)| monitoring | 

### Return type

[**SuccessResponse**](SuccessResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | SuccessResponse |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_system_m365contactsync_notifyerror**
> SuccessResponse post_system_m365contactsync_notifyerror(client_id, m365_contact_sync_monitoring_notification_info)

Notify about an error connecting to a tenant

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.m365_contact_sync_monitoring_notification_info import M365ContactSyncMonitoringNotificationInfo
from connectwise_psa.models.success_response import SuccessResponse
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
    api_instance = connectwise_psa.M365ContactSyncApi(api_client)
    client_id = 'client_id_example' # str | 
    m365_contact_sync_monitoring_notification_info = connectwise_psa.M365ContactSyncMonitoringNotificationInfo() # M365ContactSyncMonitoringNotificationInfo | monitoring

    try:
        # Notify about an error connecting to a tenant
        api_response = api_instance.post_system_m365contactsync_notifyerror(client_id, m365_contact_sync_monitoring_notification_info)
        print("The response of M365ContactSyncApi->post_system_m365contactsync_notifyerror:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling M365ContactSyncApi->post_system_m365contactsync_notifyerror: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**|  | 
 **m365_contact_sync_monitoring_notification_info** | [**M365ContactSyncMonitoringNotificationInfo**](M365ContactSyncMonitoringNotificationInfo.md)| monitoring | 

### Return type

[**SuccessResponse**](SuccessResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | SuccessResponse |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

