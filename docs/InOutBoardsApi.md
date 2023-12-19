# connectwise_psa.InOutBoardsApi

All URIs are relative to *https://aus-api.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_system_in_out_boards_by_id**](InOutBoardsApi.md#delete_system_in_out_boards_by_id) | **DELETE** /system/inOutBoards/{id} | Delete InOutBoard
[**get_system_in_out_boards**](InOutBoardsApi.md#get_system_in_out_boards) | **GET** /system/inOutBoards | Get List of InOutBoard
[**get_system_in_out_boards_by_id**](InOutBoardsApi.md#get_system_in_out_boards_by_id) | **GET** /system/inOutBoards/{id} | Get InOutBoard
[**get_system_in_out_boards_count**](InOutBoardsApi.md#get_system_in_out_boards_count) | **GET** /system/inOutBoards/count | Get Count of InOutBoard
[**patch_system_in_out_boards_by_id**](InOutBoardsApi.md#patch_system_in_out_boards_by_id) | **PATCH** /system/inOutBoards/{id} | Patch InOutBoard
[**post_system_in_out_boards**](InOutBoardsApi.md#post_system_in_out_boards) | **POST** /system/inOutBoards | Post InOutBoard
[**put_system_in_out_boards_by_id**](InOutBoardsApi.md#put_system_in_out_boards_by_id) | **PUT** /system/inOutBoards/{id} | Put InOutBoard


# **delete_system_in_out_boards_by_id**
> delete_system_in_out_boards_by_id(id, client_id)

Delete InOutBoard

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
    api_instance = connectwise_psa.InOutBoardsApi(api_client)
    id = 56 # int | inOutBoardId
    client_id = 'client_id_example' # str | 

    try:
        # Delete InOutBoard
        api_instance.delete_system_in_out_boards_by_id(id, client_id)
    except Exception as e:
        print("Exception when calling InOutBoardsApi->delete_system_in_out_boards_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| inOutBoardId | 
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

# **get_system_in_out_boards**
> List[InOutBoard] get_system_in_out_boards(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of InOutBoard

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.in_out_board import InOutBoard
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
    api_instance = connectwise_psa.InOutBoardsApi(api_client)
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
        # Get List of InOutBoard
        api_response = api_instance.get_system_in_out_boards(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of InOutBoardsApi->get_system_in_out_boards:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InOutBoardsApi->get_system_in_out_boards: %s\n" % e)
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

[**List[InOutBoard]**](InOutBoard.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of InOutBoard |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_system_in_out_boards_by_id**
> InOutBoard get_system_in_out_boards_by_id(id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get InOutBoard

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.in_out_board import InOutBoard
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
    api_instance = connectwise_psa.InOutBoardsApi(api_client)
    id = 56 # int | inOutBoardId
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
        # Get InOutBoard
        api_response = api_instance.get_system_in_out_boards_by_id(id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of InOutBoardsApi->get_system_in_out_boards_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InOutBoardsApi->get_system_in_out_boards_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| inOutBoardId | 
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

[**InOutBoard**](InOutBoard.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | InOutBoard |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_system_in_out_boards_count**
> Count get_system_in_out_boards_count(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Count of InOutBoard

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
    api_instance = connectwise_psa.InOutBoardsApi(api_client)
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
        # Get Count of InOutBoard
        api_response = api_instance.get_system_in_out_boards_count(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of InOutBoardsApi->get_system_in_out_boards_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InOutBoardsApi->get_system_in_out_boards_count: %s\n" % e)
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

# **patch_system_in_out_boards_by_id**
> InOutBoard patch_system_in_out_boards_by_id(id, client_id, patch_operation)

Patch InOutBoard

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.in_out_board import InOutBoard
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
    api_instance = connectwise_psa.InOutBoardsApi(api_client)
    id = 56 # int | inOutBoardId
    client_id = 'client_id_example' # str | 
    patch_operation = [connectwise_psa.PatchOperation()] # List[PatchOperation] | List of PatchOperation

    try:
        # Patch InOutBoard
        api_response = api_instance.patch_system_in_out_boards_by_id(id, client_id, patch_operation)
        print("The response of InOutBoardsApi->patch_system_in_out_boards_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InOutBoardsApi->patch_system_in_out_boards_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| inOutBoardId | 
 **client_id** | **str**|  | 
 **patch_operation** | [**List[PatchOperation]**](PatchOperation.md)| List of PatchOperation | 

### Return type

[**InOutBoard**](InOutBoard.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | InOutBoard |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_system_in_out_boards**
> InOutBoard post_system_in_out_boards(client_id, in_out_board)

Post InOutBoard

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.in_out_board import InOutBoard
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
    api_instance = connectwise_psa.InOutBoardsApi(api_client)
    client_id = 'client_id_example' # str | 
    in_out_board = connectwise_psa.InOutBoard() # InOutBoard | inOutBoard

    try:
        # Post InOutBoard
        api_response = api_instance.post_system_in_out_boards(client_id, in_out_board)
        print("The response of InOutBoardsApi->post_system_in_out_boards:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InOutBoardsApi->post_system_in_out_boards: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**|  | 
 **in_out_board** | [**InOutBoard**](InOutBoard.md)| inOutBoard | 

### Return type

[**InOutBoard**](InOutBoard.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | InOutBoard |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_system_in_out_boards_by_id**
> InOutBoard put_system_in_out_boards_by_id(id, client_id, in_out_board)

Put InOutBoard

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.in_out_board import InOutBoard
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
    api_instance = connectwise_psa.InOutBoardsApi(api_client)
    id = 56 # int | inOutBoardId
    client_id = 'client_id_example' # str | 
    in_out_board = connectwise_psa.InOutBoard() # InOutBoard | inOutBoard

    try:
        # Put InOutBoard
        api_response = api_instance.put_system_in_out_boards_by_id(id, client_id, in_out_board)
        print("The response of InOutBoardsApi->put_system_in_out_boards_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InOutBoardsApi->put_system_in_out_boards_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| inOutBoardId | 
 **client_id** | **str**|  | 
 **in_out_board** | [**InOutBoard**](InOutBoard.md)| inOutBoard | 

### Return type

[**InOutBoard**](InOutBoard.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | InOutBoard |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

