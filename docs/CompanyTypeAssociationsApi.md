# connectwise_psa.CompanyTypeAssociationsApi

All URIs are relative to *https://aus-api.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_company_company_type_associations_by_id**](CompanyTypeAssociationsApi.md#delete_company_company_type_associations_by_id) | **DELETE** /company/companyTypeAssociations/{id} | Delete CompanyTypeAssociation
[**get_company_company_type_associations**](CompanyTypeAssociationsApi.md#get_company_company_type_associations) | **GET** /company/companyTypeAssociations | Get List of CompanyTypeAssociation
[**get_company_company_type_associations_by_id**](CompanyTypeAssociationsApi.md#get_company_company_type_associations_by_id) | **GET** /company/companyTypeAssociations/{id} | Get CompanyTypeAssociation
[**get_company_company_type_associations_count**](CompanyTypeAssociationsApi.md#get_company_company_type_associations_count) | **GET** /company/companyTypeAssociations/count | Get Count of CompanyTypeAssociation
[**patch_company_company_type_associations_by_id**](CompanyTypeAssociationsApi.md#patch_company_company_type_associations_by_id) | **PATCH** /company/companyTypeAssociations/{id} | Patch CompanyTypeAssociation
[**post_company_company_type_associations**](CompanyTypeAssociationsApi.md#post_company_company_type_associations) | **POST** /company/companyTypeAssociations | Post CompanyTypeAssociation
[**put_company_company_type_associations_by_id**](CompanyTypeAssociationsApi.md#put_company_company_type_associations_by_id) | **PUT** /company/companyTypeAssociations/{id} | Put CompanyTypeAssociation


# **delete_company_company_type_associations_by_id**
> delete_company_company_type_associations_by_id(id, client_id)

Delete CompanyTypeAssociation

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
    api_instance = connectwise_psa.CompanyTypeAssociationsApi(api_client)
    id = 56 # int | companyTypeAssociationId
    client_id = 'client_id_example' # str | 

    try:
        # Delete CompanyTypeAssociation
        api_instance.delete_company_company_type_associations_by_id(id, client_id)
    except Exception as e:
        print("Exception when calling CompanyTypeAssociationsApi->delete_company_company_type_associations_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| companyTypeAssociationId | 
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

# **get_company_company_type_associations**
> List[CompanyCompanyTypeAssociation] get_company_company_type_associations(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of CompanyTypeAssociation

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.company_company_type_association import CompanyCompanyTypeAssociation
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
    api_instance = connectwise_psa.CompanyTypeAssociationsApi(api_client)
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
        api_response = api_instance.get_company_company_type_associations(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of CompanyTypeAssociationsApi->get_company_company_type_associations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompanyTypeAssociationsApi->get_company_company_type_associations: %s\n" % e)
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

[**List[CompanyCompanyTypeAssociation]**](CompanyCompanyTypeAssociation.md)

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

# **get_company_company_type_associations_by_id**
> CompanyCompanyTypeAssociation get_company_company_type_associations_by_id(id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get CompanyTypeAssociation

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.company_company_type_association import CompanyCompanyTypeAssociation
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
    api_instance = connectwise_psa.CompanyTypeAssociationsApi(api_client)
    id = 56 # int | companyTypeAssociationId
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
        api_response = api_instance.get_company_company_type_associations_by_id(id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of CompanyTypeAssociationsApi->get_company_company_type_associations_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompanyTypeAssociationsApi->get_company_company_type_associations_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| companyTypeAssociationId | 
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

[**CompanyCompanyTypeAssociation**](CompanyCompanyTypeAssociation.md)

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

# **get_company_company_type_associations_count**
> Count get_company_company_type_associations_count(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Count of CompanyTypeAssociation

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
    api_instance = connectwise_psa.CompanyTypeAssociationsApi(api_client)
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
        api_response = api_instance.get_company_company_type_associations_count(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of CompanyTypeAssociationsApi->get_company_company_type_associations_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompanyTypeAssociationsApi->get_company_company_type_associations_count: %s\n" % e)
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

# **patch_company_company_type_associations_by_id**
> CompanyCompanyTypeAssociation patch_company_company_type_associations_by_id(id, client_id, patch_operation)

Patch CompanyTypeAssociation

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.company_company_type_association import CompanyCompanyTypeAssociation
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
    api_instance = connectwise_psa.CompanyTypeAssociationsApi(api_client)
    id = 56 # int | companyTypeAssociationId
    client_id = 'client_id_example' # str | 
    patch_operation = [connectwise_psa.PatchOperation()] # List[PatchOperation] | List of PatchOperation

    try:
        # Patch CompanyTypeAssociation
        api_response = api_instance.patch_company_company_type_associations_by_id(id, client_id, patch_operation)
        print("The response of CompanyTypeAssociationsApi->patch_company_company_type_associations_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompanyTypeAssociationsApi->patch_company_company_type_associations_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| companyTypeAssociationId | 
 **client_id** | **str**|  | 
 **patch_operation** | [**List[PatchOperation]**](PatchOperation.md)| List of PatchOperation | 

### Return type

[**CompanyCompanyTypeAssociation**](CompanyCompanyTypeAssociation.md)

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

# **post_company_company_type_associations**
> CompanyCompanyTypeAssociation post_company_company_type_associations(client_id, company_company_type_association)

Post CompanyTypeAssociation

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.company_company_type_association import CompanyCompanyTypeAssociation
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
    api_instance = connectwise_psa.CompanyTypeAssociationsApi(api_client)
    client_id = 'client_id_example' # str | 
    company_company_type_association = connectwise_psa.CompanyCompanyTypeAssociation() # CompanyCompanyTypeAssociation | companyTypeAssociation

    try:
        # Post CompanyTypeAssociation
        api_response = api_instance.post_company_company_type_associations(client_id, company_company_type_association)
        print("The response of CompanyTypeAssociationsApi->post_company_company_type_associations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompanyTypeAssociationsApi->post_company_company_type_associations: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**|  | 
 **company_company_type_association** | [**CompanyCompanyTypeAssociation**](CompanyCompanyTypeAssociation.md)| companyTypeAssociation | 

### Return type

[**CompanyCompanyTypeAssociation**](CompanyCompanyTypeAssociation.md)

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

# **put_company_company_type_associations_by_id**
> CompanyCompanyTypeAssociation put_company_company_type_associations_by_id(id, client_id, company_company_type_association)

Put CompanyTypeAssociation

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.company_company_type_association import CompanyCompanyTypeAssociation
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
    api_instance = connectwise_psa.CompanyTypeAssociationsApi(api_client)
    id = 56 # int | companyTypeAssociationId
    client_id = 'client_id_example' # str | 
    company_company_type_association = connectwise_psa.CompanyCompanyTypeAssociation() # CompanyCompanyTypeAssociation | companyTypeAssociation

    try:
        # Put CompanyTypeAssociation
        api_response = api_instance.put_company_company_type_associations_by_id(id, client_id, company_company_type_association)
        print("The response of CompanyTypeAssociationsApi->put_company_company_type_associations_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompanyTypeAssociationsApi->put_company_company_type_associations_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| companyTypeAssociationId | 
 **client_id** | **str**|  | 
 **company_company_type_association** | [**CompanyCompanyTypeAssociation**](CompanyCompanyTypeAssociation.md)| companyTypeAssociation | 

### Return type

[**CompanyCompanyTypeAssociation**](CompanyCompanyTypeAssociation.md)

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

