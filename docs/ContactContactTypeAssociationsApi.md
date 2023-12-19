# connectwise_psa.ContactContactTypeAssociationsApi

All URIs are relative to *https://api-aus.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_company_contacts_by_parent_id_type_associations_by_id**](ContactContactTypeAssociationsApi.md#delete_company_contacts_by_parent_id_type_associations_by_id) | **DELETE** /company/contacts/{parentId}/typeAssociations/{id} | Delete ContactTypeAssociation
[**get_company_contacts_by_parent_id_type_associations**](ContactContactTypeAssociationsApi.md#get_company_contacts_by_parent_id_type_associations) | **GET** /company/contacts/{parentId}/typeAssociations | Get List of ContactTypeAssociation
[**get_company_contacts_by_parent_id_type_associations_by_id**](ContactContactTypeAssociationsApi.md#get_company_contacts_by_parent_id_type_associations_by_id) | **GET** /company/contacts/{parentId}/typeAssociations/{id} | Get ContactTypeAssociation
[**get_company_contacts_by_parent_id_type_associations_count**](ContactContactTypeAssociationsApi.md#get_company_contacts_by_parent_id_type_associations_count) | **GET** /company/contacts/{parentId}/typeAssociations/count | Get Count of ContactTypeAssociation
[**patch_company_contacts_by_parent_id_type_associations_by_id**](ContactContactTypeAssociationsApi.md#patch_company_contacts_by_parent_id_type_associations_by_id) | **PATCH** /company/contacts/{parentId}/typeAssociations/{id} | Patch ContactTypeAssociation
[**post_company_contacts_by_parent_id_type_associations**](ContactContactTypeAssociationsApi.md#post_company_contacts_by_parent_id_type_associations) | **POST** /company/contacts/{parentId}/typeAssociations | Post ContactTypeAssociation
[**put_company_contacts_by_parent_id_type_associations_by_id**](ContactContactTypeAssociationsApi.md#put_company_contacts_by_parent_id_type_associations_by_id) | **PUT** /company/contacts/{parentId}/typeAssociations/{id} | Put ContactTypeAssociation


# **delete_company_contacts_by_parent_id_type_associations_by_id**
> delete_company_contacts_by_parent_id_type_associations_by_id(id, parent_id, client_id)

Delete ContactTypeAssociation

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
    api_instance = connectwise_psa.ContactContactTypeAssociationsApi(api_client)
    id = 56 # int | typeAssociationId
    parent_id = 56 # int | contactId
    client_id = 'client_id_example' # str | 

    try:
        # Delete ContactTypeAssociation
        api_instance.delete_company_contacts_by_parent_id_type_associations_by_id(id, parent_id, client_id)
    except Exception as e:
        print("Exception when calling ContactContactTypeAssociationsApi->delete_company_contacts_by_parent_id_type_associations_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| typeAssociationId | 
 **parent_id** | **int**| contactId | 
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

# **get_company_contacts_by_parent_id_type_associations**
> List[ContactContactTypeAssociationContactTypeAssociation] get_company_contacts_by_parent_id_type_associations(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of ContactTypeAssociation

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.contact_contact_type_association_contact_type_association import ContactContactTypeAssociationContactTypeAssociation
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
    api_instance = connectwise_psa.ContactContactTypeAssociationsApi(api_client)
    parent_id = 56 # int | contactId
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
        api_response = api_instance.get_company_contacts_by_parent_id_type_associations(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of ContactContactTypeAssociationsApi->get_company_contacts_by_parent_id_type_associations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactContactTypeAssociationsApi->get_company_contacts_by_parent_id_type_associations: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| contactId | 
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

[**List[ContactContactTypeAssociationContactTypeAssociation]**](ContactContactTypeAssociationContactTypeAssociation.md)

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

# **get_company_contacts_by_parent_id_type_associations_by_id**
> ContactContactTypeAssociationContactTypeAssociation get_company_contacts_by_parent_id_type_associations_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get ContactTypeAssociation

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.contact_contact_type_association_contact_type_association import ContactContactTypeAssociationContactTypeAssociation
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
    api_instance = connectwise_psa.ContactContactTypeAssociationsApi(api_client)
    id = 56 # int | typeAssociationId
    parent_id = 56 # int | contactId
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
        api_response = api_instance.get_company_contacts_by_parent_id_type_associations_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of ContactContactTypeAssociationsApi->get_company_contacts_by_parent_id_type_associations_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactContactTypeAssociationsApi->get_company_contacts_by_parent_id_type_associations_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| typeAssociationId | 
 **parent_id** | **int**| contactId | 
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

[**ContactContactTypeAssociationContactTypeAssociation**](ContactContactTypeAssociationContactTypeAssociation.md)

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

# **get_company_contacts_by_parent_id_type_associations_count**
> Count get_company_contacts_by_parent_id_type_associations_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Count of ContactTypeAssociation

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
    api_instance = connectwise_psa.ContactContactTypeAssociationsApi(api_client)
    parent_id = 56 # int | contactId
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
        api_response = api_instance.get_company_contacts_by_parent_id_type_associations_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of ContactContactTypeAssociationsApi->get_company_contacts_by_parent_id_type_associations_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactContactTypeAssociationsApi->get_company_contacts_by_parent_id_type_associations_count: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| contactId | 
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

# **patch_company_contacts_by_parent_id_type_associations_by_id**
> ContactContactTypeAssociationContactTypeAssociation patch_company_contacts_by_parent_id_type_associations_by_id(id, parent_id, client_id, patch_operation)

Patch ContactTypeAssociation

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.contact_contact_type_association_contact_type_association import ContactContactTypeAssociationContactTypeAssociation
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
    api_instance = connectwise_psa.ContactContactTypeAssociationsApi(api_client)
    id = 56 # int | typeAssociationId
    parent_id = 56 # int | contactId
    client_id = 'client_id_example' # str | 
    patch_operation = [connectwise_psa.PatchOperation()] # List[PatchOperation] | List of PatchOperation

    try:
        # Patch ContactTypeAssociation
        api_response = api_instance.patch_company_contacts_by_parent_id_type_associations_by_id(id, parent_id, client_id, patch_operation)
        print("The response of ContactContactTypeAssociationsApi->patch_company_contacts_by_parent_id_type_associations_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactContactTypeAssociationsApi->patch_company_contacts_by_parent_id_type_associations_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| typeAssociationId | 
 **parent_id** | **int**| contactId | 
 **client_id** | **str**|  | 
 **patch_operation** | [**List[PatchOperation]**](PatchOperation.md)| List of PatchOperation | 

### Return type

[**ContactContactTypeAssociationContactTypeAssociation**](ContactContactTypeAssociationContactTypeAssociation.md)

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

# **post_company_contacts_by_parent_id_type_associations**
> ContactContactTypeAssociationContactTypeAssociation post_company_contacts_by_parent_id_type_associations(parent_id, client_id, contact_contact_type_association_contact_type_association)

Post ContactTypeAssociation

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.contact_contact_type_association_contact_type_association import ContactContactTypeAssociationContactTypeAssociation
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
    api_instance = connectwise_psa.ContactContactTypeAssociationsApi(api_client)
    parent_id = 56 # int | contactId
    client_id = 'client_id_example' # str | 
    contact_contact_type_association_contact_type_association = connectwise_psa.ContactContactTypeAssociationContactTypeAssociation() # ContactContactTypeAssociationContactTypeAssociation | contactTypeAssociation

    try:
        # Post ContactTypeAssociation
        api_response = api_instance.post_company_contacts_by_parent_id_type_associations(parent_id, client_id, contact_contact_type_association_contact_type_association)
        print("The response of ContactContactTypeAssociationsApi->post_company_contacts_by_parent_id_type_associations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactContactTypeAssociationsApi->post_company_contacts_by_parent_id_type_associations: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| contactId | 
 **client_id** | **str**|  | 
 **contact_contact_type_association_contact_type_association** | [**ContactContactTypeAssociationContactTypeAssociation**](ContactContactTypeAssociationContactTypeAssociation.md)| contactTypeAssociation | 

### Return type

[**ContactContactTypeAssociationContactTypeAssociation**](ContactContactTypeAssociationContactTypeAssociation.md)

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

# **put_company_contacts_by_parent_id_type_associations_by_id**
> ContactContactTypeAssociationContactTypeAssociation put_company_contacts_by_parent_id_type_associations_by_id(id, parent_id, client_id, contact_contact_type_association_contact_type_association)

Put ContactTypeAssociation

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.contact_contact_type_association_contact_type_association import ContactContactTypeAssociationContactTypeAssociation
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
    api_instance = connectwise_psa.ContactContactTypeAssociationsApi(api_client)
    id = 56 # int | typeAssociationId
    parent_id = 56 # int | contactId
    client_id = 'client_id_example' # str | 
    contact_contact_type_association_contact_type_association = connectwise_psa.ContactContactTypeAssociationContactTypeAssociation() # ContactContactTypeAssociationContactTypeAssociation | contactTypeAssociation

    try:
        # Put ContactTypeAssociation
        api_response = api_instance.put_company_contacts_by_parent_id_type_associations_by_id(id, parent_id, client_id, contact_contact_type_association_contact_type_association)
        print("The response of ContactContactTypeAssociationsApi->put_company_contacts_by_parent_id_type_associations_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactContactTypeAssociationsApi->put_company_contacts_by_parent_id_type_associations_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| typeAssociationId | 
 **parent_id** | **int**| contactId | 
 **client_id** | **str**|  | 
 **contact_contact_type_association_contact_type_association** | [**ContactContactTypeAssociationContactTypeAssociation**](ContactContactTypeAssociationContactTypeAssociation.md)| contactTypeAssociation | 

### Return type

[**ContactContactTypeAssociationContactTypeAssociation**](ContactContactTypeAssociationContactTypeAssociation.md)

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

