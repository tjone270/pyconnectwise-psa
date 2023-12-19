# connectwise_psa.TicketStopwatchesApi

All URIs are relative to *https://api-aus.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_time_ticketstopwatches_by_id**](TicketStopwatchesApi.md#delete_time_ticketstopwatches_by_id) | **DELETE** /time/ticketstopwatches/{id} | Delete TicketStopwatch
[**get_time_ticketstopwatches**](TicketStopwatchesApi.md#get_time_ticketstopwatches) | **GET** /time/ticketstopwatches | Get List of TicketStopwatch
[**get_time_ticketstopwatches_by_id**](TicketStopwatchesApi.md#get_time_ticketstopwatches_by_id) | **GET** /time/ticketstopwatches/{id} | Get TicketStopwatch
[**get_time_ticketstopwatches_count**](TicketStopwatchesApi.md#get_time_ticketstopwatches_count) | **GET** /time/ticketstopwatches/count | Get Count of TicketStopwatch
[**patch_time_ticketstopwatches_by_id**](TicketStopwatchesApi.md#patch_time_ticketstopwatches_by_id) | **PATCH** /time/ticketstopwatches/{id} | Patch TicketStopwatch
[**post_time_ticketstopwatches**](TicketStopwatchesApi.md#post_time_ticketstopwatches) | **POST** /time/ticketstopwatches | Post TicketStopwatch
[**put_time_ticketstopwatches_by_id**](TicketStopwatchesApi.md#put_time_ticketstopwatches_by_id) | **PUT** /time/ticketstopwatches/{id} | Put TicketStopwatch


# **delete_time_ticketstopwatches_by_id**
> delete_time_ticketstopwatches_by_id(id, client_id)

Delete TicketStopwatch

### Example

```python
import time
import os
import connectwise_psa
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
    api_instance = connectwise_psa.TicketStopwatchesApi(api_client)
    id = 56 # int | ticketstopwatcheId
    client_id = 'client_id_example' # str | 

    try:
        # Delete TicketStopwatch
        api_instance.delete_time_ticketstopwatches_by_id(id, client_id)
    except Exception as e:
        print("Exception when calling TicketStopwatchesApi->delete_time_ticketstopwatches_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ticketstopwatcheId | 
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

# **get_time_ticketstopwatches**
> List[TicketStopwatch] get_time_ticketstopwatches(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of TicketStopwatch

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.ticket_stopwatch import TicketStopwatch
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
    api_instance = connectwise_psa.TicketStopwatchesApi(api_client)
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
        # Get List of TicketStopwatch
        api_response = api_instance.get_time_ticketstopwatches(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of TicketStopwatchesApi->get_time_ticketstopwatches:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TicketStopwatchesApi->get_time_ticketstopwatches: %s\n" % e)
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

[**List[TicketStopwatch]**](TicketStopwatch.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of TicketStopwatch |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_time_ticketstopwatches_by_id**
> TicketStopwatch get_time_ticketstopwatches_by_id(id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get TicketStopwatch

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.ticket_stopwatch import TicketStopwatch
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
    api_instance = connectwise_psa.TicketStopwatchesApi(api_client)
    id = 56 # int | ticketstopwatcheId
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
        # Get TicketStopwatch
        api_response = api_instance.get_time_ticketstopwatches_by_id(id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of TicketStopwatchesApi->get_time_ticketstopwatches_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TicketStopwatchesApi->get_time_ticketstopwatches_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ticketstopwatcheId | 
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

[**TicketStopwatch**](TicketStopwatch.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | TicketStopwatch |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_time_ticketstopwatches_count**
> Count get_time_ticketstopwatches_count(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Count of TicketStopwatch

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
    api_instance = connectwise_psa.TicketStopwatchesApi(api_client)
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
        # Get Count of TicketStopwatch
        api_response = api_instance.get_time_ticketstopwatches_count(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of TicketStopwatchesApi->get_time_ticketstopwatches_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TicketStopwatchesApi->get_time_ticketstopwatches_count: %s\n" % e)
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

# **patch_time_ticketstopwatches_by_id**
> TicketStopwatch patch_time_ticketstopwatches_by_id(id, client_id, patch_operation)

Patch TicketStopwatch

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.patch_operation import PatchOperation
from connectwise_psa.models.ticket_stopwatch import TicketStopwatch
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
    api_instance = connectwise_psa.TicketStopwatchesApi(api_client)
    id = 56 # int | ticketstopwatcheId
    client_id = 'client_id_example' # str | 
    patch_operation = [connectwise_psa.PatchOperation()] # List[PatchOperation] | List of PatchOperation

    try:
        # Patch TicketStopwatch
        api_response = api_instance.patch_time_ticketstopwatches_by_id(id, client_id, patch_operation)
        print("The response of TicketStopwatchesApi->patch_time_ticketstopwatches_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TicketStopwatchesApi->patch_time_ticketstopwatches_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ticketstopwatcheId | 
 **client_id** | **str**|  | 
 **patch_operation** | [**List[PatchOperation]**](PatchOperation.md)| List of PatchOperation | 

### Return type

[**TicketStopwatch**](TicketStopwatch.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | TicketStopwatch |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_time_ticketstopwatches**
> TicketStopwatch post_time_ticketstopwatches(client_id, ticket_stopwatch)

Post TicketStopwatch

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.ticket_stopwatch import TicketStopwatch
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
    api_instance = connectwise_psa.TicketStopwatchesApi(api_client)
    client_id = 'client_id_example' # str | 
    ticket_stopwatch = connectwise_psa.TicketStopwatch() # TicketStopwatch | ticketStopwatch

    try:
        # Post TicketStopwatch
        api_response = api_instance.post_time_ticketstopwatches(client_id, ticket_stopwatch)
        print("The response of TicketStopwatchesApi->post_time_ticketstopwatches:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TicketStopwatchesApi->post_time_ticketstopwatches: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**|  | 
 **ticket_stopwatch** | [**TicketStopwatch**](TicketStopwatch.md)| ticketStopwatch | 

### Return type

[**TicketStopwatch**](TicketStopwatch.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | TicketStopwatch |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_time_ticketstopwatches_by_id**
> TicketStopwatch put_time_ticketstopwatches_by_id(id, client_id, ticket_stopwatch)

Put TicketStopwatch

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.ticket_stopwatch import TicketStopwatch
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
    api_instance = connectwise_psa.TicketStopwatchesApi(api_client)
    id = 56 # int | ticketstopwatcheId
    client_id = 'client_id_example' # str | 
    ticket_stopwatch = connectwise_psa.TicketStopwatch() # TicketStopwatch | ticketStopwatch

    try:
        # Put TicketStopwatch
        api_response = api_instance.put_time_ticketstopwatches_by_id(id, client_id, ticket_stopwatch)
        print("The response of TicketStopwatchesApi->put_time_ticketstopwatches_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TicketStopwatchesApi->put_time_ticketstopwatches_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ticketstopwatcheId | 
 **client_id** | **str**|  | 
 **ticket_stopwatch** | [**TicketStopwatch**](TicketStopwatch.md)| ticketStopwatch | 

### Return type

[**TicketStopwatch**](TicketStopwatch.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | TicketStopwatch |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

