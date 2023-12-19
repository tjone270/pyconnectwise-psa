# connectwise_psa.OpportunityForecastItemsApi

All URIs are relative to *https://api-aus.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_sales_opportunities_by_parent_id_forecast_by_id**](OpportunityForecastItemsApi.md#delete_sales_opportunities_by_parent_id_forecast_by_id) | **DELETE** /sales/opportunities/{parentId}/forecast/{id} | Delete ForecastItem
[**get_sales_opportunities_by_parent_id_forecast_by_id**](OpportunityForecastItemsApi.md#get_sales_opportunities_by_parent_id_forecast_by_id) | **GET** /sales/opportunities/{parentId}/forecast/{id} | Get ForecastItem
[**patch_sales_opportunities_by_parent_id_forecast_by_id**](OpportunityForecastItemsApi.md#patch_sales_opportunities_by_parent_id_forecast_by_id) | **PATCH** /sales/opportunities/{parentId}/forecast/{id} | Patch ForecastItem
[**post_sales_opportunities_by_parent_id_forecast_by_id**](OpportunityForecastItemsApi.md#post_sales_opportunities_by_parent_id_forecast_by_id) | **POST** /sales/opportunities/{parentId}/forecast/{id} | Post ForecastItem
[**put_sales_opportunities_by_parent_id_forecast_by_id**](OpportunityForecastItemsApi.md#put_sales_opportunities_by_parent_id_forecast_by_id) | **PUT** /sales/opportunities/{parentId}/forecast/{id} | Put ForecastItem


# **delete_sales_opportunities_by_parent_id_forecast_by_id**
> delete_sales_opportunities_by_parent_id_forecast_by_id(id, parent_id, client_id)

Delete ForecastItem

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
    api_instance = connectwise_psa.OpportunityForecastItemsApi(api_client)
    id = 56 # int | forecastId
    parent_id = 56 # int | opportunityId
    client_id = 'client_id_example' # str | 

    try:
        # Delete ForecastItem
        api_instance.delete_sales_opportunities_by_parent_id_forecast_by_id(id, parent_id, client_id)
    except Exception as e:
        print("Exception when calling OpportunityForecastItemsApi->delete_sales_opportunities_by_parent_id_forecast_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| forecastId | 
 **parent_id** | **int**| opportunityId | 
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

# **get_sales_opportunities_by_parent_id_forecast_by_id**
> ForecastItem get_sales_opportunities_by_parent_id_forecast_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get ForecastItem

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.forecast_item import ForecastItem
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
    api_instance = connectwise_psa.OpportunityForecastItemsApi(api_client)
    id = 56 # int | forecastId
    parent_id = 56 # int | opportunityId
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
        # Get ForecastItem
        api_response = api_instance.get_sales_opportunities_by_parent_id_forecast_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of OpportunityForecastItemsApi->get_sales_opportunities_by_parent_id_forecast_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpportunityForecastItemsApi->get_sales_opportunities_by_parent_id_forecast_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| forecastId | 
 **parent_id** | **int**| opportunityId | 
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

[**ForecastItem**](ForecastItem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ForecastItem |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_sales_opportunities_by_parent_id_forecast_by_id**
> ForecastItem patch_sales_opportunities_by_parent_id_forecast_by_id(id, parent_id, client_id, patch_operation)

Patch ForecastItem

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.forecast_item import ForecastItem
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
    api_instance = connectwise_psa.OpportunityForecastItemsApi(api_client)
    id = 56 # int | forecastId
    parent_id = 56 # int | opportunityId
    client_id = 'client_id_example' # str | 
    patch_operation = [connectwise_psa.PatchOperation()] # List[PatchOperation] | List of PatchOperation

    try:
        # Patch ForecastItem
        api_response = api_instance.patch_sales_opportunities_by_parent_id_forecast_by_id(id, parent_id, client_id, patch_operation)
        print("The response of OpportunityForecastItemsApi->patch_sales_opportunities_by_parent_id_forecast_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpportunityForecastItemsApi->patch_sales_opportunities_by_parent_id_forecast_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| forecastId | 
 **parent_id** | **int**| opportunityId | 
 **client_id** | **str**|  | 
 **patch_operation** | [**List[PatchOperation]**](PatchOperation.md)| List of PatchOperation | 

### Return type

[**ForecastItem**](ForecastItem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ForecastItem |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_sales_opportunities_by_parent_id_forecast_by_id**
> ForecastItem post_sales_opportunities_by_parent_id_forecast_by_id(id, parent_id, client_id, forecast_item)

Post ForecastItem

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.forecast_item import ForecastItem
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
    api_instance = connectwise_psa.OpportunityForecastItemsApi(api_client)
    id = 56 # int | forecastId
    parent_id = 56 # int | opportunityId
    client_id = 'client_id_example' # str | 
    forecast_item = connectwise_psa.ForecastItem() # ForecastItem | forecast

    try:
        # Post ForecastItem
        api_response = api_instance.post_sales_opportunities_by_parent_id_forecast_by_id(id, parent_id, client_id, forecast_item)
        print("The response of OpportunityForecastItemsApi->post_sales_opportunities_by_parent_id_forecast_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpportunityForecastItemsApi->post_sales_opportunities_by_parent_id_forecast_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| forecastId | 
 **parent_id** | **int**| opportunityId | 
 **client_id** | **str**|  | 
 **forecast_item** | [**ForecastItem**](ForecastItem.md)| forecast | 

### Return type

[**ForecastItem**](ForecastItem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | ForecastItem |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_sales_opportunities_by_parent_id_forecast_by_id**
> ForecastItem put_sales_opportunities_by_parent_id_forecast_by_id(id, parent_id, client_id, forecast_item)

Put ForecastItem

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.forecast_item import ForecastItem
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
    api_instance = connectwise_psa.OpportunityForecastItemsApi(api_client)
    id = 56 # int | forecastId
    parent_id = 56 # int | opportunityId
    client_id = 'client_id_example' # str | 
    forecast_item = connectwise_psa.ForecastItem() # ForecastItem | forecast

    try:
        # Put ForecastItem
        api_response = api_instance.put_sales_opportunities_by_parent_id_forecast_by_id(id, parent_id, client_id, forecast_item)
        print("The response of OpportunityForecastItemsApi->put_sales_opportunities_by_parent_id_forecast_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpportunityForecastItemsApi->put_sales_opportunities_by_parent_id_forecast_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| forecastId | 
 **parent_id** | **int**| opportunityId | 
 **client_id** | **str**|  | 
 **forecast_item** | [**ForecastItem**](ForecastItem.md)| forecast | 

### Return type

[**ForecastItem**](ForecastItem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ForecastItem |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

