# connectwise_psa.OpportunityContactsApi

All URIs are relative to *https://aus-api.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_sales_opportunities_by_parent_id_contacts_by_id**](OpportunityContactsApi.md#delete_sales_opportunities_by_parent_id_contacts_by_id) | **DELETE** /sales/opportunities/{parentId}/contacts/{id} | Delete OpportunityContact
[**get_sales_opportunities_by_parent_id_contacts**](OpportunityContactsApi.md#get_sales_opportunities_by_parent_id_contacts) | **GET** /sales/opportunities/{parentId}/contacts | Get List of OpportunityContact
[**get_sales_opportunities_by_parent_id_contacts_by_id**](OpportunityContactsApi.md#get_sales_opportunities_by_parent_id_contacts_by_id) | **GET** /sales/opportunities/{parentId}/contacts/{id} | Get OpportunityContact
[**get_sales_opportunities_by_parent_id_contacts_count**](OpportunityContactsApi.md#get_sales_opportunities_by_parent_id_contacts_count) | **GET** /sales/opportunities/{parentId}/contacts/count | Get Count of OpportunityContact
[**patch_sales_opportunities_by_parent_id_contacts_by_id**](OpportunityContactsApi.md#patch_sales_opportunities_by_parent_id_contacts_by_id) | **PATCH** /sales/opportunities/{parentId}/contacts/{id} | Patch OpportunityContact
[**post_sales_opportunities_by_parent_id_contacts**](OpportunityContactsApi.md#post_sales_opportunities_by_parent_id_contacts) | **POST** /sales/opportunities/{parentId}/contacts | Post OpportunityContact
[**put_sales_opportunities_by_parent_id_contacts_by_id**](OpportunityContactsApi.md#put_sales_opportunities_by_parent_id_contacts_by_id) | **PUT** /sales/opportunities/{parentId}/contacts/{id} | Put OpportunityContact


# **delete_sales_opportunities_by_parent_id_contacts_by_id**
> delete_sales_opportunities_by_parent_id_contacts_by_id(id, parent_id, client_id)

Delete OpportunityContact

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
    api_instance = connectwise_psa.OpportunityContactsApi(api_client)
    id = 56 # int | contactId
    parent_id = 56 # int | opportunityId
    client_id = 'client_id_example' # str | 

    try:
        # Delete OpportunityContact
        api_instance.delete_sales_opportunities_by_parent_id_contacts_by_id(id, parent_id, client_id)
    except Exception as e:
        print("Exception when calling OpportunityContactsApi->delete_sales_opportunities_by_parent_id_contacts_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| contactId | 
 **parent_id** | **int**| opportunityId | 
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

# **get_sales_opportunities_by_parent_id_contacts**
> List[OpportunityContact] get_sales_opportunities_by_parent_id_contacts(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of OpportunityContact

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.opportunity_contact import OpportunityContact
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
    api_instance = connectwise_psa.OpportunityContactsApi(api_client)
    parent_id = 56 # int | opportunityId
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
        # Get List of OpportunityContact
        api_response = api_instance.get_sales_opportunities_by_parent_id_contacts(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of OpportunityContactsApi->get_sales_opportunities_by_parent_id_contacts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpportunityContactsApi->get_sales_opportunities_by_parent_id_contacts: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| opportunityId | 
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

[**List[OpportunityContact]**](OpportunityContact.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of OpportunityContact |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sales_opportunities_by_parent_id_contacts_by_id**
> OpportunityContact get_sales_opportunities_by_parent_id_contacts_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get OpportunityContact

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.opportunity_contact import OpportunityContact
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
    api_instance = connectwise_psa.OpportunityContactsApi(api_client)
    id = 56 # int | contactId
    parent_id = 56 # int | opportunityId
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
        # Get OpportunityContact
        api_response = api_instance.get_sales_opportunities_by_parent_id_contacts_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of OpportunityContactsApi->get_sales_opportunities_by_parent_id_contacts_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpportunityContactsApi->get_sales_opportunities_by_parent_id_contacts_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| contactId | 
 **parent_id** | **int**| opportunityId | 
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

[**OpportunityContact**](OpportunityContact.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OpportunityContact |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sales_opportunities_by_parent_id_contacts_count**
> Count get_sales_opportunities_by_parent_id_contacts_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Count of OpportunityContact

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
    api_instance = connectwise_psa.OpportunityContactsApi(api_client)
    parent_id = 56 # int | opportunityId
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
        # Get Count of OpportunityContact
        api_response = api_instance.get_sales_opportunities_by_parent_id_contacts_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of OpportunityContactsApi->get_sales_opportunities_by_parent_id_contacts_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpportunityContactsApi->get_sales_opportunities_by_parent_id_contacts_count: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| opportunityId | 
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

# **patch_sales_opportunities_by_parent_id_contacts_by_id**
> OpportunityContact patch_sales_opportunities_by_parent_id_contacts_by_id(id, parent_id, client_id, patch_operation)

Patch OpportunityContact

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.opportunity_contact import OpportunityContact
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
    api_instance = connectwise_psa.OpportunityContactsApi(api_client)
    id = 56 # int | contactId
    parent_id = 56 # int | opportunityId
    client_id = 'client_id_example' # str | 
    patch_operation = [connectwise_psa.PatchOperation()] # List[PatchOperation] | List of PatchOperation

    try:
        # Patch OpportunityContact
        api_response = api_instance.patch_sales_opportunities_by_parent_id_contacts_by_id(id, parent_id, client_id, patch_operation)
        print("The response of OpportunityContactsApi->patch_sales_opportunities_by_parent_id_contacts_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpportunityContactsApi->patch_sales_opportunities_by_parent_id_contacts_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| contactId | 
 **parent_id** | **int**| opportunityId | 
 **client_id** | **str**|  | 
 **patch_operation** | [**List[PatchOperation]**](PatchOperation.md)| List of PatchOperation | 

### Return type

[**OpportunityContact**](OpportunityContact.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OpportunityContact |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_sales_opportunities_by_parent_id_contacts**
> OpportunityContact post_sales_opportunities_by_parent_id_contacts(parent_id, client_id, opportunity_contact)

Post OpportunityContact

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.opportunity_contact import OpportunityContact
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
    api_instance = connectwise_psa.OpportunityContactsApi(api_client)
    parent_id = 56 # int | opportunityId
    client_id = 'client_id_example' # str | 
    opportunity_contact = connectwise_psa.OpportunityContact() # OpportunityContact | opportunityContact

    try:
        # Post OpportunityContact
        api_response = api_instance.post_sales_opportunities_by_parent_id_contacts(parent_id, client_id, opportunity_contact)
        print("The response of OpportunityContactsApi->post_sales_opportunities_by_parent_id_contacts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpportunityContactsApi->post_sales_opportunities_by_parent_id_contacts: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| opportunityId | 
 **client_id** | **str**|  | 
 **opportunity_contact** | [**OpportunityContact**](OpportunityContact.md)| opportunityContact | 

### Return type

[**OpportunityContact**](OpportunityContact.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | OpportunityContact |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_sales_opportunities_by_parent_id_contacts_by_id**
> OpportunityContact put_sales_opportunities_by_parent_id_contacts_by_id(id, parent_id, client_id, opportunity_contact)

Put OpportunityContact

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.opportunity_contact import OpportunityContact
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
    api_instance = connectwise_psa.OpportunityContactsApi(api_client)
    id = 56 # int | contactId
    parent_id = 56 # int | opportunityId
    client_id = 'client_id_example' # str | 
    opportunity_contact = connectwise_psa.OpportunityContact() # OpportunityContact | opportunityContact

    try:
        # Put OpportunityContact
        api_response = api_instance.put_sales_opportunities_by_parent_id_contacts_by_id(id, parent_id, client_id, opportunity_contact)
        print("The response of OpportunityContactsApi->put_sales_opportunities_by_parent_id_contacts_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpportunityContactsApi->put_sales_opportunities_by_parent_id_contacts_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| contactId | 
 **parent_id** | **int**| opportunityId | 
 **client_id** | **str**|  | 
 **opportunity_contact** | [**OpportunityContact**](OpportunityContact.md)| opportunityContact | 

### Return type

[**OpportunityContact**](OpportunityContact.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OpportunityContact |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

