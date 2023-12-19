# connectwise_psa.ServiceTicketLinksApi

All URIs are relative to *https://aus-api.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_service_ticket_links_by_id**](ServiceTicketLinksApi.md#delete_service_ticket_links_by_id) | **DELETE** /service/ticketLinks/{id} | Delete ServiceTicketLink
[**get_service_ticket_links**](ServiceTicketLinksApi.md#get_service_ticket_links) | **GET** /service/ticketLinks | Get List of ServiceTicketLink
[**get_service_ticket_links_by_id**](ServiceTicketLinksApi.md#get_service_ticket_links_by_id) | **GET** /service/ticketLinks/{id} | Get ServiceTicketLink
[**get_service_ticket_links_count**](ServiceTicketLinksApi.md#get_service_ticket_links_count) | **GET** /service/ticketLinks/count | Get Count of ServiceTicketLink
[**patch_service_ticket_links_by_id**](ServiceTicketLinksApi.md#patch_service_ticket_links_by_id) | **PATCH** /service/ticketLinks/{id} | Patch ServiceTicketLink
[**post_service_ticket_links**](ServiceTicketLinksApi.md#post_service_ticket_links) | **POST** /service/ticketLinks | Post ServiceTicketLink
[**put_service_ticket_links_by_id**](ServiceTicketLinksApi.md#put_service_ticket_links_by_id) | **PUT** /service/ticketLinks/{id} | Put ServiceTicketLink


# **delete_service_ticket_links_by_id**
> delete_service_ticket_links_by_id(id, client_id)

Delete ServiceTicketLink

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
    api_instance = connectwise_psa.ServiceTicketLinksApi(api_client)
    id = 56 # int | ticketLinkId
    client_id = 'client_id_example' # str | 

    try:
        # Delete ServiceTicketLink
        api_instance.delete_service_ticket_links_by_id(id, client_id)
    except Exception as e:
        print("Exception when calling ServiceTicketLinksApi->delete_service_ticket_links_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ticketLinkId | 
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

# **get_service_ticket_links**
> List[ServiceTicketLink] get_service_ticket_links(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of ServiceTicketLink

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.service_ticket_link import ServiceTicketLink
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
    api_instance = connectwise_psa.ServiceTicketLinksApi(api_client)
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
        # Get List of ServiceTicketLink
        api_response = api_instance.get_service_ticket_links(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of ServiceTicketLinksApi->get_service_ticket_links:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceTicketLinksApi->get_service_ticket_links: %s\n" % e)
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

[**List[ServiceTicketLink]**](ServiceTicketLink.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of ServiceTicketLink |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_service_ticket_links_by_id**
> ServiceTicketLink get_service_ticket_links_by_id(id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get ServiceTicketLink

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.service_ticket_link import ServiceTicketLink
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
    api_instance = connectwise_psa.ServiceTicketLinksApi(api_client)
    id = 56 # int | ticketLinkId
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
        # Get ServiceTicketLink
        api_response = api_instance.get_service_ticket_links_by_id(id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of ServiceTicketLinksApi->get_service_ticket_links_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceTicketLinksApi->get_service_ticket_links_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ticketLinkId | 
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

[**ServiceTicketLink**](ServiceTicketLink.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ServiceTicketLink |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_service_ticket_links_count**
> Count get_service_ticket_links_count(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Count of ServiceTicketLink

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
    api_instance = connectwise_psa.ServiceTicketLinksApi(api_client)
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
        # Get Count of ServiceTicketLink
        api_response = api_instance.get_service_ticket_links_count(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of ServiceTicketLinksApi->get_service_ticket_links_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceTicketLinksApi->get_service_ticket_links_count: %s\n" % e)
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

# **patch_service_ticket_links_by_id**
> ServiceTicketLink patch_service_ticket_links_by_id(id, client_id, patch_operation)

Patch ServiceTicketLink

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.patch_operation import PatchOperation
from connectwise_psa.models.service_ticket_link import ServiceTicketLink
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
    api_instance = connectwise_psa.ServiceTicketLinksApi(api_client)
    id = 56 # int | ticketLinkId
    client_id = 'client_id_example' # str | 
    patch_operation = [connectwise_psa.PatchOperation()] # List[PatchOperation] | List of PatchOperation

    try:
        # Patch ServiceTicketLink
        api_response = api_instance.patch_service_ticket_links_by_id(id, client_id, patch_operation)
        print("The response of ServiceTicketLinksApi->patch_service_ticket_links_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceTicketLinksApi->patch_service_ticket_links_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ticketLinkId | 
 **client_id** | **str**|  | 
 **patch_operation** | [**List[PatchOperation]**](PatchOperation.md)| List of PatchOperation | 

### Return type

[**ServiceTicketLink**](ServiceTicketLink.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ServiceTicketLink |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_service_ticket_links**
> ServiceTicketLink post_service_ticket_links(client_id, service_ticket_link)

Post ServiceTicketLink

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.service_ticket_link import ServiceTicketLink
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
    api_instance = connectwise_psa.ServiceTicketLinksApi(api_client)
    client_id = 'client_id_example' # str | 
    service_ticket_link = connectwise_psa.ServiceTicketLink() # ServiceTicketLink | serviceTicketLink

    try:
        # Post ServiceTicketLink
        api_response = api_instance.post_service_ticket_links(client_id, service_ticket_link)
        print("The response of ServiceTicketLinksApi->post_service_ticket_links:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceTicketLinksApi->post_service_ticket_links: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**|  | 
 **service_ticket_link** | [**ServiceTicketLink**](ServiceTicketLink.md)| serviceTicketLink | 

### Return type

[**ServiceTicketLink**](ServiceTicketLink.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | ServiceTicketLink |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_service_ticket_links_by_id**
> ServiceTicketLink put_service_ticket_links_by_id(id, client_id, service_ticket_link)

Put ServiceTicketLink

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.service_ticket_link import ServiceTicketLink
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
    api_instance = connectwise_psa.ServiceTicketLinksApi(api_client)
    id = 56 # int | ticketLinkId
    client_id = 'client_id_example' # str | 
    service_ticket_link = connectwise_psa.ServiceTicketLink() # ServiceTicketLink | serviceTicketLink

    try:
        # Put ServiceTicketLink
        api_response = api_instance.put_service_ticket_links_by_id(id, client_id, service_ticket_link)
        print("The response of ServiceTicketLinksApi->put_service_ticket_links_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceTicketLinksApi->put_service_ticket_links_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ticketLinkId | 
 **client_id** | **str**|  | 
 **service_ticket_link** | [**ServiceTicketLink**](ServiceTicketLink.md)| serviceTicketLink | 

### Return type

[**ServiceTicketLink**](ServiceTicketLink.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ServiceTicketLink |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

