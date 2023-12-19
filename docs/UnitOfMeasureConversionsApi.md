# connectwise_psa.UnitOfMeasureConversionsApi

All URIs are relative to *https://api-aus.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_procurement_unit_of_measures_by_parent_id_conversions_by_id**](UnitOfMeasureConversionsApi.md#delete_procurement_unit_of_measures_by_parent_id_conversions_by_id) | **DELETE** /procurement/unitOfMeasures/{parentId}/conversions/{id} | Delete Conversion
[**get_procurement_unit_of_measures_by_parent_id_conversions**](UnitOfMeasureConversionsApi.md#get_procurement_unit_of_measures_by_parent_id_conversions) | **GET** /procurement/unitOfMeasures/{parentId}/conversions | Get List of Conversion
[**get_procurement_unit_of_measures_by_parent_id_conversions_by_id**](UnitOfMeasureConversionsApi.md#get_procurement_unit_of_measures_by_parent_id_conversions_by_id) | **GET** /procurement/unitOfMeasures/{parentId}/conversions/{id} | Get Conversion
[**get_procurement_unit_of_measures_by_parent_id_conversions_count**](UnitOfMeasureConversionsApi.md#get_procurement_unit_of_measures_by_parent_id_conversions_count) | **GET** /procurement/unitOfMeasures/{parentId}/conversions/count | Get Count of Conversion
[**patch_procurement_unit_of_measures_by_parent_id_conversions_by_id**](UnitOfMeasureConversionsApi.md#patch_procurement_unit_of_measures_by_parent_id_conversions_by_id) | **PATCH** /procurement/unitOfMeasures/{parentId}/conversions/{id} | Patch Conversion
[**post_procurement_unit_of_measures_by_parent_id_conversions**](UnitOfMeasureConversionsApi.md#post_procurement_unit_of_measures_by_parent_id_conversions) | **POST** /procurement/unitOfMeasures/{parentId}/conversions | Post Conversion
[**put_procurement_unit_of_measures_by_parent_id_conversions_by_id**](UnitOfMeasureConversionsApi.md#put_procurement_unit_of_measures_by_parent_id_conversions_by_id) | **PUT** /procurement/unitOfMeasures/{parentId}/conversions/{id} | Put Conversion


# **delete_procurement_unit_of_measures_by_parent_id_conversions_by_id**
> delete_procurement_unit_of_measures_by_parent_id_conversions_by_id(id, parent_id, client_id)

Delete Conversion

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
    api_instance = connectwise_psa.UnitOfMeasureConversionsApi(api_client)
    id = 56 # int | conversionId
    parent_id = 56 # int | unitOfMeasureId
    client_id = 'client_id_example' # str | 

    try:
        # Delete Conversion
        api_instance.delete_procurement_unit_of_measures_by_parent_id_conversions_by_id(id, parent_id, client_id)
    except Exception as e:
        print("Exception when calling UnitOfMeasureConversionsApi->delete_procurement_unit_of_measures_by_parent_id_conversions_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| conversionId | 
 **parent_id** | **int**| unitOfMeasureId | 
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

# **get_procurement_unit_of_measures_by_parent_id_conversions**
> List[Conversion] get_procurement_unit_of_measures_by_parent_id_conversions(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of Conversion

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.conversion import Conversion
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
    api_instance = connectwise_psa.UnitOfMeasureConversionsApi(api_client)
    parent_id = 56 # int | unitOfMeasureId
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
        # Get List of Conversion
        api_response = api_instance.get_procurement_unit_of_measures_by_parent_id_conversions(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of UnitOfMeasureConversionsApi->get_procurement_unit_of_measures_by_parent_id_conversions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UnitOfMeasureConversionsApi->get_procurement_unit_of_measures_by_parent_id_conversions: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| unitOfMeasureId | 
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

[**List[Conversion]**](Conversion.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of Conversion |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_procurement_unit_of_measures_by_parent_id_conversions_by_id**
> Conversion get_procurement_unit_of_measures_by_parent_id_conversions_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Conversion

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.conversion import Conversion
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
    api_instance = connectwise_psa.UnitOfMeasureConversionsApi(api_client)
    id = 56 # int | conversionId
    parent_id = 56 # int | unitOfMeasureId
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
        # Get Conversion
        api_response = api_instance.get_procurement_unit_of_measures_by_parent_id_conversions_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of UnitOfMeasureConversionsApi->get_procurement_unit_of_measures_by_parent_id_conversions_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UnitOfMeasureConversionsApi->get_procurement_unit_of_measures_by_parent_id_conversions_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| conversionId | 
 **parent_id** | **int**| unitOfMeasureId | 
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

[**Conversion**](Conversion.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Conversion |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_procurement_unit_of_measures_by_parent_id_conversions_count**
> Count get_procurement_unit_of_measures_by_parent_id_conversions_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Count of Conversion

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
    api_instance = connectwise_psa.UnitOfMeasureConversionsApi(api_client)
    parent_id = 56 # int | unitOfMeasureId
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
        # Get Count of Conversion
        api_response = api_instance.get_procurement_unit_of_measures_by_parent_id_conversions_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of UnitOfMeasureConversionsApi->get_procurement_unit_of_measures_by_parent_id_conversions_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UnitOfMeasureConversionsApi->get_procurement_unit_of_measures_by_parent_id_conversions_count: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| unitOfMeasureId | 
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

# **patch_procurement_unit_of_measures_by_parent_id_conversions_by_id**
> Conversion patch_procurement_unit_of_measures_by_parent_id_conversions_by_id(id, parent_id, client_id, patch_operation)

Patch Conversion

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.conversion import Conversion
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
    api_instance = connectwise_psa.UnitOfMeasureConversionsApi(api_client)
    id = 56 # int | conversionId
    parent_id = 56 # int | unitOfMeasureId
    client_id = 'client_id_example' # str | 
    patch_operation = [connectwise_psa.PatchOperation()] # List[PatchOperation] | List of PatchOperation

    try:
        # Patch Conversion
        api_response = api_instance.patch_procurement_unit_of_measures_by_parent_id_conversions_by_id(id, parent_id, client_id, patch_operation)
        print("The response of UnitOfMeasureConversionsApi->patch_procurement_unit_of_measures_by_parent_id_conversions_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UnitOfMeasureConversionsApi->patch_procurement_unit_of_measures_by_parent_id_conversions_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| conversionId | 
 **parent_id** | **int**| unitOfMeasureId | 
 **client_id** | **str**|  | 
 **patch_operation** | [**List[PatchOperation]**](PatchOperation.md)| List of PatchOperation | 

### Return type

[**Conversion**](Conversion.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Conversion |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_procurement_unit_of_measures_by_parent_id_conversions**
> Conversion post_procurement_unit_of_measures_by_parent_id_conversions(parent_id, client_id, conversion)

Post Conversion

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.conversion import Conversion
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
    api_instance = connectwise_psa.UnitOfMeasureConversionsApi(api_client)
    parent_id = 56 # int | unitOfMeasureId
    client_id = 'client_id_example' # str | 
    conversion = connectwise_psa.Conversion() # Conversion | conversion

    try:
        # Post Conversion
        api_response = api_instance.post_procurement_unit_of_measures_by_parent_id_conversions(parent_id, client_id, conversion)
        print("The response of UnitOfMeasureConversionsApi->post_procurement_unit_of_measures_by_parent_id_conversions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UnitOfMeasureConversionsApi->post_procurement_unit_of_measures_by_parent_id_conversions: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| unitOfMeasureId | 
 **client_id** | **str**|  | 
 **conversion** | [**Conversion**](Conversion.md)| conversion | 

### Return type

[**Conversion**](Conversion.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Conversion |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_procurement_unit_of_measures_by_parent_id_conversions_by_id**
> Conversion put_procurement_unit_of_measures_by_parent_id_conversions_by_id(id, parent_id, client_id, conversion)

Put Conversion

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.conversion import Conversion
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
    api_instance = connectwise_psa.UnitOfMeasureConversionsApi(api_client)
    id = 56 # int | conversionId
    parent_id = 56 # int | unitOfMeasureId
    client_id = 'client_id_example' # str | 
    conversion = connectwise_psa.Conversion() # Conversion | conversion

    try:
        # Put Conversion
        api_response = api_instance.put_procurement_unit_of_measures_by_parent_id_conversions_by_id(id, parent_id, client_id, conversion)
        print("The response of UnitOfMeasureConversionsApi->put_procurement_unit_of_measures_by_parent_id_conversions_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UnitOfMeasureConversionsApi->put_procurement_unit_of_measures_by_parent_id_conversions_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| conversionId | 
 **parent_id** | **int**| unitOfMeasureId | 
 **client_id** | **str**|  | 
 **conversion** | [**Conversion**](Conversion.md)| conversion | 

### Return type

[**Conversion**](Conversion.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Conversion |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

