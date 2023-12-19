# connectwise_psa.MenuEntryLocationsApi

All URIs are relative to *https://aus-api.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_system_menu_entries_by_parent_id_locations_by_id**](MenuEntryLocationsApi.md#delete_system_menu_entries_by_parent_id_locations_by_id) | **DELETE** /system/menuEntries/{parentId}/locations/{id} | Delete MenuEntryLocation
[**get_system_menu_entries_by_parent_id_locations**](MenuEntryLocationsApi.md#get_system_menu_entries_by_parent_id_locations) | **GET** /system/menuEntries/{parentId}/locations | Get List of MenuEntryLocation
[**get_system_menu_entries_by_parent_id_locations_by_id**](MenuEntryLocationsApi.md#get_system_menu_entries_by_parent_id_locations_by_id) | **GET** /system/menuEntries/{parentId}/locations/{id} | Get MenuEntryLocation
[**get_system_menu_entries_by_parent_id_locations_count**](MenuEntryLocationsApi.md#get_system_menu_entries_by_parent_id_locations_count) | **GET** /system/menuEntries/{parentId}/locations/count | Get Count of MenuEntryLocation
[**post_system_menu_entries_by_parent_id_locations**](MenuEntryLocationsApi.md#post_system_menu_entries_by_parent_id_locations) | **POST** /system/menuEntries/{parentId}/locations | Post MenuEntryLocation


# **delete_system_menu_entries_by_parent_id_locations_by_id**
> delete_system_menu_entries_by_parent_id_locations_by_id(id, parent_id, client_id)

Delete MenuEntryLocation

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
    api_instance = connectwise_psa.MenuEntryLocationsApi(api_client)
    id = 56 # int | locationId
    parent_id = 56 # int | menuEntryId
    client_id = 'client_id_example' # str | 

    try:
        # Delete MenuEntryLocation
        api_instance.delete_system_menu_entries_by_parent_id_locations_by_id(id, parent_id, client_id)
    except Exception as e:
        print("Exception when calling MenuEntryLocationsApi->delete_system_menu_entries_by_parent_id_locations_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| locationId | 
 **parent_id** | **int**| menuEntryId | 
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

# **get_system_menu_entries_by_parent_id_locations**
> List[MenuEntryLocation] get_system_menu_entries_by_parent_id_locations(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of MenuEntryLocation

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.menu_entry_location import MenuEntryLocation
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
    api_instance = connectwise_psa.MenuEntryLocationsApi(api_client)
    parent_id = 56 # int | menuEntryId
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
        # Get List of MenuEntryLocation
        api_response = api_instance.get_system_menu_entries_by_parent_id_locations(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of MenuEntryLocationsApi->get_system_menu_entries_by_parent_id_locations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MenuEntryLocationsApi->get_system_menu_entries_by_parent_id_locations: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| menuEntryId | 
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

[**List[MenuEntryLocation]**](MenuEntryLocation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of MenuEntryLocation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_system_menu_entries_by_parent_id_locations_by_id**
> MenuEntryLocation get_system_menu_entries_by_parent_id_locations_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get MenuEntryLocation

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.menu_entry_location import MenuEntryLocation
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
    api_instance = connectwise_psa.MenuEntryLocationsApi(api_client)
    id = 56 # int | locationId
    parent_id = 56 # int | menuEntryId
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
        # Get MenuEntryLocation
        api_response = api_instance.get_system_menu_entries_by_parent_id_locations_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of MenuEntryLocationsApi->get_system_menu_entries_by_parent_id_locations_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MenuEntryLocationsApi->get_system_menu_entries_by_parent_id_locations_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| locationId | 
 **parent_id** | **int**| menuEntryId | 
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

[**MenuEntryLocation**](MenuEntryLocation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | MenuEntryLocation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_system_menu_entries_by_parent_id_locations_count**
> Count get_system_menu_entries_by_parent_id_locations_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Count of MenuEntryLocation

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
    api_instance = connectwise_psa.MenuEntryLocationsApi(api_client)
    parent_id = 56 # int | menuEntryId
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
        # Get Count of MenuEntryLocation
        api_response = api_instance.get_system_menu_entries_by_parent_id_locations_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of MenuEntryLocationsApi->get_system_menu_entries_by_parent_id_locations_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MenuEntryLocationsApi->get_system_menu_entries_by_parent_id_locations_count: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| menuEntryId | 
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

# **post_system_menu_entries_by_parent_id_locations**
> MenuEntryLocation post_system_menu_entries_by_parent_id_locations(parent_id, client_id, menu_entry_location)

Post MenuEntryLocation

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.menu_entry_location import MenuEntryLocation
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
    api_instance = connectwise_psa.MenuEntryLocationsApi(api_client)
    parent_id = 56 # int | menuEntryId
    client_id = 'client_id_example' # str | 
    menu_entry_location = connectwise_psa.MenuEntryLocation() # MenuEntryLocation | menuEntryLocation

    try:
        # Post MenuEntryLocation
        api_response = api_instance.post_system_menu_entries_by_parent_id_locations(parent_id, client_id, menu_entry_location)
        print("The response of MenuEntryLocationsApi->post_system_menu_entries_by_parent_id_locations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MenuEntryLocationsApi->post_system_menu_entries_by_parent_id_locations: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| menuEntryId | 
 **client_id** | **str**|  | 
 **menu_entry_location** | [**MenuEntryLocation**](MenuEntryLocation.md)| menuEntryLocation | 

### Return type

[**MenuEntryLocation**](MenuEntryLocation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | MenuEntryLocation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

