# connectwise_psa.ContactTracksApi

All URIs are relative to *https://aus-api.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_company_contacts_by_parent_id_tracks_by_id**](ContactTracksApi.md#delete_company_contacts_by_parent_id_tracks_by_id) | **DELETE** /company/contacts/{parentId}/tracks/{id} | Delete ContactTrack
[**get_company_contacts_by_parent_id_tracks**](ContactTracksApi.md#get_company_contacts_by_parent_id_tracks) | **GET** /company/contacts/{parentId}/tracks | Get List of ContactTrack
[**get_company_contacts_by_parent_id_tracks_by_id**](ContactTracksApi.md#get_company_contacts_by_parent_id_tracks_by_id) | **GET** /company/contacts/{parentId}/tracks/{id} | Get ContactTrack
[**get_company_contacts_by_parent_id_tracks_count**](ContactTracksApi.md#get_company_contacts_by_parent_id_tracks_count) | **GET** /company/contacts/{parentId}/tracks/count | Get Count of ContactTrack
[**post_company_contacts_by_parent_id_tracks**](ContactTracksApi.md#post_company_contacts_by_parent_id_tracks) | **POST** /company/contacts/{parentId}/tracks | Post ContactTrack


# **delete_company_contacts_by_parent_id_tracks_by_id**
> delete_company_contacts_by_parent_id_tracks_by_id(id, parent_id, client_id)

Delete ContactTrack

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
    api_instance = connectwise_psa.ContactTracksApi(api_client)
    id = 56 # int | trackId
    parent_id = 56 # int | contactId
    client_id = 'client_id_example' # str | 

    try:
        # Delete ContactTrack
        api_instance.delete_company_contacts_by_parent_id_tracks_by_id(id, parent_id, client_id)
    except Exception as e:
        print("Exception when calling ContactTracksApi->delete_company_contacts_by_parent_id_tracks_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| trackId | 
 **parent_id** | **int**| contactId | 
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

# **get_company_contacts_by_parent_id_tracks**
> List[ContactTrack] get_company_contacts_by_parent_id_tracks(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of ContactTrack

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.contact_track import ContactTrack
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
    api_instance = connectwise_psa.ContactTracksApi(api_client)
    parent_id = 56 # int | contactId
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
        # Get List of ContactTrack
        api_response = api_instance.get_company_contacts_by_parent_id_tracks(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of ContactTracksApi->get_company_contacts_by_parent_id_tracks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactTracksApi->get_company_contacts_by_parent_id_tracks: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| contactId | 
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

[**List[ContactTrack]**](ContactTrack.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of ContactTrack |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_company_contacts_by_parent_id_tracks_by_id**
> ContactTrack get_company_contacts_by_parent_id_tracks_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get ContactTrack

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.contact_track import ContactTrack
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
    api_instance = connectwise_psa.ContactTracksApi(api_client)
    id = 56 # int | trackId
    parent_id = 56 # int | contactId
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
        # Get ContactTrack
        api_response = api_instance.get_company_contacts_by_parent_id_tracks_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of ContactTracksApi->get_company_contacts_by_parent_id_tracks_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactTracksApi->get_company_contacts_by_parent_id_tracks_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| trackId | 
 **parent_id** | **int**| contactId | 
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

[**ContactTrack**](ContactTrack.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ContactTrack |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_company_contacts_by_parent_id_tracks_count**
> Count get_company_contacts_by_parent_id_tracks_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Count of ContactTrack

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
    api_instance = connectwise_psa.ContactTracksApi(api_client)
    parent_id = 56 # int | contactId
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
        # Get Count of ContactTrack
        api_response = api_instance.get_company_contacts_by_parent_id_tracks_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of ContactTracksApi->get_company_contacts_by_parent_id_tracks_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactTracksApi->get_company_contacts_by_parent_id_tracks_count: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| contactId | 
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

# **post_company_contacts_by_parent_id_tracks**
> ContactTrack post_company_contacts_by_parent_id_tracks(parent_id, client_id, contact_track)

Post ContactTrack

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.contact_track import ContactTrack
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
    api_instance = connectwise_psa.ContactTracksApi(api_client)
    parent_id = 56 # int | contactId
    client_id = 'client_id_example' # str | 
    contact_track = connectwise_psa.ContactTrack() # ContactTrack | track

    try:
        # Post ContactTrack
        api_response = api_instance.post_company_contacts_by_parent_id_tracks(parent_id, client_id, contact_track)
        print("The response of ContactTracksApi->post_company_contacts_by_parent_id_tracks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactTracksApi->post_company_contacts_by_parent_id_tracks: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| contactId | 
 **client_id** | **str**|  | 
 **contact_track** | [**ContactTrack**](ContactTrack.md)| track | 

### Return type

[**ContactTrack**](ContactTrack.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | ContactTrack |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

