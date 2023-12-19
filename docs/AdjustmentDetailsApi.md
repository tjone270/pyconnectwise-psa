# connectwise_psa.AdjustmentDetailsApi

All URIs are relative to *https://api-aus.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_procurement_adjustments_by_parent_id_details_by_id**](AdjustmentDetailsApi.md#delete_procurement_adjustments_by_parent_id_details_by_id) | **DELETE** /procurement/adjustments/{parentId}/details/{id} | Delete AdjustmentDetail
[**get_procurement_adjustments_by_parent_id_details**](AdjustmentDetailsApi.md#get_procurement_adjustments_by_parent_id_details) | **GET** /procurement/adjustments/{parentId}/details | Get List of AdjustmentDetail
[**get_procurement_adjustments_by_parent_id_details_by_id**](AdjustmentDetailsApi.md#get_procurement_adjustments_by_parent_id_details_by_id) | **GET** /procurement/adjustments/{parentId}/details/{id} | Get AdjustmentDetail
[**get_procurement_adjustments_by_parent_id_details_count**](AdjustmentDetailsApi.md#get_procurement_adjustments_by_parent_id_details_count) | **GET** /procurement/adjustments/{parentId}/details/count | Get Count of AdjustmentDetail
[**post_procurement_adjustments_by_parent_id_details**](AdjustmentDetailsApi.md#post_procurement_adjustments_by_parent_id_details) | **POST** /procurement/adjustments/{parentId}/details | Post AdjustmentDetail


# **delete_procurement_adjustments_by_parent_id_details_by_id**
> delete_procurement_adjustments_by_parent_id_details_by_id(id, parent_id, client_id)

Delete AdjustmentDetail

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
    api_instance = connectwise_psa.AdjustmentDetailsApi(api_client)
    id = 56 # int | detailId
    parent_id = 56 # int | adjustmentId
    client_id = 'client_id_example' # str | 

    try:
        # Delete AdjustmentDetail
        api_instance.delete_procurement_adjustments_by_parent_id_details_by_id(id, parent_id, client_id)
    except Exception as e:
        print("Exception when calling AdjustmentDetailsApi->delete_procurement_adjustments_by_parent_id_details_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| detailId | 
 **parent_id** | **int**| adjustmentId | 
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

# **get_procurement_adjustments_by_parent_id_details**
> List[AdjustmentDetail] get_procurement_adjustments_by_parent_id_details(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of AdjustmentDetail

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.adjustment_detail import AdjustmentDetail
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
    api_instance = connectwise_psa.AdjustmentDetailsApi(api_client)
    parent_id = 56 # int | adjustmentId
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
        # Get List of AdjustmentDetail
        api_response = api_instance.get_procurement_adjustments_by_parent_id_details(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of AdjustmentDetailsApi->get_procurement_adjustments_by_parent_id_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdjustmentDetailsApi->get_procurement_adjustments_by_parent_id_details: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| adjustmentId | 
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

[**List[AdjustmentDetail]**](AdjustmentDetail.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of AdjustmentDetail |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_procurement_adjustments_by_parent_id_details_by_id**
> AdjustmentDetail get_procurement_adjustments_by_parent_id_details_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get AdjustmentDetail

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.adjustment_detail import AdjustmentDetail
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
    api_instance = connectwise_psa.AdjustmentDetailsApi(api_client)
    id = 56 # int | detailId
    parent_id = 56 # int | adjustmentId
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
        # Get AdjustmentDetail
        api_response = api_instance.get_procurement_adjustments_by_parent_id_details_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of AdjustmentDetailsApi->get_procurement_adjustments_by_parent_id_details_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdjustmentDetailsApi->get_procurement_adjustments_by_parent_id_details_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| detailId | 
 **parent_id** | **int**| adjustmentId | 
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

[**AdjustmentDetail**](AdjustmentDetail.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | AdjustmentDetail |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_procurement_adjustments_by_parent_id_details_count**
> Count get_procurement_adjustments_by_parent_id_details_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Count of AdjustmentDetail

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
    api_instance = connectwise_psa.AdjustmentDetailsApi(api_client)
    parent_id = 56 # int | adjustmentId
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
        # Get Count of AdjustmentDetail
        api_response = api_instance.get_procurement_adjustments_by_parent_id_details_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of AdjustmentDetailsApi->get_procurement_adjustments_by_parent_id_details_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdjustmentDetailsApi->get_procurement_adjustments_by_parent_id_details_count: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| adjustmentId | 
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

# **post_procurement_adjustments_by_parent_id_details**
> AdjustmentDetail post_procurement_adjustments_by_parent_id_details(parent_id, client_id, adjustment_detail)

Post AdjustmentDetail

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.adjustment_detail import AdjustmentDetail
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
    api_instance = connectwise_psa.AdjustmentDetailsApi(api_client)
    parent_id = 56 # int | adjustmentId
    client_id = 'client_id_example' # str | 
    adjustment_detail = connectwise_psa.AdjustmentDetail() # AdjustmentDetail | adjustmentDetail

    try:
        # Post AdjustmentDetail
        api_response = api_instance.post_procurement_adjustments_by_parent_id_details(parent_id, client_id, adjustment_detail)
        print("The response of AdjustmentDetailsApi->post_procurement_adjustments_by_parent_id_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdjustmentDetailsApi->post_procurement_adjustments_by_parent_id_details: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| adjustmentId | 
 **client_id** | **str**|  | 
 **adjustment_detail** | [**AdjustmentDetail**](AdjustmentDetail.md)| adjustmentDetail | 

### Return type

[**AdjustmentDetail**](AdjustmentDetail.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | AdjustmentDetail |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

