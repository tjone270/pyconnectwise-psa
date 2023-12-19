# connectwise_psa.PricingDetailsApi

All URIs are relative to *https://aus-api.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_procurement_pricingschedules_by_parent_id_details_by_id**](PricingDetailsApi.md#delete_procurement_pricingschedules_by_parent_id_details_by_id) | **DELETE** /procurement/pricingschedules/{parentId}/details/{id} | Delete PricingDetail
[**get_procurement_pricingschedules_by_parent_id_details**](PricingDetailsApi.md#get_procurement_pricingschedules_by_parent_id_details) | **GET** /procurement/pricingschedules/{parentId}/details | Get List of PricingDetail
[**get_procurement_pricingschedules_by_parent_id_details_by_id**](PricingDetailsApi.md#get_procurement_pricingschedules_by_parent_id_details_by_id) | **GET** /procurement/pricingschedules/{parentId}/details/{id} | Get PricingDetail
[**get_procurement_pricingschedules_by_parent_id_details_count**](PricingDetailsApi.md#get_procurement_pricingschedules_by_parent_id_details_count) | **GET** /procurement/pricingschedules/{parentId}/details/count | Get Count of PricingDetail
[**patch_procurement_pricingschedules_by_parent_id_details_by_id**](PricingDetailsApi.md#patch_procurement_pricingschedules_by_parent_id_details_by_id) | **PATCH** /procurement/pricingschedules/{parentId}/details/{id} | Patch PricingDetail
[**post_procurement_pricingschedules_by_parent_id_details**](PricingDetailsApi.md#post_procurement_pricingschedules_by_parent_id_details) | **POST** /procurement/pricingschedules/{parentId}/details | Post PricingDetail
[**put_procurement_pricingschedules_by_parent_id_details_by_id**](PricingDetailsApi.md#put_procurement_pricingschedules_by_parent_id_details_by_id) | **PUT** /procurement/pricingschedules/{parentId}/details/{id} | Put PricingDetail


# **delete_procurement_pricingschedules_by_parent_id_details_by_id**
> delete_procurement_pricingschedules_by_parent_id_details_by_id(id, parent_id, client_id)

Delete PricingDetail

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
    api_instance = connectwise_psa.PricingDetailsApi(api_client)
    id = 56 # int | detailId
    parent_id = 56 # int | pricingscheduleId
    client_id = 'client_id_example' # str | 

    try:
        # Delete PricingDetail
        api_instance.delete_procurement_pricingschedules_by_parent_id_details_by_id(id, parent_id, client_id)
    except Exception as e:
        print("Exception when calling PricingDetailsApi->delete_procurement_pricingschedules_by_parent_id_details_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| detailId | 
 **parent_id** | **int**| pricingscheduleId | 
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

# **get_procurement_pricingschedules_by_parent_id_details**
> List[PricingDetail] get_procurement_pricingschedules_by_parent_id_details(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of PricingDetail

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.pricing_detail import PricingDetail
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
    api_instance = connectwise_psa.PricingDetailsApi(api_client)
    parent_id = 56 # int | pricingscheduleId
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
        # Get List of PricingDetail
        api_response = api_instance.get_procurement_pricingschedules_by_parent_id_details(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of PricingDetailsApi->get_procurement_pricingschedules_by_parent_id_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PricingDetailsApi->get_procurement_pricingschedules_by_parent_id_details: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| pricingscheduleId | 
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

[**List[PricingDetail]**](PricingDetail.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of PricingDetail |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_procurement_pricingschedules_by_parent_id_details_by_id**
> PricingDetail get_procurement_pricingschedules_by_parent_id_details_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get PricingDetail

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.pricing_detail import PricingDetail
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
    api_instance = connectwise_psa.PricingDetailsApi(api_client)
    id = 56 # int | detailId
    parent_id = 56 # int | pricingscheduleId
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
        # Get PricingDetail
        api_response = api_instance.get_procurement_pricingschedules_by_parent_id_details_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of PricingDetailsApi->get_procurement_pricingschedules_by_parent_id_details_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PricingDetailsApi->get_procurement_pricingschedules_by_parent_id_details_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| detailId | 
 **parent_id** | **int**| pricingscheduleId | 
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

[**PricingDetail**](PricingDetail.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | PricingDetail |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_procurement_pricingschedules_by_parent_id_details_count**
> Count get_procurement_pricingschedules_by_parent_id_details_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Count of PricingDetail

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
    api_instance = connectwise_psa.PricingDetailsApi(api_client)
    parent_id = 56 # int | pricingscheduleId
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
        # Get Count of PricingDetail
        api_response = api_instance.get_procurement_pricingschedules_by_parent_id_details_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of PricingDetailsApi->get_procurement_pricingschedules_by_parent_id_details_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PricingDetailsApi->get_procurement_pricingschedules_by_parent_id_details_count: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| pricingscheduleId | 
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

# **patch_procurement_pricingschedules_by_parent_id_details_by_id**
> PricingDetail patch_procurement_pricingschedules_by_parent_id_details_by_id(id, parent_id, client_id, patch_operation)

Patch PricingDetail

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.patch_operation import PatchOperation
from connectwise_psa.models.pricing_detail import PricingDetail
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
    api_instance = connectwise_psa.PricingDetailsApi(api_client)
    id = 56 # int | detailId
    parent_id = 56 # int | pricingscheduleId
    client_id = 'client_id_example' # str | 
    patch_operation = [connectwise_psa.PatchOperation()] # List[PatchOperation] | List of PatchOperation

    try:
        # Patch PricingDetail
        api_response = api_instance.patch_procurement_pricingschedules_by_parent_id_details_by_id(id, parent_id, client_id, patch_operation)
        print("The response of PricingDetailsApi->patch_procurement_pricingschedules_by_parent_id_details_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PricingDetailsApi->patch_procurement_pricingschedules_by_parent_id_details_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| detailId | 
 **parent_id** | **int**| pricingscheduleId | 
 **client_id** | **str**|  | 
 **patch_operation** | [**List[PatchOperation]**](PatchOperation.md)| List of PatchOperation | 

### Return type

[**PricingDetail**](PricingDetail.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | PricingDetail |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_procurement_pricingschedules_by_parent_id_details**
> PricingDetail post_procurement_pricingschedules_by_parent_id_details(parent_id, client_id, pricing_detail)

Post PricingDetail

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.pricing_detail import PricingDetail
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
    api_instance = connectwise_psa.PricingDetailsApi(api_client)
    parent_id = 56 # int | pricingscheduleId
    client_id = 'client_id_example' # str | 
    pricing_detail = connectwise_psa.PricingDetail() # PricingDetail | pricingDetail

    try:
        # Post PricingDetail
        api_response = api_instance.post_procurement_pricingschedules_by_parent_id_details(parent_id, client_id, pricing_detail)
        print("The response of PricingDetailsApi->post_procurement_pricingschedules_by_parent_id_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PricingDetailsApi->post_procurement_pricingschedules_by_parent_id_details: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| pricingscheduleId | 
 **client_id** | **str**|  | 
 **pricing_detail** | [**PricingDetail**](PricingDetail.md)| pricingDetail | 

### Return type

[**PricingDetail**](PricingDetail.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | PricingDetail |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_procurement_pricingschedules_by_parent_id_details_by_id**
> PricingDetail put_procurement_pricingschedules_by_parent_id_details_by_id(id, parent_id, client_id, pricing_detail)

Put PricingDetail

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.pricing_detail import PricingDetail
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
    api_instance = connectwise_psa.PricingDetailsApi(api_client)
    id = 56 # int | detailId
    parent_id = 56 # int | pricingscheduleId
    client_id = 'client_id_example' # str | 
    pricing_detail = connectwise_psa.PricingDetail() # PricingDetail | pricingDetail

    try:
        # Put PricingDetail
        api_response = api_instance.put_procurement_pricingschedules_by_parent_id_details_by_id(id, parent_id, client_id, pricing_detail)
        print("The response of PricingDetailsApi->put_procurement_pricingschedules_by_parent_id_details_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PricingDetailsApi->put_procurement_pricingschedules_by_parent_id_details_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| detailId | 
 **parent_id** | **int**| pricingscheduleId | 
 **client_id** | **str**|  | 
 **pricing_detail** | [**PricingDetail**](PricingDetail.md)| pricingDetail | 

### Return type

[**PricingDetail**](PricingDetail.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | PricingDetail |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

