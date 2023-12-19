# connectwise_psa.UnitOfMeasuresApi

All URIs are relative to *https://aus-api.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_procurement_unit_of_measures_by_id**](UnitOfMeasuresApi.md#delete_procurement_unit_of_measures_by_id) | **DELETE** /procurement/unitOfMeasures/{id} | Delete UnitOfMeasure
[**get_procurement_unit_of_measures**](UnitOfMeasuresApi.md#get_procurement_unit_of_measures) | **GET** /procurement/unitOfMeasures | Get List of UnitOfMeasure
[**get_procurement_unit_of_measures_by_id**](UnitOfMeasuresApi.md#get_procurement_unit_of_measures_by_id) | **GET** /procurement/unitOfMeasures/{id} | Get UnitOfMeasure
[**get_procurement_unit_of_measures_count**](UnitOfMeasuresApi.md#get_procurement_unit_of_measures_count) | **GET** /procurement/unitOfMeasures/count | Get Count of UnitOfMeasure
[**patch_procurement_unit_of_measures_by_id**](UnitOfMeasuresApi.md#patch_procurement_unit_of_measures_by_id) | **PATCH** /procurement/unitOfMeasures/{id} | Patch UnitOfMeasure
[**post_procurement_unit_of_measures**](UnitOfMeasuresApi.md#post_procurement_unit_of_measures) | **POST** /procurement/unitOfMeasures | Post UnitOfMeasure
[**put_procurement_unit_of_measures_by_id**](UnitOfMeasuresApi.md#put_procurement_unit_of_measures_by_id) | **PUT** /procurement/unitOfMeasures/{id} | Put UnitOfMeasure


# **delete_procurement_unit_of_measures_by_id**
> delete_procurement_unit_of_measures_by_id(id, client_id)

Delete UnitOfMeasure

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
    api_instance = connectwise_psa.UnitOfMeasuresApi(api_client)
    id = 56 # int | unitOfMeasureId
    client_id = 'client_id_example' # str | 

    try:
        # Delete UnitOfMeasure
        api_instance.delete_procurement_unit_of_measures_by_id(id, client_id)
    except Exception as e:
        print("Exception when calling UnitOfMeasuresApi->delete_procurement_unit_of_measures_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| unitOfMeasureId | 
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

# **get_procurement_unit_of_measures**
> List[UnitOfMeasure] get_procurement_unit_of_measures(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of UnitOfMeasure

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.unit_of_measure import UnitOfMeasure
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
    api_instance = connectwise_psa.UnitOfMeasuresApi(api_client)
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
        # Get List of UnitOfMeasure
        api_response = api_instance.get_procurement_unit_of_measures(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of UnitOfMeasuresApi->get_procurement_unit_of_measures:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UnitOfMeasuresApi->get_procurement_unit_of_measures: %s\n" % e)
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

[**List[UnitOfMeasure]**](UnitOfMeasure.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of UnitOfMeasure |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_procurement_unit_of_measures_by_id**
> UnitOfMeasure get_procurement_unit_of_measures_by_id(id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get UnitOfMeasure

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.unit_of_measure import UnitOfMeasure
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
    api_instance = connectwise_psa.UnitOfMeasuresApi(api_client)
    id = 56 # int | unitOfMeasureId
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
        # Get UnitOfMeasure
        api_response = api_instance.get_procurement_unit_of_measures_by_id(id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of UnitOfMeasuresApi->get_procurement_unit_of_measures_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UnitOfMeasuresApi->get_procurement_unit_of_measures_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| unitOfMeasureId | 
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

[**UnitOfMeasure**](UnitOfMeasure.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | UnitOfMeasure |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_procurement_unit_of_measures_count**
> Count get_procurement_unit_of_measures_count(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Count of UnitOfMeasure

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
    api_instance = connectwise_psa.UnitOfMeasuresApi(api_client)
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
        # Get Count of UnitOfMeasure
        api_response = api_instance.get_procurement_unit_of_measures_count(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of UnitOfMeasuresApi->get_procurement_unit_of_measures_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UnitOfMeasuresApi->get_procurement_unit_of_measures_count: %s\n" % e)
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

# **patch_procurement_unit_of_measures_by_id**
> UnitOfMeasure patch_procurement_unit_of_measures_by_id(id, client_id, patch_operation)

Patch UnitOfMeasure

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.patch_operation import PatchOperation
from connectwise_psa.models.unit_of_measure import UnitOfMeasure
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
    api_instance = connectwise_psa.UnitOfMeasuresApi(api_client)
    id = 56 # int | unitOfMeasureId
    client_id = 'client_id_example' # str | 
    patch_operation = [connectwise_psa.PatchOperation()] # List[PatchOperation] | List of PatchOperation

    try:
        # Patch UnitOfMeasure
        api_response = api_instance.patch_procurement_unit_of_measures_by_id(id, client_id, patch_operation)
        print("The response of UnitOfMeasuresApi->patch_procurement_unit_of_measures_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UnitOfMeasuresApi->patch_procurement_unit_of_measures_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| unitOfMeasureId | 
 **client_id** | **str**|  | 
 **patch_operation** | [**List[PatchOperation]**](PatchOperation.md)| List of PatchOperation | 

### Return type

[**UnitOfMeasure**](UnitOfMeasure.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | UnitOfMeasure |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_procurement_unit_of_measures**
> UnitOfMeasure post_procurement_unit_of_measures(client_id, unit_of_measure)

Post UnitOfMeasure

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.unit_of_measure import UnitOfMeasure
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
    api_instance = connectwise_psa.UnitOfMeasuresApi(api_client)
    client_id = 'client_id_example' # str | 
    unit_of_measure = connectwise_psa.UnitOfMeasure() # UnitOfMeasure | unitOfMeasure

    try:
        # Post UnitOfMeasure
        api_response = api_instance.post_procurement_unit_of_measures(client_id, unit_of_measure)
        print("The response of UnitOfMeasuresApi->post_procurement_unit_of_measures:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UnitOfMeasuresApi->post_procurement_unit_of_measures: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**|  | 
 **unit_of_measure** | [**UnitOfMeasure**](UnitOfMeasure.md)| unitOfMeasure | 

### Return type

[**UnitOfMeasure**](UnitOfMeasure.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | UnitOfMeasure |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_procurement_unit_of_measures_by_id**
> UnitOfMeasure put_procurement_unit_of_measures_by_id(id, client_id, unit_of_measure)

Put UnitOfMeasure

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.unit_of_measure import UnitOfMeasure
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
    api_instance = connectwise_psa.UnitOfMeasuresApi(api_client)
    id = 56 # int | unitOfMeasureId
    client_id = 'client_id_example' # str | 
    unit_of_measure = connectwise_psa.UnitOfMeasure() # UnitOfMeasure | unitOfMeasure

    try:
        # Put UnitOfMeasure
        api_response = api_instance.put_procurement_unit_of_measures_by_id(id, client_id, unit_of_measure)
        print("The response of UnitOfMeasuresApi->put_procurement_unit_of_measures_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UnitOfMeasuresApi->put_procurement_unit_of_measures_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| unitOfMeasureId | 
 **client_id** | **str**|  | 
 **unit_of_measure** | [**UnitOfMeasure**](UnitOfMeasure.md)| unitOfMeasure | 

### Return type

[**UnitOfMeasure**](UnitOfMeasure.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | UnitOfMeasure |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

