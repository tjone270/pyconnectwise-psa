# connectwise_psa.CampaignLinksClickedApi

All URIs are relative to *https://api-aus.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_marketing_campaigns_by_parent_id_links_clicked_by_id**](CampaignLinksClickedApi.md#delete_marketing_campaigns_by_parent_id_links_clicked_by_id) | **DELETE** /marketing/campaigns/{parentId}/linksClicked/{id} | Delete LinkClicked
[**get_marketing_campaigns_by_parent_id_links_clicked**](CampaignLinksClickedApi.md#get_marketing_campaigns_by_parent_id_links_clicked) | **GET** /marketing/campaigns/{parentId}/linksClicked | Get List of LinkClicked
[**get_marketing_campaigns_by_parent_id_links_clicked_by_id**](CampaignLinksClickedApi.md#get_marketing_campaigns_by_parent_id_links_clicked_by_id) | **GET** /marketing/campaigns/{parentId}/linksClicked/{id} | Get LinkClicked
[**get_marketing_campaigns_by_parent_id_links_clicked_count**](CampaignLinksClickedApi.md#get_marketing_campaigns_by_parent_id_links_clicked_count) | **GET** /marketing/campaigns/{parentId}/linksClicked/count | Get Count of LinkClicked
[**patch_marketing_campaigns_by_parent_id_links_clicked_by_id**](CampaignLinksClickedApi.md#patch_marketing_campaigns_by_parent_id_links_clicked_by_id) | **PATCH** /marketing/campaigns/{parentId}/linksClicked/{id} | Patch LinkClicked
[**post_marketing_campaigns_by_parent_id_links_clicked**](CampaignLinksClickedApi.md#post_marketing_campaigns_by_parent_id_links_clicked) | **POST** /marketing/campaigns/{parentId}/linksClicked | Post LinkClicked
[**put_marketing_campaigns_by_parent_id_links_clicked_by_id**](CampaignLinksClickedApi.md#put_marketing_campaigns_by_parent_id_links_clicked_by_id) | **PUT** /marketing/campaigns/{parentId}/linksClicked/{id} | Put LinkClicked


# **delete_marketing_campaigns_by_parent_id_links_clicked_by_id**
> delete_marketing_campaigns_by_parent_id_links_clicked_by_id(id, parent_id, client_id)

Delete LinkClicked

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
    api_instance = connectwise_psa.CampaignLinksClickedApi(api_client)
    id = 56 # int | linksClickedId
    parent_id = 56 # int | campaignId
    client_id = 'client_id_example' # str | 

    try:
        # Delete LinkClicked
        api_instance.delete_marketing_campaigns_by_parent_id_links_clicked_by_id(id, parent_id, client_id)
    except Exception as e:
        print("Exception when calling CampaignLinksClickedApi->delete_marketing_campaigns_by_parent_id_links_clicked_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| linksClickedId | 
 **parent_id** | **int**| campaignId | 
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

# **get_marketing_campaigns_by_parent_id_links_clicked**
> List[LinkClicked] get_marketing_campaigns_by_parent_id_links_clicked(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of LinkClicked

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.link_clicked import LinkClicked
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
    api_instance = connectwise_psa.CampaignLinksClickedApi(api_client)
    parent_id = 56 # int | campaignId
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
        # Get List of LinkClicked
        api_response = api_instance.get_marketing_campaigns_by_parent_id_links_clicked(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of CampaignLinksClickedApi->get_marketing_campaigns_by_parent_id_links_clicked:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CampaignLinksClickedApi->get_marketing_campaigns_by_parent_id_links_clicked: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| campaignId | 
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

[**List[LinkClicked]**](LinkClicked.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of LinkClicked |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_marketing_campaigns_by_parent_id_links_clicked_by_id**
> LinkClicked get_marketing_campaigns_by_parent_id_links_clicked_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get LinkClicked

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.link_clicked import LinkClicked
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
    api_instance = connectwise_psa.CampaignLinksClickedApi(api_client)
    id = 56 # int | linksClickedId
    parent_id = 56 # int | campaignId
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
        # Get LinkClicked
        api_response = api_instance.get_marketing_campaigns_by_parent_id_links_clicked_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of CampaignLinksClickedApi->get_marketing_campaigns_by_parent_id_links_clicked_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CampaignLinksClickedApi->get_marketing_campaigns_by_parent_id_links_clicked_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| linksClickedId | 
 **parent_id** | **int**| campaignId | 
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

[**LinkClicked**](LinkClicked.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | LinkClicked |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_marketing_campaigns_by_parent_id_links_clicked_count**
> Count get_marketing_campaigns_by_parent_id_links_clicked_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Count of LinkClicked

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
    api_instance = connectwise_psa.CampaignLinksClickedApi(api_client)
    parent_id = 56 # int | campaignId
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
        # Get Count of LinkClicked
        api_response = api_instance.get_marketing_campaigns_by_parent_id_links_clicked_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of CampaignLinksClickedApi->get_marketing_campaigns_by_parent_id_links_clicked_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CampaignLinksClickedApi->get_marketing_campaigns_by_parent_id_links_clicked_count: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| campaignId | 
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

# **patch_marketing_campaigns_by_parent_id_links_clicked_by_id**
> LinkClicked patch_marketing_campaigns_by_parent_id_links_clicked_by_id(id, parent_id, client_id, patch_operation)

Patch LinkClicked

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.link_clicked import LinkClicked
from connectwise_psa.models.patch_operation import PatchOperation
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
    api_instance = connectwise_psa.CampaignLinksClickedApi(api_client)
    id = 56 # int | linksClickedId
    parent_id = 56 # int | campaignId
    client_id = 'client_id_example' # str | 
    patch_operation = [connectwise_psa.PatchOperation()] # List[PatchOperation] | List of PatchOperation

    try:
        # Patch LinkClicked
        api_response = api_instance.patch_marketing_campaigns_by_parent_id_links_clicked_by_id(id, parent_id, client_id, patch_operation)
        print("The response of CampaignLinksClickedApi->patch_marketing_campaigns_by_parent_id_links_clicked_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CampaignLinksClickedApi->patch_marketing_campaigns_by_parent_id_links_clicked_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| linksClickedId | 
 **parent_id** | **int**| campaignId | 
 **client_id** | **str**|  | 
 **patch_operation** | [**List[PatchOperation]**](PatchOperation.md)| List of PatchOperation | 

### Return type

[**LinkClicked**](LinkClicked.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | LinkClicked |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_marketing_campaigns_by_parent_id_links_clicked**
> LinkClicked post_marketing_campaigns_by_parent_id_links_clicked(parent_id, client_id, link_clicked)

Post LinkClicked

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.link_clicked import LinkClicked
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
    api_instance = connectwise_psa.CampaignLinksClickedApi(api_client)
    parent_id = 56 # int | campaignId
    client_id = 'client_id_example' # str | 
    link_clicked = connectwise_psa.LinkClicked() # LinkClicked | linkClicked

    try:
        # Post LinkClicked
        api_response = api_instance.post_marketing_campaigns_by_parent_id_links_clicked(parent_id, client_id, link_clicked)
        print("The response of CampaignLinksClickedApi->post_marketing_campaigns_by_parent_id_links_clicked:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CampaignLinksClickedApi->post_marketing_campaigns_by_parent_id_links_clicked: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| campaignId | 
 **client_id** | **str**|  | 
 **link_clicked** | [**LinkClicked**](LinkClicked.md)| linkClicked | 

### Return type

[**LinkClicked**](LinkClicked.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | LinkClicked |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_marketing_campaigns_by_parent_id_links_clicked_by_id**
> LinkClicked put_marketing_campaigns_by_parent_id_links_clicked_by_id(id, parent_id, client_id, link_clicked)

Put LinkClicked

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.link_clicked import LinkClicked
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
    api_instance = connectwise_psa.CampaignLinksClickedApi(api_client)
    id = 56 # int | linksClickedId
    parent_id = 56 # int | campaignId
    client_id = 'client_id_example' # str | 
    link_clicked = connectwise_psa.LinkClicked() # LinkClicked | linkClicked

    try:
        # Put LinkClicked
        api_response = api_instance.put_marketing_campaigns_by_parent_id_links_clicked_by_id(id, parent_id, client_id, link_clicked)
        print("The response of CampaignLinksClickedApi->put_marketing_campaigns_by_parent_id_links_clicked_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CampaignLinksClickedApi->put_marketing_campaigns_by_parent_id_links_clicked_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| linksClickedId | 
 **parent_id** | **int**| campaignId | 
 **client_id** | **str**|  | 
 **link_clicked** | [**LinkClicked**](LinkClicked.md)| linkClicked | 

### Return type

[**LinkClicked**](LinkClicked.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | LinkClicked |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

