# connectwise_psa.AgreementTypeBoardDefaultsApi

All URIs are relative to *https://api-aus.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_finance_agreement_types_by_parent_id_board_defaults_by_id**](AgreementTypeBoardDefaultsApi.md#delete_finance_agreement_types_by_parent_id_board_defaults_by_id) | **DELETE** /finance/agreementTypes/{parentId}/boardDefaults/{id} | Delete AgreementTypeBoardDefault
[**get_finance_agreement_types_by_parent_id_board_defaults**](AgreementTypeBoardDefaultsApi.md#get_finance_agreement_types_by_parent_id_board_defaults) | **GET** /finance/agreementTypes/{parentId}/boardDefaults | Get List of AgreementTypeBoardDefault
[**get_finance_agreement_types_by_parent_id_board_defaults_by_id**](AgreementTypeBoardDefaultsApi.md#get_finance_agreement_types_by_parent_id_board_defaults_by_id) | **GET** /finance/agreementTypes/{parentId}/boardDefaults/{id} | Get AgreementTypeBoardDefault
[**get_finance_agreement_types_by_parent_id_board_defaults_count**](AgreementTypeBoardDefaultsApi.md#get_finance_agreement_types_by_parent_id_board_defaults_count) | **GET** /finance/agreementTypes/{parentId}/boardDefaults/count | Get Count of AgreementTypeBoardDefault
[**patch_finance_agreement_types_by_parent_id_board_defaults_by_id**](AgreementTypeBoardDefaultsApi.md#patch_finance_agreement_types_by_parent_id_board_defaults_by_id) | **PATCH** /finance/agreementTypes/{parentId}/boardDefaults/{id} | Patch AgreementTypeBoardDefault
[**post_finance_agreement_types_by_parent_id_board_defaults**](AgreementTypeBoardDefaultsApi.md#post_finance_agreement_types_by_parent_id_board_defaults) | **POST** /finance/agreementTypes/{parentId}/boardDefaults | Post AgreementTypeBoardDefault
[**put_finance_agreement_types_by_parent_id_board_defaults_by_id**](AgreementTypeBoardDefaultsApi.md#put_finance_agreement_types_by_parent_id_board_defaults_by_id) | **PUT** /finance/agreementTypes/{parentId}/boardDefaults/{id} | Put AgreementTypeBoardDefault


# **delete_finance_agreement_types_by_parent_id_board_defaults_by_id**
> delete_finance_agreement_types_by_parent_id_board_defaults_by_id(id, parent_id, client_id)

Delete AgreementTypeBoardDefault

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
    api_instance = connectwise_psa.AgreementTypeBoardDefaultsApi(api_client)
    id = 56 # int | boardDefaultId
    parent_id = 56 # int | agreementTypeId
    client_id = 'client_id_example' # str | 

    try:
        # Delete AgreementTypeBoardDefault
        api_instance.delete_finance_agreement_types_by_parent_id_board_defaults_by_id(id, parent_id, client_id)
    except Exception as e:
        print("Exception when calling AgreementTypeBoardDefaultsApi->delete_finance_agreement_types_by_parent_id_board_defaults_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| boardDefaultId | 
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

# **get_finance_agreement_types_by_parent_id_board_defaults**
> List[AgreementTypeBoardDefault] get_finance_agreement_types_by_parent_id_board_defaults(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of AgreementTypeBoardDefault

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.agreement_type_board_default import AgreementTypeBoardDefault
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
    api_instance = connectwise_psa.AgreementTypeBoardDefaultsApi(api_client)
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
        # Get List of AgreementTypeBoardDefault
        api_response = api_instance.get_finance_agreement_types_by_parent_id_board_defaults(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of AgreementTypeBoardDefaultsApi->get_finance_agreement_types_by_parent_id_board_defaults:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgreementTypeBoardDefaultsApi->get_finance_agreement_types_by_parent_id_board_defaults: %s\n" % e)
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

[**List[AgreementTypeBoardDefault]**](AgreementTypeBoardDefault.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of AgreementTypeBoardDefault |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_finance_agreement_types_by_parent_id_board_defaults_by_id**
> AgreementTypeBoardDefault get_finance_agreement_types_by_parent_id_board_defaults_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get AgreementTypeBoardDefault

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.agreement_type_board_default import AgreementTypeBoardDefault
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
    api_instance = connectwise_psa.AgreementTypeBoardDefaultsApi(api_client)
    id = 56 # int | boardDefaultId
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
        # Get AgreementTypeBoardDefault
        api_response = api_instance.get_finance_agreement_types_by_parent_id_board_defaults_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of AgreementTypeBoardDefaultsApi->get_finance_agreement_types_by_parent_id_board_defaults_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgreementTypeBoardDefaultsApi->get_finance_agreement_types_by_parent_id_board_defaults_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| boardDefaultId | 
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

[**AgreementTypeBoardDefault**](AgreementTypeBoardDefault.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | AgreementTypeBoardDefault |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_finance_agreement_types_by_parent_id_board_defaults_count**
> Count get_finance_agreement_types_by_parent_id_board_defaults_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Count of AgreementTypeBoardDefault

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
    api_instance = connectwise_psa.AgreementTypeBoardDefaultsApi(api_client)
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
        # Get Count of AgreementTypeBoardDefault
        api_response = api_instance.get_finance_agreement_types_by_parent_id_board_defaults_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of AgreementTypeBoardDefaultsApi->get_finance_agreement_types_by_parent_id_board_defaults_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgreementTypeBoardDefaultsApi->get_finance_agreement_types_by_parent_id_board_defaults_count: %s\n" % e)
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

# **patch_finance_agreement_types_by_parent_id_board_defaults_by_id**
> AgreementTypeBoardDefault patch_finance_agreement_types_by_parent_id_board_defaults_by_id(id, parent_id, client_id, patch_operation)

Patch AgreementTypeBoardDefault

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.agreement_type_board_default import AgreementTypeBoardDefault
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
    api_instance = connectwise_psa.AgreementTypeBoardDefaultsApi(api_client)
    id = 56 # int | boardDefaultId
    parent_id = 56 # int | agreementTypeId
    client_id = 'client_id_example' # str | 
    patch_operation = [connectwise_psa.PatchOperation()] # List[PatchOperation] | List of PatchOperation

    try:
        # Patch AgreementTypeBoardDefault
        api_response = api_instance.patch_finance_agreement_types_by_parent_id_board_defaults_by_id(id, parent_id, client_id, patch_operation)
        print("The response of AgreementTypeBoardDefaultsApi->patch_finance_agreement_types_by_parent_id_board_defaults_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgreementTypeBoardDefaultsApi->patch_finance_agreement_types_by_parent_id_board_defaults_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| boardDefaultId | 
 **parent_id** | **int**| agreementTypeId | 
 **client_id** | **str**|  | 
 **patch_operation** | [**List[PatchOperation]**](PatchOperation.md)| List of PatchOperation | 

### Return type

[**AgreementTypeBoardDefault**](AgreementTypeBoardDefault.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | AgreementTypeBoardDefault |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_finance_agreement_types_by_parent_id_board_defaults**
> AgreementTypeBoardDefault post_finance_agreement_types_by_parent_id_board_defaults(parent_id, client_id, agreement_type_board_default)

Post AgreementTypeBoardDefault

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.agreement_type_board_default import AgreementTypeBoardDefault
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
    api_instance = connectwise_psa.AgreementTypeBoardDefaultsApi(api_client)
    parent_id = 56 # int | agreementTypeId
    client_id = 'client_id_example' # str | 
    agreement_type_board_default = connectwise_psa.AgreementTypeBoardDefault() # AgreementTypeBoardDefault | boardDefault

    try:
        # Post AgreementTypeBoardDefault
        api_response = api_instance.post_finance_agreement_types_by_parent_id_board_defaults(parent_id, client_id, agreement_type_board_default)
        print("The response of AgreementTypeBoardDefaultsApi->post_finance_agreement_types_by_parent_id_board_defaults:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgreementTypeBoardDefaultsApi->post_finance_agreement_types_by_parent_id_board_defaults: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| agreementTypeId | 
 **client_id** | **str**|  | 
 **agreement_type_board_default** | [**AgreementTypeBoardDefault**](AgreementTypeBoardDefault.md)| boardDefault | 

### Return type

[**AgreementTypeBoardDefault**](AgreementTypeBoardDefault.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | AgreementTypeBoardDefault |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_finance_agreement_types_by_parent_id_board_defaults_by_id**
> AgreementTypeBoardDefault put_finance_agreement_types_by_parent_id_board_defaults_by_id(id, parent_id, client_id, agreement_type_board_default)

Put AgreementTypeBoardDefault

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.agreement_type_board_default import AgreementTypeBoardDefault
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
    api_instance = connectwise_psa.AgreementTypeBoardDefaultsApi(api_client)
    id = 56 # int | boardDefaultId
    parent_id = 56 # int | agreementTypeId
    client_id = 'client_id_example' # str | 
    agreement_type_board_default = connectwise_psa.AgreementTypeBoardDefault() # AgreementTypeBoardDefault | boardDefault

    try:
        # Put AgreementTypeBoardDefault
        api_response = api_instance.put_finance_agreement_types_by_parent_id_board_defaults_by_id(id, parent_id, client_id, agreement_type_board_default)
        print("The response of AgreementTypeBoardDefaultsApi->put_finance_agreement_types_by_parent_id_board_defaults_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgreementTypeBoardDefaultsApi->put_finance_agreement_types_by_parent_id_board_defaults_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| boardDefaultId | 
 **parent_id** | **int**| agreementTypeId | 
 **client_id** | **str**|  | 
 **agreement_type_board_default** | [**AgreementTypeBoardDefault**](AgreementTypeBoardDefault.md)| boardDefault | 

### Return type

[**AgreementTypeBoardDefault**](AgreementTypeBoardDefault.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | AgreementTypeBoardDefault |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

