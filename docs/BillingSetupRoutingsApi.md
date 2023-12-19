# connectwise_psa.BillingSetupRoutingsApi

All URIs are relative to *https://aus-api.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_finance_billing_setups_by_parent_id_routings_by_id**](BillingSetupRoutingsApi.md#delete_finance_billing_setups_by_parent_id_routings_by_id) | **DELETE** /finance/billingSetups/{parentId}/routings/{id} | Delete BillingSetupRouting
[**get_finance_billing_setups_by_parent_id_routings**](BillingSetupRoutingsApi.md#get_finance_billing_setups_by_parent_id_routings) | **GET** /finance/billingSetups/{parentId}/routings | Get List of BillingSetupRouting
[**get_finance_billing_setups_by_parent_id_routings_by_id**](BillingSetupRoutingsApi.md#get_finance_billing_setups_by_parent_id_routings_by_id) | **GET** /finance/billingSetups/{parentId}/routings/{id} | Get BillingSetupRouting
[**get_finance_billing_setups_by_parent_id_routings_count**](BillingSetupRoutingsApi.md#get_finance_billing_setups_by_parent_id_routings_count) | **GET** /finance/billingSetups/{parentId}/routings/count | Get Count of BillingSetupRouting
[**patch_finance_billing_setups_by_parent_id_routings_by_id**](BillingSetupRoutingsApi.md#patch_finance_billing_setups_by_parent_id_routings_by_id) | **PATCH** /finance/billingSetups/{parentId}/routings/{id} | Patch BillingSetupRouting
[**post_finance_billing_setups_by_parent_id_routings**](BillingSetupRoutingsApi.md#post_finance_billing_setups_by_parent_id_routings) | **POST** /finance/billingSetups/{parentId}/routings | Post BillingSetupRouting
[**put_finance_billing_setups_by_parent_id_routings_by_id**](BillingSetupRoutingsApi.md#put_finance_billing_setups_by_parent_id_routings_by_id) | **PUT** /finance/billingSetups/{parentId}/routings/{id} | Put BillingSetupRouting


# **delete_finance_billing_setups_by_parent_id_routings_by_id**
> delete_finance_billing_setups_by_parent_id_routings_by_id(id, parent_id, client_id)

Delete BillingSetupRouting

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
    api_instance = connectwise_psa.BillingSetupRoutingsApi(api_client)
    id = 56 # int | routingId
    parent_id = 56 # int | billingSetupId
    client_id = 'client_id_example' # str | 

    try:
        # Delete BillingSetupRouting
        api_instance.delete_finance_billing_setups_by_parent_id_routings_by_id(id, parent_id, client_id)
    except Exception as e:
        print("Exception when calling BillingSetupRoutingsApi->delete_finance_billing_setups_by_parent_id_routings_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| routingId | 
 **parent_id** | **int**| billingSetupId | 
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

# **get_finance_billing_setups_by_parent_id_routings**
> List[BillingSetupRouting] get_finance_billing_setups_by_parent_id_routings(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of BillingSetupRouting

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.billing_setup_routing import BillingSetupRouting
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
    api_instance = connectwise_psa.BillingSetupRoutingsApi(api_client)
    parent_id = 56 # int | billingSetupId
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
        # Get List of BillingSetupRouting
        api_response = api_instance.get_finance_billing_setups_by_parent_id_routings(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of BillingSetupRoutingsApi->get_finance_billing_setups_by_parent_id_routings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingSetupRoutingsApi->get_finance_billing_setups_by_parent_id_routings: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| billingSetupId | 
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

[**List[BillingSetupRouting]**](BillingSetupRouting.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of BillingSetupRouting |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_finance_billing_setups_by_parent_id_routings_by_id**
> BillingSetupRouting get_finance_billing_setups_by_parent_id_routings_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get BillingSetupRouting

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.billing_setup_routing import BillingSetupRouting
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
    api_instance = connectwise_psa.BillingSetupRoutingsApi(api_client)
    id = 56 # int | routingId
    parent_id = 56 # int | billingSetupId
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
        # Get BillingSetupRouting
        api_response = api_instance.get_finance_billing_setups_by_parent_id_routings_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of BillingSetupRoutingsApi->get_finance_billing_setups_by_parent_id_routings_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingSetupRoutingsApi->get_finance_billing_setups_by_parent_id_routings_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| routingId | 
 **parent_id** | **int**| billingSetupId | 
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

[**BillingSetupRouting**](BillingSetupRouting.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | BillingSetupRouting |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_finance_billing_setups_by_parent_id_routings_count**
> Count get_finance_billing_setups_by_parent_id_routings_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Count of BillingSetupRouting

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
    api_instance = connectwise_psa.BillingSetupRoutingsApi(api_client)
    parent_id = 56 # int | billingSetupId
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
        # Get Count of BillingSetupRouting
        api_response = api_instance.get_finance_billing_setups_by_parent_id_routings_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of BillingSetupRoutingsApi->get_finance_billing_setups_by_parent_id_routings_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingSetupRoutingsApi->get_finance_billing_setups_by_parent_id_routings_count: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| billingSetupId | 
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

# **patch_finance_billing_setups_by_parent_id_routings_by_id**
> BillingSetupRouting patch_finance_billing_setups_by_parent_id_routings_by_id(id, parent_id, client_id, patch_operation)

Patch BillingSetupRouting

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.billing_setup_routing import BillingSetupRouting
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
    api_instance = connectwise_psa.BillingSetupRoutingsApi(api_client)
    id = 56 # int | routingId
    parent_id = 56 # int | billingSetupId
    client_id = 'client_id_example' # str | 
    patch_operation = [connectwise_psa.PatchOperation()] # List[PatchOperation] | List of PatchOperation

    try:
        # Patch BillingSetupRouting
        api_response = api_instance.patch_finance_billing_setups_by_parent_id_routings_by_id(id, parent_id, client_id, patch_operation)
        print("The response of BillingSetupRoutingsApi->patch_finance_billing_setups_by_parent_id_routings_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingSetupRoutingsApi->patch_finance_billing_setups_by_parent_id_routings_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| routingId | 
 **parent_id** | **int**| billingSetupId | 
 **client_id** | **str**|  | 
 **patch_operation** | [**List[PatchOperation]**](PatchOperation.md)| List of PatchOperation | 

### Return type

[**BillingSetupRouting**](BillingSetupRouting.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | BillingSetupRouting |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_finance_billing_setups_by_parent_id_routings**
> BillingSetupRouting post_finance_billing_setups_by_parent_id_routings(parent_id, client_id, billing_setup_routing)

Post BillingSetupRouting

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.billing_setup_routing import BillingSetupRouting
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
    api_instance = connectwise_psa.BillingSetupRoutingsApi(api_client)
    parent_id = 56 # int | billingSetupId
    client_id = 'client_id_example' # str | 
    billing_setup_routing = connectwise_psa.BillingSetupRouting() # BillingSetupRouting | billingSetupRouting

    try:
        # Post BillingSetupRouting
        api_response = api_instance.post_finance_billing_setups_by_parent_id_routings(parent_id, client_id, billing_setup_routing)
        print("The response of BillingSetupRoutingsApi->post_finance_billing_setups_by_parent_id_routings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingSetupRoutingsApi->post_finance_billing_setups_by_parent_id_routings: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| billingSetupId | 
 **client_id** | **str**|  | 
 **billing_setup_routing** | [**BillingSetupRouting**](BillingSetupRouting.md)| billingSetupRouting | 

### Return type

[**BillingSetupRouting**](BillingSetupRouting.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | BillingSetupRouting |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_finance_billing_setups_by_parent_id_routings_by_id**
> BillingSetupRouting put_finance_billing_setups_by_parent_id_routings_by_id(id, parent_id, client_id, billing_setup_routing)

Put BillingSetupRouting

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.billing_setup_routing import BillingSetupRouting
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
    api_instance = connectwise_psa.BillingSetupRoutingsApi(api_client)
    id = 56 # int | routingId
    parent_id = 56 # int | billingSetupId
    client_id = 'client_id_example' # str | 
    billing_setup_routing = connectwise_psa.BillingSetupRouting() # BillingSetupRouting | billingSetupRouting

    try:
        # Put BillingSetupRouting
        api_response = api_instance.put_finance_billing_setups_by_parent_id_routings_by_id(id, parent_id, client_id, billing_setup_routing)
        print("The response of BillingSetupRoutingsApi->put_finance_billing_setups_by_parent_id_routings_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingSetupRoutingsApi->put_finance_billing_setups_by_parent_id_routings_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| routingId | 
 **parent_id** | **int**| billingSetupId | 
 **client_id** | **str**|  | 
 **billing_setup_routing** | [**BillingSetupRouting**](BillingSetupRouting.md)| billingSetupRouting | 

### Return type

[**BillingSetupRouting**](BillingSetupRouting.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | BillingSetupRouting |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

