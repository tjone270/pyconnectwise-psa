# connectwise_psa.CampaignAuditsApi

All URIs are relative to *https://api-aus.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_marketing_campaigns_by_parent_id_audits_by_id**](CampaignAuditsApi.md#delete_marketing_campaigns_by_parent_id_audits_by_id) | **DELETE** /marketing/campaigns/{parentId}/audits/{id} | Delete CampaignAudit
[**get_marketing_campaigns_by_parent_id_audits**](CampaignAuditsApi.md#get_marketing_campaigns_by_parent_id_audits) | **GET** /marketing/campaigns/{parentId}/audits | Get List of CampaignAudit
[**get_marketing_campaigns_by_parent_id_audits_by_id**](CampaignAuditsApi.md#get_marketing_campaigns_by_parent_id_audits_by_id) | **GET** /marketing/campaigns/{parentId}/audits/{id} | Get CampaignAudit
[**get_marketing_campaigns_by_parent_id_audits_count**](CampaignAuditsApi.md#get_marketing_campaigns_by_parent_id_audits_count) | **GET** /marketing/campaigns/{parentId}/audits/count | Get Count of CampaignAudit
[**patch_marketing_campaigns_by_parent_id_audits_by_id**](CampaignAuditsApi.md#patch_marketing_campaigns_by_parent_id_audits_by_id) | **PATCH** /marketing/campaigns/{parentId}/audits/{id} | Patch CampaignAudit
[**post_marketing_campaigns_by_parent_id_audits**](CampaignAuditsApi.md#post_marketing_campaigns_by_parent_id_audits) | **POST** /marketing/campaigns/{parentId}/audits | Post CampaignAudit
[**put_marketing_campaigns_by_parent_id_audits_by_id**](CampaignAuditsApi.md#put_marketing_campaigns_by_parent_id_audits_by_id) | **PUT** /marketing/campaigns/{parentId}/audits/{id} | Put CampaignAudit


# **delete_marketing_campaigns_by_parent_id_audits_by_id**
> delete_marketing_campaigns_by_parent_id_audits_by_id(id, parent_id, client_id)

Delete CampaignAudit

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
    api_instance = connectwise_psa.CampaignAuditsApi(api_client)
    id = 56 # int | auditId
    parent_id = 56 # int | campaignId
    client_id = 'client_id_example' # str | 

    try:
        # Delete CampaignAudit
        api_instance.delete_marketing_campaigns_by_parent_id_audits_by_id(id, parent_id, client_id)
    except Exception as e:
        print("Exception when calling CampaignAuditsApi->delete_marketing_campaigns_by_parent_id_audits_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| auditId | 
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

# **get_marketing_campaigns_by_parent_id_audits**
> List[CampaignAudit] get_marketing_campaigns_by_parent_id_audits(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of CampaignAudit

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.campaign_audit import CampaignAudit
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
    api_instance = connectwise_psa.CampaignAuditsApi(api_client)
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
        # Get List of CampaignAudit
        api_response = api_instance.get_marketing_campaigns_by_parent_id_audits(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of CampaignAuditsApi->get_marketing_campaigns_by_parent_id_audits:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CampaignAuditsApi->get_marketing_campaigns_by_parent_id_audits: %s\n" % e)
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

[**List[CampaignAudit]**](CampaignAudit.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of CampaignAudit |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_marketing_campaigns_by_parent_id_audits_by_id**
> CampaignAudit get_marketing_campaigns_by_parent_id_audits_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get CampaignAudit

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.campaign_audit import CampaignAudit
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
    api_instance = connectwise_psa.CampaignAuditsApi(api_client)
    id = 56 # int | auditId
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
        # Get CampaignAudit
        api_response = api_instance.get_marketing_campaigns_by_parent_id_audits_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of CampaignAuditsApi->get_marketing_campaigns_by_parent_id_audits_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CampaignAuditsApi->get_marketing_campaigns_by_parent_id_audits_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| auditId | 
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

[**CampaignAudit**](CampaignAudit.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | CampaignAudit |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_marketing_campaigns_by_parent_id_audits_count**
> Count get_marketing_campaigns_by_parent_id_audits_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Count of CampaignAudit

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
    api_instance = connectwise_psa.CampaignAuditsApi(api_client)
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
        # Get Count of CampaignAudit
        api_response = api_instance.get_marketing_campaigns_by_parent_id_audits_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of CampaignAuditsApi->get_marketing_campaigns_by_parent_id_audits_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CampaignAuditsApi->get_marketing_campaigns_by_parent_id_audits_count: %s\n" % e)
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

# **patch_marketing_campaigns_by_parent_id_audits_by_id**
> CampaignAudit patch_marketing_campaigns_by_parent_id_audits_by_id(id, parent_id, client_id, patch_operation)

Patch CampaignAudit

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.campaign_audit import CampaignAudit
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
    api_instance = connectwise_psa.CampaignAuditsApi(api_client)
    id = 56 # int | auditId
    parent_id = 56 # int | campaignId
    client_id = 'client_id_example' # str | 
    patch_operation = [connectwise_psa.PatchOperation()] # List[PatchOperation] | List of PatchOperation

    try:
        # Patch CampaignAudit
        api_response = api_instance.patch_marketing_campaigns_by_parent_id_audits_by_id(id, parent_id, client_id, patch_operation)
        print("The response of CampaignAuditsApi->patch_marketing_campaigns_by_parent_id_audits_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CampaignAuditsApi->patch_marketing_campaigns_by_parent_id_audits_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| auditId | 
 **parent_id** | **int**| campaignId | 
 **client_id** | **str**|  | 
 **patch_operation** | [**List[PatchOperation]**](PatchOperation.md)| List of PatchOperation | 

### Return type

[**CampaignAudit**](CampaignAudit.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | CampaignAudit |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_marketing_campaigns_by_parent_id_audits**
> CampaignAudit post_marketing_campaigns_by_parent_id_audits(parent_id, client_id, campaign_audit)

Post CampaignAudit

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.campaign_audit import CampaignAudit
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
    api_instance = connectwise_psa.CampaignAuditsApi(api_client)
    parent_id = 56 # int | campaignId
    client_id = 'client_id_example' # str | 
    campaign_audit = connectwise_psa.CampaignAudit() # CampaignAudit | campaignAudit

    try:
        # Post CampaignAudit
        api_response = api_instance.post_marketing_campaigns_by_parent_id_audits(parent_id, client_id, campaign_audit)
        print("The response of CampaignAuditsApi->post_marketing_campaigns_by_parent_id_audits:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CampaignAuditsApi->post_marketing_campaigns_by_parent_id_audits: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| campaignId | 
 **client_id** | **str**|  | 
 **campaign_audit** | [**CampaignAudit**](CampaignAudit.md)| campaignAudit | 

### Return type

[**CampaignAudit**](CampaignAudit.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | CampaignAudit |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_marketing_campaigns_by_parent_id_audits_by_id**
> CampaignAudit put_marketing_campaigns_by_parent_id_audits_by_id(id, parent_id, client_id, campaign_audit)

Put CampaignAudit

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.campaign_audit import CampaignAudit
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
    api_instance = connectwise_psa.CampaignAuditsApi(api_client)
    id = 56 # int | auditId
    parent_id = 56 # int | campaignId
    client_id = 'client_id_example' # str | 
    campaign_audit = connectwise_psa.CampaignAudit() # CampaignAudit | campaignAudit

    try:
        # Put CampaignAudit
        api_response = api_instance.put_marketing_campaigns_by_parent_id_audits_by_id(id, parent_id, client_id, campaign_audit)
        print("The response of CampaignAuditsApi->put_marketing_campaigns_by_parent_id_audits_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CampaignAuditsApi->put_marketing_campaigns_by_parent_id_audits_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| auditId | 
 **parent_id** | **int**| campaignId | 
 **client_id** | **str**|  | 
 **campaign_audit** | [**CampaignAudit**](CampaignAudit.md)| campaignAudit | 

### Return type

[**CampaignAudit**](CampaignAudit.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | CampaignAudit |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

