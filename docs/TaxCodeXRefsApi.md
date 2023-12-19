# connectwise_psa.TaxCodeXRefsApi

All URIs are relative to *https://api-aus.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_finance_tax_codes_by_parent_id_tax_code_x_refs_by_id**](TaxCodeXRefsApi.md#delete_finance_tax_codes_by_parent_id_tax_code_x_refs_by_id) | **DELETE** /finance/taxCodes/{parentId}/taxCodeXRefs/{id} | Delete TaxCodeXRef
[**get_finance_tax_codes_by_parent_id_tax_code_x_refs**](TaxCodeXRefsApi.md#get_finance_tax_codes_by_parent_id_tax_code_x_refs) | **GET** /finance/taxCodes/{parentId}/taxCodeXRefs | Get List of TaxCodeXRef
[**get_finance_tax_codes_by_parent_id_tax_code_x_refs_by_id**](TaxCodeXRefsApi.md#get_finance_tax_codes_by_parent_id_tax_code_x_refs_by_id) | **GET** /finance/taxCodes/{parentId}/taxCodeXRefs/{id} | Get TaxCodeXRef
[**get_finance_tax_codes_by_parent_id_tax_code_x_refs_count**](TaxCodeXRefsApi.md#get_finance_tax_codes_by_parent_id_tax_code_x_refs_count) | **GET** /finance/taxCodes/{parentId}/taxCodeXRefs/count | Get Count of TaxCodeXRef
[**patch_finance_tax_codes_by_parent_id_tax_code_x_refs_by_id**](TaxCodeXRefsApi.md#patch_finance_tax_codes_by_parent_id_tax_code_x_refs_by_id) | **PATCH** /finance/taxCodes/{parentId}/taxCodeXRefs/{id} | Patch TaxCodeXRef
[**post_finance_tax_codes_by_parent_id_tax_code_x_refs**](TaxCodeXRefsApi.md#post_finance_tax_codes_by_parent_id_tax_code_x_refs) | **POST** /finance/taxCodes/{parentId}/taxCodeXRefs | Post TaxCodeXRef
[**put_finance_tax_codes_by_parent_id_tax_code_x_refs_by_id**](TaxCodeXRefsApi.md#put_finance_tax_codes_by_parent_id_tax_code_x_refs_by_id) | **PUT** /finance/taxCodes/{parentId}/taxCodeXRefs/{id} | Put TaxCodeXRef


# **delete_finance_tax_codes_by_parent_id_tax_code_x_refs_by_id**
> delete_finance_tax_codes_by_parent_id_tax_code_x_refs_by_id(id, parent_id, client_id)

Delete TaxCodeXRef

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
    api_instance = connectwise_psa.TaxCodeXRefsApi(api_client)
    id = 56 # int | taxCodeXRefId
    parent_id = 56 # int | taxCodeId
    client_id = 'client_id_example' # str | 

    try:
        # Delete TaxCodeXRef
        api_instance.delete_finance_tax_codes_by_parent_id_tax_code_x_refs_by_id(id, parent_id, client_id)
    except Exception as e:
        print("Exception when calling TaxCodeXRefsApi->delete_finance_tax_codes_by_parent_id_tax_code_x_refs_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| taxCodeXRefId | 
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

# **get_finance_tax_codes_by_parent_id_tax_code_x_refs**
> List[TaxCodeXRef] get_finance_tax_codes_by_parent_id_tax_code_x_refs(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of TaxCodeXRef

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.tax_code_x_ref import TaxCodeXRef
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
    api_instance = connectwise_psa.TaxCodeXRefsApi(api_client)
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
        # Get List of TaxCodeXRef
        api_response = api_instance.get_finance_tax_codes_by_parent_id_tax_code_x_refs(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of TaxCodeXRefsApi->get_finance_tax_codes_by_parent_id_tax_code_x_refs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaxCodeXRefsApi->get_finance_tax_codes_by_parent_id_tax_code_x_refs: %s\n" % e)
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

[**List[TaxCodeXRef]**](TaxCodeXRef.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of TaxCodeXRef |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_finance_tax_codes_by_parent_id_tax_code_x_refs_by_id**
> TaxCodeXRef get_finance_tax_codes_by_parent_id_tax_code_x_refs_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get TaxCodeXRef

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.tax_code_x_ref import TaxCodeXRef
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
    api_instance = connectwise_psa.TaxCodeXRefsApi(api_client)
    id = 56 # int | taxCodeXRefId
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
        # Get TaxCodeXRef
        api_response = api_instance.get_finance_tax_codes_by_parent_id_tax_code_x_refs_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of TaxCodeXRefsApi->get_finance_tax_codes_by_parent_id_tax_code_x_refs_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaxCodeXRefsApi->get_finance_tax_codes_by_parent_id_tax_code_x_refs_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| taxCodeXRefId | 
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

[**TaxCodeXRef**](TaxCodeXRef.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | TaxCodeXRef |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_finance_tax_codes_by_parent_id_tax_code_x_refs_count**
> Count get_finance_tax_codes_by_parent_id_tax_code_x_refs_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Count of TaxCodeXRef

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
    api_instance = connectwise_psa.TaxCodeXRefsApi(api_client)
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
        # Get Count of TaxCodeXRef
        api_response = api_instance.get_finance_tax_codes_by_parent_id_tax_code_x_refs_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of TaxCodeXRefsApi->get_finance_tax_codes_by_parent_id_tax_code_x_refs_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaxCodeXRefsApi->get_finance_tax_codes_by_parent_id_tax_code_x_refs_count: %s\n" % e)
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

# **patch_finance_tax_codes_by_parent_id_tax_code_x_refs_by_id**
> TaxCodeXRef patch_finance_tax_codes_by_parent_id_tax_code_x_refs_by_id(id, parent_id, client_id, patch_operation)

Patch TaxCodeXRef

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.patch_operation import PatchOperation
from connectwise_psa.models.tax_code_x_ref import TaxCodeXRef
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
    api_instance = connectwise_psa.TaxCodeXRefsApi(api_client)
    id = 56 # int | taxCodeXRefId
    parent_id = 56 # int | taxCodeId
    client_id = 'client_id_example' # str | 
    patch_operation = [connectwise_psa.PatchOperation()] # List[PatchOperation] | List of PatchOperation

    try:
        # Patch TaxCodeXRef
        api_response = api_instance.patch_finance_tax_codes_by_parent_id_tax_code_x_refs_by_id(id, parent_id, client_id, patch_operation)
        print("The response of TaxCodeXRefsApi->patch_finance_tax_codes_by_parent_id_tax_code_x_refs_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaxCodeXRefsApi->patch_finance_tax_codes_by_parent_id_tax_code_x_refs_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| taxCodeXRefId | 
 **parent_id** | **int**| taxCodeId | 
 **client_id** | **str**|  | 
 **patch_operation** | [**List[PatchOperation]**](PatchOperation.md)| List of PatchOperation | 

### Return type

[**TaxCodeXRef**](TaxCodeXRef.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | TaxCodeXRef |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_finance_tax_codes_by_parent_id_tax_code_x_refs**
> TaxCodeXRef post_finance_tax_codes_by_parent_id_tax_code_x_refs(parent_id, client_id, tax_code_x_ref)

Post TaxCodeXRef

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.tax_code_x_ref import TaxCodeXRef
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
    api_instance = connectwise_psa.TaxCodeXRefsApi(api_client)
    parent_id = 56 # int | taxCodeId
    client_id = 'client_id_example' # str | 
    tax_code_x_ref = connectwise_psa.TaxCodeXRef() # TaxCodeXRef | taxCodeXRef

    try:
        # Post TaxCodeXRef
        api_response = api_instance.post_finance_tax_codes_by_parent_id_tax_code_x_refs(parent_id, client_id, tax_code_x_ref)
        print("The response of TaxCodeXRefsApi->post_finance_tax_codes_by_parent_id_tax_code_x_refs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaxCodeXRefsApi->post_finance_tax_codes_by_parent_id_tax_code_x_refs: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| taxCodeId | 
 **client_id** | **str**|  | 
 **tax_code_x_ref** | [**TaxCodeXRef**](TaxCodeXRef.md)| taxCodeXRef | 

### Return type

[**TaxCodeXRef**](TaxCodeXRef.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | TaxCodeXRef |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_finance_tax_codes_by_parent_id_tax_code_x_refs_by_id**
> TaxCodeXRef put_finance_tax_codes_by_parent_id_tax_code_x_refs_by_id(id, parent_id, client_id, tax_code_x_ref)

Put TaxCodeXRef

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.tax_code_x_ref import TaxCodeXRef
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
    api_instance = connectwise_psa.TaxCodeXRefsApi(api_client)
    id = 56 # int | taxCodeXRefId
    parent_id = 56 # int | taxCodeId
    client_id = 'client_id_example' # str | 
    tax_code_x_ref = connectwise_psa.TaxCodeXRef() # TaxCodeXRef | taxCodeXRef

    try:
        # Put TaxCodeXRef
        api_response = api_instance.put_finance_tax_codes_by_parent_id_tax_code_x_refs_by_id(id, parent_id, client_id, tax_code_x_ref)
        print("The response of TaxCodeXRefsApi->put_finance_tax_codes_by_parent_id_tax_code_x_refs_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaxCodeXRefsApi->put_finance_tax_codes_by_parent_id_tax_code_x_refs_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| taxCodeXRefId | 
 **parent_id** | **int**| taxCodeId | 
 **client_id** | **str**|  | 
 **tax_code_x_ref** | [**TaxCodeXRef**](TaxCodeXRef.md)| taxCodeXRef | 

### Return type

[**TaxCodeXRef**](TaxCodeXRef.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | TaxCodeXRef |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

