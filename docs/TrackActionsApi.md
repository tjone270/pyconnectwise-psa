# connectwise_psa.TrackActionsApi

All URIs are relative to *https://api-aus.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_company_tracks_by_parent_id_actions_by_id**](TrackActionsApi.md#delete_company_tracks_by_parent_id_actions_by_id) | **DELETE** /company/tracks/{parentId}/actions/{id} | Delete TrackAction
[**get_company_tracks_by_parent_id_actions**](TrackActionsApi.md#get_company_tracks_by_parent_id_actions) | **GET** /company/tracks/{parentId}/actions | Get List of TrackAction
[**get_company_tracks_by_parent_id_actions_by_id**](TrackActionsApi.md#get_company_tracks_by_parent_id_actions_by_id) | **GET** /company/tracks/{parentId}/actions/{id} | Get TrackAction
[**get_company_tracks_by_parent_id_actions_count**](TrackActionsApi.md#get_company_tracks_by_parent_id_actions_count) | **GET** /company/tracks/{parentId}/actions/count | Get Count of TrackAction
[**patch_company_tracks_by_parent_id_actions_by_id**](TrackActionsApi.md#patch_company_tracks_by_parent_id_actions_by_id) | **PATCH** /company/tracks/{parentId}/actions/{id} | Patch TrackAction
[**post_company_tracks_by_parent_id_actions**](TrackActionsApi.md#post_company_tracks_by_parent_id_actions) | **POST** /company/tracks/{parentId}/actions | Post TrackAction
[**put_company_tracks_by_parent_id_actions_by_id**](TrackActionsApi.md#put_company_tracks_by_parent_id_actions_by_id) | **PUT** /company/tracks/{parentId}/actions/{id} | Put TrackAction


# **delete_company_tracks_by_parent_id_actions_by_id**
> delete_company_tracks_by_parent_id_actions_by_id(id, parent_id, client_id)

Delete TrackAction

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
    api_instance = connectwise_psa.TrackActionsApi(api_client)
    id = 56 # int | actionId
    parent_id = 56 # int | trackId
    client_id = 'client_id_example' # str | 

    try:
        # Delete TrackAction
        api_instance.delete_company_tracks_by_parent_id_actions_by_id(id, parent_id, client_id)
    except Exception as e:
        print("Exception when calling TrackActionsApi->delete_company_tracks_by_parent_id_actions_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| actionId | 
 **parent_id** | **int**| trackId | 
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

# **get_company_tracks_by_parent_id_actions**
> List[TrackAction] get_company_tracks_by_parent_id_actions(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of TrackAction

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.track_action import TrackAction
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
    api_instance = connectwise_psa.TrackActionsApi(api_client)
    parent_id = 56 # int | trackId
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
        # Get List of TrackAction
        api_response = api_instance.get_company_tracks_by_parent_id_actions(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of TrackActionsApi->get_company_tracks_by_parent_id_actions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackActionsApi->get_company_tracks_by_parent_id_actions: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| trackId | 
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

[**List[TrackAction]**](TrackAction.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of TrackAction |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_company_tracks_by_parent_id_actions_by_id**
> TrackAction get_company_tracks_by_parent_id_actions_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get TrackAction

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.track_action import TrackAction
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
    api_instance = connectwise_psa.TrackActionsApi(api_client)
    id = 56 # int | actionId
    parent_id = 56 # int | trackId
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
        # Get TrackAction
        api_response = api_instance.get_company_tracks_by_parent_id_actions_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of TrackActionsApi->get_company_tracks_by_parent_id_actions_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackActionsApi->get_company_tracks_by_parent_id_actions_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| actionId | 
 **parent_id** | **int**| trackId | 
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

[**TrackAction**](TrackAction.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | TrackAction |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_company_tracks_by_parent_id_actions_count**
> Count get_company_tracks_by_parent_id_actions_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Count of TrackAction

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
    api_instance = connectwise_psa.TrackActionsApi(api_client)
    parent_id = 56 # int | trackId
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
        # Get Count of TrackAction
        api_response = api_instance.get_company_tracks_by_parent_id_actions_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of TrackActionsApi->get_company_tracks_by_parent_id_actions_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackActionsApi->get_company_tracks_by_parent_id_actions_count: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| trackId | 
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

# **patch_company_tracks_by_parent_id_actions_by_id**
> TrackAction patch_company_tracks_by_parent_id_actions_by_id(id, parent_id, client_id)

Patch TrackAction

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.track_action import TrackAction
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
    api_instance = connectwise_psa.TrackActionsApi(api_client)
    id = 56 # int | actionId
    parent_id = 56 # int | trackId
    client_id = 'client_id_example' # str | 

    try:
        # Patch TrackAction
        api_response = api_instance.patch_company_tracks_by_parent_id_actions_by_id(id, parent_id, client_id)
        print("The response of TrackActionsApi->patch_company_tracks_by_parent_id_actions_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackActionsApi->patch_company_tracks_by_parent_id_actions_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| actionId | 
 **parent_id** | **int**| trackId | 
 **client_id** | **str**|  | 

### Return type

[**TrackAction**](TrackAction.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | TrackAction |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_company_tracks_by_parent_id_actions**
> TrackAction post_company_tracks_by_parent_id_actions(parent_id, client_id, track_action)

Post TrackAction

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.track_action import TrackAction
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
    api_instance = connectwise_psa.TrackActionsApi(api_client)
    parent_id = 56 # int | trackId
    client_id = 'client_id_example' # str | 
    track_action = connectwise_psa.TrackAction() # TrackAction | trackAction

    try:
        # Post TrackAction
        api_response = api_instance.post_company_tracks_by_parent_id_actions(parent_id, client_id, track_action)
        print("The response of TrackActionsApi->post_company_tracks_by_parent_id_actions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackActionsApi->post_company_tracks_by_parent_id_actions: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| trackId | 
 **client_id** | **str**|  | 
 **track_action** | [**TrackAction**](TrackAction.md)| trackAction | 

### Return type

[**TrackAction**](TrackAction.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | TrackAction |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_company_tracks_by_parent_id_actions_by_id**
> TrackAction put_company_tracks_by_parent_id_actions_by_id(id, parent_id, client_id, track_action)

Put TrackAction

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.track_action import TrackAction
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
    api_instance = connectwise_psa.TrackActionsApi(api_client)
    id = 56 # int | actionId
    parent_id = 56 # int | trackId
    client_id = 'client_id_example' # str | 
    track_action = connectwise_psa.TrackAction() # TrackAction | trackAction

    try:
        # Put TrackAction
        api_response = api_instance.put_company_tracks_by_parent_id_actions_by_id(id, parent_id, client_id, track_action)
        print("The response of TrackActionsApi->put_company_tracks_by_parent_id_actions_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackActionsApi->put_company_tracks_by_parent_id_actions_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| actionId | 
 **parent_id** | **int**| trackId | 
 **client_id** | **str**|  | 
 **track_action** | [**TrackAction**](TrackAction.md)| trackAction | 

### Return type

[**TrackAction**](TrackAction.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | TrackAction |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

