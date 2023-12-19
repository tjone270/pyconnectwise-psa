# connectwise_psa.TimeSheetsApi

All URIs are relative to *https://aus-api.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_time_sheets_by_id**](TimeSheetsApi.md#delete_time_sheets_by_id) | **DELETE** /time/sheets/{id} | Delete TimeSheet
[**get_time_sheets**](TimeSheetsApi.md#get_time_sheets) | **GET** /time/sheets | Get List of TimeSheet
[**get_time_sheets_by_id**](TimeSheetsApi.md#get_time_sheets_by_id) | **GET** /time/sheets/{id} | Get TimeSheet
[**get_time_sheets_count**](TimeSheetsApi.md#get_time_sheets_count) | **GET** /time/sheets/count | Get Count of TimeSheet
[**post_time_sheets_by_id_approve**](TimeSheetsApi.md#post_time_sheets_by_id_approve) | **POST** /time/sheets/{id}/approve | Post SuccessResponse
[**post_time_sheets_by_id_reject**](TimeSheetsApi.md#post_time_sheets_by_id_reject) | **POST** /time/sheets/{id}/reject | Post SuccessResponse
[**post_time_sheets_by_id_reverse**](TimeSheetsApi.md#post_time_sheets_by_id_reverse) | **POST** /time/sheets/{id}/reverse | Post SuccessResponse
[**post_time_sheets_by_id_submit**](TimeSheetsApi.md#post_time_sheets_by_id_submit) | **POST** /time/sheets/{id}/submit | Post SuccessResponse


# **delete_time_sheets_by_id**
> delete_time_sheets_by_id(id, client_id)

Delete TimeSheet

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
    api_instance = connectwise_psa.TimeSheetsApi(api_client)
    id = 56 # int | workTypeId
    client_id = 'client_id_example' # str | 

    try:
        # Delete TimeSheet
        api_instance.delete_time_sheets_by_id(id, client_id)
    except Exception as e:
        print("Exception when calling TimeSheetsApi->delete_time_sheets_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| workTypeId | 
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

# **get_time_sheets**
> List[TimeSheet] get_time_sheets(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of TimeSheet

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.time_sheet import TimeSheet
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
    api_instance = connectwise_psa.TimeSheetsApi(api_client)
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
        # Get List of TimeSheet
        api_response = api_instance.get_time_sheets(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of TimeSheetsApi->get_time_sheets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TimeSheetsApi->get_time_sheets: %s\n" % e)
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

[**List[TimeSheet]**](TimeSheet.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of TimeSheet |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_time_sheets_by_id**
> TimeSheet get_time_sheets_by_id(id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get TimeSheet

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.time_sheet import TimeSheet
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
    api_instance = connectwise_psa.TimeSheetsApi(api_client)
    id = 56 # int | sheetId
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
        # Get TimeSheet
        api_response = api_instance.get_time_sheets_by_id(id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of TimeSheetsApi->get_time_sheets_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TimeSheetsApi->get_time_sheets_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| sheetId | 
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

[**TimeSheet**](TimeSheet.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | TimeSheet |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_time_sheets_count**
> Count get_time_sheets_count(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Count of TimeSheet

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
    api_instance = connectwise_psa.TimeSheetsApi(api_client)
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
        # Get Count of TimeSheet
        api_response = api_instance.get_time_sheets_count(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of TimeSheetsApi->get_time_sheets_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TimeSheetsApi->get_time_sheets_count: %s\n" % e)
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

# **post_time_sheets_by_id_approve**
> SuccessResponse post_time_sheets_by_id_approve(id, client_id, time_sheet_tier_update)

Post SuccessResponse

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.success_response import SuccessResponse
from connectwise_psa.models.time_sheet_tier_update import TimeSheetTierUpdate
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
    api_instance = connectwise_psa.TimeSheetsApi(api_client)
    id = 56 # int | sheetId
    client_id = 'client_id_example' # str | 
    time_sheet_tier_update = connectwise_psa.TimeSheetTierUpdate() # TimeSheetTierUpdate | sheetId

    try:
        # Post SuccessResponse
        api_response = api_instance.post_time_sheets_by_id_approve(id, client_id, time_sheet_tier_update)
        print("The response of TimeSheetsApi->post_time_sheets_by_id_approve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TimeSheetsApi->post_time_sheets_by_id_approve: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| sheetId | 
 **client_id** | **str**|  | 
 **time_sheet_tier_update** | [**TimeSheetTierUpdate**](TimeSheetTierUpdate.md)| sheetId | 

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
**200** | SuccessResponse |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_time_sheets_by_id_reject**
> SuccessResponse post_time_sheets_by_id_reject(id, client_id)

Post SuccessResponse

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
    api_instance = connectwise_psa.TimeSheetsApi(api_client)
    id = 56 # int | sheetId
    client_id = 'client_id_example' # str | 

    try:
        # Post SuccessResponse
        api_response = api_instance.post_time_sheets_by_id_reject(id, client_id)
        print("The response of TimeSheetsApi->post_time_sheets_by_id_reject:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TimeSheetsApi->post_time_sheets_by_id_reject: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| sheetId | 
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
**200** | SuccessResponse |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_time_sheets_by_id_reverse**
> SuccessResponse post_time_sheets_by_id_reverse(id, client_id)

Post SuccessResponse

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
    api_instance = connectwise_psa.TimeSheetsApi(api_client)
    id = 56 # int | sheetId
    client_id = 'client_id_example' # str | 

    try:
        # Post SuccessResponse
        api_response = api_instance.post_time_sheets_by_id_reverse(id, client_id)
        print("The response of TimeSheetsApi->post_time_sheets_by_id_reverse:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TimeSheetsApi->post_time_sheets_by_id_reverse: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| sheetId | 
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
**200** | SuccessResponse |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_time_sheets_by_id_submit**
> SuccessResponse post_time_sheets_by_id_submit(id, client_id)

Post SuccessResponse

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
    api_instance = connectwise_psa.TimeSheetsApi(api_client)
    id = 56 # int | sheetId
    client_id = 'client_id_example' # str | 

    try:
        # Post SuccessResponse
        api_response = api_instance.post_time_sheets_by_id_submit(id, client_id)
        print("The response of TimeSheetsApi->post_time_sheets_by_id_submit:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TimeSheetsApi->post_time_sheets_by_id_submit: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| sheetId | 
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
**200** | SuccessResponse |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

