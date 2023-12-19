# connectwise_psa.HolidaysApi

All URIs are relative to *https://aus-api.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_schedule_holiday_lists_by_parent_id_holidays_by_id**](HolidaysApi.md#delete_schedule_holiday_lists_by_parent_id_holidays_by_id) | **DELETE** /schedule/holidayLists/{parentId}/holidays/{id} | Delete Holiday
[**get_schedule_holiday_lists_by_parent_id_holidays**](HolidaysApi.md#get_schedule_holiday_lists_by_parent_id_holidays) | **GET** /schedule/holidayLists/{parentId}/holidays | Get List of Holiday
[**get_schedule_holiday_lists_by_parent_id_holidays_by_id**](HolidaysApi.md#get_schedule_holiday_lists_by_parent_id_holidays_by_id) | **GET** /schedule/holidayLists/{parentId}/holidays/{id} | Get Holiday
[**get_schedule_holiday_lists_by_parent_id_holidays_count**](HolidaysApi.md#get_schedule_holiday_lists_by_parent_id_holidays_count) | **GET** /schedule/holidayLists/{parentId}/holidays/count | Get Count of Holiday
[**patch_schedule_holiday_lists_by_parent_id_holidays_by_id**](HolidaysApi.md#patch_schedule_holiday_lists_by_parent_id_holidays_by_id) | **PATCH** /schedule/holidayLists/{parentId}/holidays/{id} | Patch Holiday
[**post_schedule_holiday_lists_by_parent_id_holidays**](HolidaysApi.md#post_schedule_holiday_lists_by_parent_id_holidays) | **POST** /schedule/holidayLists/{parentId}/holidays | Post Holiday
[**put_schedule_holiday_lists_by_parent_id_holidays_by_id**](HolidaysApi.md#put_schedule_holiday_lists_by_parent_id_holidays_by_id) | **PUT** /schedule/holidayLists/{parentId}/holidays/{id} | Put Holiday


# **delete_schedule_holiday_lists_by_parent_id_holidays_by_id**
> delete_schedule_holiday_lists_by_parent_id_holidays_by_id(id, parent_id, client_id)

Delete Holiday

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
    api_instance = connectwise_psa.HolidaysApi(api_client)
    id = 56 # int | holidayId
    parent_id = 56 # int | holidayListId
    client_id = 'client_id_example' # str | 

    try:
        # Delete Holiday
        api_instance.delete_schedule_holiday_lists_by_parent_id_holidays_by_id(id, parent_id, client_id)
    except Exception as e:
        print("Exception when calling HolidaysApi->delete_schedule_holiday_lists_by_parent_id_holidays_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| holidayId | 
 **parent_id** | **int**| holidayListId | 
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

# **get_schedule_holiday_lists_by_parent_id_holidays**
> List[Holiday] get_schedule_holiday_lists_by_parent_id_holidays(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of Holiday

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.holiday import Holiday
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
    api_instance = connectwise_psa.HolidaysApi(api_client)
    parent_id = 56 # int | holidayListId
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
        # Get List of Holiday
        api_response = api_instance.get_schedule_holiday_lists_by_parent_id_holidays(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of HolidaysApi->get_schedule_holiday_lists_by_parent_id_holidays:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HolidaysApi->get_schedule_holiday_lists_by_parent_id_holidays: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| holidayListId | 
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

[**List[Holiday]**](Holiday.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of Holiday |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_schedule_holiday_lists_by_parent_id_holidays_by_id**
> Holiday get_schedule_holiday_lists_by_parent_id_holidays_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Holiday

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.holiday import Holiday
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
    api_instance = connectwise_psa.HolidaysApi(api_client)
    id = 56 # int | holidayId
    parent_id = 56 # int | holidayListId
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
        # Get Holiday
        api_response = api_instance.get_schedule_holiday_lists_by_parent_id_holidays_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of HolidaysApi->get_schedule_holiday_lists_by_parent_id_holidays_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HolidaysApi->get_schedule_holiday_lists_by_parent_id_holidays_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| holidayId | 
 **parent_id** | **int**| holidayListId | 
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

[**Holiday**](Holiday.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Holiday |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_schedule_holiday_lists_by_parent_id_holidays_count**
> Count get_schedule_holiday_lists_by_parent_id_holidays_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Count of Holiday

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
    api_instance = connectwise_psa.HolidaysApi(api_client)
    parent_id = 56 # int | holidayListId
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
        # Get Count of Holiday
        api_response = api_instance.get_schedule_holiday_lists_by_parent_id_holidays_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of HolidaysApi->get_schedule_holiday_lists_by_parent_id_holidays_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HolidaysApi->get_schedule_holiday_lists_by_parent_id_holidays_count: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| holidayListId | 
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

# **patch_schedule_holiday_lists_by_parent_id_holidays_by_id**
> Holiday patch_schedule_holiday_lists_by_parent_id_holidays_by_id(id, parent_id, client_id, patch_operation)

Patch Holiday

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.holiday import Holiday
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
    api_instance = connectwise_psa.HolidaysApi(api_client)
    id = 56 # int | holidayId
    parent_id = 56 # int | holidayListId
    client_id = 'client_id_example' # str | 
    patch_operation = [connectwise_psa.PatchOperation()] # List[PatchOperation] | List of PatchOperation

    try:
        # Patch Holiday
        api_response = api_instance.patch_schedule_holiday_lists_by_parent_id_holidays_by_id(id, parent_id, client_id, patch_operation)
        print("The response of HolidaysApi->patch_schedule_holiday_lists_by_parent_id_holidays_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HolidaysApi->patch_schedule_holiday_lists_by_parent_id_holidays_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| holidayId | 
 **parent_id** | **int**| holidayListId | 
 **client_id** | **str**|  | 
 **patch_operation** | [**List[PatchOperation]**](PatchOperation.md)| List of PatchOperation | 

### Return type

[**Holiday**](Holiday.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Holiday |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_schedule_holiday_lists_by_parent_id_holidays**
> Holiday post_schedule_holiday_lists_by_parent_id_holidays(parent_id, client_id, holiday)

Post Holiday

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.holiday import Holiday
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
    api_instance = connectwise_psa.HolidaysApi(api_client)
    parent_id = 56 # int | holidayListId
    client_id = 'client_id_example' # str | 
    holiday = connectwise_psa.Holiday() # Holiday | holiday

    try:
        # Post Holiday
        api_response = api_instance.post_schedule_holiday_lists_by_parent_id_holidays(parent_id, client_id, holiday)
        print("The response of HolidaysApi->post_schedule_holiday_lists_by_parent_id_holidays:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HolidaysApi->post_schedule_holiday_lists_by_parent_id_holidays: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| holidayListId | 
 **client_id** | **str**|  | 
 **holiday** | [**Holiday**](Holiday.md)| holiday | 

### Return type

[**Holiday**](Holiday.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Holiday |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_schedule_holiday_lists_by_parent_id_holidays_by_id**
> Holiday put_schedule_holiday_lists_by_parent_id_holidays_by_id(id, parent_id, client_id, holiday)

Put Holiday

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.holiday import Holiday
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
    api_instance = connectwise_psa.HolidaysApi(api_client)
    id = 56 # int | holidayId
    parent_id = 56 # int | holidayListId
    client_id = 'client_id_example' # str | 
    holiday = connectwise_psa.Holiday() # Holiday | holiday

    try:
        # Put Holiday
        api_response = api_instance.put_schedule_holiday_lists_by_parent_id_holidays_by_id(id, parent_id, client_id, holiday)
        print("The response of HolidaysApi->put_schedule_holiday_lists_by_parent_id_holidays_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HolidaysApi->put_schedule_holiday_lists_by_parent_id_holidays_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| holidayId | 
 **parent_id** | **int**| holidayListId | 
 **client_id** | **str**|  | 
 **holiday** | [**Holiday**](Holiday.md)| holiday | 

### Return type

[**Holiday**](Holiday.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Holiday |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

