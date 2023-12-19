# connectwise_psa.ScheduleColorsApi

All URIs are relative to *https://aus-api.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_schedule_colors**](ScheduleColorsApi.md#get_schedule_colors) | **GET** /schedule/colors | Get List of ScheduleColor
[**get_schedule_colors_by_id**](ScheduleColorsApi.md#get_schedule_colors_by_id) | **GET** /schedule/colors/{id} | Get ScheduleColor
[**get_schedule_colors_count**](ScheduleColorsApi.md#get_schedule_colors_count) | **GET** /schedule/colors/count | Get Count of ScheduleColor
[**patch_schedule_colors_by_id**](ScheduleColorsApi.md#patch_schedule_colors_by_id) | **PATCH** /schedule/colors/{id} | Patch ScheduleColor
[**post_schedule_colors_by_id_clear**](ScheduleColorsApi.md#post_schedule_colors_by_id_clear) | **POST** /schedule/colors/{id}/clear | Post ScheduleColor
[**post_schedule_colors_reset**](ScheduleColorsApi.md#post_schedule_colors_reset) | **POST** /schedule/colors/reset | Post List of ScheduleColor
[**put_schedule_colors_by_id**](ScheduleColorsApi.md#put_schedule_colors_by_id) | **PUT** /schedule/colors/{id} | Put ScheduleColor


# **get_schedule_colors**
> List[ScheduleColor] get_schedule_colors(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of ScheduleColor

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.schedule_color import ScheduleColor
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
    api_instance = connectwise_psa.ScheduleColorsApi(api_client)
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
        # Get List of ScheduleColor
        api_response = api_instance.get_schedule_colors(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of ScheduleColorsApi->get_schedule_colors:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScheduleColorsApi->get_schedule_colors: %s\n" % e)
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

[**List[ScheduleColor]**](ScheduleColor.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of ScheduleColor |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_schedule_colors_by_id**
> ScheduleColor get_schedule_colors_by_id(id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get ScheduleColor

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.schedule_color import ScheduleColor
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
    api_instance = connectwise_psa.ScheduleColorsApi(api_client)
    id = 56 # int | colorId
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
        # Get ScheduleColor
        api_response = api_instance.get_schedule_colors_by_id(id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of ScheduleColorsApi->get_schedule_colors_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScheduleColorsApi->get_schedule_colors_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| colorId | 
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

[**ScheduleColor**](ScheduleColor.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ScheduleColor |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_schedule_colors_count**
> Count get_schedule_colors_count(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Count of ScheduleColor

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
    api_instance = connectwise_psa.ScheduleColorsApi(api_client)
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
        # Get Count of ScheduleColor
        api_response = api_instance.get_schedule_colors_count(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of ScheduleColorsApi->get_schedule_colors_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScheduleColorsApi->get_schedule_colors_count: %s\n" % e)
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

# **patch_schedule_colors_by_id**
> ScheduleColor patch_schedule_colors_by_id(id, client_id, patch_operation)

Patch ScheduleColor

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.patch_operation import PatchOperation
from connectwise_psa.models.schedule_color import ScheduleColor
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
    api_instance = connectwise_psa.ScheduleColorsApi(api_client)
    id = 56 # int | colorId
    client_id = 'client_id_example' # str | 
    patch_operation = [connectwise_psa.PatchOperation()] # List[PatchOperation] | List of PatchOperation

    try:
        # Patch ScheduleColor
        api_response = api_instance.patch_schedule_colors_by_id(id, client_id, patch_operation)
        print("The response of ScheduleColorsApi->patch_schedule_colors_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScheduleColorsApi->patch_schedule_colors_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| colorId | 
 **client_id** | **str**|  | 
 **patch_operation** | [**List[PatchOperation]**](PatchOperation.md)| List of PatchOperation | 

### Return type

[**ScheduleColor**](ScheduleColor.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ScheduleColor |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_schedule_colors_by_id_clear**
> ScheduleColor post_schedule_colors_by_id_clear(id, client_id)

Post ScheduleColor

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.schedule_color import ScheduleColor
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
    api_instance = connectwise_psa.ScheduleColorsApi(api_client)
    id = 56 # int | colorId
    client_id = 'client_id_example' # str | 

    try:
        # Post ScheduleColor
        api_response = api_instance.post_schedule_colors_by_id_clear(id, client_id)
        print("The response of ScheduleColorsApi->post_schedule_colors_by_id_clear:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScheduleColorsApi->post_schedule_colors_by_id_clear: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| colorId | 
 **client_id** | **str**|  | 

### Return type

[**ScheduleColor**](ScheduleColor.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ScheduleColor |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_schedule_colors_reset**
> List[ScheduleColor] post_schedule_colors_reset(client_id)

Post List of ScheduleColor

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.schedule_color import ScheduleColor
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
    api_instance = connectwise_psa.ScheduleColorsApi(api_client)
    client_id = 'client_id_example' # str | 

    try:
        # Post List of ScheduleColor
        api_response = api_instance.post_schedule_colors_reset(client_id)
        print("The response of ScheduleColorsApi->post_schedule_colors_reset:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScheduleColorsApi->post_schedule_colors_reset: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**|  | 

### Return type

[**List[ScheduleColor]**](ScheduleColor.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of ScheduleColor |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_schedule_colors_by_id**
> ScheduleColor put_schedule_colors_by_id(id, client_id, schedule_color)

Put ScheduleColor

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.schedule_color import ScheduleColor
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
    api_instance = connectwise_psa.ScheduleColorsApi(api_client)
    id = 56 # int | colorId
    client_id = 'client_id_example' # str | 
    schedule_color = connectwise_psa.ScheduleColor() # ScheduleColor | scheduleColor

    try:
        # Put ScheduleColor
        api_response = api_instance.put_schedule_colors_by_id(id, client_id, schedule_color)
        print("The response of ScheduleColorsApi->put_schedule_colors_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScheduleColorsApi->put_schedule_colors_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| colorId | 
 **client_id** | **str**|  | 
 **schedule_color** | [**ScheduleColor**](ScheduleColor.md)| scheduleColor | 

### Return type

[**ScheduleColor**](ScheduleColor.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ScheduleColor |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

