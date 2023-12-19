# connectwise_psa.QuoteLinksApi

All URIs are relative to *https://aus-api.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_system_quote_link_setup_by_id**](QuoteLinksApi.md#delete_system_quote_link_setup_by_id) | **DELETE** /system/quoteLinkSetup/{id} | Delete QuoteLink
[**get_system_quote_link_setup**](QuoteLinksApi.md#get_system_quote_link_setup) | **GET** /system/quoteLinkSetup | Get List of QuoteLink
[**get_system_quote_link_setup_by_id**](QuoteLinksApi.md#get_system_quote_link_setup_by_id) | **GET** /system/quoteLinkSetup/{id} | Get QuoteLink
[**get_system_quote_link_setup_count**](QuoteLinksApi.md#get_system_quote_link_setup_count) | **GET** /system/quoteLinkSetup/count | Get Count of QuoteLink
[**get_system_quote_link_setup_test_connection**](QuoteLinksApi.md#get_system_quote_link_setup_test_connection) | **GET** /system/quoteLinkSetup/testConnection | Get SuccessResponse
[**patch_system_quote_link_setup_by_id**](QuoteLinksApi.md#patch_system_quote_link_setup_by_id) | **PATCH** /system/quoteLinkSetup/{id} | Patch QuoteLink
[**post_system_quote_link_setup**](QuoteLinksApi.md#post_system_quote_link_setup) | **POST** /system/quoteLinkSetup | Post QuoteLink
[**put_system_quote_link_setup_by_id**](QuoteLinksApi.md#put_system_quote_link_setup_by_id) | **PUT** /system/quoteLinkSetup/{id} | Put QuoteLink


# **delete_system_quote_link_setup_by_id**
> delete_system_quote_link_setup_by_id(id, client_id)

Delete QuoteLink

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
    api_instance = connectwise_psa.QuoteLinksApi(api_client)
    id = 56 # int | quoteLinkSetupId
    client_id = 'client_id_example' # str | 

    try:
        # Delete QuoteLink
        api_instance.delete_system_quote_link_setup_by_id(id, client_id)
    except Exception as e:
        print("Exception when calling QuoteLinksApi->delete_system_quote_link_setup_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| quoteLinkSetupId | 
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

# **get_system_quote_link_setup**
> List[QuoteLink] get_system_quote_link_setup(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of QuoteLink

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.quote_link import QuoteLink
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
    api_instance = connectwise_psa.QuoteLinksApi(api_client)
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
        # Get List of QuoteLink
        api_response = api_instance.get_system_quote_link_setup(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of QuoteLinksApi->get_system_quote_link_setup:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuoteLinksApi->get_system_quote_link_setup: %s\n" % e)
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

[**List[QuoteLink]**](QuoteLink.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of QuoteLink |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_system_quote_link_setup_by_id**
> QuoteLink get_system_quote_link_setup_by_id(id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get QuoteLink

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.quote_link import QuoteLink
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
    api_instance = connectwise_psa.QuoteLinksApi(api_client)
    id = 56 # int | quoteLinkSetupId
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
        # Get QuoteLink
        api_response = api_instance.get_system_quote_link_setup_by_id(id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of QuoteLinksApi->get_system_quote_link_setup_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuoteLinksApi->get_system_quote_link_setup_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| quoteLinkSetupId | 
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

[**QuoteLink**](QuoteLink.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | QuoteLink |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_system_quote_link_setup_count**
> Count get_system_quote_link_setup_count(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Count of QuoteLink

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
    api_instance = connectwise_psa.QuoteLinksApi(api_client)
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
        # Get Count of QuoteLink
        api_response = api_instance.get_system_quote_link_setup_count(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of QuoteLinksApi->get_system_quote_link_setup_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuoteLinksApi->get_system_quote_link_setup_count: %s\n" % e)
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

# **get_system_quote_link_setup_test_connection**
> SuccessResponse get_system_quote_link_setup_test_connection(client_id, url, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get SuccessResponse

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
    api_instance = connectwise_psa.QuoteLinksApi(api_client)
    client_id = 'client_id_example' # str | 
    url = 'url_example' # str | url
    conditions = 'conditions_example' # str |  (optional)
    child_conditions = 'child_conditions_example' # str |  (optional)
    custom_field_conditions = 'custom_field_conditions_example' # str |  (optional)
    order_by = 'order_by_example' # str |  (optional)
    fields = 'fields_example' # str |  (optional)
    page = 56 # int |  (optional)
    page_size = 56 # int |  (optional)
    page_id = 56 # int |  (optional)

    try:
        # Get SuccessResponse
        api_response = api_instance.get_system_quote_link_setup_test_connection(client_id, url, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of QuoteLinksApi->get_system_quote_link_setup_test_connection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuoteLinksApi->get_system_quote_link_setup_test_connection: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**|  | 
 **url** | **str**| url | 
 **conditions** | **str**|  | [optional] 
 **child_conditions** | **str**|  | [optional] 
 **custom_field_conditions** | **str**|  | [optional] 
 **order_by** | **str**|  | [optional] 
 **fields** | **str**|  | [optional] 
 **page** | **int**|  | [optional] 
 **page_size** | **int**|  | [optional] 
 **page_id** | **int**|  | [optional] 

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

# **patch_system_quote_link_setup_by_id**
> QuoteLink patch_system_quote_link_setup_by_id(id, client_id, patch_operation)

Patch QuoteLink

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.patch_operation import PatchOperation
from connectwise_psa.models.quote_link import QuoteLink
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
    api_instance = connectwise_psa.QuoteLinksApi(api_client)
    id = 56 # int | quoteLinkSetupId
    client_id = 'client_id_example' # str | 
    patch_operation = [connectwise_psa.PatchOperation()] # List[PatchOperation] | List of PatchOperation

    try:
        # Patch QuoteLink
        api_response = api_instance.patch_system_quote_link_setup_by_id(id, client_id, patch_operation)
        print("The response of QuoteLinksApi->patch_system_quote_link_setup_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuoteLinksApi->patch_system_quote_link_setup_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| quoteLinkSetupId | 
 **client_id** | **str**|  | 
 **patch_operation** | [**List[PatchOperation]**](PatchOperation.md)| List of PatchOperation | 

### Return type

[**QuoteLink**](QuoteLink.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | QuoteLink |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_system_quote_link_setup**
> QuoteLink post_system_quote_link_setup(client_id, quote_link)

Post QuoteLink

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.quote_link import QuoteLink
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
    api_instance = connectwise_psa.QuoteLinksApi(api_client)
    client_id = 'client_id_example' # str | 
    quote_link = connectwise_psa.QuoteLink() # QuoteLink | quoteLink

    try:
        # Post QuoteLink
        api_response = api_instance.post_system_quote_link_setup(client_id, quote_link)
        print("The response of QuoteLinksApi->post_system_quote_link_setup:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuoteLinksApi->post_system_quote_link_setup: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**|  | 
 **quote_link** | [**QuoteLink**](QuoteLink.md)| quoteLink | 

### Return type

[**QuoteLink**](QuoteLink.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | QuoteLink |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_system_quote_link_setup_by_id**
> QuoteLink put_system_quote_link_setup_by_id(id, client_id, quote_link)

Put QuoteLink

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.quote_link import QuoteLink
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
    api_instance = connectwise_psa.QuoteLinksApi(api_client)
    id = 56 # int | quoteLinkSetupId
    client_id = 'client_id_example' # str | 
    quote_link = connectwise_psa.QuoteLink() # QuoteLink | quoteLink

    try:
        # Put QuoteLink
        api_response = api_instance.put_system_quote_link_setup_by_id(id, client_id, quote_link)
        print("The response of QuoteLinksApi->put_system_quote_link_setup_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuoteLinksApi->put_system_quote_link_setup_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| quoteLinkSetupId | 
 **client_id** | **str**|  | 
 **quote_link** | [**QuoteLink**](QuoteLink.md)| quoteLink | 

### Return type

[**QuoteLink**](QuoteLink.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | QuoteLink |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

