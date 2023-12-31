# connectwise_psa.CampaignEmailsOpenedApi

All URIs are relative to *https://api-aus.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_marketing_campaigns_by_parent_id_emails_opened_by_id**](CampaignEmailsOpenedApi.md#delete_marketing_campaigns_by_parent_id_emails_opened_by_id) | **DELETE** /marketing/campaigns/{parentId}/emailsOpened/{id} | Delete EmailOpened
[**get_marketing_campaigns_by_parent_id_emails_opened**](CampaignEmailsOpenedApi.md#get_marketing_campaigns_by_parent_id_emails_opened) | **GET** /marketing/campaigns/{parentId}/emailsOpened | Get List of EmailOpened
[**get_marketing_campaigns_by_parent_id_emails_opened_by_id**](CampaignEmailsOpenedApi.md#get_marketing_campaigns_by_parent_id_emails_opened_by_id) | **GET** /marketing/campaigns/{parentId}/emailsOpened/{id} | Get EmailOpened
[**get_marketing_campaigns_by_parent_id_emails_opened_count**](CampaignEmailsOpenedApi.md#get_marketing_campaigns_by_parent_id_emails_opened_count) | **GET** /marketing/campaigns/{parentId}/emailsOpened/count | Get Count of EmailOpened
[**patch_marketing_campaigns_by_parent_id_emails_opened_by_id**](CampaignEmailsOpenedApi.md#patch_marketing_campaigns_by_parent_id_emails_opened_by_id) | **PATCH** /marketing/campaigns/{parentId}/emailsOpened/{id} | Patch EmailOpened
[**post_marketing_campaigns_by_parent_id_emails_opened**](CampaignEmailsOpenedApi.md#post_marketing_campaigns_by_parent_id_emails_opened) | **POST** /marketing/campaigns/{parentId}/emailsOpened | Post EmailOpened
[**put_marketing_campaigns_by_parent_id_emails_opened_by_id**](CampaignEmailsOpenedApi.md#put_marketing_campaigns_by_parent_id_emails_opened_by_id) | **PUT** /marketing/campaigns/{parentId}/emailsOpened/{id} | Put EmailOpened


# **delete_marketing_campaigns_by_parent_id_emails_opened_by_id**
> delete_marketing_campaigns_by_parent_id_emails_opened_by_id(id, parent_id, client_id)

Delete EmailOpened

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
    api_instance = connectwise_psa.CampaignEmailsOpenedApi(api_client)
    id = 56 # int | emailsOpenedId
    parent_id = 56 # int | campaignId
    client_id = 'client_id_example' # str | 

    try:
        # Delete EmailOpened
        api_instance.delete_marketing_campaigns_by_parent_id_emails_opened_by_id(id, parent_id, client_id)
    except Exception as e:
        print("Exception when calling CampaignEmailsOpenedApi->delete_marketing_campaigns_by_parent_id_emails_opened_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| emailsOpenedId | 
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

# **get_marketing_campaigns_by_parent_id_emails_opened**
> List[EmailOpened] get_marketing_campaigns_by_parent_id_emails_opened(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of EmailOpened

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.email_opened import EmailOpened
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
    api_instance = connectwise_psa.CampaignEmailsOpenedApi(api_client)
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
        # Get List of EmailOpened
        api_response = api_instance.get_marketing_campaigns_by_parent_id_emails_opened(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of CampaignEmailsOpenedApi->get_marketing_campaigns_by_parent_id_emails_opened:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CampaignEmailsOpenedApi->get_marketing_campaigns_by_parent_id_emails_opened: %s\n" % e)
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

[**List[EmailOpened]**](EmailOpened.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of EmailOpened |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_marketing_campaigns_by_parent_id_emails_opened_by_id**
> EmailOpened get_marketing_campaigns_by_parent_id_emails_opened_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get EmailOpened

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.email_opened import EmailOpened
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
    api_instance = connectwise_psa.CampaignEmailsOpenedApi(api_client)
    id = 56 # int | emailsOpenedId
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
        # Get EmailOpened
        api_response = api_instance.get_marketing_campaigns_by_parent_id_emails_opened_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of CampaignEmailsOpenedApi->get_marketing_campaigns_by_parent_id_emails_opened_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CampaignEmailsOpenedApi->get_marketing_campaigns_by_parent_id_emails_opened_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| emailsOpenedId | 
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

[**EmailOpened**](EmailOpened.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | EmailOpened |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_marketing_campaigns_by_parent_id_emails_opened_count**
> Count get_marketing_campaigns_by_parent_id_emails_opened_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Count of EmailOpened

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
    api_instance = connectwise_psa.CampaignEmailsOpenedApi(api_client)
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
        # Get Count of EmailOpened
        api_response = api_instance.get_marketing_campaigns_by_parent_id_emails_opened_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of CampaignEmailsOpenedApi->get_marketing_campaigns_by_parent_id_emails_opened_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CampaignEmailsOpenedApi->get_marketing_campaigns_by_parent_id_emails_opened_count: %s\n" % e)
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

# **patch_marketing_campaigns_by_parent_id_emails_opened_by_id**
> EmailOpened patch_marketing_campaigns_by_parent_id_emails_opened_by_id(id, parent_id, client_id, patch_operation)

Patch EmailOpened

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.email_opened import EmailOpened
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
    api_instance = connectwise_psa.CampaignEmailsOpenedApi(api_client)
    id = 56 # int | emailsOpenedId
    parent_id = 56 # int | campaignId
    client_id = 'client_id_example' # str | 
    patch_operation = [connectwise_psa.PatchOperation()] # List[PatchOperation] | List of PatchOperation

    try:
        # Patch EmailOpened
        api_response = api_instance.patch_marketing_campaigns_by_parent_id_emails_opened_by_id(id, parent_id, client_id, patch_operation)
        print("The response of CampaignEmailsOpenedApi->patch_marketing_campaigns_by_parent_id_emails_opened_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CampaignEmailsOpenedApi->patch_marketing_campaigns_by_parent_id_emails_opened_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| emailsOpenedId | 
 **parent_id** | **int**| campaignId | 
 **client_id** | **str**|  | 
 **patch_operation** | [**List[PatchOperation]**](PatchOperation.md)| List of PatchOperation | 

### Return type

[**EmailOpened**](EmailOpened.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | EmailOpened |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_marketing_campaigns_by_parent_id_emails_opened**
> EmailOpened post_marketing_campaigns_by_parent_id_emails_opened(parent_id, client_id, email_opened)

Post EmailOpened

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.email_opened import EmailOpened
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
    api_instance = connectwise_psa.CampaignEmailsOpenedApi(api_client)
    parent_id = 56 # int | campaignId
    client_id = 'client_id_example' # str | 
    email_opened = connectwise_psa.EmailOpened() # EmailOpened | emailOpened

    try:
        # Post EmailOpened
        api_response = api_instance.post_marketing_campaigns_by_parent_id_emails_opened(parent_id, client_id, email_opened)
        print("The response of CampaignEmailsOpenedApi->post_marketing_campaigns_by_parent_id_emails_opened:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CampaignEmailsOpenedApi->post_marketing_campaigns_by_parent_id_emails_opened: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| campaignId | 
 **client_id** | **str**|  | 
 **email_opened** | [**EmailOpened**](EmailOpened.md)| emailOpened | 

### Return type

[**EmailOpened**](EmailOpened.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | EmailOpened |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_marketing_campaigns_by_parent_id_emails_opened_by_id**
> EmailOpened put_marketing_campaigns_by_parent_id_emails_opened_by_id(id, parent_id, client_id, email_opened)

Put EmailOpened

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.email_opened import EmailOpened
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
    api_instance = connectwise_psa.CampaignEmailsOpenedApi(api_client)
    id = 56 # int | emailsOpenedId
    parent_id = 56 # int | campaignId
    client_id = 'client_id_example' # str | 
    email_opened = connectwise_psa.EmailOpened() # EmailOpened | emailOpened

    try:
        # Put EmailOpened
        api_response = api_instance.put_marketing_campaigns_by_parent_id_emails_opened_by_id(id, parent_id, client_id, email_opened)
        print("The response of CampaignEmailsOpenedApi->put_marketing_campaigns_by_parent_id_emails_opened_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CampaignEmailsOpenedApi->put_marketing_campaigns_by_parent_id_emails_opened_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| emailsOpenedId | 
 **parent_id** | **int**| campaignId | 
 **client_id** | **str**|  | 
 **email_opened** | [**EmailOpened**](EmailOpened.md)| emailOpened | 

### Return type

[**EmailOpened**](EmailOpened.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | EmailOpened |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

