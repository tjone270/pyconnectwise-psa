# connectwise_psa.CompanySitesApi

All URIs are relative to *https://api-aus.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_company_companies_by_parent_id_sites_by_id**](CompanySitesApi.md#delete_company_companies_by_parent_id_sites_by_id) | **DELETE** /company/companies/{parentId}/sites/{id} | Delete CompanySite
[**get_company_companies_by_parent_id_sites**](CompanySitesApi.md#get_company_companies_by_parent_id_sites) | **GET** /company/companies/{parentId}/sites | Get List of CompanySite
[**get_company_companies_by_parent_id_sites_by_id**](CompanySitesApi.md#get_company_companies_by_parent_id_sites_by_id) | **GET** /company/companies/{parentId}/sites/{id} | Get CompanySite
[**get_company_companies_by_parent_id_sites_by_id_usages**](CompanySitesApi.md#get_company_companies_by_parent_id_sites_by_id_usages) | **GET** /company/companies/{parentId}/sites/{id}/usages | Get List of Usage Count
[**get_company_companies_by_parent_id_sites_by_id_usages_list**](CompanySitesApi.md#get_company_companies_by_parent_id_sites_by_id_usages_list) | **GET** /company/companies/{parentId}/sites/{id}/usages/list | Get List of Usage
[**get_company_companies_by_parent_id_sites_count**](CompanySitesApi.md#get_company_companies_by_parent_id_sites_count) | **GET** /company/companies/{parentId}/sites/count | Get Count of CompanySite
[**patch_company_companies_by_parent_id_sites_by_id**](CompanySitesApi.md#patch_company_companies_by_parent_id_sites_by_id) | **PATCH** /company/companies/{parentId}/sites/{id} | Patch CompanySite
[**post_company_companies_by_parent_id_sites**](CompanySitesApi.md#post_company_companies_by_parent_id_sites) | **POST** /company/companies/{parentId}/sites | Post CompanySite
[**put_company_companies_by_parent_id_sites_by_id**](CompanySitesApi.md#put_company_companies_by_parent_id_sites_by_id) | **PUT** /company/companies/{parentId}/sites/{id} | Put CompanySite


# **delete_company_companies_by_parent_id_sites_by_id**
> delete_company_companies_by_parent_id_sites_by_id(id, parent_id, client_id)

Delete CompanySite

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
    api_instance = connectwise_psa.CompanySitesApi(api_client)
    id = 56 # int | siteId
    parent_id = 56 # int | companyId
    client_id = 'client_id_example' # str | 

    try:
        # Delete CompanySite
        api_instance.delete_company_companies_by_parent_id_sites_by_id(id, parent_id, client_id)
    except Exception as e:
        print("Exception when calling CompanySitesApi->delete_company_companies_by_parent_id_sites_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| siteId | 
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

# **get_company_companies_by_parent_id_sites**
> List[CompanySite] get_company_companies_by_parent_id_sites(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of CompanySite

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.company_site import CompanySite
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
    api_instance = connectwise_psa.CompanySitesApi(api_client)
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
        # Get List of CompanySite
        api_response = api_instance.get_company_companies_by_parent_id_sites(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of CompanySitesApi->get_company_companies_by_parent_id_sites:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompanySitesApi->get_company_companies_by_parent_id_sites: %s\n" % e)
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

[**List[CompanySite]**](CompanySite.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of CompanySite |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_company_companies_by_parent_id_sites_by_id**
> CompanySite get_company_companies_by_parent_id_sites_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get CompanySite

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.company_site import CompanySite
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
    api_instance = connectwise_psa.CompanySitesApi(api_client)
    id = 56 # int | siteId
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
        # Get CompanySite
        api_response = api_instance.get_company_companies_by_parent_id_sites_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of CompanySitesApi->get_company_companies_by_parent_id_sites_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompanySitesApi->get_company_companies_by_parent_id_sites_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| siteId | 
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

[**CompanySite**](CompanySite.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | CompanySite |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_company_companies_by_parent_id_sites_by_id_usages**
> List[Usage] get_company_companies_by_parent_id_sites_by_id_usages(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of Usage Count

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.usage import Usage
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
    api_instance = connectwise_psa.CompanySitesApi(api_client)
    id = 56 # int | siteId
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
        # Get List of Usage Count
        api_response = api_instance.get_company_companies_by_parent_id_sites_by_id_usages(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of CompanySitesApi->get_company_companies_by_parent_id_sites_by_id_usages:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompanySitesApi->get_company_companies_by_parent_id_sites_by_id_usages: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| siteId | 
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

[**List[Usage]**](Usage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of Usage |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_company_companies_by_parent_id_sites_by_id_usages_list**
> List[Usage] get_company_companies_by_parent_id_sites_by_id_usages_list(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of Usage

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.usage import Usage
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
    api_instance = connectwise_psa.CompanySitesApi(api_client)
    id = 56 # int | siteId
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
        # Get List of Usage
        api_response = api_instance.get_company_companies_by_parent_id_sites_by_id_usages_list(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of CompanySitesApi->get_company_companies_by_parent_id_sites_by_id_usages_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompanySitesApi->get_company_companies_by_parent_id_sites_by_id_usages_list: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| siteId | 
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

[**List[Usage]**](Usage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of Usage |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_company_companies_by_parent_id_sites_count**
> Count get_company_companies_by_parent_id_sites_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Count of CompanySite

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
    api_instance = connectwise_psa.CompanySitesApi(api_client)
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
        # Get Count of CompanySite
        api_response = api_instance.get_company_companies_by_parent_id_sites_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of CompanySitesApi->get_company_companies_by_parent_id_sites_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompanySitesApi->get_company_companies_by_parent_id_sites_count: %s\n" % e)
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

# **patch_company_companies_by_parent_id_sites_by_id**
> CompanySite patch_company_companies_by_parent_id_sites_by_id(id, parent_id, client_id, patch_operation)

Patch CompanySite

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.company_site import CompanySite
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
    api_instance = connectwise_psa.CompanySitesApi(api_client)
    id = 56 # int | siteId
    parent_id = 56 # int | companyId
    client_id = 'client_id_example' # str | 
    patch_operation = [connectwise_psa.PatchOperation()] # List[PatchOperation] | List of PatchOperation

    try:
        # Patch CompanySite
        api_response = api_instance.patch_company_companies_by_parent_id_sites_by_id(id, parent_id, client_id, patch_operation)
        print("The response of CompanySitesApi->patch_company_companies_by_parent_id_sites_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompanySitesApi->patch_company_companies_by_parent_id_sites_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| siteId | 
 **parent_id** | **int**| companyId | 
 **client_id** | **str**|  | 
 **patch_operation** | [**List[PatchOperation]**](PatchOperation.md)| List of PatchOperation | 

### Return type

[**CompanySite**](CompanySite.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | CompanySite |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_company_companies_by_parent_id_sites**
> CompanySite post_company_companies_by_parent_id_sites(parent_id, client_id, company_site)

Post CompanySite

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.company_site import CompanySite
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
    api_instance = connectwise_psa.CompanySitesApi(api_client)
    parent_id = 56 # int | companyId
    client_id = 'client_id_example' # str | 
    company_site = connectwise_psa.CompanySite() # CompanySite | site

    try:
        # Post CompanySite
        api_response = api_instance.post_company_companies_by_parent_id_sites(parent_id, client_id, company_site)
        print("The response of CompanySitesApi->post_company_companies_by_parent_id_sites:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompanySitesApi->post_company_companies_by_parent_id_sites: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| companyId | 
 **client_id** | **str**|  | 
 **company_site** | [**CompanySite**](CompanySite.md)| site | 

### Return type

[**CompanySite**](CompanySite.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | CompanySite |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_company_companies_by_parent_id_sites_by_id**
> CompanySite put_company_companies_by_parent_id_sites_by_id(id, parent_id, client_id, company_site)

Put CompanySite

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.company_site import CompanySite
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
    api_instance = connectwise_psa.CompanySitesApi(api_client)
    id = 56 # int | siteId
    parent_id = 56 # int | companyId
    client_id = 'client_id_example' # str | 
    company_site = connectwise_psa.CompanySite() # CompanySite | site

    try:
        # Put CompanySite
        api_response = api_instance.put_company_companies_by_parent_id_sites_by_id(id, parent_id, client_id, company_site)
        print("The response of CompanySitesApi->put_company_companies_by_parent_id_sites_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompanySitesApi->put_company_companies_by_parent_id_sites_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| siteId | 
 **parent_id** | **int**| companyId | 
 **client_id** | **str**|  | 
 **company_site** | [**CompanySite**](CompanySite.md)| site | 

### Return type

[**CompanySite**](CompanySite.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | CompanySite |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

