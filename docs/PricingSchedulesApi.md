# connectwise_psa.PricingSchedulesApi

All URIs are relative to *https://api-aus.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_procurement_pricingschedules_by_id**](PricingSchedulesApi.md#delete_procurement_pricingschedules_by_id) | **DELETE** /procurement/pricingschedules/{id} | Delete PricingSchedule
[**get_procurement_pricingschedules**](PricingSchedulesApi.md#get_procurement_pricingschedules) | **GET** /procurement/pricingschedules | Get List of PricingSchedule
[**get_procurement_pricingschedules_by_id**](PricingSchedulesApi.md#get_procurement_pricingschedules_by_id) | **GET** /procurement/pricingschedules/{id} | Get PricingSchedule
[**get_procurement_pricingschedules_count**](PricingSchedulesApi.md#get_procurement_pricingschedules_count) | **GET** /procurement/pricingschedules/count | Get Count of PricingSchedule
[**patch_procurement_pricingschedules_by_id**](PricingSchedulesApi.md#patch_procurement_pricingschedules_by_id) | **PATCH** /procurement/pricingschedules/{id} | Patch PricingSchedule
[**post_procurement_pricingschedules**](PricingSchedulesApi.md#post_procurement_pricingschedules) | **POST** /procurement/pricingschedules | Post PricingSchedule
[**put_procurement_pricingschedules_by_id**](PricingSchedulesApi.md#put_procurement_pricingschedules_by_id) | **PUT** /procurement/pricingschedules/{id} | Put PricingSchedule


# **delete_procurement_pricingschedules_by_id**
> delete_procurement_pricingschedules_by_id(id, client_id)

Delete PricingSchedule

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
    api_instance = connectwise_psa.PricingSchedulesApi(api_client)
    id = 56 # int | pricingscheduleId
    client_id = 'client_id_example' # str | 

    try:
        # Delete PricingSchedule
        api_instance.delete_procurement_pricingschedules_by_id(id, client_id)
    except Exception as e:
        print("Exception when calling PricingSchedulesApi->delete_procurement_pricingschedules_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| pricingscheduleId | 
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

# **get_procurement_pricingschedules**
> List[PricingSchedule] get_procurement_pricingschedules(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of PricingSchedule

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.pricing_schedule import PricingSchedule
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
    api_instance = connectwise_psa.PricingSchedulesApi(api_client)
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
        # Get List of PricingSchedule
        api_response = api_instance.get_procurement_pricingschedules(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of PricingSchedulesApi->get_procurement_pricingschedules:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PricingSchedulesApi->get_procurement_pricingschedules: %s\n" % e)
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

[**List[PricingSchedule]**](PricingSchedule.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of PricingSchedule |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_procurement_pricingschedules_by_id**
> PricingSchedule get_procurement_pricingschedules_by_id(id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get PricingSchedule

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.pricing_schedule import PricingSchedule
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
    api_instance = connectwise_psa.PricingSchedulesApi(api_client)
    id = 56 # int | pricingscheduleId
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
        # Get PricingSchedule
        api_response = api_instance.get_procurement_pricingschedules_by_id(id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of PricingSchedulesApi->get_procurement_pricingschedules_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PricingSchedulesApi->get_procurement_pricingschedules_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| pricingscheduleId | 
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

[**PricingSchedule**](PricingSchedule.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | PricingSchedule |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_procurement_pricingschedules_count**
> Count get_procurement_pricingschedules_count(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Count of PricingSchedule

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
    api_instance = connectwise_psa.PricingSchedulesApi(api_client)
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
        # Get Count of PricingSchedule
        api_response = api_instance.get_procurement_pricingschedules_count(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of PricingSchedulesApi->get_procurement_pricingschedules_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PricingSchedulesApi->get_procurement_pricingschedules_count: %s\n" % e)
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

# **patch_procurement_pricingschedules_by_id**
> PricingSchedule patch_procurement_pricingschedules_by_id(id, client_id, patch_operation)

Patch PricingSchedule

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.patch_operation import PatchOperation
from connectwise_psa.models.pricing_schedule import PricingSchedule
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
    api_instance = connectwise_psa.PricingSchedulesApi(api_client)
    id = 56 # int | pricingscheduleId
    client_id = 'client_id_example' # str | 
    patch_operation = [connectwise_psa.PatchOperation()] # List[PatchOperation] | List of PatchOperation

    try:
        # Patch PricingSchedule
        api_response = api_instance.patch_procurement_pricingschedules_by_id(id, client_id, patch_operation)
        print("The response of PricingSchedulesApi->patch_procurement_pricingschedules_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PricingSchedulesApi->patch_procurement_pricingschedules_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| pricingscheduleId | 
 **client_id** | **str**|  | 
 **patch_operation** | [**List[PatchOperation]**](PatchOperation.md)| List of PatchOperation | 

### Return type

[**PricingSchedule**](PricingSchedule.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | PricingSchedule |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_procurement_pricingschedules**
> PricingSchedule post_procurement_pricingschedules(client_id, pricing_schedule)

Post PricingSchedule

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.pricing_schedule import PricingSchedule
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
    api_instance = connectwise_psa.PricingSchedulesApi(api_client)
    client_id = 'client_id_example' # str | 
    pricing_schedule = connectwise_psa.PricingSchedule() # PricingSchedule | pricingSchedule

    try:
        # Post PricingSchedule
        api_response = api_instance.post_procurement_pricingschedules(client_id, pricing_schedule)
        print("The response of PricingSchedulesApi->post_procurement_pricingschedules:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PricingSchedulesApi->post_procurement_pricingschedules: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**|  | 
 **pricing_schedule** | [**PricingSchedule**](PricingSchedule.md)| pricingSchedule | 

### Return type

[**PricingSchedule**](PricingSchedule.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | PricingSchedule |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_procurement_pricingschedules_by_id**
> PricingSchedule put_procurement_pricingschedules_by_id(id, client_id, pricing_schedule)

Put PricingSchedule

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.pricing_schedule import PricingSchedule
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
    api_instance = connectwise_psa.PricingSchedulesApi(api_client)
    id = 56 # int | pricingscheduleId
    client_id = 'client_id_example' # str | 
    pricing_schedule = connectwise_psa.PricingSchedule() # PricingSchedule | pricingSchedule

    try:
        # Put PricingSchedule
        api_response = api_instance.put_procurement_pricingschedules_by_id(id, client_id, pricing_schedule)
        print("The response of PricingSchedulesApi->put_procurement_pricingschedules_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PricingSchedulesApi->put_procurement_pricingschedules_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| pricingscheduleId | 
 **client_id** | **str**|  | 
 **pricing_schedule** | [**PricingSchedule**](PricingSchedule.md)| pricingSchedule | 

### Return type

[**PricingSchedule**](PricingSchedule.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | PricingSchedule |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

