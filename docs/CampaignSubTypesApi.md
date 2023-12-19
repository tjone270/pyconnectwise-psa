# connectwise_psa.CampaignSubTypesApi

All URIs are relative to *https://aus-api.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_marketing_campaigns_sub_types_by_id**](CampaignSubTypesApi.md#delete_marketing_campaigns_sub_types_by_id) | **DELETE** /marketing/campaigns/subTypes/{id} | Delete CampaignSubType
[**get_marketing_campaigns_sub_types**](CampaignSubTypesApi.md#get_marketing_campaigns_sub_types) | **GET** /marketing/campaigns/subTypes | Get List of CampaignSubType
[**get_marketing_campaigns_sub_types_by_id**](CampaignSubTypesApi.md#get_marketing_campaigns_sub_types_by_id) | **GET** /marketing/campaigns/subTypes/{id} | Get CampaignSubType
[**get_marketing_campaigns_sub_types_count**](CampaignSubTypesApi.md#get_marketing_campaigns_sub_types_count) | **GET** /marketing/campaigns/subTypes/count | Get Count of CampaignSubType
[**patch_marketing_campaigns_sub_types_by_id**](CampaignSubTypesApi.md#patch_marketing_campaigns_sub_types_by_id) | **PATCH** /marketing/campaigns/subTypes/{id} | Patch CampaignSubType
[**post_marketing_campaigns_sub_types**](CampaignSubTypesApi.md#post_marketing_campaigns_sub_types) | **POST** /marketing/campaigns/subTypes | Post CampaignSubType
[**put_marketing_campaigns_sub_types_by_id**](CampaignSubTypesApi.md#put_marketing_campaigns_sub_types_by_id) | **PUT** /marketing/campaigns/subTypes/{id} | Put CampaignSubType


# **delete_marketing_campaigns_sub_types_by_id**
> delete_marketing_campaigns_sub_types_by_id(id, client_id)

Delete CampaignSubType

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
    api_instance = connectwise_psa.CampaignSubTypesApi(api_client)
    id = 56 # int | subTypeId
    client_id = 'client_id_example' # str | 

    try:
        # Delete CampaignSubType
        api_instance.delete_marketing_campaigns_sub_types_by_id(id, client_id)
    except Exception as e:
        print("Exception when calling CampaignSubTypesApi->delete_marketing_campaigns_sub_types_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| subTypeId | 
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

# **get_marketing_campaigns_sub_types**
> List[CampaignSubTypeCampaignSubType] get_marketing_campaigns_sub_types(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of CampaignSubType

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.campaign_sub_type_campaign_sub_type import CampaignSubTypeCampaignSubType
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
    api_instance = connectwise_psa.CampaignSubTypesApi(api_client)
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
        # Get List of CampaignSubType
        api_response = api_instance.get_marketing_campaigns_sub_types(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of CampaignSubTypesApi->get_marketing_campaigns_sub_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CampaignSubTypesApi->get_marketing_campaigns_sub_types: %s\n" % e)
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

[**List[CampaignSubTypeCampaignSubType]**](CampaignSubTypeCampaignSubType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of CampaignSubType |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_marketing_campaigns_sub_types_by_id**
> CampaignSubTypeCampaignSubType get_marketing_campaigns_sub_types_by_id(id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get CampaignSubType

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.campaign_sub_type_campaign_sub_type import CampaignSubTypeCampaignSubType
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
    api_instance = connectwise_psa.CampaignSubTypesApi(api_client)
    id = 56 # int | subTypeId
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
        # Get CampaignSubType
        api_response = api_instance.get_marketing_campaigns_sub_types_by_id(id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of CampaignSubTypesApi->get_marketing_campaigns_sub_types_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CampaignSubTypesApi->get_marketing_campaigns_sub_types_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| subTypeId | 
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

[**CampaignSubTypeCampaignSubType**](CampaignSubTypeCampaignSubType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | CampaignSubType |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_marketing_campaigns_sub_types_count**
> Count get_marketing_campaigns_sub_types_count(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Count of CampaignSubType

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
    api_instance = connectwise_psa.CampaignSubTypesApi(api_client)
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
        # Get Count of CampaignSubType
        api_response = api_instance.get_marketing_campaigns_sub_types_count(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of CampaignSubTypesApi->get_marketing_campaigns_sub_types_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CampaignSubTypesApi->get_marketing_campaigns_sub_types_count: %s\n" % e)
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

# **patch_marketing_campaigns_sub_types_by_id**
> CampaignSubTypeCampaignSubType patch_marketing_campaigns_sub_types_by_id(id, client_id, patch_operation)

Patch CampaignSubType

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.campaign_sub_type_campaign_sub_type import CampaignSubTypeCampaignSubType
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
    api_instance = connectwise_psa.CampaignSubTypesApi(api_client)
    id = 56 # int | subTypeId
    client_id = 'client_id_example' # str | 
    patch_operation = [connectwise_psa.PatchOperation()] # List[PatchOperation] | List of PatchOperation

    try:
        # Patch CampaignSubType
        api_response = api_instance.patch_marketing_campaigns_sub_types_by_id(id, client_id, patch_operation)
        print("The response of CampaignSubTypesApi->patch_marketing_campaigns_sub_types_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CampaignSubTypesApi->patch_marketing_campaigns_sub_types_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| subTypeId | 
 **client_id** | **str**|  | 
 **patch_operation** | [**List[PatchOperation]**](PatchOperation.md)| List of PatchOperation | 

### Return type

[**CampaignSubTypeCampaignSubType**](CampaignSubTypeCampaignSubType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | CampaignSubType |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_marketing_campaigns_sub_types**
> CampaignSubTypeCampaignSubType post_marketing_campaigns_sub_types(client_id, campaign_sub_type_campaign_sub_type)

Post CampaignSubType

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.campaign_sub_type_campaign_sub_type import CampaignSubTypeCampaignSubType
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
    api_instance = connectwise_psa.CampaignSubTypesApi(api_client)
    client_id = 'client_id_example' # str | 
    campaign_sub_type_campaign_sub_type = connectwise_psa.CampaignSubTypeCampaignSubType() # CampaignSubTypeCampaignSubType | campaignSubType

    try:
        # Post CampaignSubType
        api_response = api_instance.post_marketing_campaigns_sub_types(client_id, campaign_sub_type_campaign_sub_type)
        print("The response of CampaignSubTypesApi->post_marketing_campaigns_sub_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CampaignSubTypesApi->post_marketing_campaigns_sub_types: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**|  | 
 **campaign_sub_type_campaign_sub_type** | [**CampaignSubTypeCampaignSubType**](CampaignSubTypeCampaignSubType.md)| campaignSubType | 

### Return type

[**CampaignSubTypeCampaignSubType**](CampaignSubTypeCampaignSubType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | CampaignSubType |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_marketing_campaigns_sub_types_by_id**
> CampaignSubTypeCampaignSubType put_marketing_campaigns_sub_types_by_id(id, client_id, campaign_sub_type_campaign_sub_type)

Put CampaignSubType

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.campaign_sub_type_campaign_sub_type import CampaignSubTypeCampaignSubType
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
    api_instance = connectwise_psa.CampaignSubTypesApi(api_client)
    id = 56 # int | subTypeId
    client_id = 'client_id_example' # str | 
    campaign_sub_type_campaign_sub_type = connectwise_psa.CampaignSubTypeCampaignSubType() # CampaignSubTypeCampaignSubType | campaignSubType

    try:
        # Put CampaignSubType
        api_response = api_instance.put_marketing_campaigns_sub_types_by_id(id, client_id, campaign_sub_type_campaign_sub_type)
        print("The response of CampaignSubTypesApi->put_marketing_campaigns_sub_types_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CampaignSubTypesApi->put_marketing_campaigns_sub_types_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| subTypeId | 
 **client_id** | **str**|  | 
 **campaign_sub_type_campaign_sub_type** | [**CampaignSubTypeCampaignSubType**](CampaignSubTypeCampaignSubType.md)| campaignSubType | 

### Return type

[**CampaignSubTypeCampaignSubType**](CampaignSubTypeCampaignSubType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | CampaignSubType |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
