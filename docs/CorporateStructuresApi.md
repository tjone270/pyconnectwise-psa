# connectwise_psa.CorporateStructuresApi

All URIs are relative to *https://api-aus.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_system_my_company_corporate_structure**](CorporateStructuresApi.md#get_system_my_company_corporate_structure) | **GET** /system/myCompany/corporateStructure | Get List of CorporateStructure
[**get_system_my_company_corporate_structure_by_id**](CorporateStructuresApi.md#get_system_my_company_corporate_structure_by_id) | **GET** /system/myCompany/corporateStructure/{id} | Get CorporateStructure
[**get_system_my_company_corporate_structure_count**](CorporateStructuresApi.md#get_system_my_company_corporate_structure_count) | **GET** /system/myCompany/corporateStructure/count | Get Count of CorporateStructure
[**patch_system_my_company_corporate_structure_by_id**](CorporateStructuresApi.md#patch_system_my_company_corporate_structure_by_id) | **PATCH** /system/myCompany/corporateStructure/{id} | Patch CorporateStructure
[**put_system_my_company_corporate_structure_by_id**](CorporateStructuresApi.md#put_system_my_company_corporate_structure_by_id) | **PUT** /system/myCompany/corporateStructure/{id} | Put CorporateStructure


# **get_system_my_company_corporate_structure**
> List[CorporateStructure] get_system_my_company_corporate_structure(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of CorporateStructure

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.corporate_structure import CorporateStructure
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
    api_instance = connectwise_psa.CorporateStructuresApi(api_client)
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
        # Get List of CorporateStructure
        api_response = api_instance.get_system_my_company_corporate_structure(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of CorporateStructuresApi->get_system_my_company_corporate_structure:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CorporateStructuresApi->get_system_my_company_corporate_structure: %s\n" % e)
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

[**List[CorporateStructure]**](CorporateStructure.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of CorporateStructure |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_system_my_company_corporate_structure_by_id**
> CorporateStructure get_system_my_company_corporate_structure_by_id(id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get CorporateStructure

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.corporate_structure import CorporateStructure
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
    api_instance = connectwise_psa.CorporateStructuresApi(api_client)
    id = 56 # int | corporateStructureId
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
        # Get CorporateStructure
        api_response = api_instance.get_system_my_company_corporate_structure_by_id(id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of CorporateStructuresApi->get_system_my_company_corporate_structure_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CorporateStructuresApi->get_system_my_company_corporate_structure_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| corporateStructureId | 
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

[**CorporateStructure**](CorporateStructure.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | CorporateStructure |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_system_my_company_corporate_structure_count**
> Count get_system_my_company_corporate_structure_count(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Count of CorporateStructure

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
    api_instance = connectwise_psa.CorporateStructuresApi(api_client)
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
        # Get Count of CorporateStructure
        api_response = api_instance.get_system_my_company_corporate_structure_count(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of CorporateStructuresApi->get_system_my_company_corporate_structure_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CorporateStructuresApi->get_system_my_company_corporate_structure_count: %s\n" % e)
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

# **patch_system_my_company_corporate_structure_by_id**
> CorporateStructure patch_system_my_company_corporate_structure_by_id(id, client_id, patch_operation)

Patch CorporateStructure

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.corporate_structure import CorporateStructure
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
    api_instance = connectwise_psa.CorporateStructuresApi(api_client)
    id = 56 # int | corporateStructureId
    client_id = 'client_id_example' # str | 
    patch_operation = [connectwise_psa.PatchOperation()] # List[PatchOperation] | List of PatchOperation

    try:
        # Patch CorporateStructure
        api_response = api_instance.patch_system_my_company_corporate_structure_by_id(id, client_id, patch_operation)
        print("The response of CorporateStructuresApi->patch_system_my_company_corporate_structure_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CorporateStructuresApi->patch_system_my_company_corporate_structure_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| corporateStructureId | 
 **client_id** | **str**|  | 
 **patch_operation** | [**List[PatchOperation]**](PatchOperation.md)| List of PatchOperation | 

### Return type

[**CorporateStructure**](CorporateStructure.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | CorporateStructure |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_system_my_company_corporate_structure_by_id**
> CorporateStructure put_system_my_company_corporate_structure_by_id(id, client_id, corporate_structure)

Put CorporateStructure

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.corporate_structure import CorporateStructure
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
    api_instance = connectwise_psa.CorporateStructuresApi(api_client)
    id = 56 # int | corporateStructureId
    client_id = 'client_id_example' # str | 
    corporate_structure = connectwise_psa.CorporateStructure() # CorporateStructure | corporateStructure

    try:
        # Put CorporateStructure
        api_response = api_instance.put_system_my_company_corporate_structure_by_id(id, client_id, corporate_structure)
        print("The response of CorporateStructuresApi->put_system_my_company_corporate_structure_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CorporateStructuresApi->put_system_my_company_corporate_structure_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| corporateStructureId | 
 **client_id** | **str**|  | 
 **corporate_structure** | [**CorporateStructure**](CorporateStructure.md)| corporateStructure | 

### Return type

[**CorporateStructure**](CorporateStructure.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | CorporateStructure |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

