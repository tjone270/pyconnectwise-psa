# connectwise_psa.CompanyCompanyTypeAssociationsApi

All URIs are relative to *https://api-aus.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_company_companies_by_parent_id_type_associations_by_id**](CompanyCompanyTypeAssociationsApi.md#delete_company_companies_by_parent_id_type_associations_by_id) | **DELETE** /company/companies/{parentId}/typeAssociations/{id} | Delete CompanyTypeAssociation
[**get_company_companies_by_parent_id_type_associations**](CompanyCompanyTypeAssociationsApi.md#get_company_companies_by_parent_id_type_associations) | **GET** /company/companies/{parentId}/typeAssociations | Get List of CompanyTypeAssociation
[**get_company_companies_by_parent_id_type_associations_by_id**](CompanyCompanyTypeAssociationsApi.md#get_company_companies_by_parent_id_type_associations_by_id) | **GET** /company/companies/{parentId}/typeAssociations/{id} | Get CompanyTypeAssociation
[**get_company_companies_by_parent_id_type_associations_count**](CompanyCompanyTypeAssociationsApi.md#get_company_companies_by_parent_id_type_associations_count) | **GET** /company/companies/{parentId}/typeAssociations/count | Get Count of CompanyTypeAssociation
[**patch_company_companies_by_parent_id_type_associations_by_id**](CompanyCompanyTypeAssociationsApi.md#patch_company_companies_by_parent_id_type_associations_by_id) | **PATCH** /company/companies/{parentId}/typeAssociations/{id} | Patch CompanyTypeAssociation
[**post_company_companies_by_parent_id_type_associations**](CompanyCompanyTypeAssociationsApi.md#post_company_companies_by_parent_id_type_associations) | **POST** /company/companies/{parentId}/typeAssociations | Post CompanyTypeAssociation
[**put_company_companies_by_parent_id_type_associations_by_id**](CompanyCompanyTypeAssociationsApi.md#put_company_companies_by_parent_id_type_associations_by_id) | **PUT** /company/companies/{parentId}/typeAssociations/{id} | Put CompanyTypeAssociation


# **delete_company_companies_by_parent_id_type_associations_by_id**
> delete_company_companies_by_parent_id_type_associations_by_id(id, parent_id, client_id)

Delete CompanyTypeAssociation

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
    api_instance = connectwise_psa.CompanyCompanyTypeAssociationsApi(api_client)
    id = 56 # int | typeAssociationId
    parent_id = 56 # int | companyId
    client_id = 'client_id_example' # str | 

    try:
        # Delete CompanyTypeAssociation
        api_instance.delete_company_companies_by_parent_id_type_associations_by_id(id, parent_id, client_id)
    except Exception as e:
        print("Exception when calling CompanyCompanyTypeAssociationsApi->delete_company_companies_by_parent_id_type_associations_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| typeAssociationId | 
 **parent_id** | **int**| companyId | 
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

# **get_company_companies_by_parent_id_type_associations**
> List[CompanyCompanyTypeAssociationCompanyTypeAssociation] get_company_companies_by_parent_id_type_associations(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of CompanyTypeAssociation

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.company_company_type_association_company_type_association import CompanyCompanyTypeAssociationCompanyTypeAssociation
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
    api_instance = connectwise_psa.CompanyCompanyTypeAssociationsApi(api_client)
    parent_id = 56 # int | companyId
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
        # Get List of CompanyTypeAssociation
        api_response = api_instance.get_company_companies_by_parent_id_type_associations(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of CompanyCompanyTypeAssociationsApi->get_company_companies_by_parent_id_type_associations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompanyCompanyTypeAssociationsApi->get_company_companies_by_parent_id_type_associations: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| companyId | 
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

[**List[CompanyCompanyTypeAssociationCompanyTypeAssociation]**](CompanyCompanyTypeAssociationCompanyTypeAssociation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of CompanyTypeAssociation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_company_companies_by_parent_id_type_associations_by_id**
> CompanyCompanyTypeAssociationCompanyTypeAssociation get_company_companies_by_parent_id_type_associations_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get CompanyTypeAssociation

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.company_company_type_association_company_type_association import CompanyCompanyTypeAssociationCompanyTypeAssociation
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
    api_instance = connectwise_psa.CompanyCompanyTypeAssociationsApi(api_client)
    id = 56 # int | typeAssociationId
    parent_id = 56 # int | companyId
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
        # Get CompanyTypeAssociation
        api_response = api_instance.get_company_companies_by_parent_id_type_associations_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of CompanyCompanyTypeAssociationsApi->get_company_companies_by_parent_id_type_associations_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompanyCompanyTypeAssociationsApi->get_company_companies_by_parent_id_type_associations_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| typeAssociationId | 
 **parent_id** | **int**| companyId | 
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

[**CompanyCompanyTypeAssociationCompanyTypeAssociation**](CompanyCompanyTypeAssociationCompanyTypeAssociation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | CompanyTypeAssociation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_company_companies_by_parent_id_type_associations_count**
> Count get_company_companies_by_parent_id_type_associations_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Count of CompanyTypeAssociation

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
    api_instance = connectwise_psa.CompanyCompanyTypeAssociationsApi(api_client)
    parent_id = 56 # int | companyId
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
        # Get Count of CompanyTypeAssociation
        api_response = api_instance.get_company_companies_by_parent_id_type_associations_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of CompanyCompanyTypeAssociationsApi->get_company_companies_by_parent_id_type_associations_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompanyCompanyTypeAssociationsApi->get_company_companies_by_parent_id_type_associations_count: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| companyId | 
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

# **patch_company_companies_by_parent_id_type_associations_by_id**
> CompanyCompanyTypeAssociationCompanyTypeAssociation patch_company_companies_by_parent_id_type_associations_by_id(id, parent_id, client_id, patch_operation)

Patch CompanyTypeAssociation

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.company_company_type_association_company_type_association import CompanyCompanyTypeAssociationCompanyTypeAssociation
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
    api_instance = connectwise_psa.CompanyCompanyTypeAssociationsApi(api_client)
    id = 56 # int | typeAssociationId
    parent_id = 56 # int | companyId
    client_id = 'client_id_example' # str | 
    patch_operation = [connectwise_psa.PatchOperation()] # List[PatchOperation] | List of PatchOperation

    try:
        # Patch CompanyTypeAssociation
        api_response = api_instance.patch_company_companies_by_parent_id_type_associations_by_id(id, parent_id, client_id, patch_operation)
        print("The response of CompanyCompanyTypeAssociationsApi->patch_company_companies_by_parent_id_type_associations_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompanyCompanyTypeAssociationsApi->patch_company_companies_by_parent_id_type_associations_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| typeAssociationId | 
 **parent_id** | **int**| companyId | 
 **client_id** | **str**|  | 
 **patch_operation** | [**List[PatchOperation]**](PatchOperation.md)| List of PatchOperation | 

### Return type

[**CompanyCompanyTypeAssociationCompanyTypeAssociation**](CompanyCompanyTypeAssociationCompanyTypeAssociation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | CompanyTypeAssociation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_company_companies_by_parent_id_type_associations**
> CompanyCompanyTypeAssociationCompanyTypeAssociation post_company_companies_by_parent_id_type_associations(parent_id, client_id, company_company_type_association_company_type_association)

Post CompanyTypeAssociation

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.company_company_type_association_company_type_association import CompanyCompanyTypeAssociationCompanyTypeAssociation
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
    api_instance = connectwise_psa.CompanyCompanyTypeAssociationsApi(api_client)
    parent_id = 56 # int | companyId
    client_id = 'client_id_example' # str | 
    company_company_type_association_company_type_association = connectwise_psa.CompanyCompanyTypeAssociationCompanyTypeAssociation() # CompanyCompanyTypeAssociationCompanyTypeAssociation | companyTypeAssociation

    try:
        # Post CompanyTypeAssociation
        api_response = api_instance.post_company_companies_by_parent_id_type_associations(parent_id, client_id, company_company_type_association_company_type_association)
        print("The response of CompanyCompanyTypeAssociationsApi->post_company_companies_by_parent_id_type_associations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompanyCompanyTypeAssociationsApi->post_company_companies_by_parent_id_type_associations: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| companyId | 
 **client_id** | **str**|  | 
 **company_company_type_association_company_type_association** | [**CompanyCompanyTypeAssociationCompanyTypeAssociation**](CompanyCompanyTypeAssociationCompanyTypeAssociation.md)| companyTypeAssociation | 

### Return type

[**CompanyCompanyTypeAssociationCompanyTypeAssociation**](CompanyCompanyTypeAssociationCompanyTypeAssociation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | CompanyTypeAssociation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_company_companies_by_parent_id_type_associations_by_id**
> CompanyCompanyTypeAssociationCompanyTypeAssociation put_company_companies_by_parent_id_type_associations_by_id(id, parent_id, client_id, company_company_type_association_company_type_association)

Put CompanyTypeAssociation

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.company_company_type_association_company_type_association import CompanyCompanyTypeAssociationCompanyTypeAssociation
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
    api_instance = connectwise_psa.CompanyCompanyTypeAssociationsApi(api_client)
    id = 56 # int | typeAssociationId
    parent_id = 56 # int | companyId
    client_id = 'client_id_example' # str | 
    company_company_type_association_company_type_association = connectwise_psa.CompanyCompanyTypeAssociationCompanyTypeAssociation() # CompanyCompanyTypeAssociationCompanyTypeAssociation | companyTypeAssociation

    try:
        # Put CompanyTypeAssociation
        api_response = api_instance.put_company_companies_by_parent_id_type_associations_by_id(id, parent_id, client_id, company_company_type_association_company_type_association)
        print("The response of CompanyCompanyTypeAssociationsApi->put_company_companies_by_parent_id_type_associations_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompanyCompanyTypeAssociationsApi->put_company_companies_by_parent_id_type_associations_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| typeAssociationId | 
 **parent_id** | **int**| companyId | 
 **client_id** | **str**|  | 
 **company_company_type_association_company_type_association** | [**CompanyCompanyTypeAssociationCompanyTypeAssociation**](CompanyCompanyTypeAssociationCompanyTypeAssociation.md)| companyTypeAssociation | 

### Return type

[**CompanyCompanyTypeAssociationCompanyTypeAssociation**](CompanyCompanyTypeAssociationCompanyTypeAssociation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | CompanyTypeAssociation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

