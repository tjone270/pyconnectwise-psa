# connectwise_psa.AgreementTypeWorkTypesApi

All URIs are relative to *https://aus-api.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_finance_agreement_types_by_parent_id_worktypes_by_id**](AgreementTypeWorkTypesApi.md#delete_finance_agreement_types_by_parent_id_worktypes_by_id) | **DELETE** /finance/agreementTypes/{parentId}/worktypes/{id} | Delete AgreementTypeWorkType
[**get_finance_agreement_types_by_parent_id_worktypes**](AgreementTypeWorkTypesApi.md#get_finance_agreement_types_by_parent_id_worktypes) | **GET** /finance/agreementTypes/{parentId}/worktypes | Get List of AgreementTypeWorkType
[**get_finance_agreement_types_by_parent_id_worktypes_by_id**](AgreementTypeWorkTypesApi.md#get_finance_agreement_types_by_parent_id_worktypes_by_id) | **GET** /finance/agreementTypes/{parentId}/worktypes/{id} | Get AgreementTypeWorkType
[**get_finance_agreement_types_by_parent_id_worktypes_count**](AgreementTypeWorkTypesApi.md#get_finance_agreement_types_by_parent_id_worktypes_count) | **GET** /finance/agreementTypes/{parentId}/worktypes/count | Get Count of AgreementTypeWorkType
[**patch_finance_agreement_types_by_parent_id_worktypes_by_id**](AgreementTypeWorkTypesApi.md#patch_finance_agreement_types_by_parent_id_worktypes_by_id) | **PATCH** /finance/agreementTypes/{parentId}/worktypes/{id} | Patch AgreementTypeWorkType
[**post_finance_agreement_types_by_parent_id_worktypes**](AgreementTypeWorkTypesApi.md#post_finance_agreement_types_by_parent_id_worktypes) | **POST** /finance/agreementTypes/{parentId}/worktypes | Post AgreementTypeWorkType
[**put_finance_agreement_types_by_parent_id_worktypes_by_id**](AgreementTypeWorkTypesApi.md#put_finance_agreement_types_by_parent_id_worktypes_by_id) | **PUT** /finance/agreementTypes/{parentId}/worktypes/{id} | Put AgreementTypeWorkType


# **delete_finance_agreement_types_by_parent_id_worktypes_by_id**
> delete_finance_agreement_types_by_parent_id_worktypes_by_id(id, parent_id, client_id)

Delete AgreementTypeWorkType

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
    api_instance = connectwise_psa.AgreementTypeWorkTypesApi(api_client)
    id = 56 # int | worktypeId
    parent_id = 56 # int | agreementTypeId
    client_id = 'client_id_example' # str | 

    try:
        # Delete AgreementTypeWorkType
        api_instance.delete_finance_agreement_types_by_parent_id_worktypes_by_id(id, parent_id, client_id)
    except Exception as e:
        print("Exception when calling AgreementTypeWorkTypesApi->delete_finance_agreement_types_by_parent_id_worktypes_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| worktypeId | 
 **parent_id** | **int**| agreementTypeId | 
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

# **get_finance_agreement_types_by_parent_id_worktypes**
> List[AgreementTypeWorkType] get_finance_agreement_types_by_parent_id_worktypes(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of AgreementTypeWorkType

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.agreement_type_work_type import AgreementTypeWorkType
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
    api_instance = connectwise_psa.AgreementTypeWorkTypesApi(api_client)
    parent_id = 56 # int | agreementTypeId
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
        # Get List of AgreementTypeWorkType
        api_response = api_instance.get_finance_agreement_types_by_parent_id_worktypes(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of AgreementTypeWorkTypesApi->get_finance_agreement_types_by_parent_id_worktypes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgreementTypeWorkTypesApi->get_finance_agreement_types_by_parent_id_worktypes: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| agreementTypeId | 
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

[**List[AgreementTypeWorkType]**](AgreementTypeWorkType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of AgreementTypeWorkType |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_finance_agreement_types_by_parent_id_worktypes_by_id**
> AgreementTypeWorkType get_finance_agreement_types_by_parent_id_worktypes_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get AgreementTypeWorkType

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.agreement_type_work_type import AgreementTypeWorkType
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
    api_instance = connectwise_psa.AgreementTypeWorkTypesApi(api_client)
    id = 56 # int | worktypeId
    parent_id = 56 # int | agreementTypeId
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
        # Get AgreementTypeWorkType
        api_response = api_instance.get_finance_agreement_types_by_parent_id_worktypes_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of AgreementTypeWorkTypesApi->get_finance_agreement_types_by_parent_id_worktypes_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgreementTypeWorkTypesApi->get_finance_agreement_types_by_parent_id_worktypes_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| worktypeId | 
 **parent_id** | **int**| agreementTypeId | 
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

[**AgreementTypeWorkType**](AgreementTypeWorkType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | AgreementTypeWorkType |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_finance_agreement_types_by_parent_id_worktypes_count**
> Count get_finance_agreement_types_by_parent_id_worktypes_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Count of AgreementTypeWorkType

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
    api_instance = connectwise_psa.AgreementTypeWorkTypesApi(api_client)
    parent_id = 56 # int | agreementTypeId
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
        # Get Count of AgreementTypeWorkType
        api_response = api_instance.get_finance_agreement_types_by_parent_id_worktypes_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of AgreementTypeWorkTypesApi->get_finance_agreement_types_by_parent_id_worktypes_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgreementTypeWorkTypesApi->get_finance_agreement_types_by_parent_id_worktypes_count: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| agreementTypeId | 
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

# **patch_finance_agreement_types_by_parent_id_worktypes_by_id**
> AgreementTypeWorkType patch_finance_agreement_types_by_parent_id_worktypes_by_id(id, parent_id, client_id, patch_operation)

Patch AgreementTypeWorkType

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.agreement_type_work_type import AgreementTypeWorkType
from connectwise_psa.models.patch_operation import PatchOperation
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
    api_instance = connectwise_psa.AgreementTypeWorkTypesApi(api_client)
    id = 56 # int | worktypeId
    parent_id = 56 # int | agreementTypeId
    client_id = 'client_id_example' # str | 
    patch_operation = [connectwise_psa.PatchOperation()] # List[PatchOperation] | List of PatchOperation

    try:
        # Patch AgreementTypeWorkType
        api_response = api_instance.patch_finance_agreement_types_by_parent_id_worktypes_by_id(id, parent_id, client_id, patch_operation)
        print("The response of AgreementTypeWorkTypesApi->patch_finance_agreement_types_by_parent_id_worktypes_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgreementTypeWorkTypesApi->patch_finance_agreement_types_by_parent_id_worktypes_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| worktypeId | 
 **parent_id** | **int**| agreementTypeId | 
 **client_id** | **str**|  | 
 **patch_operation** | [**List[PatchOperation]**](PatchOperation.md)| List of PatchOperation | 

### Return type

[**AgreementTypeWorkType**](AgreementTypeWorkType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | AgreementTypeWorkType |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_finance_agreement_types_by_parent_id_worktypes**
> AgreementTypeWorkType post_finance_agreement_types_by_parent_id_worktypes(parent_id, client_id, agreement_type_work_type)

Post AgreementTypeWorkType

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.agreement_type_work_type import AgreementTypeWorkType
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
    api_instance = connectwise_psa.AgreementTypeWorkTypesApi(api_client)
    parent_id = 56 # int | agreementTypeId
    client_id = 'client_id_example' # str | 
    agreement_type_work_type = connectwise_psa.AgreementTypeWorkType() # AgreementTypeWorkType | workType

    try:
        # Post AgreementTypeWorkType
        api_response = api_instance.post_finance_agreement_types_by_parent_id_worktypes(parent_id, client_id, agreement_type_work_type)
        print("The response of AgreementTypeWorkTypesApi->post_finance_agreement_types_by_parent_id_worktypes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgreementTypeWorkTypesApi->post_finance_agreement_types_by_parent_id_worktypes: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| agreementTypeId | 
 **client_id** | **str**|  | 
 **agreement_type_work_type** | [**AgreementTypeWorkType**](AgreementTypeWorkType.md)| workType | 

### Return type

[**AgreementTypeWorkType**](AgreementTypeWorkType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | AgreementTypeWorkType |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_finance_agreement_types_by_parent_id_worktypes_by_id**
> AgreementTypeWorkType put_finance_agreement_types_by_parent_id_worktypes_by_id(id, parent_id, client_id, agreement_type_work_type)

Put AgreementTypeWorkType

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.agreement_type_work_type import AgreementTypeWorkType
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
    api_instance = connectwise_psa.AgreementTypeWorkTypesApi(api_client)
    id = 56 # int | worktypeId
    parent_id = 56 # int | agreementTypeId
    client_id = 'client_id_example' # str | 
    agreement_type_work_type = connectwise_psa.AgreementTypeWorkType() # AgreementTypeWorkType | workType

    try:
        # Put AgreementTypeWorkType
        api_response = api_instance.put_finance_agreement_types_by_parent_id_worktypes_by_id(id, parent_id, client_id, agreement_type_work_type)
        print("The response of AgreementTypeWorkTypesApi->put_finance_agreement_types_by_parent_id_worktypes_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgreementTypeWorkTypesApi->put_finance_agreement_types_by_parent_id_worktypes_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| worktypeId | 
 **parent_id** | **int**| agreementTypeId | 
 **client_id** | **str**|  | 
 **agreement_type_work_type** | [**AgreementTypeWorkType**](AgreementTypeWorkType.md)| workType | 

### Return type

[**AgreementTypeWorkType**](AgreementTypeWorkType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | AgreementTypeWorkType |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

