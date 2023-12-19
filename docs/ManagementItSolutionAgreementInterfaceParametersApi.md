# connectwise_psa.ManagementItSolutionAgreementInterfaceParametersApi

All URIs are relative to *https://api-aus.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_company_management_it_solutions_by_parent_id_management_products_by_id**](ManagementItSolutionAgreementInterfaceParametersApi.md#delete_company_management_it_solutions_by_parent_id_management_products_by_id) | **DELETE** /company/managementItSolutions/{parentId}/managementProducts/{id} | Delete ManagementItSolutionAgreementInterfaceParameter
[**get_company_management_it_solutions_by_parent_id_management_products**](ManagementItSolutionAgreementInterfaceParametersApi.md#get_company_management_it_solutions_by_parent_id_management_products) | **GET** /company/managementItSolutions/{parentId}/managementProducts | Get List of ManagementItSolutionAgreementInterfaceParameter
[**get_company_management_it_solutions_by_parent_id_management_products_by_id**](ManagementItSolutionAgreementInterfaceParametersApi.md#get_company_management_it_solutions_by_parent_id_management_products_by_id) | **GET** /company/managementItSolutions/{parentId}/managementProducts/{id} | Get ManagementItSolutionAgreementInterfaceParameter
[**get_company_management_it_solutions_by_parent_id_management_products_count**](ManagementItSolutionAgreementInterfaceParametersApi.md#get_company_management_it_solutions_by_parent_id_management_products_count) | **GET** /company/managementItSolutions/{parentId}/managementProducts/count | Get Count of ManagementItSolutionAgreementInterfaceParameter
[**patch_company_management_it_solutions_by_parent_id_management_products_by_id**](ManagementItSolutionAgreementInterfaceParametersApi.md#patch_company_management_it_solutions_by_parent_id_management_products_by_id) | **PATCH** /company/managementItSolutions/{parentId}/managementProducts/{id} | Patch ManagementItSolutionAgreementInterfaceParameter
[**post_company_management_it_solutions_by_parent_id_management_products**](ManagementItSolutionAgreementInterfaceParametersApi.md#post_company_management_it_solutions_by_parent_id_management_products) | **POST** /company/managementItSolutions/{parentId}/managementProducts | Post ManagementItSolutionAgreementInterfaceParameter
[**put_company_management_it_solutions_by_parent_id_management_products_by_id**](ManagementItSolutionAgreementInterfaceParametersApi.md#put_company_management_it_solutions_by_parent_id_management_products_by_id) | **PUT** /company/managementItSolutions/{parentId}/managementProducts/{id} | Put ManagementItSolutionAgreementInterfaceParameter


# **delete_company_management_it_solutions_by_parent_id_management_products_by_id**
> ManagementItSolutionAgreementInterfaceParameter delete_company_management_it_solutions_by_parent_id_management_products_by_id(id, parent_id, client_id)

Delete ManagementItSolutionAgreementInterfaceParameter

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.management_it_solution_agreement_interface_parameter import ManagementItSolutionAgreementInterfaceParameter
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
    api_instance = connectwise_psa.ManagementItSolutionAgreementInterfaceParametersApi(api_client)
    id = 56 # int | managementProductId
    parent_id = 56 # int | managementItSolutionId
    client_id = 'client_id_example' # str | 

    try:
        # Delete ManagementItSolutionAgreementInterfaceParameter
        api_response = api_instance.delete_company_management_it_solutions_by_parent_id_management_products_by_id(id, parent_id, client_id)
        print("The response of ManagementItSolutionAgreementInterfaceParametersApi->delete_company_management_it_solutions_by_parent_id_management_products_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagementItSolutionAgreementInterfaceParametersApi->delete_company_management_it_solutions_by_parent_id_management_products_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| managementProductId | 
 **parent_id** | **int**| managementItSolutionId | 
 **client_id** | **str**|  | 

### Return type

[**ManagementItSolutionAgreementInterfaceParameter**](ManagementItSolutionAgreementInterfaceParameter.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ManagementItSolutionAgreementInterfaceParameter |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_company_management_it_solutions_by_parent_id_management_products**
> List[ManagementItSolutionAgreementInterfaceParameter] get_company_management_it_solutions_by_parent_id_management_products(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of ManagementItSolutionAgreementInterfaceParameter

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.management_it_solution_agreement_interface_parameter import ManagementItSolutionAgreementInterfaceParameter
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
    api_instance = connectwise_psa.ManagementItSolutionAgreementInterfaceParametersApi(api_client)
    parent_id = 56 # int | managementItSolutionId
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
        # Get List of ManagementItSolutionAgreementInterfaceParameter
        api_response = api_instance.get_company_management_it_solutions_by_parent_id_management_products(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of ManagementItSolutionAgreementInterfaceParametersApi->get_company_management_it_solutions_by_parent_id_management_products:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagementItSolutionAgreementInterfaceParametersApi->get_company_management_it_solutions_by_parent_id_management_products: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| managementItSolutionId | 
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

[**List[ManagementItSolutionAgreementInterfaceParameter]**](ManagementItSolutionAgreementInterfaceParameter.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of ManagementItSolutionAgreementInterfaceParameter |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_company_management_it_solutions_by_parent_id_management_products_by_id**
> ManagementItSolutionAgreementInterfaceParameter get_company_management_it_solutions_by_parent_id_management_products_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get ManagementItSolutionAgreementInterfaceParameter

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.management_it_solution_agreement_interface_parameter import ManagementItSolutionAgreementInterfaceParameter
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
    api_instance = connectwise_psa.ManagementItSolutionAgreementInterfaceParametersApi(api_client)
    id = 56 # int | managementProductId
    parent_id = 56 # int | managementItSolutionId
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
        # Get ManagementItSolutionAgreementInterfaceParameter
        api_response = api_instance.get_company_management_it_solutions_by_parent_id_management_products_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of ManagementItSolutionAgreementInterfaceParametersApi->get_company_management_it_solutions_by_parent_id_management_products_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagementItSolutionAgreementInterfaceParametersApi->get_company_management_it_solutions_by_parent_id_management_products_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| managementProductId | 
 **parent_id** | **int**| managementItSolutionId | 
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

[**ManagementItSolutionAgreementInterfaceParameter**](ManagementItSolutionAgreementInterfaceParameter.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ManagementItSolutionAgreementInterfaceParameter |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_company_management_it_solutions_by_parent_id_management_products_count**
> Count get_company_management_it_solutions_by_parent_id_management_products_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Count of ManagementItSolutionAgreementInterfaceParameter

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
    api_instance = connectwise_psa.ManagementItSolutionAgreementInterfaceParametersApi(api_client)
    parent_id = 56 # int | managementItSolutionId
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
        # Get Count of ManagementItSolutionAgreementInterfaceParameter
        api_response = api_instance.get_company_management_it_solutions_by_parent_id_management_products_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of ManagementItSolutionAgreementInterfaceParametersApi->get_company_management_it_solutions_by_parent_id_management_products_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagementItSolutionAgreementInterfaceParametersApi->get_company_management_it_solutions_by_parent_id_management_products_count: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| managementItSolutionId | 
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

# **patch_company_management_it_solutions_by_parent_id_management_products_by_id**
> ManagementItSolutionAgreementInterfaceParameter patch_company_management_it_solutions_by_parent_id_management_products_by_id(id, parent_id, client_id, patch_operation)

Patch ManagementItSolutionAgreementInterfaceParameter

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.management_it_solution_agreement_interface_parameter import ManagementItSolutionAgreementInterfaceParameter
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
    api_instance = connectwise_psa.ManagementItSolutionAgreementInterfaceParametersApi(api_client)
    id = 56 # int | managementProductId
    parent_id = 56 # int | managementItSolutionId
    client_id = 'client_id_example' # str | 
    patch_operation = [connectwise_psa.PatchOperation()] # List[PatchOperation] | List of PatchOperation

    try:
        # Patch ManagementItSolutionAgreementInterfaceParameter
        api_response = api_instance.patch_company_management_it_solutions_by_parent_id_management_products_by_id(id, parent_id, client_id, patch_operation)
        print("The response of ManagementItSolutionAgreementInterfaceParametersApi->patch_company_management_it_solutions_by_parent_id_management_products_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagementItSolutionAgreementInterfaceParametersApi->patch_company_management_it_solutions_by_parent_id_management_products_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| managementProductId | 
 **parent_id** | **int**| managementItSolutionId | 
 **client_id** | **str**|  | 
 **patch_operation** | [**List[PatchOperation]**](PatchOperation.md)| List of PatchOperation | 

### Return type

[**ManagementItSolutionAgreementInterfaceParameter**](ManagementItSolutionAgreementInterfaceParameter.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ManagementItSolutionAgreementInterfaceParameter |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_company_management_it_solutions_by_parent_id_management_products**
> ManagementItSolutionAgreementInterfaceParameter post_company_management_it_solutions_by_parent_id_management_products(parent_id, client_id, management_it_solution_agreement_interface_parameter)

Post ManagementItSolutionAgreementInterfaceParameter

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.management_it_solution_agreement_interface_parameter import ManagementItSolutionAgreementInterfaceParameter
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
    api_instance = connectwise_psa.ManagementItSolutionAgreementInterfaceParametersApi(api_client)
    parent_id = 56 # int | managementItSolutionId
    client_id = 'client_id_example' # str | 
    management_it_solution_agreement_interface_parameter = connectwise_psa.ManagementItSolutionAgreementInterfaceParameter() # ManagementItSolutionAgreementInterfaceParameter | managementProduct

    try:
        # Post ManagementItSolutionAgreementInterfaceParameter
        api_response = api_instance.post_company_management_it_solutions_by_parent_id_management_products(parent_id, client_id, management_it_solution_agreement_interface_parameter)
        print("The response of ManagementItSolutionAgreementInterfaceParametersApi->post_company_management_it_solutions_by_parent_id_management_products:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagementItSolutionAgreementInterfaceParametersApi->post_company_management_it_solutions_by_parent_id_management_products: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| managementItSolutionId | 
 **client_id** | **str**|  | 
 **management_it_solution_agreement_interface_parameter** | [**ManagementItSolutionAgreementInterfaceParameter**](ManagementItSolutionAgreementInterfaceParameter.md)| managementProduct | 

### Return type

[**ManagementItSolutionAgreementInterfaceParameter**](ManagementItSolutionAgreementInterfaceParameter.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ManagementItSolutionAgreementInterfaceParameter |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_company_management_it_solutions_by_parent_id_management_products_by_id**
> ManagementItSolutionAgreementInterfaceParameter put_company_management_it_solutions_by_parent_id_management_products_by_id(id, parent_id, client_id, management_it_solution_agreement_interface_parameter)

Put ManagementItSolutionAgreementInterfaceParameter

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.management_it_solution_agreement_interface_parameter import ManagementItSolutionAgreementInterfaceParameter
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
    api_instance = connectwise_psa.ManagementItSolutionAgreementInterfaceParametersApi(api_client)
    id = 56 # int | managementProductId
    parent_id = 56 # int | managementItSolutionId
    client_id = 'client_id_example' # str | 
    management_it_solution_agreement_interface_parameter = connectwise_psa.ManagementItSolutionAgreementInterfaceParameter() # ManagementItSolutionAgreementInterfaceParameter | managementProduct

    try:
        # Put ManagementItSolutionAgreementInterfaceParameter
        api_response = api_instance.put_company_management_it_solutions_by_parent_id_management_products_by_id(id, parent_id, client_id, management_it_solution_agreement_interface_parameter)
        print("The response of ManagementItSolutionAgreementInterfaceParametersApi->put_company_management_it_solutions_by_parent_id_management_products_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagementItSolutionAgreementInterfaceParametersApi->put_company_management_it_solutions_by_parent_id_management_products_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| managementProductId | 
 **parent_id** | **int**| managementItSolutionId | 
 **client_id** | **str**|  | 
 **management_it_solution_agreement_interface_parameter** | [**ManagementItSolutionAgreementInterfaceParameter**](ManagementItSolutionAgreementInterfaceParameter.md)| managementProduct | 

### Return type

[**ManagementItSolutionAgreementInterfaceParameter**](ManagementItSolutionAgreementInterfaceParameter.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ManagementItSolutionAgreementInterfaceParameter |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

