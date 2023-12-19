# connectwise_psa.PurchaseOrderStatusEmailTemplatesApi

All URIs are relative to *https://aus-api.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_procurement_purchaseorderstatuses_by_parent_id_emailtemplates_by_id**](PurchaseOrderStatusEmailTemplatesApi.md#delete_procurement_purchaseorderstatuses_by_parent_id_emailtemplates_by_id) | **DELETE** /procurement/purchaseorderstatuses/{parentId}/emailtemplates/{id} | Delete PurchaseOrderStatusEmailTemplate
[**get_procurement_purchaseorderstatuses_by_parent_id_emailtemplates**](PurchaseOrderStatusEmailTemplatesApi.md#get_procurement_purchaseorderstatuses_by_parent_id_emailtemplates) | **GET** /procurement/purchaseorderstatuses/{parentId}/emailtemplates/ | Get List of PurchaseOrderStatusEmailTemplate
[**get_procurement_purchaseorderstatuses_by_parent_id_emailtemplates_by_id**](PurchaseOrderStatusEmailTemplatesApi.md#get_procurement_purchaseorderstatuses_by_parent_id_emailtemplates_by_id) | **GET** /procurement/purchaseorderstatuses/{parentId}/emailtemplates/{id} | Get PurchaseOrderStatusEmailTemplate
[**get_procurement_purchaseorderstatuses_by_parent_id_emailtemplates_count**](PurchaseOrderStatusEmailTemplatesApi.md#get_procurement_purchaseorderstatuses_by_parent_id_emailtemplates_count) | **GET** /procurement/purchaseorderstatuses/{parentId}/emailtemplates/count | Get Count of PurchaseOrderStatusEmailTemplate
[**patch_procurement_purchaseorderstatuses_by_parent_id_emailtemplates_by_id**](PurchaseOrderStatusEmailTemplatesApi.md#patch_procurement_purchaseorderstatuses_by_parent_id_emailtemplates_by_id) | **PATCH** /procurement/purchaseorderstatuses/{parentId}/emailtemplates/{id} | Patch PurchaseOrderStatusEmailTemplate
[**post_procurement_purchaseorderstatuses_by_parent_id_emailtemplates**](PurchaseOrderStatusEmailTemplatesApi.md#post_procurement_purchaseorderstatuses_by_parent_id_emailtemplates) | **POST** /procurement/purchaseorderstatuses/{parentId}/emailtemplates/ | Post PurchaseOrderStatusEmailTemplate
[**put_procurement_purchaseorderstatuses_by_parent_id_emailtemplates_by_id**](PurchaseOrderStatusEmailTemplatesApi.md#put_procurement_purchaseorderstatuses_by_parent_id_emailtemplates_by_id) | **PUT** /procurement/purchaseorderstatuses/{parentId}/emailtemplates/{id} | Put PurchaseOrderStatusEmailTemplate


# **delete_procurement_purchaseorderstatuses_by_parent_id_emailtemplates_by_id**
> delete_procurement_purchaseorderstatuses_by_parent_id_emailtemplates_by_id(id, parent_id, client_id)

Delete PurchaseOrderStatusEmailTemplate

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
    api_instance = connectwise_psa.PurchaseOrderStatusEmailTemplatesApi(api_client)
    id = 56 # int | emailtemplateId
    parent_id = 56 # int | purchaseorderstatusId
    client_id = 'client_id_example' # str | 

    try:
        # Delete PurchaseOrderStatusEmailTemplate
        api_instance.delete_procurement_purchaseorderstatuses_by_parent_id_emailtemplates_by_id(id, parent_id, client_id)
    except Exception as e:
        print("Exception when calling PurchaseOrderStatusEmailTemplatesApi->delete_procurement_purchaseorderstatuses_by_parent_id_emailtemplates_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| emailtemplateId | 
 **parent_id** | **int**| purchaseorderstatusId | 
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

# **get_procurement_purchaseorderstatuses_by_parent_id_emailtemplates**
> List[PurchaseOrderStatusEmailTemplate] get_procurement_purchaseorderstatuses_by_parent_id_emailtemplates(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of PurchaseOrderStatusEmailTemplate

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.purchase_order_status_email_template import PurchaseOrderStatusEmailTemplate
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
    api_instance = connectwise_psa.PurchaseOrderStatusEmailTemplatesApi(api_client)
    parent_id = 56 # int | purchaseorderstatusId
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
        # Get List of PurchaseOrderStatusEmailTemplate
        api_response = api_instance.get_procurement_purchaseorderstatuses_by_parent_id_emailtemplates(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of PurchaseOrderStatusEmailTemplatesApi->get_procurement_purchaseorderstatuses_by_parent_id_emailtemplates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PurchaseOrderStatusEmailTemplatesApi->get_procurement_purchaseorderstatuses_by_parent_id_emailtemplates: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| purchaseorderstatusId | 
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

[**List[PurchaseOrderStatusEmailTemplate]**](PurchaseOrderStatusEmailTemplate.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of PurchaseOrderStatusEmailTemplate |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_procurement_purchaseorderstatuses_by_parent_id_emailtemplates_by_id**
> PurchaseOrderStatusEmailTemplate get_procurement_purchaseorderstatuses_by_parent_id_emailtemplates_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get PurchaseOrderStatusEmailTemplate

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.purchase_order_status_email_template import PurchaseOrderStatusEmailTemplate
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
    api_instance = connectwise_psa.PurchaseOrderStatusEmailTemplatesApi(api_client)
    id = 56 # int | emailtemplateId
    parent_id = 56 # int | purchaseorderstatusId
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
        # Get PurchaseOrderStatusEmailTemplate
        api_response = api_instance.get_procurement_purchaseorderstatuses_by_parent_id_emailtemplates_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of PurchaseOrderStatusEmailTemplatesApi->get_procurement_purchaseorderstatuses_by_parent_id_emailtemplates_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PurchaseOrderStatusEmailTemplatesApi->get_procurement_purchaseorderstatuses_by_parent_id_emailtemplates_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| emailtemplateId | 
 **parent_id** | **int**| purchaseorderstatusId | 
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

[**PurchaseOrderStatusEmailTemplate**](PurchaseOrderStatusEmailTemplate.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | PurchaseOrderStatusEmailTemplate |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_procurement_purchaseorderstatuses_by_parent_id_emailtemplates_count**
> Count get_procurement_purchaseorderstatuses_by_parent_id_emailtemplates_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Count of PurchaseOrderStatusEmailTemplate

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
    api_instance = connectwise_psa.PurchaseOrderStatusEmailTemplatesApi(api_client)
    parent_id = 56 # int | purchaseorderstatusId
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
        # Get Count of PurchaseOrderStatusEmailTemplate
        api_response = api_instance.get_procurement_purchaseorderstatuses_by_parent_id_emailtemplates_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of PurchaseOrderStatusEmailTemplatesApi->get_procurement_purchaseorderstatuses_by_parent_id_emailtemplates_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PurchaseOrderStatusEmailTemplatesApi->get_procurement_purchaseorderstatuses_by_parent_id_emailtemplates_count: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| purchaseorderstatusId | 
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

# **patch_procurement_purchaseorderstatuses_by_parent_id_emailtemplates_by_id**
> PurchaseOrderStatusEmailTemplate patch_procurement_purchaseorderstatuses_by_parent_id_emailtemplates_by_id(id, parent_id, client_id, patch_operation)

Patch PurchaseOrderStatusEmailTemplate

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.patch_operation import PatchOperation
from connectwise_psa.models.purchase_order_status_email_template import PurchaseOrderStatusEmailTemplate
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
    api_instance = connectwise_psa.PurchaseOrderStatusEmailTemplatesApi(api_client)
    id = 56 # int | emailtemplateId
    parent_id = 56 # int | purchaseorderstatusId
    client_id = 'client_id_example' # str | 
    patch_operation = [connectwise_psa.PatchOperation()] # List[PatchOperation] | List of PatchOperation

    try:
        # Patch PurchaseOrderStatusEmailTemplate
        api_response = api_instance.patch_procurement_purchaseorderstatuses_by_parent_id_emailtemplates_by_id(id, parent_id, client_id, patch_operation)
        print("The response of PurchaseOrderStatusEmailTemplatesApi->patch_procurement_purchaseorderstatuses_by_parent_id_emailtemplates_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PurchaseOrderStatusEmailTemplatesApi->patch_procurement_purchaseorderstatuses_by_parent_id_emailtemplates_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| emailtemplateId | 
 **parent_id** | **int**| purchaseorderstatusId | 
 **client_id** | **str**|  | 
 **patch_operation** | [**List[PatchOperation]**](PatchOperation.md)| List of PatchOperation | 

### Return type

[**PurchaseOrderStatusEmailTemplate**](PurchaseOrderStatusEmailTemplate.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | PurchaseOrderStatusEmailTemplate |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_procurement_purchaseorderstatuses_by_parent_id_emailtemplates**
> PurchaseOrderStatusEmailTemplate post_procurement_purchaseorderstatuses_by_parent_id_emailtemplates(parent_id, client_id, purchase_order_status_email_template)

Post PurchaseOrderStatusEmailTemplate

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.purchase_order_status_email_template import PurchaseOrderStatusEmailTemplate
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
    api_instance = connectwise_psa.PurchaseOrderStatusEmailTemplatesApi(api_client)
    parent_id = 56 # int | purchaseorderstatusId
    client_id = 'client_id_example' # str | 
    purchase_order_status_email_template = connectwise_psa.PurchaseOrderStatusEmailTemplate() # PurchaseOrderStatusEmailTemplate | purchaseOrderStatusEmailTemplate

    try:
        # Post PurchaseOrderStatusEmailTemplate
        api_response = api_instance.post_procurement_purchaseorderstatuses_by_parent_id_emailtemplates(parent_id, client_id, purchase_order_status_email_template)
        print("The response of PurchaseOrderStatusEmailTemplatesApi->post_procurement_purchaseorderstatuses_by_parent_id_emailtemplates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PurchaseOrderStatusEmailTemplatesApi->post_procurement_purchaseorderstatuses_by_parent_id_emailtemplates: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| purchaseorderstatusId | 
 **client_id** | **str**|  | 
 **purchase_order_status_email_template** | [**PurchaseOrderStatusEmailTemplate**](PurchaseOrderStatusEmailTemplate.md)| purchaseOrderStatusEmailTemplate | 

### Return type

[**PurchaseOrderStatusEmailTemplate**](PurchaseOrderStatusEmailTemplate.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | PurchaseOrderStatusEmailTemplate |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_procurement_purchaseorderstatuses_by_parent_id_emailtemplates_by_id**
> PurchaseOrderStatusEmailTemplate put_procurement_purchaseorderstatuses_by_parent_id_emailtemplates_by_id(id, parent_id, client_id, purchase_order_status_email_template)

Put PurchaseOrderStatusEmailTemplate

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.purchase_order_status_email_template import PurchaseOrderStatusEmailTemplate
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
    api_instance = connectwise_psa.PurchaseOrderStatusEmailTemplatesApi(api_client)
    id = 56 # int | emailtemplateId
    parent_id = 56 # int | purchaseorderstatusId
    client_id = 'client_id_example' # str | 
    purchase_order_status_email_template = connectwise_psa.PurchaseOrderStatusEmailTemplate() # PurchaseOrderStatusEmailTemplate | purchaseOrderStatusEmailTemplate

    try:
        # Put PurchaseOrderStatusEmailTemplate
        api_response = api_instance.put_procurement_purchaseorderstatuses_by_parent_id_emailtemplates_by_id(id, parent_id, client_id, purchase_order_status_email_template)
        print("The response of PurchaseOrderStatusEmailTemplatesApi->put_procurement_purchaseorderstatuses_by_parent_id_emailtemplates_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PurchaseOrderStatusEmailTemplatesApi->put_procurement_purchaseorderstatuses_by_parent_id_emailtemplates_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| emailtemplateId | 
 **parent_id** | **int**| purchaseorderstatusId | 
 **client_id** | **str**|  | 
 **purchase_order_status_email_template** | [**PurchaseOrderStatusEmailTemplate**](PurchaseOrderStatusEmailTemplate.md)| purchaseOrderStatusEmailTemplate | 

### Return type

[**PurchaseOrderStatusEmailTemplate**](PurchaseOrderStatusEmailTemplate.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | PurchaseOrderStatusEmailTemplate |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

