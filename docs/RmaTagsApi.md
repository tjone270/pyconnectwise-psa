# connectwise_psa.RmaTagsApi

All URIs are relative to *https://api-aus.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_procurement_rma_tags_by_id**](RmaTagsApi.md#delete_procurement_rma_tags_by_id) | **DELETE** /procurement/rmaTags/{id} | Delete RmaTag
[**get_procurement_rma_tags**](RmaTagsApi.md#get_procurement_rma_tags) | **GET** /procurement/rmaTags | Get List of RmaTag
[**get_procurement_rma_tags_by_id**](RmaTagsApi.md#get_procurement_rma_tags_by_id) | **GET** /procurement/rmaTags/{id} | Get RmaTag
[**get_procurement_rma_tags_count**](RmaTagsApi.md#get_procurement_rma_tags_count) | **GET** /procurement/rmaTags/count | Get Count of RmaTag
[**get_procurement_rma_tags_default**](RmaTagsApi.md#get_procurement_rma_tags_default) | **GET** /procurement/rmaTags/default | Get RmaTag
[**patch_procurement_rma_tags_by_id**](RmaTagsApi.md#patch_procurement_rma_tags_by_id) | **PATCH** /procurement/rmaTags/{id} | Patch RmaTag
[**post_procurement_rma_tags**](RmaTagsApi.md#post_procurement_rma_tags) | **POST** /procurement/rmaTags | Post RmaTag
[**put_procurement_rma_tags_by_id**](RmaTagsApi.md#put_procurement_rma_tags_by_id) | **PUT** /procurement/rmaTags/{id} | Put RmaTag


# **delete_procurement_rma_tags_by_id**
> delete_procurement_rma_tags_by_id(id, client_id)

Delete RmaTag

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
    api_instance = connectwise_psa.RmaTagsApi(api_client)
    id = 56 # int | rmaTagId
    client_id = 'client_id_example' # str | 

    try:
        # Delete RmaTag
        api_instance.delete_procurement_rma_tags_by_id(id, client_id)
    except Exception as e:
        print("Exception when calling RmaTagsApi->delete_procurement_rma_tags_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| rmaTagId | 
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

# **get_procurement_rma_tags**
> List[RmaTag] get_procurement_rma_tags(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of RmaTag

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.rma_tag import RmaTag
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
    api_instance = connectwise_psa.RmaTagsApi(api_client)
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
        # Get List of RmaTag
        api_response = api_instance.get_procurement_rma_tags(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of RmaTagsApi->get_procurement_rma_tags:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RmaTagsApi->get_procurement_rma_tags: %s\n" % e)
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

[**List[RmaTag]**](RmaTag.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of RmaTag |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_procurement_rma_tags_by_id**
> RmaTag get_procurement_rma_tags_by_id(id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get RmaTag

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.rma_tag import RmaTag
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
    api_instance = connectwise_psa.RmaTagsApi(api_client)
    id = 56 # int | rmaTagId
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
        # Get RmaTag
        api_response = api_instance.get_procurement_rma_tags_by_id(id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of RmaTagsApi->get_procurement_rma_tags_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RmaTagsApi->get_procurement_rma_tags_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| rmaTagId | 
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

[**RmaTag**](RmaTag.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | RmaTag |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_procurement_rma_tags_count**
> Count get_procurement_rma_tags_count(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Count of RmaTag

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
    api_instance = connectwise_psa.RmaTagsApi(api_client)
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
        # Get Count of RmaTag
        api_response = api_instance.get_procurement_rma_tags_count(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of RmaTagsApi->get_procurement_rma_tags_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RmaTagsApi->get_procurement_rma_tags_count: %s\n" % e)
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

# **get_procurement_rma_tags_default**
> RmaTag get_procurement_rma_tags_default(client_id, product_id, billing_log_id, ticket_id, project_id, sales_order_id, company_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get RmaTag

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.rma_tag import RmaTag
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
    api_instance = connectwise_psa.RmaTagsApi(api_client)
    client_id = 'client_id_example' # str | 
    product_id = 56 # int | productId
    billing_log_id = 56 # int | billingLogId
    ticket_id = 56 # int | ticketId
    project_id = 56 # int | projectId
    sales_order_id = 56 # int | salesOrderId
    company_id = 56 # int | companyId
    conditions = 'conditions_example' # str |  (optional)
    child_conditions = 'child_conditions_example' # str |  (optional)
    custom_field_conditions = 'custom_field_conditions_example' # str |  (optional)
    order_by = 'order_by_example' # str |  (optional)
    fields = 'fields_example' # str |  (optional)
    page = 56 # int |  (optional)
    page_size = 56 # int |  (optional)
    page_id = 56 # int |  (optional)

    try:
        # Get RmaTag
        api_response = api_instance.get_procurement_rma_tags_default(client_id, product_id, billing_log_id, ticket_id, project_id, sales_order_id, company_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of RmaTagsApi->get_procurement_rma_tags_default:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RmaTagsApi->get_procurement_rma_tags_default: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**|  | 
 **product_id** | **int**| productId | 
 **billing_log_id** | **int**| billingLogId | 
 **ticket_id** | **int**| ticketId | 
 **project_id** | **int**| projectId | 
 **sales_order_id** | **int**| salesOrderId | 
 **company_id** | **int**| companyId | 
 **conditions** | **str**|  | [optional] 
 **child_conditions** | **str**|  | [optional] 
 **custom_field_conditions** | **str**|  | [optional] 
 **order_by** | **str**|  | [optional] 
 **fields** | **str**|  | [optional] 
 **page** | **int**|  | [optional] 
 **page_size** | **int**|  | [optional] 
 **page_id** | **int**|  | [optional] 

### Return type

[**RmaTag**](RmaTag.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | RmaTag |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_procurement_rma_tags_by_id**
> RmaTag patch_procurement_rma_tags_by_id(id, client_id, patch_operation)

Patch RmaTag

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.patch_operation import PatchOperation
from connectwise_psa.models.rma_tag import RmaTag
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
    api_instance = connectwise_psa.RmaTagsApi(api_client)
    id = 56 # int | rmaTagId
    client_id = 'client_id_example' # str | 
    patch_operation = [connectwise_psa.PatchOperation()] # List[PatchOperation] | List of PatchOperation

    try:
        # Patch RmaTag
        api_response = api_instance.patch_procurement_rma_tags_by_id(id, client_id, patch_operation)
        print("The response of RmaTagsApi->patch_procurement_rma_tags_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RmaTagsApi->patch_procurement_rma_tags_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| rmaTagId | 
 **client_id** | **str**|  | 
 **patch_operation** | [**List[PatchOperation]**](PatchOperation.md)| List of PatchOperation | 

### Return type

[**RmaTag**](RmaTag.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | RmaTag |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_procurement_rma_tags**
> RmaTag post_procurement_rma_tags(client_id, rma_tag)

Post RmaTag

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.rma_tag import RmaTag
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
    api_instance = connectwise_psa.RmaTagsApi(api_client)
    client_id = 'client_id_example' # str | 
    rma_tag = connectwise_psa.RmaTag() # RmaTag | rmaTag

    try:
        # Post RmaTag
        api_response = api_instance.post_procurement_rma_tags(client_id, rma_tag)
        print("The response of RmaTagsApi->post_procurement_rma_tags:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RmaTagsApi->post_procurement_rma_tags: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**|  | 
 **rma_tag** | [**RmaTag**](RmaTag.md)| rmaTag | 

### Return type

[**RmaTag**](RmaTag.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | RmaTag |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_procurement_rma_tags_by_id**
> RmaTag put_procurement_rma_tags_by_id(id, client_id, rma_tag)

Put RmaTag

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.rma_tag import RmaTag
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
    api_instance = connectwise_psa.RmaTagsApi(api_client)
    id = 56 # int | rmaTagId
    client_id = 'client_id_example' # str | 
    rma_tag = connectwise_psa.RmaTag() # RmaTag | rmaTag

    try:
        # Put RmaTag
        api_response = api_instance.put_procurement_rma_tags_by_id(id, client_id, rma_tag)
        print("The response of RmaTagsApi->put_procurement_rma_tags_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RmaTagsApi->put_procurement_rma_tags_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| rmaTagId | 
 **client_id** | **str**|  | 
 **rma_tag** | [**RmaTag**](RmaTag.md)| rmaTag | 

### Return type

[**RmaTag**](RmaTag.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | RmaTag |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

