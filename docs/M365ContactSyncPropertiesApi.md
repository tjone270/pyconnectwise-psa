# connectwise_psa.M365ContactSyncPropertiesApi

All URIs are relative to *https://aus-api.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_company_m365contactsync_property**](M365ContactSyncPropertiesApi.md#delete_company_m365contactsync_property) | **DELETE** /company/m365contactsync/property/ | Delete M365ContactSyncProperty
[**get_company_m365contactsync_by_id_property**](M365ContactSyncPropertiesApi.md#get_company_m365contactsync_by_id_property) | **GET** /company/m365contactsync/{id}/property | Get M365ContactSyncProperties
[**get_company_m365contactsync_property_count**](M365ContactSyncPropertiesApi.md#get_company_m365contactsync_property_count) | **GET** /company/m365contactsync/property/count | Get Count of M365ContactSyncProperty
[**get_company_m365contactsync_property_excluded**](M365ContactSyncPropertiesApi.md#get_company_m365contactsync_property_excluded) | **GET** /company/m365contactsync/property/excluded | Get List of M365ContactSyncPropertiesExcluded
[**get_company_m365contactsync_property_included**](M365ContactSyncPropertiesApi.md#get_company_m365contactsync_property_included) | **GET** /company/m365contactsync/property/included | Get List of M365ContactSyncPropertiesIncluded
[**post_company_m365contactsync_property**](M365ContactSyncPropertiesApi.md#post_company_m365contactsync_property) | **POST** /company/m365contactsync/property | Create M365ContactSyncProperty


# **delete_company_m365contactsync_property**
> delete_company_m365contactsync_property(client_id)

Delete M365ContactSyncProperty

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
    api_instance = connectwise_psa.M365ContactSyncPropertiesApi(api_client)
    client_id = 'client_id_example' # str | 

    try:
        # Delete M365ContactSyncProperty
        api_instance.delete_company_m365contactsync_property(client_id)
    except Exception as e:
        print("Exception when calling M365ContactSyncPropertiesApi->delete_company_m365contactsync_property: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **get_company_m365contactsync_by_id_property**
> M365ContactSyncProperty get_company_m365contactsync_by_id_property(id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get M365ContactSyncProperties

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.m365_contact_sync_property import M365ContactSyncProperty
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
    api_instance = connectwise_psa.M365ContactSyncPropertiesApi(api_client)
    id = 56 # int | M365ContactSyncPropertyId
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
        # Get M365ContactSyncProperties
        api_response = api_instance.get_company_m365contactsync_by_id_property(id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of M365ContactSyncPropertiesApi->get_company_m365contactsync_by_id_property:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling M365ContactSyncPropertiesApi->get_company_m365contactsync_by_id_property: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| M365ContactSyncPropertyId | 
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

[**M365ContactSyncProperty**](M365ContactSyncProperty.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | M365ContactSyncProperty |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_company_m365contactsync_property_count**
> Count get_company_m365contactsync_property_count(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Count of M365ContactSyncProperty

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
    api_instance = connectwise_psa.M365ContactSyncPropertiesApi(api_client)
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
        # Get Count of M365ContactSyncProperty
        api_response = api_instance.get_company_m365contactsync_property_count(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of M365ContactSyncPropertiesApi->get_company_m365contactsync_property_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling M365ContactSyncPropertiesApi->get_company_m365contactsync_property_count: %s\n" % e)
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

# **get_company_m365contactsync_property_excluded**
> List[M365ContactSyncProperty] get_company_m365contactsync_property_excluded(client_id, id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of M365ContactSyncPropertiesExcluded

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.m365_contact_sync_property import M365ContactSyncProperty
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
    api_instance = connectwise_psa.M365ContactSyncPropertiesApi(api_client)
    client_id = 'client_id_example' # str | 
    id = 56 # int | companyRecId
    conditions = 'conditions_example' # str |  (optional)
    child_conditions = 'child_conditions_example' # str |  (optional)
    custom_field_conditions = 'custom_field_conditions_example' # str |  (optional)
    order_by = 'order_by_example' # str |  (optional)
    fields = 'fields_example' # str |  (optional)
    page = 56 # int |  (optional)
    page_size = 56 # int |  (optional)
    page_id = 56 # int |  (optional)

    try:
        # Get List of M365ContactSyncPropertiesExcluded
        api_response = api_instance.get_company_m365contactsync_property_excluded(client_id, id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of M365ContactSyncPropertiesApi->get_company_m365contactsync_property_excluded:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling M365ContactSyncPropertiesApi->get_company_m365contactsync_property_excluded: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**|  | 
 **id** | **int**| companyRecId | 
 **conditions** | **str**|  | [optional] 
 **child_conditions** | **str**|  | [optional] 
 **custom_field_conditions** | **str**|  | [optional] 
 **order_by** | **str**|  | [optional] 
 **fields** | **str**|  | [optional] 
 **page** | **int**|  | [optional] 
 **page_size** | **int**|  | [optional] 
 **page_id** | **int**|  | [optional] 

### Return type

[**List[M365ContactSyncProperty]**](M365ContactSyncProperty.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of m365ContactSyncProperties |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_company_m365contactsync_property_included**
> List[M365ContactSyncProperty] get_company_m365contactsync_property_included(client_id, id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of M365ContactSyncPropertiesIncluded

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.m365_contact_sync_property import M365ContactSyncProperty
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
    api_instance = connectwise_psa.M365ContactSyncPropertiesApi(api_client)
    client_id = 'client_id_example' # str | 
    id = 56 # int | companyRecId
    conditions = 'conditions_example' # str |  (optional)
    child_conditions = 'child_conditions_example' # str |  (optional)
    custom_field_conditions = 'custom_field_conditions_example' # str |  (optional)
    order_by = 'order_by_example' # str |  (optional)
    fields = 'fields_example' # str |  (optional)
    page = 56 # int |  (optional)
    page_size = 56 # int |  (optional)
    page_id = 56 # int |  (optional)

    try:
        # Get List of M365ContactSyncPropertiesIncluded
        api_response = api_instance.get_company_m365contactsync_property_included(client_id, id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of M365ContactSyncPropertiesApi->get_company_m365contactsync_property_included:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling M365ContactSyncPropertiesApi->get_company_m365contactsync_property_included: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**|  | 
 **id** | **int**| companyRecId | 
 **conditions** | **str**|  | [optional] 
 **child_conditions** | **str**|  | [optional] 
 **custom_field_conditions** | **str**|  | [optional] 
 **order_by** | **str**|  | [optional] 
 **fields** | **str**|  | [optional] 
 **page** | **int**|  | [optional] 
 **page_size** | **int**|  | [optional] 
 **page_id** | **int**|  | [optional] 

### Return type

[**List[M365ContactSyncProperty]**](M365ContactSyncProperty.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of m365ContactSyncProperties |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_company_m365contactsync_property**
> M365ContactSyncProperty post_company_m365contactsync_property(client_id, m365_contact_sync_property)

Create M365ContactSyncProperty

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.m365_contact_sync_property import M365ContactSyncProperty
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
    api_instance = connectwise_psa.M365ContactSyncPropertiesApi(api_client)
    client_id = 'client_id_example' # str | 
    m365_contact_sync_property = connectwise_psa.M365ContactSyncProperty() # M365ContactSyncProperty | country

    try:
        # Create M365ContactSyncProperty
        api_response = api_instance.post_company_m365contactsync_property(client_id, m365_contact_sync_property)
        print("The response of M365ContactSyncPropertiesApi->post_company_m365contactsync_property:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling M365ContactSyncPropertiesApi->post_company_m365contactsync_property: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**|  | 
 **m365_contact_sync_property** | [**M365ContactSyncProperty**](M365ContactSyncProperty.md)| country | 

### Return type

[**M365ContactSyncProperty**](M365ContactSyncProperty.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Country |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

