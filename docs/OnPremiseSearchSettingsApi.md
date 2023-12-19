# connectwise_psa.OnPremiseSearchSettingsApi

All URIs are relative to *https://api-aus.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_system_on_premise_search_setting**](OnPremiseSearchSettingsApi.md#get_system_on_premise_search_setting) | **GET** /system/onPremiseSearchSetting/ | Get List of OnPremiseSearchSettings
[**get_system_on_premise_search_setting_by_id**](OnPremiseSearchSettingsApi.md#get_system_on_premise_search_setting_by_id) | **GET** /system/onPremiseSearchSetting/{id} | Get OnPremiseSearchSettings
[**get_system_on_premise_search_setting_count**](OnPremiseSearchSettingsApi.md#get_system_on_premise_search_setting_count) | **GET** /system/onPremiseSearchSetting/count | Get Count of OnPremiseSearchSettings
[**patch_system_on_premise_search_setting_by_id**](OnPremiseSearchSettingsApi.md#patch_system_on_premise_search_setting_by_id) | **PATCH** /system/onPremiseSearchSetting/{id} | Patch OnPremiseSearchSettings
[**put_system_on_premise_search_setting_by_id**](OnPremiseSearchSettingsApi.md#put_system_on_premise_search_setting_by_id) | **PUT** /system/onPremiseSearchSetting/{id} | Put OnPremiseSearchSettings              This does not update Solr. This allows you to set Manage to the Solr password.


# **get_system_on_premise_search_setting**
> List[OnPremiseSearchSetting] get_system_on_premise_search_setting(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of OnPremiseSearchSettings

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.on_premise_search_setting import OnPremiseSearchSetting
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
    api_instance = connectwise_psa.OnPremiseSearchSettingsApi(api_client)
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
        # Get List of OnPremiseSearchSettings
        api_response = api_instance.get_system_on_premise_search_setting(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of OnPremiseSearchSettingsApi->get_system_on_premise_search_setting:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OnPremiseSearchSettingsApi->get_system_on_premise_search_setting: %s\n" % e)
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

[**List[OnPremiseSearchSetting]**](OnPremiseSearchSetting.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of onPremiseSearchSettings |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_system_on_premise_search_setting_by_id**
> OnPremiseSearchSetting get_system_on_premise_search_setting_by_id(id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get OnPremiseSearchSettings

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.on_premise_search_setting import OnPremiseSearchSetting
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
    api_instance = connectwise_psa.OnPremiseSearchSettingsApi(api_client)
    id = 56 # int | OnPremiseSearchSettingId
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
        # Get OnPremiseSearchSettings
        api_response = api_instance.get_system_on_premise_search_setting_by_id(id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of OnPremiseSearchSettingsApi->get_system_on_premise_search_setting_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OnPremiseSearchSettingsApi->get_system_on_premise_search_setting_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| OnPremiseSearchSettingId | 
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

[**OnPremiseSearchSetting**](OnPremiseSearchSetting.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OnPremiseSearchSetting |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_system_on_premise_search_setting_count**
> Count get_system_on_premise_search_setting_count(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Count of OnPremiseSearchSettings

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
    api_instance = connectwise_psa.OnPremiseSearchSettingsApi(api_client)
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
        # Get Count of OnPremiseSearchSettings
        api_response = api_instance.get_system_on_premise_search_setting_count(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of OnPremiseSearchSettingsApi->get_system_on_premise_search_setting_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OnPremiseSearchSettingsApi->get_system_on_premise_search_setting_count: %s\n" % e)
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

# **patch_system_on_premise_search_setting_by_id**
> OnPremiseSearchSetting patch_system_on_premise_search_setting_by_id(id, client_id, patch_operation)

Patch OnPremiseSearchSettings

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.on_premise_search_setting import OnPremiseSearchSetting
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
    api_instance = connectwise_psa.OnPremiseSearchSettingsApi(api_client)
    id = 56 # int | OnPremiseSearchSettingId
    client_id = 'client_id_example' # str | 
    patch_operation = [connectwise_psa.PatchOperation()] # List[PatchOperation] | List of PatchOperation

    try:
        # Patch OnPremiseSearchSettings
        api_response = api_instance.patch_system_on_premise_search_setting_by_id(id, client_id, patch_operation)
        print("The response of OnPremiseSearchSettingsApi->patch_system_on_premise_search_setting_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OnPremiseSearchSettingsApi->patch_system_on_premise_search_setting_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| OnPremiseSearchSettingId | 
 **client_id** | **str**|  | 
 **patch_operation** | [**List[PatchOperation]**](PatchOperation.md)| List of PatchOperation | 

### Return type

[**OnPremiseSearchSetting**](OnPremiseSearchSetting.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OnPremiseSearch |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_system_on_premise_search_setting_by_id**
> OnPremiseSearchSetting put_system_on_premise_search_setting_by_id(id, client_id, on_premise_search_setting)

Put OnPremiseSearchSettings              This does not update Solr. This allows you to set Manage to the Solr password.

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.on_premise_search_setting import OnPremiseSearchSetting
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
    api_instance = connectwise_psa.OnPremiseSearchSettingsApi(api_client)
    id = 56 # int | OnPremiseSearchSettingId
    client_id = 'client_id_example' # str | 
    on_premise_search_setting = connectwise_psa.OnPremiseSearchSetting() # OnPremiseSearchSetting | onPremiseSearchSetting

    try:
        # Put OnPremiseSearchSettings              This does not update Solr. This allows you to set Manage to the Solr password.
        api_response = api_instance.put_system_on_premise_search_setting_by_id(id, client_id, on_premise_search_setting)
        print("The response of OnPremiseSearchSettingsApi->put_system_on_premise_search_setting_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OnPremiseSearchSettingsApi->put_system_on_premise_search_setting_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| OnPremiseSearchSettingId | 
 **client_id** | **str**|  | 
 **on_premise_search_setting** | [**OnPremiseSearchSetting**](OnPremiseSearchSetting.md)| onPremiseSearchSetting | 

### Return type

[**OnPremiseSearchSetting**](OnPremiseSearchSetting.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OnPremiseSearchSetting |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

