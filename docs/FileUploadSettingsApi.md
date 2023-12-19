# connectwise_psa.FileUploadSettingsApi

All URIs are relative to *https://aus-api.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_system_fileuploadsettings**](FileUploadSettingsApi.md#get_system_fileuploadsettings) | **GET** /system/fileuploadsettings/ | Get List of FileUploadSettings
[**get_system_fileuploadsettings_by_id**](FileUploadSettingsApi.md#get_system_fileuploadsettings_by_id) | **GET** /system/fileuploadsettings/{id} | Get FileUploadSettings
[**get_system_fileuploadsettings_count**](FileUploadSettingsApi.md#get_system_fileuploadsettings_count) | **GET** /system/fileuploadsettings/count | Get Count of FileUploadSettings
[**patch_system_fileuploadsettings_by_id**](FileUploadSettingsApi.md#patch_system_fileuploadsettings_by_id) | **PATCH** /system/fileuploadsettings/{id} | Patch FileUploadSettings
[**put_system_fileuploadsettings_by_id**](FileUploadSettingsApi.md#put_system_fileuploadsettings_by_id) | **PUT** /system/fileuploadsettings/{id} | Put FileUploadSettings


# **get_system_fileuploadsettings**
> List[FileUploadSetting] get_system_fileuploadsettings(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of FileUploadSettings

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.file_upload_setting import FileUploadSetting
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
    api_instance = connectwise_psa.FileUploadSettingsApi(api_client)
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
        # Get List of FileUploadSettings
        api_response = api_instance.get_system_fileuploadsettings(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of FileUploadSettingsApi->get_system_fileuploadsettings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FileUploadSettingsApi->get_system_fileuploadsettings: %s\n" % e)
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

[**List[FileUploadSetting]**](FileUploadSetting.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of fileUploadSettingses |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_system_fileuploadsettings_by_id**
> FileUploadSetting get_system_fileuploadsettings_by_id(id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get FileUploadSettings

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.file_upload_setting import FileUploadSetting
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
    api_instance = connectwise_psa.FileUploadSettingsApi(api_client)
    id = 56 # int | FileUploadSettingId
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
        # Get FileUploadSettings
        api_response = api_instance.get_system_fileuploadsettings_by_id(id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of FileUploadSettingsApi->get_system_fileuploadsettings_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FileUploadSettingsApi->get_system_fileuploadsettings_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| FileUploadSettingId | 
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

[**FileUploadSetting**](FileUploadSetting.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | FileUploadSetting |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_system_fileuploadsettings_count**
> Count get_system_fileuploadsettings_count(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Count of FileUploadSettings

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
    api_instance = connectwise_psa.FileUploadSettingsApi(api_client)
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
        # Get Count of FileUploadSettings
        api_response = api_instance.get_system_fileuploadsettings_count(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of FileUploadSettingsApi->get_system_fileuploadsettings_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FileUploadSettingsApi->get_system_fileuploadsettings_count: %s\n" % e)
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

# **patch_system_fileuploadsettings_by_id**
> FileUploadSetting patch_system_fileuploadsettings_by_id(id, client_id, patch_operation)

Patch FileUploadSettings

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.file_upload_setting import FileUploadSetting
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
    api_instance = connectwise_psa.FileUploadSettingsApi(api_client)
    id = 56 # int | FileUploadSettingId
    client_id = 'client_id_example' # str | 
    patch_operation = [connectwise_psa.PatchOperation()] # List[PatchOperation] | List of PatchOperation

    try:
        # Patch FileUploadSettings
        api_response = api_instance.patch_system_fileuploadsettings_by_id(id, client_id, patch_operation)
        print("The response of FileUploadSettingsApi->patch_system_fileuploadsettings_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FileUploadSettingsApi->patch_system_fileuploadsettings_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| FileUploadSettingId | 
 **client_id** | **str**|  | 
 **patch_operation** | [**List[PatchOperation]**](PatchOperation.md)| List of PatchOperation | 

### Return type

[**FileUploadSetting**](FileUploadSetting.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | FileUploadSetting |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_system_fileuploadsettings_by_id**
> FileUploadSetting put_system_fileuploadsettings_by_id(id, client_id, file_upload_setting)

Put FileUploadSettings

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.file_upload_setting import FileUploadSetting
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
    api_instance = connectwise_psa.FileUploadSettingsApi(api_client)
    id = 56 # int | FileUploadSettingId
    client_id = 'client_id_example' # str | 
    file_upload_setting = connectwise_psa.FileUploadSetting() # FileUploadSetting | companyTypeAssociation

    try:
        # Put FileUploadSettings
        api_response = api_instance.put_system_fileuploadsettings_by_id(id, client_id, file_upload_setting)
        print("The response of FileUploadSettingsApi->put_system_fileuploadsettings_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FileUploadSettingsApi->put_system_fileuploadsettings_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| FileUploadSettingId | 
 **client_id** | **str**|  | 
 **file_upload_setting** | [**FileUploadSetting**](FileUploadSetting.md)| companyTypeAssociation | 

### Return type

[**FileUploadSetting**](FileUploadSetting.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | FileUploadSetting |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

