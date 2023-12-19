# connectwise_psa.CampaignStatusesApi

All URIs are relative to *https://aus-api.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_marketing_campaigns_statuses_by_id**](CampaignStatusesApi.md#delete_marketing_campaigns_statuses_by_id) | **DELETE** /marketing/campaigns/statuses/{id} | Delete CampaignStatus
[**get_marketing_campaigns_statuses**](CampaignStatusesApi.md#get_marketing_campaigns_statuses) | **GET** /marketing/campaigns/statuses | Get List of CampaignStatus
[**get_marketing_campaigns_statuses_by_id**](CampaignStatusesApi.md#get_marketing_campaigns_statuses_by_id) | **GET** /marketing/campaigns/statuses/{id} | Get CampaignStatus
[**get_marketing_campaigns_statuses_count**](CampaignStatusesApi.md#get_marketing_campaigns_statuses_count) | **GET** /marketing/campaigns/statuses/count | Get Count of CampaignStatus
[**patch_marketing_campaigns_statuses_by_id**](CampaignStatusesApi.md#patch_marketing_campaigns_statuses_by_id) | **PATCH** /marketing/campaigns/statuses/{id} | Patch CampaignStatus
[**post_marketing_campaigns_statuses**](CampaignStatusesApi.md#post_marketing_campaigns_statuses) | **POST** /marketing/campaigns/statuses | Post CampaignStatus
[**put_marketing_campaigns_statuses_by_id**](CampaignStatusesApi.md#put_marketing_campaigns_statuses_by_id) | **PUT** /marketing/campaigns/statuses/{id} | Put CampaignStatus


# **delete_marketing_campaigns_statuses_by_id**
> delete_marketing_campaigns_statuses_by_id(id, client_id)

Delete CampaignStatus

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
    api_instance = connectwise_psa.CampaignStatusesApi(api_client)
    id = 56 # int | statusId
    client_id = 'client_id_example' # str | 

    try:
        # Delete CampaignStatus
        api_instance.delete_marketing_campaigns_statuses_by_id(id, client_id)
    except Exception as e:
        print("Exception when calling CampaignStatusesApi->delete_marketing_campaigns_statuses_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| statusId | 
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

# **get_marketing_campaigns_statuses**
> List[CampaignStatus] get_marketing_campaigns_statuses(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of CampaignStatus

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.campaign_status import CampaignStatus
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
    api_instance = connectwise_psa.CampaignStatusesApi(api_client)
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
        # Get List of CampaignStatus
        api_response = api_instance.get_marketing_campaigns_statuses(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of CampaignStatusesApi->get_marketing_campaigns_statuses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CampaignStatusesApi->get_marketing_campaigns_statuses: %s\n" % e)
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

[**List[CampaignStatus]**](CampaignStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of CampaignStatus |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_marketing_campaigns_statuses_by_id**
> CampaignStatus get_marketing_campaigns_statuses_by_id(id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get CampaignStatus

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.campaign_status import CampaignStatus
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
    api_instance = connectwise_psa.CampaignStatusesApi(api_client)
    id = 56 # int | statusId
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
        # Get CampaignStatus
        api_response = api_instance.get_marketing_campaigns_statuses_by_id(id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of CampaignStatusesApi->get_marketing_campaigns_statuses_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CampaignStatusesApi->get_marketing_campaigns_statuses_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| statusId | 
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

[**CampaignStatus**](CampaignStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | CampaignStatus |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_marketing_campaigns_statuses_count**
> Count get_marketing_campaigns_statuses_count(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Count of CampaignStatus

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
    api_instance = connectwise_psa.CampaignStatusesApi(api_client)
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
        # Get Count of CampaignStatus
        api_response = api_instance.get_marketing_campaigns_statuses_count(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of CampaignStatusesApi->get_marketing_campaigns_statuses_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CampaignStatusesApi->get_marketing_campaigns_statuses_count: %s\n" % e)
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

# **patch_marketing_campaigns_statuses_by_id**
> CampaignStatus patch_marketing_campaigns_statuses_by_id(id, client_id, patch_operation)

Patch CampaignStatus

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.campaign_status import CampaignStatus
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
    api_instance = connectwise_psa.CampaignStatusesApi(api_client)
    id = 56 # int | statusId
    client_id = 'client_id_example' # str | 
    patch_operation = [connectwise_psa.PatchOperation()] # List[PatchOperation] | List of PatchOperation

    try:
        # Patch CampaignStatus
        api_response = api_instance.patch_marketing_campaigns_statuses_by_id(id, client_id, patch_operation)
        print("The response of CampaignStatusesApi->patch_marketing_campaigns_statuses_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CampaignStatusesApi->patch_marketing_campaigns_statuses_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| statusId | 
 **client_id** | **str**|  | 
 **patch_operation** | [**List[PatchOperation]**](PatchOperation.md)| List of PatchOperation | 

### Return type

[**CampaignStatus**](CampaignStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | CampaignStatus |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_marketing_campaigns_statuses**
> CampaignStatus post_marketing_campaigns_statuses(client_id, campaign_status)

Post CampaignStatus

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.campaign_status import CampaignStatus
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
    api_instance = connectwise_psa.CampaignStatusesApi(api_client)
    client_id = 'client_id_example' # str | 
    campaign_status = connectwise_psa.CampaignStatus() # CampaignStatus | campaignStatus

    try:
        # Post CampaignStatus
        api_response = api_instance.post_marketing_campaigns_statuses(client_id, campaign_status)
        print("The response of CampaignStatusesApi->post_marketing_campaigns_statuses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CampaignStatusesApi->post_marketing_campaigns_statuses: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**|  | 
 **campaign_status** | [**CampaignStatus**](CampaignStatus.md)| campaignStatus | 

### Return type

[**CampaignStatus**](CampaignStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | CampaignStatus |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_marketing_campaigns_statuses_by_id**
> CampaignStatus put_marketing_campaigns_statuses_by_id(id, client_id, campaign_status)

Put CampaignStatus

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.campaign_status import CampaignStatus
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
    api_instance = connectwise_psa.CampaignStatusesApi(api_client)
    id = 56 # int | statusId
    client_id = 'client_id_example' # str | 
    campaign_status = connectwise_psa.CampaignStatus() # CampaignStatus | campaignStatus

    try:
        # Put CampaignStatus
        api_response = api_instance.put_marketing_campaigns_statuses_by_id(id, client_id, campaign_status)
        print("The response of CampaignStatusesApi->put_marketing_campaigns_statuses_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CampaignStatusesApi->put_marketing_campaigns_statuses_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| statusId | 
 **client_id** | **str**|  | 
 **campaign_status** | [**CampaignStatus**](CampaignStatus.md)| campaignStatus | 

### Return type

[**CampaignStatus**](CampaignStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | CampaignStatus |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

