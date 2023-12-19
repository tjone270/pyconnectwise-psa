# connectwise_psa.ProcurementAdjustmentsApi

All URIs are relative to *https://api-aus.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_procurement_adjustments_by_id**](ProcurementAdjustmentsApi.md#delete_procurement_adjustments_by_id) | **DELETE** /procurement/adjustments/{id} | Delete ProcurementAdjustment
[**get_procurement_adjustments**](ProcurementAdjustmentsApi.md#get_procurement_adjustments) | **GET** /procurement/adjustments | Get List of ProcurementAdjustment
[**get_procurement_adjustments_by_id**](ProcurementAdjustmentsApi.md#get_procurement_adjustments_by_id) | **GET** /procurement/adjustments/{id} | Get ProcurementAdjustment
[**get_procurement_adjustments_count**](ProcurementAdjustmentsApi.md#get_procurement_adjustments_count) | **GET** /procurement/adjustments/count | Get Count of ProcurementAdjustment
[**patch_procurement_adjustments_by_id**](ProcurementAdjustmentsApi.md#patch_procurement_adjustments_by_id) | **PATCH** /procurement/adjustments/{id} | Patch ProcurementAdjustment
[**post_procurement_adjustments**](ProcurementAdjustmentsApi.md#post_procurement_adjustments) | **POST** /procurement/adjustments | Post ProcurementAdjustment
[**put_procurement_adjustments_by_id**](ProcurementAdjustmentsApi.md#put_procurement_adjustments_by_id) | **PUT** /procurement/adjustments/{id} | Put ProcurementAdjustment


# **delete_procurement_adjustments_by_id**
> delete_procurement_adjustments_by_id(id, client_id)

Delete ProcurementAdjustment

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
    api_instance = connectwise_psa.ProcurementAdjustmentsApi(api_client)
    id = 56 # int | adjustmentId
    client_id = 'client_id_example' # str | 

    try:
        # Delete ProcurementAdjustment
        api_instance.delete_procurement_adjustments_by_id(id, client_id)
    except Exception as e:
        print("Exception when calling ProcurementAdjustmentsApi->delete_procurement_adjustments_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| adjustmentId | 
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

# **get_procurement_adjustments**
> List[ProcurementAdjustment] get_procurement_adjustments(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of ProcurementAdjustment

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.procurement_adjustment import ProcurementAdjustment
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
    api_instance = connectwise_psa.ProcurementAdjustmentsApi(api_client)
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
        # Get List of ProcurementAdjustment
        api_response = api_instance.get_procurement_adjustments(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of ProcurementAdjustmentsApi->get_procurement_adjustments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProcurementAdjustmentsApi->get_procurement_adjustments: %s\n" % e)
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

[**List[ProcurementAdjustment]**](ProcurementAdjustment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of ProcurementAdjustment |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_procurement_adjustments_by_id**
> ProcurementAdjustment get_procurement_adjustments_by_id(id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get ProcurementAdjustment

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.procurement_adjustment import ProcurementAdjustment
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
    api_instance = connectwise_psa.ProcurementAdjustmentsApi(api_client)
    id = 56 # int | adjustmentId
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
        # Get ProcurementAdjustment
        api_response = api_instance.get_procurement_adjustments_by_id(id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of ProcurementAdjustmentsApi->get_procurement_adjustments_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProcurementAdjustmentsApi->get_procurement_adjustments_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| adjustmentId | 
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

[**ProcurementAdjustment**](ProcurementAdjustment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ProcurementAdjustment |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_procurement_adjustments_count**
> Count get_procurement_adjustments_count(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Count of ProcurementAdjustment

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
    api_instance = connectwise_psa.ProcurementAdjustmentsApi(api_client)
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
        # Get Count of ProcurementAdjustment
        api_response = api_instance.get_procurement_adjustments_count(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of ProcurementAdjustmentsApi->get_procurement_adjustments_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProcurementAdjustmentsApi->get_procurement_adjustments_count: %s\n" % e)
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

# **patch_procurement_adjustments_by_id**
> ProcurementAdjustment patch_procurement_adjustments_by_id(id, client_id, patch_operation)

Patch ProcurementAdjustment

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.patch_operation import PatchOperation
from connectwise_psa.models.procurement_adjustment import ProcurementAdjustment
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
    api_instance = connectwise_psa.ProcurementAdjustmentsApi(api_client)
    id = 56 # int | adjustmentId
    client_id = 'client_id_example' # str | 
    patch_operation = [connectwise_psa.PatchOperation()] # List[PatchOperation] | List of PatchOperation

    try:
        # Patch ProcurementAdjustment
        api_response = api_instance.patch_procurement_adjustments_by_id(id, client_id, patch_operation)
        print("The response of ProcurementAdjustmentsApi->patch_procurement_adjustments_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProcurementAdjustmentsApi->patch_procurement_adjustments_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| adjustmentId | 
 **client_id** | **str**|  | 
 **patch_operation** | [**List[PatchOperation]**](PatchOperation.md)| List of PatchOperation | 

### Return type

[**ProcurementAdjustment**](ProcurementAdjustment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ProcurementAdjustment |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_procurement_adjustments**
> ProcurementAdjustment post_procurement_adjustments(client_id, procurement_adjustment)

Post ProcurementAdjustment

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.procurement_adjustment import ProcurementAdjustment
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
    api_instance = connectwise_psa.ProcurementAdjustmentsApi(api_client)
    client_id = 'client_id_example' # str | 
    procurement_adjustment = connectwise_psa.ProcurementAdjustment() # ProcurementAdjustment | adjustment

    try:
        # Post ProcurementAdjustment
        api_response = api_instance.post_procurement_adjustments(client_id, procurement_adjustment)
        print("The response of ProcurementAdjustmentsApi->post_procurement_adjustments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProcurementAdjustmentsApi->post_procurement_adjustments: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**|  | 
 **procurement_adjustment** | [**ProcurementAdjustment**](ProcurementAdjustment.md)| adjustment | 

### Return type

[**ProcurementAdjustment**](ProcurementAdjustment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | ProcurementAdjustment |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_procurement_adjustments_by_id**
> ProcurementAdjustment put_procurement_adjustments_by_id(id, client_id, procurement_adjustment)

Put ProcurementAdjustment

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.procurement_adjustment import ProcurementAdjustment
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
    api_instance = connectwise_psa.ProcurementAdjustmentsApi(api_client)
    id = 56 # int | adjustmentId
    client_id = 'client_id_example' # str | 
    procurement_adjustment = connectwise_psa.ProcurementAdjustment() # ProcurementAdjustment | adjustment

    try:
        # Put ProcurementAdjustment
        api_response = api_instance.put_procurement_adjustments_by_id(id, client_id, procurement_adjustment)
        print("The response of ProcurementAdjustmentsApi->put_procurement_adjustments_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProcurementAdjustmentsApi->put_procurement_adjustments_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| adjustmentId | 
 **client_id** | **str**|  | 
 **procurement_adjustment** | [**ProcurementAdjustment**](ProcurementAdjustment.md)| adjustment | 

### Return type

[**ProcurementAdjustment**](ProcurementAdjustment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ProcurementAdjustment |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

