# connectwise_psa.TaxableWorkRoleLevelsApi

All URIs are relative to *https://api-aus.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_finance_tax_codes_by_grandparent_id_work_role_exemptions_by_parent_id_taxable_work_role_levels_by_id**](TaxableWorkRoleLevelsApi.md#delete_finance_tax_codes_by_grandparent_id_work_role_exemptions_by_parent_id_taxable_work_role_levels_by_id) | **DELETE** /finance/taxCodes/{grandparentId}/workRoleExemptions/{parentId}/taxableWorkRoleLevels/{id} | Delete TaxableWorkRoleLevel
[**get_finance_tax_codes_by_grandparent_id_work_role_exemptions_by_parent_id_taxable_work_role_levels**](TaxableWorkRoleLevelsApi.md#get_finance_tax_codes_by_grandparent_id_work_role_exemptions_by_parent_id_taxable_work_role_levels) | **GET** /finance/taxCodes/{grandparentId}/workRoleExemptions/{parentId}/taxableWorkRoleLevels | Get List of TaxableWorkRoleLevel
[**get_finance_tax_codes_by_grandparent_id_work_role_exemptions_by_parent_id_taxable_work_role_levels_by_id**](TaxableWorkRoleLevelsApi.md#get_finance_tax_codes_by_grandparent_id_work_role_exemptions_by_parent_id_taxable_work_role_levels_by_id) | **GET** /finance/taxCodes/{grandparentId}/workRoleExemptions/{parentId}/taxableWorkRoleLevels/{id} | Get TaxableWorkRoleLevel
[**get_finance_tax_codes_by_grandparent_id_work_role_exemptions_by_parent_id_taxable_work_role_levels_count**](TaxableWorkRoleLevelsApi.md#get_finance_tax_codes_by_grandparent_id_work_role_exemptions_by_parent_id_taxable_work_role_levels_count) | **GET** /finance/taxCodes/{grandparentId}/workRoleExemptions/{parentId}/taxableWorkRoleLevels/count | Get Count of TaxableWorkRoleLevel
[**patch_finance_tax_codes_by_grandparent_id_work_role_exemptions_by_parent_id_taxable_work_role_levels_by_id**](TaxableWorkRoleLevelsApi.md#patch_finance_tax_codes_by_grandparent_id_work_role_exemptions_by_parent_id_taxable_work_role_levels_by_id) | **PATCH** /finance/taxCodes/{grandparentId}/workRoleExemptions/{parentId}/taxableWorkRoleLevels/{id} | Patch TaxableWorkRoleLevel
[**post_finance_tax_codes_by_grandparent_id_work_role_exemptions_by_parent_id_taxable_work_role_levels**](TaxableWorkRoleLevelsApi.md#post_finance_tax_codes_by_grandparent_id_work_role_exemptions_by_parent_id_taxable_work_role_levels) | **POST** /finance/taxCodes/{grandparentId}/workRoleExemptions/{parentId}/taxableWorkRoleLevels | Post TaxableWorkRoleLevel
[**put_finance_tax_codes_by_grandparent_id_work_role_exemptions_by_parent_id_taxable_work_role_levels_by_id**](TaxableWorkRoleLevelsApi.md#put_finance_tax_codes_by_grandparent_id_work_role_exemptions_by_parent_id_taxable_work_role_levels_by_id) | **PUT** /finance/taxCodes/{grandparentId}/workRoleExemptions/{parentId}/taxableWorkRoleLevels/{id} | Put TaxableWorkRoleLevel


# **delete_finance_tax_codes_by_grandparent_id_work_role_exemptions_by_parent_id_taxable_work_role_levels_by_id**
> delete_finance_tax_codes_by_grandparent_id_work_role_exemptions_by_parent_id_taxable_work_role_levels_by_id(id, parent_id, grandparent_id, client_id)

Delete TaxableWorkRoleLevel

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
    api_instance = connectwise_psa.TaxableWorkRoleLevelsApi(api_client)
    id = 56 # int | taxableWorkRoleLevelId
    parent_id = 56 # int | workRoleExemptionId
    grandparent_id = 56 # int | taxCodeId
    client_id = 'client_id_example' # str | 

    try:
        # Delete TaxableWorkRoleLevel
        api_instance.delete_finance_tax_codes_by_grandparent_id_work_role_exemptions_by_parent_id_taxable_work_role_levels_by_id(id, parent_id, grandparent_id, client_id)
    except Exception as e:
        print("Exception when calling TaxableWorkRoleLevelsApi->delete_finance_tax_codes_by_grandparent_id_work_role_exemptions_by_parent_id_taxable_work_role_levels_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| taxableWorkRoleLevelId | 
 **parent_id** | **int**| workRoleExemptionId | 
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

# **get_finance_tax_codes_by_grandparent_id_work_role_exemptions_by_parent_id_taxable_work_role_levels**
> List[TaxableWorkRoleLevel] get_finance_tax_codes_by_grandparent_id_work_role_exemptions_by_parent_id_taxable_work_role_levels(parent_id, grandparent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of TaxableWorkRoleLevel

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.taxable_work_role_level import TaxableWorkRoleLevel
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
    api_instance = connectwise_psa.TaxableWorkRoleLevelsApi(api_client)
    parent_id = 56 # int | workRoleExemptionId
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
        # Get List of TaxableWorkRoleLevel
        api_response = api_instance.get_finance_tax_codes_by_grandparent_id_work_role_exemptions_by_parent_id_taxable_work_role_levels(parent_id, grandparent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of TaxableWorkRoleLevelsApi->get_finance_tax_codes_by_grandparent_id_work_role_exemptions_by_parent_id_taxable_work_role_levels:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaxableWorkRoleLevelsApi->get_finance_tax_codes_by_grandparent_id_work_role_exemptions_by_parent_id_taxable_work_role_levels: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| workRoleExemptionId | 
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

[**List[TaxableWorkRoleLevel]**](TaxableWorkRoleLevel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of TaxableWorkRoleLevel |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_finance_tax_codes_by_grandparent_id_work_role_exemptions_by_parent_id_taxable_work_role_levels_by_id**
> TaxableWorkRoleLevel get_finance_tax_codes_by_grandparent_id_work_role_exemptions_by_parent_id_taxable_work_role_levels_by_id(id, parent_id, grandparent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get TaxableWorkRoleLevel

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.taxable_work_role_level import TaxableWorkRoleLevel
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
    api_instance = connectwise_psa.TaxableWorkRoleLevelsApi(api_client)
    id = 56 # int | taxableWorkRoleLevelId
    parent_id = 56 # int | workRoleExemptionId
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
        # Get TaxableWorkRoleLevel
        api_response = api_instance.get_finance_tax_codes_by_grandparent_id_work_role_exemptions_by_parent_id_taxable_work_role_levels_by_id(id, parent_id, grandparent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of TaxableWorkRoleLevelsApi->get_finance_tax_codes_by_grandparent_id_work_role_exemptions_by_parent_id_taxable_work_role_levels_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaxableWorkRoleLevelsApi->get_finance_tax_codes_by_grandparent_id_work_role_exemptions_by_parent_id_taxable_work_role_levels_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| taxableWorkRoleLevelId | 
 **parent_id** | **int**| workRoleExemptionId | 
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

[**TaxableWorkRoleLevel**](TaxableWorkRoleLevel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | TaxableWorkRoleLevel |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_finance_tax_codes_by_grandparent_id_work_role_exemptions_by_parent_id_taxable_work_role_levels_count**
> Count get_finance_tax_codes_by_grandparent_id_work_role_exemptions_by_parent_id_taxable_work_role_levels_count(parent_id, grandparent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Count of TaxableWorkRoleLevel

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
    api_instance = connectwise_psa.TaxableWorkRoleLevelsApi(api_client)
    parent_id = 56 # int | workRoleExemptionId
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
        # Get Count of TaxableWorkRoleLevel
        api_response = api_instance.get_finance_tax_codes_by_grandparent_id_work_role_exemptions_by_parent_id_taxable_work_role_levels_count(parent_id, grandparent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of TaxableWorkRoleLevelsApi->get_finance_tax_codes_by_grandparent_id_work_role_exemptions_by_parent_id_taxable_work_role_levels_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaxableWorkRoleLevelsApi->get_finance_tax_codes_by_grandparent_id_work_role_exemptions_by_parent_id_taxable_work_role_levels_count: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| workRoleExemptionId | 
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

# **patch_finance_tax_codes_by_grandparent_id_work_role_exemptions_by_parent_id_taxable_work_role_levels_by_id**
> TaxableWorkRoleLevel patch_finance_tax_codes_by_grandparent_id_work_role_exemptions_by_parent_id_taxable_work_role_levels_by_id(id, parent_id, grandparent_id, client_id, patch_operation)

Patch TaxableWorkRoleLevel

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.patch_operation import PatchOperation
from connectwise_psa.models.taxable_work_role_level import TaxableWorkRoleLevel
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
    api_instance = connectwise_psa.TaxableWorkRoleLevelsApi(api_client)
    id = 56 # int | taxableWorkRoleLevelId
    parent_id = 56 # int | workRoleExemptionId
    grandparent_id = 56 # int | taxCodeId
    client_id = 'client_id_example' # str | 
    patch_operation = [connectwise_psa.PatchOperation()] # List[PatchOperation] | List of PatchOperation

    try:
        # Patch TaxableWorkRoleLevel
        api_response = api_instance.patch_finance_tax_codes_by_grandparent_id_work_role_exemptions_by_parent_id_taxable_work_role_levels_by_id(id, parent_id, grandparent_id, client_id, patch_operation)
        print("The response of TaxableWorkRoleLevelsApi->patch_finance_tax_codes_by_grandparent_id_work_role_exemptions_by_parent_id_taxable_work_role_levels_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaxableWorkRoleLevelsApi->patch_finance_tax_codes_by_grandparent_id_work_role_exemptions_by_parent_id_taxable_work_role_levels_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| taxableWorkRoleLevelId | 
 **parent_id** | **int**| workRoleExemptionId | 
 **grandparent_id** | **int**| taxCodeId | 
 **client_id** | **str**|  | 
 **patch_operation** | [**List[PatchOperation]**](PatchOperation.md)| List of PatchOperation | 

### Return type

[**TaxableWorkRoleLevel**](TaxableWorkRoleLevel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | TaxableWorkRoleLevel |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_finance_tax_codes_by_grandparent_id_work_role_exemptions_by_parent_id_taxable_work_role_levels**
> TaxableWorkRoleLevel post_finance_tax_codes_by_grandparent_id_work_role_exemptions_by_parent_id_taxable_work_role_levels(parent_id, grandparent_id, client_id, taxable_work_role_level)

Post TaxableWorkRoleLevel

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.taxable_work_role_level import TaxableWorkRoleLevel
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
    api_instance = connectwise_psa.TaxableWorkRoleLevelsApi(api_client)
    parent_id = 56 # int | workRoleExemptionId
    grandparent_id = 56 # int | taxCodeId
    client_id = 'client_id_example' # str | 
    taxable_work_role_level = connectwise_psa.TaxableWorkRoleLevel() # TaxableWorkRoleLevel | taxableWorkRoleLevel

    try:
        # Post TaxableWorkRoleLevel
        api_response = api_instance.post_finance_tax_codes_by_grandparent_id_work_role_exemptions_by_parent_id_taxable_work_role_levels(parent_id, grandparent_id, client_id, taxable_work_role_level)
        print("The response of TaxableWorkRoleLevelsApi->post_finance_tax_codes_by_grandparent_id_work_role_exemptions_by_parent_id_taxable_work_role_levels:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaxableWorkRoleLevelsApi->post_finance_tax_codes_by_grandparent_id_work_role_exemptions_by_parent_id_taxable_work_role_levels: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| workRoleExemptionId | 
 **grandparent_id** | **int**| taxCodeId | 
 **client_id** | **str**|  | 
 **taxable_work_role_level** | [**TaxableWorkRoleLevel**](TaxableWorkRoleLevel.md)| taxableWorkRoleLevel | 

### Return type

[**TaxableWorkRoleLevel**](TaxableWorkRoleLevel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | TaxableWorkRoleLevel |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_finance_tax_codes_by_grandparent_id_work_role_exemptions_by_parent_id_taxable_work_role_levels_by_id**
> TaxableWorkRoleLevel put_finance_tax_codes_by_grandparent_id_work_role_exemptions_by_parent_id_taxable_work_role_levels_by_id(id, parent_id, grandparent_id, client_id, taxable_work_role_level)

Put TaxableWorkRoleLevel

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.taxable_work_role_level import TaxableWorkRoleLevel
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
    api_instance = connectwise_psa.TaxableWorkRoleLevelsApi(api_client)
    id = 56 # int | taxableWorkRoleLevelId
    parent_id = 56 # int | workRoleExemptionId
    grandparent_id = 56 # int | taxCodeId
    client_id = 'client_id_example' # str | 
    taxable_work_role_level = connectwise_psa.TaxableWorkRoleLevel() # TaxableWorkRoleLevel | taxableWorkRoleLevel

    try:
        # Put TaxableWorkRoleLevel
        api_response = api_instance.put_finance_tax_codes_by_grandparent_id_work_role_exemptions_by_parent_id_taxable_work_role_levels_by_id(id, parent_id, grandparent_id, client_id, taxable_work_role_level)
        print("The response of TaxableWorkRoleLevelsApi->put_finance_tax_codes_by_grandparent_id_work_role_exemptions_by_parent_id_taxable_work_role_levels_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaxableWorkRoleLevelsApi->put_finance_tax_codes_by_grandparent_id_work_role_exemptions_by_parent_id_taxable_work_role_levels_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| taxableWorkRoleLevelId | 
 **parent_id** | **int**| workRoleExemptionId | 
 **grandparent_id** | **int**| taxCodeId | 
 **client_id** | **str**|  | 
 **taxable_work_role_level** | [**TaxableWorkRoleLevel**](TaxableWorkRoleLevel.md)| taxableWorkRoleLevel | 

### Return type

[**TaxableWorkRoleLevel**](TaxableWorkRoleLevel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | TaxableWorkRoleLevel |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

