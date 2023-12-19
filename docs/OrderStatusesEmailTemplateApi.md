# connectwise_psa.OrderStatusesEmailTemplateApi

All URIs are relative to *https://aus-api.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_sales_orders_statuses_by_parent_id_emailtemplates_by_id**](OrderStatusesEmailTemplateApi.md#delete_sales_orders_statuses_by_parent_id_emailtemplates_by_id) | **DELETE** /sales/orders/statuses/{parentId}/emailtemplates/{id} | Delete OrderStatusEmailTemplate
[**get_sales_orders_statuses_by_parent_id_emailtemplates**](OrderStatusesEmailTemplateApi.md#get_sales_orders_statuses_by_parent_id_emailtemplates) | **GET** /sales/orders/statuses/{parentId}/emailtemplates/ | Get List of OrderStatusEmailTemplate
[**get_sales_orders_statuses_by_parent_id_emailtemplates_by_id**](OrderStatusesEmailTemplateApi.md#get_sales_orders_statuses_by_parent_id_emailtemplates_by_id) | **GET** /sales/orders/statuses/{parentId}/emailtemplates/{id} | Get OrderStatusEmailTemplate
[**get_sales_orders_statuses_by_parent_id_emailtemplates_count**](OrderStatusesEmailTemplateApi.md#get_sales_orders_statuses_by_parent_id_emailtemplates_count) | **GET** /sales/orders/statuses/{parentId}/emailtemplates/count | Get Count of OrderStatusEmailTemplate
[**patch_sales_orders_statuses_by_parent_id_emailtemplates_by_id**](OrderStatusesEmailTemplateApi.md#patch_sales_orders_statuses_by_parent_id_emailtemplates_by_id) | **PATCH** /sales/orders/statuses/{parentId}/emailtemplates/{id} | Patch OrderStatusEmailTemplate
[**post_sales_orders_statuses_by_parent_id_emailtemplates**](OrderStatusesEmailTemplateApi.md#post_sales_orders_statuses_by_parent_id_emailtemplates) | **POST** /sales/orders/statuses/{parentId}/emailtemplates/ | Post OrderStatusEmailTemplate
[**put_sales_orders_statuses_by_parent_id_emailtemplates_by_id**](OrderStatusesEmailTemplateApi.md#put_sales_orders_statuses_by_parent_id_emailtemplates_by_id) | **PUT** /sales/orders/statuses/{parentId}/emailtemplates/{id} | Put OrderStatusEmailTemplate


# **delete_sales_orders_statuses_by_parent_id_emailtemplates_by_id**
> delete_sales_orders_statuses_by_parent_id_emailtemplates_by_id(id, parent_id, client_id)

Delete OrderStatusEmailTemplate

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
    api_instance = connectwise_psa.OrderStatusesEmailTemplateApi(api_client)
    id = 56 # int | emailtemplateId
    parent_id = 56 # int | statusId
    client_id = 'client_id_example' # str | 

    try:
        # Delete OrderStatusEmailTemplate
        api_instance.delete_sales_orders_statuses_by_parent_id_emailtemplates_by_id(id, parent_id, client_id)
    except Exception as e:
        print("Exception when calling OrderStatusesEmailTemplateApi->delete_sales_orders_statuses_by_parent_id_emailtemplates_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| emailtemplateId | 
 **parent_id** | **int**| statusId | 
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

# **get_sales_orders_statuses_by_parent_id_emailtemplates**
> List[OrderStatusEmailTemplate] get_sales_orders_statuses_by_parent_id_emailtemplates(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of OrderStatusEmailTemplate

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.order_status_email_template import OrderStatusEmailTemplate
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
    api_instance = connectwise_psa.OrderStatusesEmailTemplateApi(api_client)
    parent_id = 56 # int | statusId
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
        # Get List of OrderStatusEmailTemplate
        api_response = api_instance.get_sales_orders_statuses_by_parent_id_emailtemplates(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of OrderStatusesEmailTemplateApi->get_sales_orders_statuses_by_parent_id_emailtemplates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrderStatusesEmailTemplateApi->get_sales_orders_statuses_by_parent_id_emailtemplates: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| statusId | 
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

[**List[OrderStatusEmailTemplate]**](OrderStatusEmailTemplate.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of OrderStatusEmailTemplate |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sales_orders_statuses_by_parent_id_emailtemplates_by_id**
> OrderStatusEmailTemplate get_sales_orders_statuses_by_parent_id_emailtemplates_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get OrderStatusEmailTemplate

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.order_status_email_template import OrderStatusEmailTemplate
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
    api_instance = connectwise_psa.OrderStatusesEmailTemplateApi(api_client)
    id = 56 # int | emailtemplateId
    parent_id = 56 # int | statusId
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
        # Get OrderStatusEmailTemplate
        api_response = api_instance.get_sales_orders_statuses_by_parent_id_emailtemplates_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of OrderStatusesEmailTemplateApi->get_sales_orders_statuses_by_parent_id_emailtemplates_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrderStatusesEmailTemplateApi->get_sales_orders_statuses_by_parent_id_emailtemplates_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| emailtemplateId | 
 **parent_id** | **int**| statusId | 
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

[**OrderStatusEmailTemplate**](OrderStatusEmailTemplate.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OrderStatusEmailTemplate |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sales_orders_statuses_by_parent_id_emailtemplates_count**
> Count get_sales_orders_statuses_by_parent_id_emailtemplates_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Count of OrderStatusEmailTemplate

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
    api_instance = connectwise_psa.OrderStatusesEmailTemplateApi(api_client)
    parent_id = 56 # int | statusId
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
        # Get Count of OrderStatusEmailTemplate
        api_response = api_instance.get_sales_orders_statuses_by_parent_id_emailtemplates_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of OrderStatusesEmailTemplateApi->get_sales_orders_statuses_by_parent_id_emailtemplates_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrderStatusesEmailTemplateApi->get_sales_orders_statuses_by_parent_id_emailtemplates_count: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| statusId | 
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

# **patch_sales_orders_statuses_by_parent_id_emailtemplates_by_id**
> OrderStatusEmailTemplate patch_sales_orders_statuses_by_parent_id_emailtemplates_by_id(id, parent_id, client_id, patch_operation)

Patch OrderStatusEmailTemplate

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.order_status_email_template import OrderStatusEmailTemplate
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
    api_instance = connectwise_psa.OrderStatusesEmailTemplateApi(api_client)
    id = 56 # int | emailtemplateId
    parent_id = 56 # int | statusId
    client_id = 'client_id_example' # str | 
    patch_operation = [connectwise_psa.PatchOperation()] # List[PatchOperation] | List of PatchOperation

    try:
        # Patch OrderStatusEmailTemplate
        api_response = api_instance.patch_sales_orders_statuses_by_parent_id_emailtemplates_by_id(id, parent_id, client_id, patch_operation)
        print("The response of OrderStatusesEmailTemplateApi->patch_sales_orders_statuses_by_parent_id_emailtemplates_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrderStatusesEmailTemplateApi->patch_sales_orders_statuses_by_parent_id_emailtemplates_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| emailtemplateId | 
 **parent_id** | **int**| statusId | 
 **client_id** | **str**|  | 
 **patch_operation** | [**List[PatchOperation]**](PatchOperation.md)| List of PatchOperation | 

### Return type

[**OrderStatusEmailTemplate**](OrderStatusEmailTemplate.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OrderStatusEmailTemplate |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_sales_orders_statuses_by_parent_id_emailtemplates**
> OrderStatusEmailTemplate post_sales_orders_statuses_by_parent_id_emailtemplates(parent_id, client_id, order_status_email_template)

Post OrderStatusEmailTemplate

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.order_status_email_template import OrderStatusEmailTemplate
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
    api_instance = connectwise_psa.OrderStatusesEmailTemplateApi(api_client)
    parent_id = 56 # int | statusId
    client_id = 'client_id_example' # str | 
    order_status_email_template = connectwise_psa.OrderStatusEmailTemplate() # OrderStatusEmailTemplate | orderStatusEmailTemplate

    try:
        # Post OrderStatusEmailTemplate
        api_response = api_instance.post_sales_orders_statuses_by_parent_id_emailtemplates(parent_id, client_id, order_status_email_template)
        print("The response of OrderStatusesEmailTemplateApi->post_sales_orders_statuses_by_parent_id_emailtemplates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrderStatusesEmailTemplateApi->post_sales_orders_statuses_by_parent_id_emailtemplates: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| statusId | 
 **client_id** | **str**|  | 
 **order_status_email_template** | [**OrderStatusEmailTemplate**](OrderStatusEmailTemplate.md)| orderStatusEmailTemplate | 

### Return type

[**OrderStatusEmailTemplate**](OrderStatusEmailTemplate.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | OrderStatusEmailTemplate |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_sales_orders_statuses_by_parent_id_emailtemplates_by_id**
> OrderStatusEmailTemplate put_sales_orders_statuses_by_parent_id_emailtemplates_by_id(id, parent_id, client_id, order_status_email_template)

Put OrderStatusEmailTemplate

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.order_status_email_template import OrderStatusEmailTemplate
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
    api_instance = connectwise_psa.OrderStatusesEmailTemplateApi(api_client)
    id = 56 # int | emailtemplateId
    parent_id = 56 # int | statusId
    client_id = 'client_id_example' # str | 
    order_status_email_template = connectwise_psa.OrderStatusEmailTemplate() # OrderStatusEmailTemplate | orderStatusEmailTemplate

    try:
        # Put OrderStatusEmailTemplate
        api_response = api_instance.put_sales_orders_statuses_by_parent_id_emailtemplates_by_id(id, parent_id, client_id, order_status_email_template)
        print("The response of OrderStatusesEmailTemplateApi->put_sales_orders_statuses_by_parent_id_emailtemplates_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrderStatusesEmailTemplateApi->put_sales_orders_statuses_by_parent_id_emailtemplates_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| emailtemplateId | 
 **parent_id** | **int**| statusId | 
 **client_id** | **str**|  | 
 **order_status_email_template** | [**OrderStatusEmailTemplate**](OrderStatusEmailTemplate.md)| orderStatusEmailTemplate | 

### Return type

[**OrderStatusEmailTemplate**](OrderStatusEmailTemplate.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OrderStatusEmailTemplate |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

