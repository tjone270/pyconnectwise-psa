# connectwise_psa.MemberNotificationSettingsApi

All URIs are relative to *https://aus-api.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_system_members_by_parent_id_notification_settings_by_id**](MemberNotificationSettingsApi.md#delete_system_members_by_parent_id_notification_settings_by_id) | **DELETE** /system/members/{parentId}/notificationSettings/{id} | Delete MemberNotificationSetting
[**get_system_members_by_parent_id_notification_settings**](MemberNotificationSettingsApi.md#get_system_members_by_parent_id_notification_settings) | **GET** /system/members/{parentId}/notificationSettings | Get List of MemberNotificationSetting
[**get_system_members_by_parent_id_notification_settings_by_id**](MemberNotificationSettingsApi.md#get_system_members_by_parent_id_notification_settings_by_id) | **GET** /system/members/{parentId}/notificationSettings/{id} | Get MemberNotificationSetting
[**get_system_members_by_parent_id_notification_settings_count**](MemberNotificationSettingsApi.md#get_system_members_by_parent_id_notification_settings_count) | **GET** /system/members/{parentId}/notificationSettings/count | Get Count of MemberNotificationSetting
[**patch_system_members_by_parent_id_notification_settings_by_id**](MemberNotificationSettingsApi.md#patch_system_members_by_parent_id_notification_settings_by_id) | **PATCH** /system/members/{parentId}/notificationSettings/{id} | Patch MemberNotificationSetting
[**post_system_members_by_parent_id_notification_settings**](MemberNotificationSettingsApi.md#post_system_members_by_parent_id_notification_settings) | **POST** /system/members/{parentId}/notificationSettings | Post MemberNotificationSetting
[**put_system_members_by_parent_id_notification_settings_by_id**](MemberNotificationSettingsApi.md#put_system_members_by_parent_id_notification_settings_by_id) | **PUT** /system/members/{parentId}/notificationSettings/{id} | Put MemberNotificationSetting


# **delete_system_members_by_parent_id_notification_settings_by_id**
> delete_system_members_by_parent_id_notification_settings_by_id(id, parent_id, client_id)

Delete MemberNotificationSetting

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
    api_instance = connectwise_psa.MemberNotificationSettingsApi(api_client)
    id = 56 # int | notificationSettingId
    parent_id = 56 # int | memberId
    client_id = 'client_id_example' # str | 

    try:
        # Delete MemberNotificationSetting
        api_instance.delete_system_members_by_parent_id_notification_settings_by_id(id, parent_id, client_id)
    except Exception as e:
        print("Exception when calling MemberNotificationSettingsApi->delete_system_members_by_parent_id_notification_settings_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| notificationSettingId | 
 **parent_id** | **int**| memberId | 
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

# **get_system_members_by_parent_id_notification_settings**
> List[MemberNotificationSetting] get_system_members_by_parent_id_notification_settings(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of MemberNotificationSetting

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.member_notification_setting import MemberNotificationSetting
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
    api_instance = connectwise_psa.MemberNotificationSettingsApi(api_client)
    parent_id = 56 # int | memberId
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
        # Get List of MemberNotificationSetting
        api_response = api_instance.get_system_members_by_parent_id_notification_settings(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of MemberNotificationSettingsApi->get_system_members_by_parent_id_notification_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MemberNotificationSettingsApi->get_system_members_by_parent_id_notification_settings: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| memberId | 
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

[**List[MemberNotificationSetting]**](MemberNotificationSetting.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of MemberNotificationSetting |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_system_members_by_parent_id_notification_settings_by_id**
> MemberNotificationSetting get_system_members_by_parent_id_notification_settings_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get MemberNotificationSetting

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.member_notification_setting import MemberNotificationSetting
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
    api_instance = connectwise_psa.MemberNotificationSettingsApi(api_client)
    id = 56 # int | notificationSettingId
    parent_id = 56 # int | memberId
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
        # Get MemberNotificationSetting
        api_response = api_instance.get_system_members_by_parent_id_notification_settings_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of MemberNotificationSettingsApi->get_system_members_by_parent_id_notification_settings_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MemberNotificationSettingsApi->get_system_members_by_parent_id_notification_settings_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| notificationSettingId | 
 **parent_id** | **int**| memberId | 
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

[**MemberNotificationSetting**](MemberNotificationSetting.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | MemberNotificationSetting |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_system_members_by_parent_id_notification_settings_count**
> Count get_system_members_by_parent_id_notification_settings_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Count of MemberNotificationSetting

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
    api_instance = connectwise_psa.MemberNotificationSettingsApi(api_client)
    parent_id = 56 # int | memberId
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
        # Get Count of MemberNotificationSetting
        api_response = api_instance.get_system_members_by_parent_id_notification_settings_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of MemberNotificationSettingsApi->get_system_members_by_parent_id_notification_settings_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MemberNotificationSettingsApi->get_system_members_by_parent_id_notification_settings_count: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| memberId | 
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

# **patch_system_members_by_parent_id_notification_settings_by_id**
> MemberNotificationSetting patch_system_members_by_parent_id_notification_settings_by_id(id, parent_id, client_id, patch_operation)

Patch MemberNotificationSetting

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.member_notification_setting import MemberNotificationSetting
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
    api_instance = connectwise_psa.MemberNotificationSettingsApi(api_client)
    id = 56 # int | notificationSettingId
    parent_id = 56 # int | memberId
    client_id = 'client_id_example' # str | 
    patch_operation = [connectwise_psa.PatchOperation()] # List[PatchOperation] | List of PatchOperation

    try:
        # Patch MemberNotificationSetting
        api_response = api_instance.patch_system_members_by_parent_id_notification_settings_by_id(id, parent_id, client_id, patch_operation)
        print("The response of MemberNotificationSettingsApi->patch_system_members_by_parent_id_notification_settings_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MemberNotificationSettingsApi->patch_system_members_by_parent_id_notification_settings_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| notificationSettingId | 
 **parent_id** | **int**| memberId | 
 **client_id** | **str**|  | 
 **patch_operation** | [**List[PatchOperation]**](PatchOperation.md)| List of PatchOperation | 

### Return type

[**MemberNotificationSetting**](MemberNotificationSetting.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | MemberNotificationSetting |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_system_members_by_parent_id_notification_settings**
> MemberNotificationSetting post_system_members_by_parent_id_notification_settings(parent_id, client_id, member_notification_setting)

Post MemberNotificationSetting

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.member_notification_setting import MemberNotificationSetting
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
    api_instance = connectwise_psa.MemberNotificationSettingsApi(api_client)
    parent_id = 56 # int | memberId
    client_id = 'client_id_example' # str | 
    member_notification_setting = connectwise_psa.MemberNotificationSetting() # MemberNotificationSetting | memberNotificationSetting

    try:
        # Post MemberNotificationSetting
        api_response = api_instance.post_system_members_by_parent_id_notification_settings(parent_id, client_id, member_notification_setting)
        print("The response of MemberNotificationSettingsApi->post_system_members_by_parent_id_notification_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MemberNotificationSettingsApi->post_system_members_by_parent_id_notification_settings: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| memberId | 
 **client_id** | **str**|  | 
 **member_notification_setting** | [**MemberNotificationSetting**](MemberNotificationSetting.md)| memberNotificationSetting | 

### Return type

[**MemberNotificationSetting**](MemberNotificationSetting.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | MemberNotificationSetting |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_system_members_by_parent_id_notification_settings_by_id**
> MemberNotificationSetting put_system_members_by_parent_id_notification_settings_by_id(id, parent_id, client_id, member_notification_setting)

Put MemberNotificationSetting

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.member_notification_setting import MemberNotificationSetting
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
    api_instance = connectwise_psa.MemberNotificationSettingsApi(api_client)
    id = 56 # int | notificationSettingId
    parent_id = 56 # int | memberId
    client_id = 'client_id_example' # str | 
    member_notification_setting = connectwise_psa.MemberNotificationSetting() # MemberNotificationSetting | memberNotificationSetting

    try:
        # Put MemberNotificationSetting
        api_response = api_instance.put_system_members_by_parent_id_notification_settings_by_id(id, parent_id, client_id, member_notification_setting)
        print("The response of MemberNotificationSettingsApi->put_system_members_by_parent_id_notification_settings_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MemberNotificationSettingsApi->put_system_members_by_parent_id_notification_settings_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| notificationSettingId | 
 **parent_id** | **int**| memberId | 
 **client_id** | **str**|  | 
 **member_notification_setting** | [**MemberNotificationSetting**](MemberNotificationSetting.md)| memberNotificationSetting | 

### Return type

[**MemberNotificationSetting**](MemberNotificationSetting.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | MemberNotificationSetting |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

