# connectwise_psa.AgreementSitesApi

All URIs are relative to *https://aus-api.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_finance_agreements_by_parent_id_sites_by_id**](AgreementSitesApi.md#delete_finance_agreements_by_parent_id_sites_by_id) | **DELETE** /finance/agreements/{parentId}/sites/{id} | Delete AgreementSite
[**get_finance_agreements_by_parent_id_sites**](AgreementSitesApi.md#get_finance_agreements_by_parent_id_sites) | **GET** /finance/agreements/{parentId}/sites | Get List of AgreementSite
[**get_finance_agreements_by_parent_id_sites_by_id**](AgreementSitesApi.md#get_finance_agreements_by_parent_id_sites_by_id) | **GET** /finance/agreements/{parentId}/sites/{id} | Get AgreementSite
[**get_finance_agreements_by_parent_id_sites_count**](AgreementSitesApi.md#get_finance_agreements_by_parent_id_sites_count) | **GET** /finance/agreements/{parentId}/sites/count | Get Count of AgreementSite
[**patch_finance_agreements_by_parent_id_sites_by_id**](AgreementSitesApi.md#patch_finance_agreements_by_parent_id_sites_by_id) | **PATCH** /finance/agreements/{parentId}/sites/{id} | Patch AgreementSite
[**post_finance_agreements_by_parent_id_sites**](AgreementSitesApi.md#post_finance_agreements_by_parent_id_sites) | **POST** /finance/agreements/{parentId}/sites | Post AgreementSite
[**put_finance_agreements_by_parent_id_sites_by_id**](AgreementSitesApi.md#put_finance_agreements_by_parent_id_sites_by_id) | **PUT** /finance/agreements/{parentId}/sites/{id} | Put AgreementSite


# **delete_finance_agreements_by_parent_id_sites_by_id**
> delete_finance_agreements_by_parent_id_sites_by_id(id, parent_id, client_id)

Delete AgreementSite

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
    api_instance = connectwise_psa.AgreementSitesApi(api_client)
    id = 56 # int | siteId
    parent_id = 56 # int | agreementId
    client_id = 'client_id_example' # str | 

    try:
        # Delete AgreementSite
        api_instance.delete_finance_agreements_by_parent_id_sites_by_id(id, parent_id, client_id)
    except Exception as e:
        print("Exception when calling AgreementSitesApi->delete_finance_agreements_by_parent_id_sites_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| siteId | 
 **parent_id** | **int**| agreementId | 
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

# **get_finance_agreements_by_parent_id_sites**
> List[AgreementSite] get_finance_agreements_by_parent_id_sites(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of AgreementSite

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.agreement_site import AgreementSite
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
    api_instance = connectwise_psa.AgreementSitesApi(api_client)
    parent_id = 56 # int | agreementId
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
        # Get List of AgreementSite
        api_response = api_instance.get_finance_agreements_by_parent_id_sites(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of AgreementSitesApi->get_finance_agreements_by_parent_id_sites:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgreementSitesApi->get_finance_agreements_by_parent_id_sites: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| agreementId | 
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

[**List[AgreementSite]**](AgreementSite.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of AgreementSite |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_finance_agreements_by_parent_id_sites_by_id**
> AgreementSite get_finance_agreements_by_parent_id_sites_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get AgreementSite

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.agreement_site import AgreementSite
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
    api_instance = connectwise_psa.AgreementSitesApi(api_client)
    id = 56 # int | siteId
    parent_id = 56 # int | agreementId
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
        # Get AgreementSite
        api_response = api_instance.get_finance_agreements_by_parent_id_sites_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of AgreementSitesApi->get_finance_agreements_by_parent_id_sites_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgreementSitesApi->get_finance_agreements_by_parent_id_sites_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| siteId | 
 **parent_id** | **int**| agreementId | 
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

[**AgreementSite**](AgreementSite.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | AgreementSite |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_finance_agreements_by_parent_id_sites_count**
> Count get_finance_agreements_by_parent_id_sites_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Count of AgreementSite

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
    api_instance = connectwise_psa.AgreementSitesApi(api_client)
    parent_id = 56 # int | agreementId
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
        # Get Count of AgreementSite
        api_response = api_instance.get_finance_agreements_by_parent_id_sites_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of AgreementSitesApi->get_finance_agreements_by_parent_id_sites_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgreementSitesApi->get_finance_agreements_by_parent_id_sites_count: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| agreementId | 
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

# **patch_finance_agreements_by_parent_id_sites_by_id**
> AgreementSite patch_finance_agreements_by_parent_id_sites_by_id(id, parent_id, client_id, patch_operation)

Patch AgreementSite

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.agreement_site import AgreementSite
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
    api_instance = connectwise_psa.AgreementSitesApi(api_client)
    id = 56 # int | siteId
    parent_id = 56 # int | agreementId
    client_id = 'client_id_example' # str | 
    patch_operation = [connectwise_psa.PatchOperation()] # List[PatchOperation] | List of PatchOperation

    try:
        # Patch AgreementSite
        api_response = api_instance.patch_finance_agreements_by_parent_id_sites_by_id(id, parent_id, client_id, patch_operation)
        print("The response of AgreementSitesApi->patch_finance_agreements_by_parent_id_sites_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgreementSitesApi->patch_finance_agreements_by_parent_id_sites_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| siteId | 
 **parent_id** | **int**| agreementId | 
 **client_id** | **str**|  | 
 **patch_operation** | [**List[PatchOperation]**](PatchOperation.md)| List of PatchOperation | 

### Return type

[**AgreementSite**](AgreementSite.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | AgreementSite |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_finance_agreements_by_parent_id_sites**
> AgreementSite post_finance_agreements_by_parent_id_sites(parent_id, client_id, agreement_site)

Post AgreementSite

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.agreement_site import AgreementSite
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
    api_instance = connectwise_psa.AgreementSitesApi(api_client)
    parent_id = 56 # int | agreementId
    client_id = 'client_id_example' # str | 
    agreement_site = connectwise_psa.AgreementSite() # AgreementSite | site

    try:
        # Post AgreementSite
        api_response = api_instance.post_finance_agreements_by_parent_id_sites(parent_id, client_id, agreement_site)
        print("The response of AgreementSitesApi->post_finance_agreements_by_parent_id_sites:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgreementSitesApi->post_finance_agreements_by_parent_id_sites: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| agreementId | 
 **client_id** | **str**|  | 
 **agreement_site** | [**AgreementSite**](AgreementSite.md)| site | 

### Return type

[**AgreementSite**](AgreementSite.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | AgreementSite |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_finance_agreements_by_parent_id_sites_by_id**
> AgreementSite put_finance_agreements_by_parent_id_sites_by_id(id, parent_id, client_id, agreement_site)

Put AgreementSite

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.agreement_site import AgreementSite
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
    api_instance = connectwise_psa.AgreementSitesApi(api_client)
    id = 56 # int | siteId
    parent_id = 56 # int | agreementId
    client_id = 'client_id_example' # str | 
    agreement_site = connectwise_psa.AgreementSite() # AgreementSite | site

    try:
        # Put AgreementSite
        api_response = api_instance.put_finance_agreements_by_parent_id_sites_by_id(id, parent_id, client_id, agreement_site)
        print("The response of AgreementSitesApi->put_finance_agreements_by_parent_id_sites_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgreementSitesApi->put_finance_agreements_by_parent_id_sites_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| siteId | 
 **parent_id** | **int**| agreementId | 
 **client_id** | **str**|  | 
 **agreement_site** | [**AgreementSite**](AgreementSite.md)| site | 

### Return type

[**AgreementSite**](AgreementSite.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | AgreementSite |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

