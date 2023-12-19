# connectwise_psa.RMADispositionsApi

All URIs are relative to *https://api-aus.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_procurement_rma_dispositions_by_id**](RMADispositionsApi.md#delete_procurement_rma_dispositions_by_id) | **DELETE** /procurement/RMADispositions/{id} | Delete RmaDisposition
[**get_procurement_rma_dispositions**](RMADispositionsApi.md#get_procurement_rma_dispositions) | **GET** /procurement/RMADispositions | Get List of RmaDisposition
[**get_procurement_rma_dispositions_by_id**](RMADispositionsApi.md#get_procurement_rma_dispositions_by_id) | **GET** /procurement/RMADispositions/{id} | Get RmaDisposition
[**get_procurement_rma_dispositions_count**](RMADispositionsApi.md#get_procurement_rma_dispositions_count) | **GET** /procurement/RMADispositions/count | Get Count of RmaDisposition
[**patch_procurement_rma_dispositions_by_id**](RMADispositionsApi.md#patch_procurement_rma_dispositions_by_id) | **PATCH** /procurement/RMADispositions/{id} | Patch RmaDisposition
[**post_procurement_rma_dispositions**](RMADispositionsApi.md#post_procurement_rma_dispositions) | **POST** /procurement/RMADispositions | Post RmaDisposition
[**put_procurement_rma_dispositions_by_id**](RMADispositionsApi.md#put_procurement_rma_dispositions_by_id) | **PUT** /procurement/RMADispositions/{id} | Put RmaDisposition


# **delete_procurement_rma_dispositions_by_id**
> delete_procurement_rma_dispositions_by_id(id, client_id)

Delete RmaDisposition

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
    api_instance = connectwise_psa.RMADispositionsApi(api_client)
    id = 56 # int | RMADispositionId
    client_id = 'client_id_example' # str | 

    try:
        # Delete RmaDisposition
        api_instance.delete_procurement_rma_dispositions_by_id(id, client_id)
    except Exception as e:
        print("Exception when calling RMADispositionsApi->delete_procurement_rma_dispositions_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| RMADispositionId | 
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

# **get_procurement_rma_dispositions**
> List[RmaDisposition] get_procurement_rma_dispositions(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of RmaDisposition

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.rma_disposition import RmaDisposition
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
    api_instance = connectwise_psa.RMADispositionsApi(api_client)
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
        # Get List of RmaDisposition
        api_response = api_instance.get_procurement_rma_dispositions(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of RMADispositionsApi->get_procurement_rma_dispositions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RMADispositionsApi->get_procurement_rma_dispositions: %s\n" % e)
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

[**List[RmaDisposition]**](RmaDisposition.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of RmaDisposition |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_procurement_rma_dispositions_by_id**
> RmaDisposition get_procurement_rma_dispositions_by_id(id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get RmaDisposition

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.rma_disposition import RmaDisposition
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
    api_instance = connectwise_psa.RMADispositionsApi(api_client)
    id = 56 # int | RMADispositionId
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
        # Get RmaDisposition
        api_response = api_instance.get_procurement_rma_dispositions_by_id(id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of RMADispositionsApi->get_procurement_rma_dispositions_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RMADispositionsApi->get_procurement_rma_dispositions_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| RMADispositionId | 
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

[**RmaDisposition**](RmaDisposition.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | RmaDisposition |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_procurement_rma_dispositions_count**
> Count get_procurement_rma_dispositions_count(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Count of RmaDisposition

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
    api_instance = connectwise_psa.RMADispositionsApi(api_client)
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
        # Get Count of RmaDisposition
        api_response = api_instance.get_procurement_rma_dispositions_count(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of RMADispositionsApi->get_procurement_rma_dispositions_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RMADispositionsApi->get_procurement_rma_dispositions_count: %s\n" % e)
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

# **patch_procurement_rma_dispositions_by_id**
> RmaDisposition patch_procurement_rma_dispositions_by_id(id, client_id, patch_operation)

Patch RmaDisposition

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.patch_operation import PatchOperation
from connectwise_psa.models.rma_disposition import RmaDisposition
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
    api_instance = connectwise_psa.RMADispositionsApi(api_client)
    id = 56 # int | RMADispositionId
    client_id = 'client_id_example' # str | 
    patch_operation = [connectwise_psa.PatchOperation()] # List[PatchOperation] | List of PatchOperation

    try:
        # Patch RmaDisposition
        api_response = api_instance.patch_procurement_rma_dispositions_by_id(id, client_id, patch_operation)
        print("The response of RMADispositionsApi->patch_procurement_rma_dispositions_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RMADispositionsApi->patch_procurement_rma_dispositions_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| RMADispositionId | 
 **client_id** | **str**|  | 
 **patch_operation** | [**List[PatchOperation]**](PatchOperation.md)| List of PatchOperation | 

### Return type

[**RmaDisposition**](RmaDisposition.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | RmaDisposition |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_procurement_rma_dispositions**
> RmaDisposition post_procurement_rma_dispositions(client_id, rma_disposition)

Post RmaDisposition

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.rma_disposition import RmaDisposition
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
    api_instance = connectwise_psa.RMADispositionsApi(api_client)
    client_id = 'client_id_example' # str | 
    rma_disposition = connectwise_psa.RmaDisposition() # RmaDisposition | rmaDisposition

    try:
        # Post RmaDisposition
        api_response = api_instance.post_procurement_rma_dispositions(client_id, rma_disposition)
        print("The response of RMADispositionsApi->post_procurement_rma_dispositions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RMADispositionsApi->post_procurement_rma_dispositions: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**|  | 
 **rma_disposition** | [**RmaDisposition**](RmaDisposition.md)| rmaDisposition | 

### Return type

[**RmaDisposition**](RmaDisposition.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | RmaDisposition |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_procurement_rma_dispositions_by_id**
> RmaDisposition put_procurement_rma_dispositions_by_id(id, client_id, rma_disposition)

Put RmaDisposition

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.rma_disposition import RmaDisposition
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
    api_instance = connectwise_psa.RMADispositionsApi(api_client)
    id = 56 # int | RMADispositionId
    client_id = 'client_id_example' # str | 
    rma_disposition = connectwise_psa.RmaDisposition() # RmaDisposition | rmaDisposition

    try:
        # Put RmaDisposition
        api_response = api_instance.put_procurement_rma_dispositions_by_id(id, client_id, rma_disposition)
        print("The response of RMADispositionsApi->put_procurement_rma_dispositions_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RMADispositionsApi->put_procurement_rma_dispositions_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| RMADispositionId | 
 **client_id** | **str**|  | 
 **rma_disposition** | [**RmaDisposition**](RmaDisposition.md)| rmaDisposition | 

### Return type

[**RmaDisposition**](RmaDisposition.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | RmaDisposition |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

