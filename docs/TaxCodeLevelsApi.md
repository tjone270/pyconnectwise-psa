# connectwise_psa.TaxCodeLevelsApi

All URIs are relative to *https://aus-api.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_finance_tax_codes_by_parent_id_tax_code_levels_by_id**](TaxCodeLevelsApi.md#delete_finance_tax_codes_by_parent_id_tax_code_levels_by_id) | **DELETE** /finance/taxCodes/{parentId}/taxCodeLevels/{id} | Delete TaxCodeLevel
[**get_finance_tax_codes_by_parent_id_tax_code_levels**](TaxCodeLevelsApi.md#get_finance_tax_codes_by_parent_id_tax_code_levels) | **GET** /finance/taxCodes/{parentId}/taxCodeLevels | Get List of TaxCodeLevel
[**get_finance_tax_codes_by_parent_id_tax_code_levels_by_id**](TaxCodeLevelsApi.md#get_finance_tax_codes_by_parent_id_tax_code_levels_by_id) | **GET** /finance/taxCodes/{parentId}/taxCodeLevels/{id} | Get TaxCodeLevel
[**get_finance_tax_codes_by_parent_id_tax_code_levels_count**](TaxCodeLevelsApi.md#get_finance_tax_codes_by_parent_id_tax_code_levels_count) | **GET** /finance/taxCodes/{parentId}/taxCodeLevels/count | Get Count of TaxCodeLevel
[**patch_finance_tax_codes_by_parent_id_tax_code_levels_by_id**](TaxCodeLevelsApi.md#patch_finance_tax_codes_by_parent_id_tax_code_levels_by_id) | **PATCH** /finance/taxCodes/{parentId}/taxCodeLevels/{id} | Patch TaxCodeLevel
[**post_finance_tax_codes_by_parent_id_tax_code_levels**](TaxCodeLevelsApi.md#post_finance_tax_codes_by_parent_id_tax_code_levels) | **POST** /finance/taxCodes/{parentId}/taxCodeLevels | Post TaxCodeLevel
[**put_finance_tax_codes_by_parent_id_tax_code_levels_by_id**](TaxCodeLevelsApi.md#put_finance_tax_codes_by_parent_id_tax_code_levels_by_id) | **PUT** /finance/taxCodes/{parentId}/taxCodeLevels/{id} | Put TaxCodeLevel


# **delete_finance_tax_codes_by_parent_id_tax_code_levels_by_id**
> delete_finance_tax_codes_by_parent_id_tax_code_levels_by_id(id, parent_id, client_id)

Delete TaxCodeLevel

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
    api_instance = connectwise_psa.TaxCodeLevelsApi(api_client)
    id = 56 # int | taxCodeLevelId
    parent_id = 56 # int | taxCodeId
    client_id = 'client_id_example' # str | 

    try:
        # Delete TaxCodeLevel
        api_instance.delete_finance_tax_codes_by_parent_id_tax_code_levels_by_id(id, parent_id, client_id)
    except Exception as e:
        print("Exception when calling TaxCodeLevelsApi->delete_finance_tax_codes_by_parent_id_tax_code_levels_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| taxCodeLevelId | 
 **parent_id** | **int**| taxCodeId | 
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

# **get_finance_tax_codes_by_parent_id_tax_code_levels**
> List[TaxCodeLevel] get_finance_tax_codes_by_parent_id_tax_code_levels(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of TaxCodeLevel

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.tax_code_level import TaxCodeLevel
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
    api_instance = connectwise_psa.TaxCodeLevelsApi(api_client)
    parent_id = 56 # int | taxCodeId
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
        # Get List of TaxCodeLevel
        api_response = api_instance.get_finance_tax_codes_by_parent_id_tax_code_levels(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of TaxCodeLevelsApi->get_finance_tax_codes_by_parent_id_tax_code_levels:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaxCodeLevelsApi->get_finance_tax_codes_by_parent_id_tax_code_levels: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| taxCodeId | 
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

[**List[TaxCodeLevel]**](TaxCodeLevel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of TaxCodeLevel |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_finance_tax_codes_by_parent_id_tax_code_levels_by_id**
> TaxCodeLevel get_finance_tax_codes_by_parent_id_tax_code_levels_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get TaxCodeLevel

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.tax_code_level import TaxCodeLevel
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
    api_instance = connectwise_psa.TaxCodeLevelsApi(api_client)
    id = 56 # int | taxCodeLevelId
    parent_id = 56 # int | taxCodeId
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
        # Get TaxCodeLevel
        api_response = api_instance.get_finance_tax_codes_by_parent_id_tax_code_levels_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of TaxCodeLevelsApi->get_finance_tax_codes_by_parent_id_tax_code_levels_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaxCodeLevelsApi->get_finance_tax_codes_by_parent_id_tax_code_levels_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| taxCodeLevelId | 
 **parent_id** | **int**| taxCodeId | 
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

[**TaxCodeLevel**](TaxCodeLevel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | TaxCodeLevel |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_finance_tax_codes_by_parent_id_tax_code_levels_count**
> Count get_finance_tax_codes_by_parent_id_tax_code_levels_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Count of TaxCodeLevel

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
    api_instance = connectwise_psa.TaxCodeLevelsApi(api_client)
    parent_id = 56 # int | taxCodeId
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
        # Get Count of TaxCodeLevel
        api_response = api_instance.get_finance_tax_codes_by_parent_id_tax_code_levels_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of TaxCodeLevelsApi->get_finance_tax_codes_by_parent_id_tax_code_levels_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaxCodeLevelsApi->get_finance_tax_codes_by_parent_id_tax_code_levels_count: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| taxCodeId | 
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

# **patch_finance_tax_codes_by_parent_id_tax_code_levels_by_id**
> TaxCodeLevel patch_finance_tax_codes_by_parent_id_tax_code_levels_by_id(id, parent_id, client_id, patch_operation)

Patch TaxCodeLevel

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.patch_operation import PatchOperation
from connectwise_psa.models.tax_code_level import TaxCodeLevel
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
    api_instance = connectwise_psa.TaxCodeLevelsApi(api_client)
    id = 56 # int | taxCodeLevelId
    parent_id = 56 # int | taxCodeId
    client_id = 'client_id_example' # str | 
    patch_operation = [connectwise_psa.PatchOperation()] # List[PatchOperation] | List of PatchOperation

    try:
        # Patch TaxCodeLevel
        api_response = api_instance.patch_finance_tax_codes_by_parent_id_tax_code_levels_by_id(id, parent_id, client_id, patch_operation)
        print("The response of TaxCodeLevelsApi->patch_finance_tax_codes_by_parent_id_tax_code_levels_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaxCodeLevelsApi->patch_finance_tax_codes_by_parent_id_tax_code_levels_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| taxCodeLevelId | 
 **parent_id** | **int**| taxCodeId | 
 **client_id** | **str**|  | 
 **patch_operation** | [**List[PatchOperation]**](PatchOperation.md)| List of PatchOperation | 

### Return type

[**TaxCodeLevel**](TaxCodeLevel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | TaxCodeLevel |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_finance_tax_codes_by_parent_id_tax_code_levels**
> TaxCodeLevel post_finance_tax_codes_by_parent_id_tax_code_levels(parent_id, client_id, tax_code_level)

Post TaxCodeLevel

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.tax_code_level import TaxCodeLevel
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
    api_instance = connectwise_psa.TaxCodeLevelsApi(api_client)
    parent_id = 56 # int | taxCodeId
    client_id = 'client_id_example' # str | 
    tax_code_level = connectwise_psa.TaxCodeLevel() # TaxCodeLevel | taxCodeLevel

    try:
        # Post TaxCodeLevel
        api_response = api_instance.post_finance_tax_codes_by_parent_id_tax_code_levels(parent_id, client_id, tax_code_level)
        print("The response of TaxCodeLevelsApi->post_finance_tax_codes_by_parent_id_tax_code_levels:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaxCodeLevelsApi->post_finance_tax_codes_by_parent_id_tax_code_levels: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| taxCodeId | 
 **client_id** | **str**|  | 
 **tax_code_level** | [**TaxCodeLevel**](TaxCodeLevel.md)| taxCodeLevel | 

### Return type

[**TaxCodeLevel**](TaxCodeLevel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | TaxCodeLevel |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_finance_tax_codes_by_parent_id_tax_code_levels_by_id**
> TaxCodeLevel put_finance_tax_codes_by_parent_id_tax_code_levels_by_id(id, parent_id, client_id, tax_code_level)

Put TaxCodeLevel

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.tax_code_level import TaxCodeLevel
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
    api_instance = connectwise_psa.TaxCodeLevelsApi(api_client)
    id = 56 # int | taxCodeLevelId
    parent_id = 56 # int | taxCodeId
    client_id = 'client_id_example' # str | 
    tax_code_level = connectwise_psa.TaxCodeLevel() # TaxCodeLevel | taxCodeLevel

    try:
        # Put TaxCodeLevel
        api_response = api_instance.put_finance_tax_codes_by_parent_id_tax_code_levels_by_id(id, parent_id, client_id, tax_code_level)
        print("The response of TaxCodeLevelsApi->put_finance_tax_codes_by_parent_id_tax_code_levels_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaxCodeLevelsApi->put_finance_tax_codes_by_parent_id_tax_code_levels_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| taxCodeLevelId | 
 **parent_id** | **int**| taxCodeId | 
 **client_id** | **str**|  | 
 **tax_code_level** | [**TaxCodeLevel**](TaxCodeLevel.md)| taxCodeLevel | 

### Return type

[**TaxCodeLevel**](TaxCodeLevel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | TaxCodeLevel |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

