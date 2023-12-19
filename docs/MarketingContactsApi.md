# connectwise_psa.MarketingContactsApi

All URIs are relative to *https://aus-api.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_marketing_groups_by_parent_id_contacts_by_id**](MarketingContactsApi.md#delete_marketing_groups_by_parent_id_contacts_by_id) | **DELETE** /marketing/groups/{parentId}/contacts/{id} | Delete MarketingContact
[**get_marketing_groups_by_parent_id_contacts**](MarketingContactsApi.md#get_marketing_groups_by_parent_id_contacts) | **GET** /marketing/groups/{parentId}/contacts | Get List of MarketingContact
[**get_marketing_groups_by_parent_id_contacts_by_id**](MarketingContactsApi.md#get_marketing_groups_by_parent_id_contacts_by_id) | **GET** /marketing/groups/{parentId}/contacts/{id} | Get MarketingContact
[**get_marketing_groups_by_parent_id_contacts_count**](MarketingContactsApi.md#get_marketing_groups_by_parent_id_contacts_count) | **GET** /marketing/groups/{parentId}/contacts/count | Get Count of MarketingContact
[**patch_marketing_groups_by_parent_id_contacts_by_id**](MarketingContactsApi.md#patch_marketing_groups_by_parent_id_contacts_by_id) | **PATCH** /marketing/groups/{parentId}/contacts/{id} | Patch MarketingContact
[**post_marketing_groups_by_parent_id_contacts**](MarketingContactsApi.md#post_marketing_groups_by_parent_id_contacts) | **POST** /marketing/groups/{parentId}/contacts | Post MarketingContact
[**put_marketing_groups_by_parent_id_contacts_by_id**](MarketingContactsApi.md#put_marketing_groups_by_parent_id_contacts_by_id) | **PUT** /marketing/groups/{parentId}/contacts/{id} | Put MarketingContact


# **delete_marketing_groups_by_parent_id_contacts_by_id**
> delete_marketing_groups_by_parent_id_contacts_by_id(id, parent_id, client_id)

Delete MarketingContact

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
    api_instance = connectwise_psa.MarketingContactsApi(api_client)
    id = 56 # int | contactId
    parent_id = 56 # int | groupId
    client_id = 'client_id_example' # str | 

    try:
        # Delete MarketingContact
        api_instance.delete_marketing_groups_by_parent_id_contacts_by_id(id, parent_id, client_id)
    except Exception as e:
        print("Exception when calling MarketingContactsApi->delete_marketing_groups_by_parent_id_contacts_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| contactId | 
 **parent_id** | **int**| groupId | 
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

# **get_marketing_groups_by_parent_id_contacts**
> List[MarketingContact] get_marketing_groups_by_parent_id_contacts(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of MarketingContact

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.marketing_contact import MarketingContact
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
    api_instance = connectwise_psa.MarketingContactsApi(api_client)
    parent_id = 56 # int | groupId
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
        # Get List of MarketingContact
        api_response = api_instance.get_marketing_groups_by_parent_id_contacts(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of MarketingContactsApi->get_marketing_groups_by_parent_id_contacts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketingContactsApi->get_marketing_groups_by_parent_id_contacts: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| groupId | 
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

[**List[MarketingContact]**](MarketingContact.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of MarketingContact |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_marketing_groups_by_parent_id_contacts_by_id**
> MarketingContact get_marketing_groups_by_parent_id_contacts_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get MarketingContact

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.marketing_contact import MarketingContact
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
    api_instance = connectwise_psa.MarketingContactsApi(api_client)
    id = 56 # int | contactId
    parent_id = 56 # int | groupId
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
        # Get MarketingContact
        api_response = api_instance.get_marketing_groups_by_parent_id_contacts_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of MarketingContactsApi->get_marketing_groups_by_parent_id_contacts_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketingContactsApi->get_marketing_groups_by_parent_id_contacts_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| contactId | 
 **parent_id** | **int**| groupId | 
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

[**MarketingContact**](MarketingContact.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | MarketingContact |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_marketing_groups_by_parent_id_contacts_count**
> Count get_marketing_groups_by_parent_id_contacts_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Count of MarketingContact

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
    api_instance = connectwise_psa.MarketingContactsApi(api_client)
    parent_id = 56 # int | groupId
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
        # Get Count of MarketingContact
        api_response = api_instance.get_marketing_groups_by_parent_id_contacts_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of MarketingContactsApi->get_marketing_groups_by_parent_id_contacts_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketingContactsApi->get_marketing_groups_by_parent_id_contacts_count: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| groupId | 
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

# **patch_marketing_groups_by_parent_id_contacts_by_id**
> MarketingContact patch_marketing_groups_by_parent_id_contacts_by_id(id, parent_id, client_id, patch_operation)

Patch MarketingContact

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.marketing_contact import MarketingContact
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
    api_instance = connectwise_psa.MarketingContactsApi(api_client)
    id = 56 # int | contactId
    parent_id = 56 # int | groupId
    client_id = 'client_id_example' # str | 
    patch_operation = [connectwise_psa.PatchOperation()] # List[PatchOperation] | List of PatchOperation

    try:
        # Patch MarketingContact
        api_response = api_instance.patch_marketing_groups_by_parent_id_contacts_by_id(id, parent_id, client_id, patch_operation)
        print("The response of MarketingContactsApi->patch_marketing_groups_by_parent_id_contacts_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketingContactsApi->patch_marketing_groups_by_parent_id_contacts_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| contactId | 
 **parent_id** | **int**| groupId | 
 **client_id** | **str**|  | 
 **patch_operation** | [**List[PatchOperation]**](PatchOperation.md)| List of PatchOperation | 

### Return type

[**MarketingContact**](MarketingContact.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | MarketingContact |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_marketing_groups_by_parent_id_contacts**
> MarketingContact post_marketing_groups_by_parent_id_contacts(parent_id, client_id, marketing_contact)

Post MarketingContact

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.marketing_contact import MarketingContact
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
    api_instance = connectwise_psa.MarketingContactsApi(api_client)
    parent_id = 56 # int | groupId
    client_id = 'client_id_example' # str | 
    marketing_contact = connectwise_psa.MarketingContact() # MarketingContact | marketingContact

    try:
        # Post MarketingContact
        api_response = api_instance.post_marketing_groups_by_parent_id_contacts(parent_id, client_id, marketing_contact)
        print("The response of MarketingContactsApi->post_marketing_groups_by_parent_id_contacts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketingContactsApi->post_marketing_groups_by_parent_id_contacts: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| groupId | 
 **client_id** | **str**|  | 
 **marketing_contact** | [**MarketingContact**](MarketingContact.md)| marketingContact | 

### Return type

[**MarketingContact**](MarketingContact.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | MarketingContact |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_marketing_groups_by_parent_id_contacts_by_id**
> MarketingContact put_marketing_groups_by_parent_id_contacts_by_id(id, parent_id, client_id, marketing_contact)

Put MarketingContact

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.marketing_contact import MarketingContact
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
    api_instance = connectwise_psa.MarketingContactsApi(api_client)
    id = 56 # int | contactId
    parent_id = 56 # int | groupId
    client_id = 'client_id_example' # str | 
    marketing_contact = connectwise_psa.MarketingContact() # MarketingContact | marketingContact

    try:
        # Put MarketingContact
        api_response = api_instance.put_marketing_groups_by_parent_id_contacts_by_id(id, parent_id, client_id, marketing_contact)
        print("The response of MarketingContactsApi->put_marketing_groups_by_parent_id_contacts_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketingContactsApi->put_marketing_groups_by_parent_id_contacts_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| contactId | 
 **parent_id** | **int**| groupId | 
 **client_id** | **str**|  | 
 **marketing_contact** | [**MarketingContact**](MarketingContact.md)| marketingContact | 

### Return type

[**MarketingContact**](MarketingContact.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | MarketingContact |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

