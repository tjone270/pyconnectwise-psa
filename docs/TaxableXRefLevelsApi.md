# connectwise_psa.TaxableXRefLevelsApi

All URIs are relative to *https://aus-api.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_finance_tax_codes_by_grandparent_id_tax_code_x_refs_by_parent_id_taxable_x_ref_levels_by_id**](TaxableXRefLevelsApi.md#delete_finance_tax_codes_by_grandparent_id_tax_code_x_refs_by_parent_id_taxable_x_ref_levels_by_id) | **DELETE** /finance/taxCodes/{grandparentId}/taxCodeXRefs/{parentId}/taxableXRefLevels/{id} | Delete TaxableXRefLevel
[**get_finance_tax_codes_by_grandparent_id_tax_code_x_refs_by_parent_id_taxable_x_ref_levels**](TaxableXRefLevelsApi.md#get_finance_tax_codes_by_grandparent_id_tax_code_x_refs_by_parent_id_taxable_x_ref_levels) | **GET** /finance/taxCodes/{grandparentId}/taxCodeXRefs/{parentId}/taxableXRefLevels | Get List of TaxableXRefLevel
[**get_finance_tax_codes_by_grandparent_id_tax_code_x_refs_by_parent_id_taxable_x_ref_levels_by_id**](TaxableXRefLevelsApi.md#get_finance_tax_codes_by_grandparent_id_tax_code_x_refs_by_parent_id_taxable_x_ref_levels_by_id) | **GET** /finance/taxCodes/{grandparentId}/taxCodeXRefs/{parentId}/taxableXRefLevels/{id} | Get TaxableXRefLevel
[**get_finance_tax_codes_by_grandparent_id_tax_code_x_refs_by_parent_id_taxable_x_ref_levels_count**](TaxableXRefLevelsApi.md#get_finance_tax_codes_by_grandparent_id_tax_code_x_refs_by_parent_id_taxable_x_ref_levels_count) | **GET** /finance/taxCodes/{grandparentId}/taxCodeXRefs/{parentId}/taxableXRefLevels/count | Get Count of TaxableXRefLevel
[**patch_finance_tax_codes_by_grandparent_id_tax_code_x_refs_by_parent_id_taxable_x_ref_levels_by_id**](TaxableXRefLevelsApi.md#patch_finance_tax_codes_by_grandparent_id_tax_code_x_refs_by_parent_id_taxable_x_ref_levels_by_id) | **PATCH** /finance/taxCodes/{grandparentId}/taxCodeXRefs/{parentId}/taxableXRefLevels/{id} | Patch TaxableXRefLevel
[**post_finance_tax_codes_by_grandparent_id_tax_code_x_refs_by_parent_id_taxable_x_ref_levels**](TaxableXRefLevelsApi.md#post_finance_tax_codes_by_grandparent_id_tax_code_x_refs_by_parent_id_taxable_x_ref_levels) | **POST** /finance/taxCodes/{grandparentId}/taxCodeXRefs/{parentId}/taxableXRefLevels | Post TaxableXRefLevel
[**put_finance_tax_codes_by_grandparent_id_tax_code_x_refs_by_parent_id_taxable_x_ref_levels_by_id**](TaxableXRefLevelsApi.md#put_finance_tax_codes_by_grandparent_id_tax_code_x_refs_by_parent_id_taxable_x_ref_levels_by_id) | **PUT** /finance/taxCodes/{grandparentId}/taxCodeXRefs/{parentId}/taxableXRefLevels/{id} | Put TaxableXRefLevel


# **delete_finance_tax_codes_by_grandparent_id_tax_code_x_refs_by_parent_id_taxable_x_ref_levels_by_id**
> delete_finance_tax_codes_by_grandparent_id_tax_code_x_refs_by_parent_id_taxable_x_ref_levels_by_id(id, parent_id, grandparent_id, client_id)

Delete TaxableXRefLevel

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
    api_instance = connectwise_psa.TaxableXRefLevelsApi(api_client)
    id = 56 # int | taxableXRefLevelId
    parent_id = 56 # int | taxCodeXRefId
    grandparent_id = 56 # int | taxCodeId
    client_id = 'client_id_example' # str | 

    try:
        # Delete TaxableXRefLevel
        api_instance.delete_finance_tax_codes_by_grandparent_id_tax_code_x_refs_by_parent_id_taxable_x_ref_levels_by_id(id, parent_id, grandparent_id, client_id)
    except Exception as e:
        print("Exception when calling TaxableXRefLevelsApi->delete_finance_tax_codes_by_grandparent_id_tax_code_x_refs_by_parent_id_taxable_x_ref_levels_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| taxableXRefLevelId | 
 **parent_id** | **int**| taxCodeXRefId | 
 **grandparent_id** | **int**| taxCodeId | 
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

# **get_finance_tax_codes_by_grandparent_id_tax_code_x_refs_by_parent_id_taxable_x_ref_levels**
> List[TaxableXRefLevel] get_finance_tax_codes_by_grandparent_id_tax_code_x_refs_by_parent_id_taxable_x_ref_levels(parent_id, grandparent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of TaxableXRefLevel

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.taxable_x_ref_level import TaxableXRefLevel
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
    api_instance = connectwise_psa.TaxableXRefLevelsApi(api_client)
    parent_id = 56 # int | taxCodeXRefId
    grandparent_id = 56 # int | taxCodeId
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
        # Get List of TaxableXRefLevel
        api_response = api_instance.get_finance_tax_codes_by_grandparent_id_tax_code_x_refs_by_parent_id_taxable_x_ref_levels(parent_id, grandparent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of TaxableXRefLevelsApi->get_finance_tax_codes_by_grandparent_id_tax_code_x_refs_by_parent_id_taxable_x_ref_levels:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaxableXRefLevelsApi->get_finance_tax_codes_by_grandparent_id_tax_code_x_refs_by_parent_id_taxable_x_ref_levels: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| taxCodeXRefId | 
 **grandparent_id** | **int**| taxCodeId | 
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

[**List[TaxableXRefLevel]**](TaxableXRefLevel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of TaxableXRefLevel |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_finance_tax_codes_by_grandparent_id_tax_code_x_refs_by_parent_id_taxable_x_ref_levels_by_id**
> TaxableXRefLevel get_finance_tax_codes_by_grandparent_id_tax_code_x_refs_by_parent_id_taxable_x_ref_levels_by_id(id, parent_id, grandparent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get TaxableXRefLevel

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.taxable_x_ref_level import TaxableXRefLevel
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
    api_instance = connectwise_psa.TaxableXRefLevelsApi(api_client)
    id = 56 # int | taxableXRefLevelId
    parent_id = 56 # int | taxCodeXRefId
    grandparent_id = 56 # int | taxCodeId
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
        # Get TaxableXRefLevel
        api_response = api_instance.get_finance_tax_codes_by_grandparent_id_tax_code_x_refs_by_parent_id_taxable_x_ref_levels_by_id(id, parent_id, grandparent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of TaxableXRefLevelsApi->get_finance_tax_codes_by_grandparent_id_tax_code_x_refs_by_parent_id_taxable_x_ref_levels_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaxableXRefLevelsApi->get_finance_tax_codes_by_grandparent_id_tax_code_x_refs_by_parent_id_taxable_x_ref_levels_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| taxableXRefLevelId | 
 **parent_id** | **int**| taxCodeXRefId | 
 **grandparent_id** | **int**| taxCodeId | 
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

[**TaxableXRefLevel**](TaxableXRefLevel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | TaxableXRefLevel |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_finance_tax_codes_by_grandparent_id_tax_code_x_refs_by_parent_id_taxable_x_ref_levels_count**
> Count get_finance_tax_codes_by_grandparent_id_tax_code_x_refs_by_parent_id_taxable_x_ref_levels_count(parent_id, grandparent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Count of TaxableXRefLevel

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
    api_instance = connectwise_psa.TaxableXRefLevelsApi(api_client)
    parent_id = 56 # int | taxCodeXRefId
    grandparent_id = 56 # int | taxCodeId
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
        # Get Count of TaxableXRefLevel
        api_response = api_instance.get_finance_tax_codes_by_grandparent_id_tax_code_x_refs_by_parent_id_taxable_x_ref_levels_count(parent_id, grandparent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of TaxableXRefLevelsApi->get_finance_tax_codes_by_grandparent_id_tax_code_x_refs_by_parent_id_taxable_x_ref_levels_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaxableXRefLevelsApi->get_finance_tax_codes_by_grandparent_id_tax_code_x_refs_by_parent_id_taxable_x_ref_levels_count: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| taxCodeXRefId | 
 **grandparent_id** | **int**| taxCodeId | 
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

# **patch_finance_tax_codes_by_grandparent_id_tax_code_x_refs_by_parent_id_taxable_x_ref_levels_by_id**
> TaxableXRefLevel patch_finance_tax_codes_by_grandparent_id_tax_code_x_refs_by_parent_id_taxable_x_ref_levels_by_id(id, parent_id, grandparent_id, client_id, patch_operation)

Patch TaxableXRefLevel

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.patch_operation import PatchOperation
from connectwise_psa.models.taxable_x_ref_level import TaxableXRefLevel
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
    api_instance = connectwise_psa.TaxableXRefLevelsApi(api_client)
    id = 56 # int | taxableXRefLevelId
    parent_id = 56 # int | taxCodeXRefId
    grandparent_id = 56 # int | taxCodeId
    client_id = 'client_id_example' # str | 
    patch_operation = [connectwise_psa.PatchOperation()] # List[PatchOperation] | List of PatchOperation

    try:
        # Patch TaxableXRefLevel
        api_response = api_instance.patch_finance_tax_codes_by_grandparent_id_tax_code_x_refs_by_parent_id_taxable_x_ref_levels_by_id(id, parent_id, grandparent_id, client_id, patch_operation)
        print("The response of TaxableXRefLevelsApi->patch_finance_tax_codes_by_grandparent_id_tax_code_x_refs_by_parent_id_taxable_x_ref_levels_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaxableXRefLevelsApi->patch_finance_tax_codes_by_grandparent_id_tax_code_x_refs_by_parent_id_taxable_x_ref_levels_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| taxableXRefLevelId | 
 **parent_id** | **int**| taxCodeXRefId | 
 **grandparent_id** | **int**| taxCodeId | 
 **client_id** | **str**|  | 
 **patch_operation** | [**List[PatchOperation]**](PatchOperation.md)| List of PatchOperation | 

### Return type

[**TaxableXRefLevel**](TaxableXRefLevel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | TaxableXRefLevel |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_finance_tax_codes_by_grandparent_id_tax_code_x_refs_by_parent_id_taxable_x_ref_levels**
> TaxableXRefLevel post_finance_tax_codes_by_grandparent_id_tax_code_x_refs_by_parent_id_taxable_x_ref_levels(parent_id, grandparent_id, client_id, taxable_x_ref_level)

Post TaxableXRefLevel

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.taxable_x_ref_level import TaxableXRefLevel
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
    api_instance = connectwise_psa.TaxableXRefLevelsApi(api_client)
    parent_id = 56 # int | taxCodeXRefId
    grandparent_id = 56 # int | taxCodeId
    client_id = 'client_id_example' # str | 
    taxable_x_ref_level = connectwise_psa.TaxableXRefLevel() # TaxableXRefLevel | taxableXRefLevel

    try:
        # Post TaxableXRefLevel
        api_response = api_instance.post_finance_tax_codes_by_grandparent_id_tax_code_x_refs_by_parent_id_taxable_x_ref_levels(parent_id, grandparent_id, client_id, taxable_x_ref_level)
        print("The response of TaxableXRefLevelsApi->post_finance_tax_codes_by_grandparent_id_tax_code_x_refs_by_parent_id_taxable_x_ref_levels:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaxableXRefLevelsApi->post_finance_tax_codes_by_grandparent_id_tax_code_x_refs_by_parent_id_taxable_x_ref_levels: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| taxCodeXRefId | 
 **grandparent_id** | **int**| taxCodeId | 
 **client_id** | **str**|  | 
 **taxable_x_ref_level** | [**TaxableXRefLevel**](TaxableXRefLevel.md)| taxableXRefLevel | 

### Return type

[**TaxableXRefLevel**](TaxableXRefLevel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | TaxableXRefLevel |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_finance_tax_codes_by_grandparent_id_tax_code_x_refs_by_parent_id_taxable_x_ref_levels_by_id**
> TaxableXRefLevel put_finance_tax_codes_by_grandparent_id_tax_code_x_refs_by_parent_id_taxable_x_ref_levels_by_id(id, parent_id, grandparent_id, client_id, taxable_x_ref_level)

Put TaxableXRefLevel

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.taxable_x_ref_level import TaxableXRefLevel
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
    api_instance = connectwise_psa.TaxableXRefLevelsApi(api_client)
    id = 56 # int | taxableXRefLevelId
    parent_id = 56 # int | taxCodeXRefId
    grandparent_id = 56 # int | taxCodeId
    client_id = 'client_id_example' # str | 
    taxable_x_ref_level = connectwise_psa.TaxableXRefLevel() # TaxableXRefLevel | taxableXRefLevel

    try:
        # Put TaxableXRefLevel
        api_response = api_instance.put_finance_tax_codes_by_grandparent_id_tax_code_x_refs_by_parent_id_taxable_x_ref_levels_by_id(id, parent_id, grandparent_id, client_id, taxable_x_ref_level)
        print("The response of TaxableXRefLevelsApi->put_finance_tax_codes_by_grandparent_id_tax_code_x_refs_by_parent_id_taxable_x_ref_levels_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaxableXRefLevelsApi->put_finance_tax_codes_by_grandparent_id_tax_code_x_refs_by_parent_id_taxable_x_ref_levels_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| taxableXRefLevelId | 
 **parent_id** | **int**| taxCodeXRefId | 
 **grandparent_id** | **int**| taxCodeId | 
 **client_id** | **str**|  | 
 **taxable_x_ref_level** | [**TaxableXRefLevel**](TaxableXRefLevel.md)| taxableXRefLevel | 

### Return type

[**TaxableXRefLevel**](TaxableXRefLevel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | TaxableXRefLevel |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

