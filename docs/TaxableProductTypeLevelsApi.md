# connectwise_psa.TaxableProductTypeLevelsApi

All URIs are relative to *https://api-aus.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_finance_tax_codes_by_grandparent_id_product_type_exemptions_by_parent_id_taxable_product_type_levels_by_id**](TaxableProductTypeLevelsApi.md#delete_finance_tax_codes_by_grandparent_id_product_type_exemptions_by_parent_id_taxable_product_type_levels_by_id) | **DELETE** /finance/taxCodes/{grandparentId}/productTypeExemptions/{parentId}/taxableProductTypeLevels/{id} | Delete TaxableProductTypeLevel
[**get_finance_tax_codes_by_grandparent_id_product_type_exemptions_by_parent_id_taxable_product_type_levels**](TaxableProductTypeLevelsApi.md#get_finance_tax_codes_by_grandparent_id_product_type_exemptions_by_parent_id_taxable_product_type_levels) | **GET** /finance/taxCodes/{grandparentId}/productTypeExemptions/{parentId}/taxableProductTypeLevels | Get List of TaxableProductTypeLevel
[**get_finance_tax_codes_by_grandparent_id_product_type_exemptions_by_parent_id_taxable_product_type_levels_by_id**](TaxableProductTypeLevelsApi.md#get_finance_tax_codes_by_grandparent_id_product_type_exemptions_by_parent_id_taxable_product_type_levels_by_id) | **GET** /finance/taxCodes/{grandparentId}/productTypeExemptions/{parentId}/taxableProductTypeLevels/{id} | Get TaxableProductTypeLevel
[**get_finance_tax_codes_by_grandparent_id_product_type_exemptions_by_parent_id_taxable_product_type_levels_count**](TaxableProductTypeLevelsApi.md#get_finance_tax_codes_by_grandparent_id_product_type_exemptions_by_parent_id_taxable_product_type_levels_count) | **GET** /finance/taxCodes/{grandparentId}/productTypeExemptions/{parentId}/taxableProductTypeLevels/count | Get Count of TaxableProductTypeLevel
[**patch_finance_tax_codes_by_grandparent_id_product_type_exemptions_by_parent_id_taxable_product_type_levels_by_id**](TaxableProductTypeLevelsApi.md#patch_finance_tax_codes_by_grandparent_id_product_type_exemptions_by_parent_id_taxable_product_type_levels_by_id) | **PATCH** /finance/taxCodes/{grandparentId}/productTypeExemptions/{parentId}/taxableProductTypeLevels/{id} | Patch TaxableProductTypeLevel
[**post_finance_tax_codes_by_grandparent_id_product_type_exemptions_by_parent_id_taxable_product_type_levels**](TaxableProductTypeLevelsApi.md#post_finance_tax_codes_by_grandparent_id_product_type_exemptions_by_parent_id_taxable_product_type_levels) | **POST** /finance/taxCodes/{grandparentId}/productTypeExemptions/{parentId}/taxableProductTypeLevels | Post TaxableProductTypeLevel
[**put_finance_tax_codes_by_grandparent_id_product_type_exemptions_by_parent_id_taxable_product_type_levels_by_id**](TaxableProductTypeLevelsApi.md#put_finance_tax_codes_by_grandparent_id_product_type_exemptions_by_parent_id_taxable_product_type_levels_by_id) | **PUT** /finance/taxCodes/{grandparentId}/productTypeExemptions/{parentId}/taxableProductTypeLevels/{id} | Put TaxableProductTypeLevel


# **delete_finance_tax_codes_by_grandparent_id_product_type_exemptions_by_parent_id_taxable_product_type_levels_by_id**
> delete_finance_tax_codes_by_grandparent_id_product_type_exemptions_by_parent_id_taxable_product_type_levels_by_id(id, parent_id, grandparent_id, client_id)

Delete TaxableProductTypeLevel

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
    api_instance = connectwise_psa.TaxableProductTypeLevelsApi(api_client)
    id = 56 # int | taxableProductTypeLevelId
    parent_id = 56 # int | productTypeExemptionId
    grandparent_id = 56 # int | taxCodeId
    client_id = 'client_id_example' # str | 

    try:
        # Delete TaxableProductTypeLevel
        api_instance.delete_finance_tax_codes_by_grandparent_id_product_type_exemptions_by_parent_id_taxable_product_type_levels_by_id(id, parent_id, grandparent_id, client_id)
    except Exception as e:
        print("Exception when calling TaxableProductTypeLevelsApi->delete_finance_tax_codes_by_grandparent_id_product_type_exemptions_by_parent_id_taxable_product_type_levels_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| taxableProductTypeLevelId | 
 **parent_id** | **int**| productTypeExemptionId | 
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

# **get_finance_tax_codes_by_grandparent_id_product_type_exemptions_by_parent_id_taxable_product_type_levels**
> List[TaxableProductTypeLevel] get_finance_tax_codes_by_grandparent_id_product_type_exemptions_by_parent_id_taxable_product_type_levels(parent_id, grandparent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of TaxableProductTypeLevel

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.taxable_product_type_level import TaxableProductTypeLevel
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
    api_instance = connectwise_psa.TaxableProductTypeLevelsApi(api_client)
    parent_id = 56 # int | productTypeExemptionId
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
        # Get List of TaxableProductTypeLevel
        api_response = api_instance.get_finance_tax_codes_by_grandparent_id_product_type_exemptions_by_parent_id_taxable_product_type_levels(parent_id, grandparent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of TaxableProductTypeLevelsApi->get_finance_tax_codes_by_grandparent_id_product_type_exemptions_by_parent_id_taxable_product_type_levels:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaxableProductTypeLevelsApi->get_finance_tax_codes_by_grandparent_id_product_type_exemptions_by_parent_id_taxable_product_type_levels: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| productTypeExemptionId | 
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

[**List[TaxableProductTypeLevel]**](TaxableProductTypeLevel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of TaxableProductTypeLevel |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_finance_tax_codes_by_grandparent_id_product_type_exemptions_by_parent_id_taxable_product_type_levels_by_id**
> TaxableProductTypeLevel get_finance_tax_codes_by_grandparent_id_product_type_exemptions_by_parent_id_taxable_product_type_levels_by_id(id, parent_id, grandparent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get TaxableProductTypeLevel

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.taxable_product_type_level import TaxableProductTypeLevel
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
    api_instance = connectwise_psa.TaxableProductTypeLevelsApi(api_client)
    id = 56 # int | taxableProductTypeLevelId
    parent_id = 56 # int | productTypeExemptionId
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
        # Get TaxableProductTypeLevel
        api_response = api_instance.get_finance_tax_codes_by_grandparent_id_product_type_exemptions_by_parent_id_taxable_product_type_levels_by_id(id, parent_id, grandparent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of TaxableProductTypeLevelsApi->get_finance_tax_codes_by_grandparent_id_product_type_exemptions_by_parent_id_taxable_product_type_levels_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaxableProductTypeLevelsApi->get_finance_tax_codes_by_grandparent_id_product_type_exemptions_by_parent_id_taxable_product_type_levels_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| taxableProductTypeLevelId | 
 **parent_id** | **int**| productTypeExemptionId | 
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

[**TaxableProductTypeLevel**](TaxableProductTypeLevel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | TaxableProductTypeLevel |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_finance_tax_codes_by_grandparent_id_product_type_exemptions_by_parent_id_taxable_product_type_levels_count**
> Count get_finance_tax_codes_by_grandparent_id_product_type_exemptions_by_parent_id_taxable_product_type_levels_count(parent_id, grandparent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Count of TaxableProductTypeLevel

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
    api_instance = connectwise_psa.TaxableProductTypeLevelsApi(api_client)
    parent_id = 56 # int | productTypeExemptionId
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
        # Get Count of TaxableProductTypeLevel
        api_response = api_instance.get_finance_tax_codes_by_grandparent_id_product_type_exemptions_by_parent_id_taxable_product_type_levels_count(parent_id, grandparent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of TaxableProductTypeLevelsApi->get_finance_tax_codes_by_grandparent_id_product_type_exemptions_by_parent_id_taxable_product_type_levels_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaxableProductTypeLevelsApi->get_finance_tax_codes_by_grandparent_id_product_type_exemptions_by_parent_id_taxable_product_type_levels_count: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| productTypeExemptionId | 
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

# **patch_finance_tax_codes_by_grandparent_id_product_type_exemptions_by_parent_id_taxable_product_type_levels_by_id**
> TaxableProductTypeLevel patch_finance_tax_codes_by_grandparent_id_product_type_exemptions_by_parent_id_taxable_product_type_levels_by_id(id, parent_id, grandparent_id, client_id, patch_operation)

Patch TaxableProductTypeLevel

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.patch_operation import PatchOperation
from connectwise_psa.models.taxable_product_type_level import TaxableProductTypeLevel
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
    api_instance = connectwise_psa.TaxableProductTypeLevelsApi(api_client)
    id = 56 # int | taxableProductTypeLevelId
    parent_id = 56 # int | productTypeExemptionId
    grandparent_id = 56 # int | taxCodeId
    client_id = 'client_id_example' # str | 
    patch_operation = [connectwise_psa.PatchOperation()] # List[PatchOperation] | List of PatchOperation

    try:
        # Patch TaxableProductTypeLevel
        api_response = api_instance.patch_finance_tax_codes_by_grandparent_id_product_type_exemptions_by_parent_id_taxable_product_type_levels_by_id(id, parent_id, grandparent_id, client_id, patch_operation)
        print("The response of TaxableProductTypeLevelsApi->patch_finance_tax_codes_by_grandparent_id_product_type_exemptions_by_parent_id_taxable_product_type_levels_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaxableProductTypeLevelsApi->patch_finance_tax_codes_by_grandparent_id_product_type_exemptions_by_parent_id_taxable_product_type_levels_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| taxableProductTypeLevelId | 
 **parent_id** | **int**| productTypeExemptionId | 
 **grandparent_id** | **int**| taxCodeId | 
 **client_id** | **str**|  | 
 **patch_operation** | [**List[PatchOperation]**](PatchOperation.md)| List of PatchOperation | 

### Return type

[**TaxableProductTypeLevel**](TaxableProductTypeLevel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | TaxableProductTypeLevel |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_finance_tax_codes_by_grandparent_id_product_type_exemptions_by_parent_id_taxable_product_type_levels**
> TaxableProductTypeLevel post_finance_tax_codes_by_grandparent_id_product_type_exemptions_by_parent_id_taxable_product_type_levels(parent_id, grandparent_id, client_id, taxable_product_type_level)

Post TaxableProductTypeLevel

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.taxable_product_type_level import TaxableProductTypeLevel
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
    api_instance = connectwise_psa.TaxableProductTypeLevelsApi(api_client)
    parent_id = 56 # int | productTypeExemptionId
    grandparent_id = 56 # int | taxCodeId
    client_id = 'client_id_example' # str | 
    taxable_product_type_level = connectwise_psa.TaxableProductTypeLevel() # TaxableProductTypeLevel | taxableProductTypeLevel

    try:
        # Post TaxableProductTypeLevel
        api_response = api_instance.post_finance_tax_codes_by_grandparent_id_product_type_exemptions_by_parent_id_taxable_product_type_levels(parent_id, grandparent_id, client_id, taxable_product_type_level)
        print("The response of TaxableProductTypeLevelsApi->post_finance_tax_codes_by_grandparent_id_product_type_exemptions_by_parent_id_taxable_product_type_levels:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaxableProductTypeLevelsApi->post_finance_tax_codes_by_grandparent_id_product_type_exemptions_by_parent_id_taxable_product_type_levels: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| productTypeExemptionId | 
 **grandparent_id** | **int**| taxCodeId | 
 **client_id** | **str**|  | 
 **taxable_product_type_level** | [**TaxableProductTypeLevel**](TaxableProductTypeLevel.md)| taxableProductTypeLevel | 

### Return type

[**TaxableProductTypeLevel**](TaxableProductTypeLevel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | TaxableProductTypeLevel |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_finance_tax_codes_by_grandparent_id_product_type_exemptions_by_parent_id_taxable_product_type_levels_by_id**
> TaxableProductTypeLevel put_finance_tax_codes_by_grandparent_id_product_type_exemptions_by_parent_id_taxable_product_type_levels_by_id(id, parent_id, grandparent_id, client_id, taxable_product_type_level)

Put TaxableProductTypeLevel

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.taxable_product_type_level import TaxableProductTypeLevel
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
    api_instance = connectwise_psa.TaxableProductTypeLevelsApi(api_client)
    id = 56 # int | taxableProductTypeLevelId
    parent_id = 56 # int | productTypeExemptionId
    grandparent_id = 56 # int | taxCodeId
    client_id = 'client_id_example' # str | 
    taxable_product_type_level = connectwise_psa.TaxableProductTypeLevel() # TaxableProductTypeLevel | taxableProductTypeLevel

    try:
        # Put TaxableProductTypeLevel
        api_response = api_instance.put_finance_tax_codes_by_grandparent_id_product_type_exemptions_by_parent_id_taxable_product_type_levels_by_id(id, parent_id, grandparent_id, client_id, taxable_product_type_level)
        print("The response of TaxableProductTypeLevelsApi->put_finance_tax_codes_by_grandparent_id_product_type_exemptions_by_parent_id_taxable_product_type_levels_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaxableProductTypeLevelsApi->put_finance_tax_codes_by_grandparent_id_product_type_exemptions_by_parent_id_taxable_product_type_levels_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| taxableProductTypeLevelId | 
 **parent_id** | **int**| productTypeExemptionId | 
 **grandparent_id** | **int**| taxCodeId | 
 **client_id** | **str**|  | 
 **taxable_product_type_level** | [**TaxableProductTypeLevel**](TaxableProductTypeLevel.md)| taxableProductTypeLevel | 

### Return type

[**TaxableProductTypeLevel**](TaxableProductTypeLevel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | TaxableProductTypeLevel |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

