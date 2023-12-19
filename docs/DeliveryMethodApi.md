# connectwise_psa.DeliveryMethodApi

All URIs are relative to *https://aus-api.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_finance_delivery_methods_by_id**](DeliveryMethodApi.md#delete_finance_delivery_methods_by_id) | **DELETE** /finance/deliveryMethods/{id} | Delete DeliveryMethod
[**get_finance_delivery_methods**](DeliveryMethodApi.md#get_finance_delivery_methods) | **GET** /finance/deliveryMethods | Get List of DeliveryMethod
[**get_finance_delivery_methods_by_id**](DeliveryMethodApi.md#get_finance_delivery_methods_by_id) | **GET** /finance/deliveryMethods/{id} | Get DeliveryMethod
[**get_finance_delivery_methods_count**](DeliveryMethodApi.md#get_finance_delivery_methods_count) | **GET** /finance/deliveryMethods/count | Get Count of DeliveryMethod
[**patch_finance_delivery_methods_by_id**](DeliveryMethodApi.md#patch_finance_delivery_methods_by_id) | **PATCH** /finance/deliveryMethods/{id} | Patch DeliveryMethod
[**post_finance_delivery_methods**](DeliveryMethodApi.md#post_finance_delivery_methods) | **POST** /finance/deliveryMethods | Post DeliveryMethod
[**put_finance_delivery_methods_by_id**](DeliveryMethodApi.md#put_finance_delivery_methods_by_id) | **PUT** /finance/deliveryMethods/{id} | Put DeliveryMethod


# **delete_finance_delivery_methods_by_id**
> delete_finance_delivery_methods_by_id(id, client_id)

Delete DeliveryMethod

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
    api_instance = connectwise_psa.DeliveryMethodApi(api_client)
    id = 56 # int | deliveryMethodId
    client_id = 'client_id_example' # str | 

    try:
        # Delete DeliveryMethod
        api_instance.delete_finance_delivery_methods_by_id(id, client_id)
    except Exception as e:
        print("Exception when calling DeliveryMethodApi->delete_finance_delivery_methods_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| deliveryMethodId | 
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

# **get_finance_delivery_methods**
> List[DeliveryMethod] get_finance_delivery_methods(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of DeliveryMethod

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.delivery_method import DeliveryMethod
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
    api_instance = connectwise_psa.DeliveryMethodApi(api_client)
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
        # Get List of DeliveryMethod
        api_response = api_instance.get_finance_delivery_methods(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of DeliveryMethodApi->get_finance_delivery_methods:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeliveryMethodApi->get_finance_delivery_methods: %s\n" % e)
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

[**List[DeliveryMethod]**](DeliveryMethod.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of DeliveryMethod |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_finance_delivery_methods_by_id**
> DeliveryMethod get_finance_delivery_methods_by_id(id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get DeliveryMethod

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.delivery_method import DeliveryMethod
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
    api_instance = connectwise_psa.DeliveryMethodApi(api_client)
    id = 56 # int | deliveryMethodId
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
        # Get DeliveryMethod
        api_response = api_instance.get_finance_delivery_methods_by_id(id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of DeliveryMethodApi->get_finance_delivery_methods_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeliveryMethodApi->get_finance_delivery_methods_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| deliveryMethodId | 
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

[**DeliveryMethod**](DeliveryMethod.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | DeliveryMethod |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_finance_delivery_methods_count**
> Count get_finance_delivery_methods_count(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Count of DeliveryMethod

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
    api_instance = connectwise_psa.DeliveryMethodApi(api_client)
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
        # Get Count of DeliveryMethod
        api_response = api_instance.get_finance_delivery_methods_count(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of DeliveryMethodApi->get_finance_delivery_methods_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeliveryMethodApi->get_finance_delivery_methods_count: %s\n" % e)
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

# **patch_finance_delivery_methods_by_id**
> DeliveryMethod patch_finance_delivery_methods_by_id(id, client_id, patch_operation)

Patch DeliveryMethod

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.delivery_method import DeliveryMethod
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
    api_instance = connectwise_psa.DeliveryMethodApi(api_client)
    id = 56 # int | deliveryMethodId
    client_id = 'client_id_example' # str | 
    patch_operation = [connectwise_psa.PatchOperation()] # List[PatchOperation] | List of PatchOperation

    try:
        # Patch DeliveryMethod
        api_response = api_instance.patch_finance_delivery_methods_by_id(id, client_id, patch_operation)
        print("The response of DeliveryMethodApi->patch_finance_delivery_methods_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeliveryMethodApi->patch_finance_delivery_methods_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| deliveryMethodId | 
 **client_id** | **str**|  | 
 **patch_operation** | [**List[PatchOperation]**](PatchOperation.md)| List of PatchOperation | 

### Return type

[**DeliveryMethod**](DeliveryMethod.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | DeliveryMethod |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_finance_delivery_methods**
> DeliveryMethod post_finance_delivery_methods(client_id, delivery_method)

Post DeliveryMethod

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.delivery_method import DeliveryMethod
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
    api_instance = connectwise_psa.DeliveryMethodApi(api_client)
    client_id = 'client_id_example' # str | 
    delivery_method = connectwise_psa.DeliveryMethod() # DeliveryMethod | deliveryMethod

    try:
        # Post DeliveryMethod
        api_response = api_instance.post_finance_delivery_methods(client_id, delivery_method)
        print("The response of DeliveryMethodApi->post_finance_delivery_methods:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeliveryMethodApi->post_finance_delivery_methods: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**|  | 
 **delivery_method** | [**DeliveryMethod**](DeliveryMethod.md)| deliveryMethod | 

### Return type

[**DeliveryMethod**](DeliveryMethod.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | DeliveryMethod |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_finance_delivery_methods_by_id**
> DeliveryMethod put_finance_delivery_methods_by_id(id, client_id, delivery_method)

Put DeliveryMethod

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.delivery_method import DeliveryMethod
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
    api_instance = connectwise_psa.DeliveryMethodApi(api_client)
    id = 56 # int | deliveryMethodId
    client_id = 'client_id_example' # str | 
    delivery_method = connectwise_psa.DeliveryMethod() # DeliveryMethod | deliveryMethod

    try:
        # Put DeliveryMethod
        api_response = api_instance.put_finance_delivery_methods_by_id(id, client_id, delivery_method)
        print("The response of DeliveryMethodApi->put_finance_delivery_methods_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeliveryMethodApi->put_finance_delivery_methods_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| deliveryMethodId | 
 **client_id** | **str**|  | 
 **delivery_method** | [**DeliveryMethod**](DeliveryMethod.md)| deliveryMethod | 

### Return type

[**DeliveryMethod**](DeliveryMethod.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | DeliveryMethod |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

