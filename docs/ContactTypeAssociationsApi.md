# connectwise_psa.ContactTypeAssociationsApi

All URIs are relative to *https://aus-api.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_company_contact_type_associations_by_id**](ContactTypeAssociationsApi.md#delete_company_contact_type_associations_by_id) | **DELETE** /company/contactTypeAssociations/{id} | Delete ContactTypeAssociation
[**get_company_contact_type_associations**](ContactTypeAssociationsApi.md#get_company_contact_type_associations) | **GET** /company/contactTypeAssociations | Get List of ContactTypeAssociation
[**get_company_contact_type_associations_by_id**](ContactTypeAssociationsApi.md#get_company_contact_type_associations_by_id) | **GET** /company/contactTypeAssociations/{id} | Get ContactTypeAssociation
[**get_company_contact_type_associations_count**](ContactTypeAssociationsApi.md#get_company_contact_type_associations_count) | **GET** /company/contactTypeAssociations/count | Get Count of ContactTypeAssociation
[**patch_company_contact_type_associations_by_id**](ContactTypeAssociationsApi.md#patch_company_contact_type_associations_by_id) | **PATCH** /company/contactTypeAssociations/{id} | Patch ContactTypeAssociation
[**post_company_contact_type_associations**](ContactTypeAssociationsApi.md#post_company_contact_type_associations) | **POST** /company/contactTypeAssociations | Post ContactTypeAssociation
[**put_company_contact_type_associations_by_id**](ContactTypeAssociationsApi.md#put_company_contact_type_associations_by_id) | **PUT** /company/contactTypeAssociations/{id} | Put ContactTypeAssociation


# **delete_company_contact_type_associations_by_id**
> delete_company_contact_type_associations_by_id(id, client_id)

Delete ContactTypeAssociation

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
    api_instance = connectwise_psa.ContactTypeAssociationsApi(api_client)
    id = 56 # int | contactTypeAssociationId
    client_id = 'client_id_example' # str | 

    try:
        # Delete ContactTypeAssociation
        api_instance.delete_company_contact_type_associations_by_id(id, client_id)
    except Exception as e:
        print("Exception when calling ContactTypeAssociationsApi->delete_company_contact_type_associations_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| contactTypeAssociationId | 
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

# **get_company_contact_type_associations**
> List[CompanyContactTypeAssociation] get_company_contact_type_associations(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of ContactTypeAssociation

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.company_contact_type_association import CompanyContactTypeAssociation
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
    api_instance = connectwise_psa.ContactTypeAssociationsApi(api_client)
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
        # Get List of ContactTypeAssociation
        api_response = api_instance.get_company_contact_type_associations(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of ContactTypeAssociationsApi->get_company_contact_type_associations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactTypeAssociationsApi->get_company_contact_type_associations: %s\n" % e)
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

[**List[CompanyContactTypeAssociation]**](CompanyContactTypeAssociation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of ContactTypeAssociation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_company_contact_type_associations_by_id**
> CompanyContactTypeAssociation get_company_contact_type_associations_by_id(id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get ContactTypeAssociation

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.company_contact_type_association import CompanyContactTypeAssociation
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
    api_instance = connectwise_psa.ContactTypeAssociationsApi(api_client)
    id = 56 # int | contactTypeAssociationId
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
        # Get ContactTypeAssociation
        api_response = api_instance.get_company_contact_type_associations_by_id(id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of ContactTypeAssociationsApi->get_company_contact_type_associations_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactTypeAssociationsApi->get_company_contact_type_associations_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| contactTypeAssociationId | 
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

[**CompanyContactTypeAssociation**](CompanyContactTypeAssociation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ContactTypeAssociation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_company_contact_type_associations_count**
> Count get_company_contact_type_associations_count(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Count of ContactTypeAssociation

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
    api_instance = connectwise_psa.ContactTypeAssociationsApi(api_client)
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
        # Get Count of ContactTypeAssociation
        api_response = api_instance.get_company_contact_type_associations_count(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of ContactTypeAssociationsApi->get_company_contact_type_associations_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactTypeAssociationsApi->get_company_contact_type_associations_count: %s\n" % e)
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

# **patch_company_contact_type_associations_by_id**
> CompanyContactTypeAssociation patch_company_contact_type_associations_by_id(id, client_id, patch_operation)

Patch ContactTypeAssociation

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.company_contact_type_association import CompanyContactTypeAssociation
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
    api_instance = connectwise_psa.ContactTypeAssociationsApi(api_client)
    id = 56 # int | contactTypeAssociationId
    client_id = 'client_id_example' # str | 
    patch_operation = [connectwise_psa.PatchOperation()] # List[PatchOperation] | List of PatchOperation

    try:
        # Patch ContactTypeAssociation
        api_response = api_instance.patch_company_contact_type_associations_by_id(id, client_id, patch_operation)
        print("The response of ContactTypeAssociationsApi->patch_company_contact_type_associations_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactTypeAssociationsApi->patch_company_contact_type_associations_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| contactTypeAssociationId | 
 **client_id** | **str**|  | 
 **patch_operation** | [**List[PatchOperation]**](PatchOperation.md)| List of PatchOperation | 

### Return type

[**CompanyContactTypeAssociation**](CompanyContactTypeAssociation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ContactTypeAssociation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_company_contact_type_associations**
> CompanyContactTypeAssociation post_company_contact_type_associations(client_id, company_contact_type_association)

Post ContactTypeAssociation

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.company_contact_type_association import CompanyContactTypeAssociation
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
    api_instance = connectwise_psa.ContactTypeAssociationsApi(api_client)
    client_id = 'client_id_example' # str | 
    company_contact_type_association = connectwise_psa.CompanyContactTypeAssociation() # CompanyContactTypeAssociation | contactTypeAssociation

    try:
        # Post ContactTypeAssociation
        api_response = api_instance.post_company_contact_type_associations(client_id, company_contact_type_association)
        print("The response of ContactTypeAssociationsApi->post_company_contact_type_associations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactTypeAssociationsApi->post_company_contact_type_associations: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**|  | 
 **company_contact_type_association** | [**CompanyContactTypeAssociation**](CompanyContactTypeAssociation.md)| contactTypeAssociation | 

### Return type

[**CompanyContactTypeAssociation**](CompanyContactTypeAssociation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | ContactTypeAssociation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_company_contact_type_associations_by_id**
> CompanyContactTypeAssociation put_company_contact_type_associations_by_id(id, client_id, company_contact_type_association)

Put ContactTypeAssociation

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.company_contact_type_association import CompanyContactTypeAssociation
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
    api_instance = connectwise_psa.ContactTypeAssociationsApi(api_client)
    id = 56 # int | contactTypeAssociationId
    client_id = 'client_id_example' # str | 
    company_contact_type_association = connectwise_psa.CompanyContactTypeAssociation() # CompanyContactTypeAssociation | contactTypeAssociation

    try:
        # Put ContactTypeAssociation
        api_response = api_instance.put_company_contact_type_associations_by_id(id, client_id, company_contact_type_association)
        print("The response of ContactTypeAssociationsApi->put_company_contact_type_associations_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactTypeAssociationsApi->put_company_contact_type_associations_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| contactTypeAssociationId | 
 **client_id** | **str**|  | 
 **company_contact_type_association** | [**CompanyContactTypeAssociation**](CompanyContactTypeAssociation.md)| contactTypeAssociation | 

### Return type

[**CompanyContactTypeAssociation**](CompanyContactTypeAssociation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ContactTypeAssociation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

