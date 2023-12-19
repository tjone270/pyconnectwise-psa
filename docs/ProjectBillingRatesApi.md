# connectwise_psa.ProjectBillingRatesApi

All URIs are relative to *https://api-aus.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_project_by_parent_id_billing_rates_by_id**](ProjectBillingRatesApi.md#delete_project_by_parent_id_billing_rates_by_id) | **DELETE** /project/{parentId}/billingRates/{id} | Delete ProjectBillingRate
[**get_project_by_parent_id_billing_rates**](ProjectBillingRatesApi.md#get_project_by_parent_id_billing_rates) | **GET** /project/{parentId}/billingRates | Get List of ProjectBillingRate
[**get_project_by_parent_id_billing_rates_by_id**](ProjectBillingRatesApi.md#get_project_by_parent_id_billing_rates_by_id) | **GET** /project/{parentId}/billingRates/{id} | Get ProjectBillingRate
[**get_project_by_parent_id_billing_rates_count**](ProjectBillingRatesApi.md#get_project_by_parent_id_billing_rates_count) | **GET** /project/{parentId}/billingRates/count | Get Count of ProjectBillingRate
[**patch_project_billing_rates_by_parent_id_billing_rates_by_id**](ProjectBillingRatesApi.md#patch_project_billing_rates_by_parent_id_billing_rates_by_id) | **PATCH** /project/billingRates/{parentId}/billingRates/{id} | Patch ProjectBillingRate
[**post_project_by_parent_id_billing_rates**](ProjectBillingRatesApi.md#post_project_by_parent_id_billing_rates) | **POST** /project/{parentId}/billingRates | Post ProjectBillingRate
[**put_project_by_parent_id_billing_rates_by_id**](ProjectBillingRatesApi.md#put_project_by_parent_id_billing_rates_by_id) | **PUT** /project/{parentId}/billingRates/{id} | Put ProjectBillingRate


# **delete_project_by_parent_id_billing_rates_by_id**
> delete_project_by_parent_id_billing_rates_by_id(id, parent_id, client_id)

Delete ProjectBillingRate

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
    api_instance = connectwise_psa.ProjectBillingRatesApi(api_client)
    id = 56 # int | billingRate
    parent_id = 56 # int | projectId
    client_id = 'client_id_example' # str | 

    try:
        # Delete ProjectBillingRate
        api_instance.delete_project_by_parent_id_billing_rates_by_id(id, parent_id, client_id)
    except Exception as e:
        print("Exception when calling ProjectBillingRatesApi->delete_project_by_parent_id_billing_rates_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| billingRate | 
 **parent_id** | **int**| projectId | 
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

# **get_project_by_parent_id_billing_rates**
> List[ProjectBillingRate] get_project_by_parent_id_billing_rates(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of ProjectBillingRate

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.project_billing_rate import ProjectBillingRate
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
    api_instance = connectwise_psa.ProjectBillingRatesApi(api_client)
    parent_id = 56 # int | projectId
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
        # Get List of ProjectBillingRate
        api_response = api_instance.get_project_by_parent_id_billing_rates(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of ProjectBillingRatesApi->get_project_by_parent_id_billing_rates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectBillingRatesApi->get_project_by_parent_id_billing_rates: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| projectId | 
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

[**List[ProjectBillingRate]**](ProjectBillingRate.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of ProjectBillingRate |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_by_parent_id_billing_rates_by_id**
> ProjectBillingRate get_project_by_parent_id_billing_rates_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get ProjectBillingRate

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.project_billing_rate import ProjectBillingRate
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
    api_instance = connectwise_psa.ProjectBillingRatesApi(api_client)
    id = 56 # int | billingRateId
    parent_id = 56 # int | projectId
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
        # Get ProjectBillingRate
        api_response = api_instance.get_project_by_parent_id_billing_rates_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of ProjectBillingRatesApi->get_project_by_parent_id_billing_rates_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectBillingRatesApi->get_project_by_parent_id_billing_rates_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| billingRateId | 
 **parent_id** | **int**| projectId | 
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

[**ProjectBillingRate**](ProjectBillingRate.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ProjectBillingRate |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_by_parent_id_billing_rates_count**
> Count get_project_by_parent_id_billing_rates_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Count of ProjectBillingRate

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
    api_instance = connectwise_psa.ProjectBillingRatesApi(api_client)
    parent_id = 56 # int | projectId
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
        # Get Count of ProjectBillingRate
        api_response = api_instance.get_project_by_parent_id_billing_rates_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of ProjectBillingRatesApi->get_project_by_parent_id_billing_rates_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectBillingRatesApi->get_project_by_parent_id_billing_rates_count: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| projectId | 
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

# **patch_project_billing_rates_by_parent_id_billing_rates_by_id**
> ProjectBillingRate patch_project_billing_rates_by_parent_id_billing_rates_by_id(id, parent_id, client_id, patch_operation)

Patch ProjectBillingRate

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.patch_operation import PatchOperation
from connectwise_psa.models.project_billing_rate import ProjectBillingRate
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
    api_instance = connectwise_psa.ProjectBillingRatesApi(api_client)
    id = 56 # int | billingRateId
    parent_id = 56 # int | projectId
    client_id = 'client_id_example' # str | 
    patch_operation = [connectwise_psa.PatchOperation()] # List[PatchOperation] | List of PatchOperation

    try:
        # Patch ProjectBillingRate
        api_response = api_instance.patch_project_billing_rates_by_parent_id_billing_rates_by_id(id, parent_id, client_id, patch_operation)
        print("The response of ProjectBillingRatesApi->patch_project_billing_rates_by_parent_id_billing_rates_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectBillingRatesApi->patch_project_billing_rates_by_parent_id_billing_rates_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| billingRateId | 
 **parent_id** | **int**| projectId | 
 **client_id** | **str**|  | 
 **patch_operation** | [**List[PatchOperation]**](PatchOperation.md)| List of PatchOperation | 

### Return type

[**ProjectBillingRate**](ProjectBillingRate.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ProjectBillingRate |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_project_by_parent_id_billing_rates**
> ProjectBillingRate post_project_by_parent_id_billing_rates(parent_id, client_id, project_billing_rate)

Post ProjectBillingRate

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.project_billing_rate import ProjectBillingRate
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
    api_instance = connectwise_psa.ProjectBillingRatesApi(api_client)
    parent_id = 56 # int | projectId
    client_id = 'client_id_example' # str | 
    project_billing_rate = connectwise_psa.ProjectBillingRate() # ProjectBillingRate | billingRate

    try:
        # Post ProjectBillingRate
        api_response = api_instance.post_project_by_parent_id_billing_rates(parent_id, client_id, project_billing_rate)
        print("The response of ProjectBillingRatesApi->post_project_by_parent_id_billing_rates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectBillingRatesApi->post_project_by_parent_id_billing_rates: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| projectId | 
 **client_id** | **str**|  | 
 **project_billing_rate** | [**ProjectBillingRate**](ProjectBillingRate.md)| billingRate | 

### Return type

[**ProjectBillingRate**](ProjectBillingRate.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | ProjectBillingRate |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_project_by_parent_id_billing_rates_by_id**
> ProjectBillingRate put_project_by_parent_id_billing_rates_by_id(id, parent_id, client_id, project_billing_rate)

Put ProjectBillingRate

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.project_billing_rate import ProjectBillingRate
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
    api_instance = connectwise_psa.ProjectBillingRatesApi(api_client)
    id = 56 # int | billingRateId
    parent_id = 56 # int | projectId
    client_id = 'client_id_example' # str | 
    project_billing_rate = connectwise_psa.ProjectBillingRate() # ProjectBillingRate | billingRate

    try:
        # Put ProjectBillingRate
        api_response = api_instance.put_project_by_parent_id_billing_rates_by_id(id, parent_id, client_id, project_billing_rate)
        print("The response of ProjectBillingRatesApi->put_project_by_parent_id_billing_rates_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectBillingRatesApi->put_project_by_parent_id_billing_rates_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| billingRateId | 
 **parent_id** | **int**| projectId | 
 **client_id** | **str**|  | 
 **project_billing_rate** | [**ProjectBillingRate**](ProjectBillingRate.md)| billingRate | 

### Return type

[**ProjectBillingRate**](ProjectBillingRate.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ProjectBillingRate |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

