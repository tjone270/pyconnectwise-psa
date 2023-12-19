# connectwise_psa.MarketingCompaniesApi

All URIs are relative to *https://api-aus.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_marketing_groups_by_parent_id_companies_by_id**](MarketingCompaniesApi.md#delete_marketing_groups_by_parent_id_companies_by_id) | **DELETE** /marketing/groups/{parentId}/companies/{id} | Delete MarketingCompany
[**get_marketing_groups_by_parent_id_companies**](MarketingCompaniesApi.md#get_marketing_groups_by_parent_id_companies) | **GET** /marketing/groups/{parentId}/companies | Get List of MarketingCompany
[**get_marketing_groups_by_parent_id_companies_by_id**](MarketingCompaniesApi.md#get_marketing_groups_by_parent_id_companies_by_id) | **GET** /marketing/groups/{parentId}/companies/{id} | Get MarketingCompany
[**get_marketing_groups_by_parent_id_companies_count**](MarketingCompaniesApi.md#get_marketing_groups_by_parent_id_companies_count) | **GET** /marketing/groups/{parentId}/companies/count | Get Count of MarketingCompany
[**patch_marketing_groups_by_parent_id_companies_by_id**](MarketingCompaniesApi.md#patch_marketing_groups_by_parent_id_companies_by_id) | **PATCH** /marketing/groups/{parentId}/companies/{id} | Patch MarketingCompany
[**post_marketing_groups_by_parent_id_companies**](MarketingCompaniesApi.md#post_marketing_groups_by_parent_id_companies) | **POST** /marketing/groups/{parentId}/companies | Post MarketingCompany
[**put_marketing_groups_by_parent_id_companies_by_id**](MarketingCompaniesApi.md#put_marketing_groups_by_parent_id_companies_by_id) | **PUT** /marketing/groups/{parentId}/companies/{id} | Put MarketingCompany


# **delete_marketing_groups_by_parent_id_companies_by_id**
> delete_marketing_groups_by_parent_id_companies_by_id(id, parent_id, client_id)

Delete MarketingCompany

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
    api_instance = connectwise_psa.MarketingCompaniesApi(api_client)
    id = 56 # int | companyId
    parent_id = 56 # int | groupId
    client_id = 'client_id_example' # str | 

    try:
        # Delete MarketingCompany
        api_instance.delete_marketing_groups_by_parent_id_companies_by_id(id, parent_id, client_id)
    except Exception as e:
        print("Exception when calling MarketingCompaniesApi->delete_marketing_groups_by_parent_id_companies_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| companyId | 
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

# **get_marketing_groups_by_parent_id_companies**
> List[MarketingCompany] get_marketing_groups_by_parent_id_companies(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of MarketingCompany

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.marketing_company import MarketingCompany
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
    api_instance = connectwise_psa.MarketingCompaniesApi(api_client)
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
        # Get List of MarketingCompany
        api_response = api_instance.get_marketing_groups_by_parent_id_companies(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of MarketingCompaniesApi->get_marketing_groups_by_parent_id_companies:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketingCompaniesApi->get_marketing_groups_by_parent_id_companies: %s\n" % e)
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

[**List[MarketingCompany]**](MarketingCompany.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of MarketingCompany |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_marketing_groups_by_parent_id_companies_by_id**
> MarketingCompany get_marketing_groups_by_parent_id_companies_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get MarketingCompany

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.marketing_company import MarketingCompany
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
    api_instance = connectwise_psa.MarketingCompaniesApi(api_client)
    id = 56 # int | companyId
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
        # Get MarketingCompany
        api_response = api_instance.get_marketing_groups_by_parent_id_companies_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of MarketingCompaniesApi->get_marketing_groups_by_parent_id_companies_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketingCompaniesApi->get_marketing_groups_by_parent_id_companies_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| companyId | 
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

[**MarketingCompany**](MarketingCompany.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | MarketingCompany |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_marketing_groups_by_parent_id_companies_count**
> Count get_marketing_groups_by_parent_id_companies_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Count of MarketingCompany

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
    api_instance = connectwise_psa.MarketingCompaniesApi(api_client)
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
        # Get Count of MarketingCompany
        api_response = api_instance.get_marketing_groups_by_parent_id_companies_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of MarketingCompaniesApi->get_marketing_groups_by_parent_id_companies_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketingCompaniesApi->get_marketing_groups_by_parent_id_companies_count: %s\n" % e)
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

# **patch_marketing_groups_by_parent_id_companies_by_id**
> MarketingCompany patch_marketing_groups_by_parent_id_companies_by_id(id, parent_id, client_id, patch_operation)

Patch MarketingCompany

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.marketing_company import MarketingCompany
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
    api_instance = connectwise_psa.MarketingCompaniesApi(api_client)
    id = 56 # int | companyId
    parent_id = 56 # int | groupId
    client_id = 'client_id_example' # str | 
    patch_operation = [connectwise_psa.PatchOperation()] # List[PatchOperation] | List of PatchOperation

    try:
        # Patch MarketingCompany
        api_response = api_instance.patch_marketing_groups_by_parent_id_companies_by_id(id, parent_id, client_id, patch_operation)
        print("The response of MarketingCompaniesApi->patch_marketing_groups_by_parent_id_companies_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketingCompaniesApi->patch_marketing_groups_by_parent_id_companies_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| companyId | 
 **parent_id** | **int**| groupId | 
 **client_id** | **str**|  | 
 **patch_operation** | [**List[PatchOperation]**](PatchOperation.md)| List of PatchOperation | 

### Return type

[**MarketingCompany**](MarketingCompany.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | MarketingCompany |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_marketing_groups_by_parent_id_companies**
> MarketingCompany post_marketing_groups_by_parent_id_companies(parent_id, client_id, marketing_company)

Post MarketingCompany

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.marketing_company import MarketingCompany
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
    api_instance = connectwise_psa.MarketingCompaniesApi(api_client)
    parent_id = 56 # int | groupId
    client_id = 'client_id_example' # str | 
    marketing_company = connectwise_psa.MarketingCompany() # MarketingCompany | marketingCompany

    try:
        # Post MarketingCompany
        api_response = api_instance.post_marketing_groups_by_parent_id_companies(parent_id, client_id, marketing_company)
        print("The response of MarketingCompaniesApi->post_marketing_groups_by_parent_id_companies:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketingCompaniesApi->post_marketing_groups_by_parent_id_companies: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| groupId | 
 **client_id** | **str**|  | 
 **marketing_company** | [**MarketingCompany**](MarketingCompany.md)| marketingCompany | 

### Return type

[**MarketingCompany**](MarketingCompany.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | MarketingCompany |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_marketing_groups_by_parent_id_companies_by_id**
> MarketingCompany put_marketing_groups_by_parent_id_companies_by_id(id, parent_id, client_id, marketing_company)

Put MarketingCompany

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.marketing_company import MarketingCompany
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
    api_instance = connectwise_psa.MarketingCompaniesApi(api_client)
    id = 56 # int | companyId
    parent_id = 56 # int | groupId
    client_id = 'client_id_example' # str | 
    marketing_company = connectwise_psa.MarketingCompany() # MarketingCompany | marketingCompany

    try:
        # Put MarketingCompany
        api_response = api_instance.put_marketing_groups_by_parent_id_companies_by_id(id, parent_id, client_id, marketing_company)
        print("The response of MarketingCompaniesApi->put_marketing_groups_by_parent_id_companies_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketingCompaniesApi->put_marketing_groups_by_parent_id_companies_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| companyId | 
 **parent_id** | **int**| groupId | 
 **client_id** | **str**|  | 
 **marketing_company** | [**MarketingCompany**](MarketingCompany.md)| marketingCompany | 

### Return type

[**MarketingCompany**](MarketingCompany.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | MarketingCompany |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

