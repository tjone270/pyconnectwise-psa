# connectwise_psa.TodayPageCategoriesApi

All URIs are relative to *https://api-aus.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_system_today_page_categories_by_id**](TodayPageCategoriesApi.md#delete_system_today_page_categories_by_id) | **DELETE** /system/todayPageCategories/{id} | Delete TodayPageCategory
[**get_system_today_page_categories**](TodayPageCategoriesApi.md#get_system_today_page_categories) | **GET** /system/todayPageCategories | Get List of TodayPageCategory
[**get_system_today_page_categories_by_id**](TodayPageCategoriesApi.md#get_system_today_page_categories_by_id) | **GET** /system/todayPageCategories/{id} | Get TodayPageCategory
[**get_system_today_page_categories_count**](TodayPageCategoriesApi.md#get_system_today_page_categories_count) | **GET** /system/todayPageCategories/count | Get Count of TodayPageCategory
[**patch_system_today_page_categories_by_id**](TodayPageCategoriesApi.md#patch_system_today_page_categories_by_id) | **PATCH** /system/todayPageCategories/{id} | Patch TodayPageCategory
[**post_system_today_page_categories**](TodayPageCategoriesApi.md#post_system_today_page_categories) | **POST** /system/todayPageCategories | Post TodayPageCategory
[**put_system_today_page_categories_by_id**](TodayPageCategoriesApi.md#put_system_today_page_categories_by_id) | **PUT** /system/todayPageCategories/{id} | Put TodayPageCategory


# **delete_system_today_page_categories_by_id**
> delete_system_today_page_categories_by_id(id, client_id)

Delete TodayPageCategory

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
    api_instance = connectwise_psa.TodayPageCategoriesApi(api_client)
    id = 56 # int | todayPageCategoryId
    client_id = 'client_id_example' # str | 

    try:
        # Delete TodayPageCategory
        api_instance.delete_system_today_page_categories_by_id(id, client_id)
    except Exception as e:
        print("Exception when calling TodayPageCategoriesApi->delete_system_today_page_categories_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| todayPageCategoryId | 
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

# **get_system_today_page_categories**
> List[TodayPageCategory] get_system_today_page_categories(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of TodayPageCategory

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.today_page_category import TodayPageCategory
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
    api_instance = connectwise_psa.TodayPageCategoriesApi(api_client)
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
        # Get List of TodayPageCategory
        api_response = api_instance.get_system_today_page_categories(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of TodayPageCategoriesApi->get_system_today_page_categories:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TodayPageCategoriesApi->get_system_today_page_categories: %s\n" % e)
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

[**List[TodayPageCategory]**](TodayPageCategory.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of TodayPageCategory |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_system_today_page_categories_by_id**
> TodayPageCategory get_system_today_page_categories_by_id(id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get TodayPageCategory

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.today_page_category import TodayPageCategory
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
    api_instance = connectwise_psa.TodayPageCategoriesApi(api_client)
    id = 56 # int | todayPageCategoryId
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
        # Get TodayPageCategory
        api_response = api_instance.get_system_today_page_categories_by_id(id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of TodayPageCategoriesApi->get_system_today_page_categories_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TodayPageCategoriesApi->get_system_today_page_categories_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| todayPageCategoryId | 
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

[**TodayPageCategory**](TodayPageCategory.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | TodayPageCategory |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_system_today_page_categories_count**
> Count get_system_today_page_categories_count(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Count of TodayPageCategory

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
    api_instance = connectwise_psa.TodayPageCategoriesApi(api_client)
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
        # Get Count of TodayPageCategory
        api_response = api_instance.get_system_today_page_categories_count(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of TodayPageCategoriesApi->get_system_today_page_categories_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TodayPageCategoriesApi->get_system_today_page_categories_count: %s\n" % e)
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

# **patch_system_today_page_categories_by_id**
> TodayPageCategory patch_system_today_page_categories_by_id(id, client_id, patch_operation)

Patch TodayPageCategory

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.patch_operation import PatchOperation
from connectwise_psa.models.today_page_category import TodayPageCategory
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
    api_instance = connectwise_psa.TodayPageCategoriesApi(api_client)
    id = 56 # int | todayPageCategoryId
    client_id = 'client_id_example' # str | 
    patch_operation = [connectwise_psa.PatchOperation()] # List[PatchOperation] | List of PatchOperation

    try:
        # Patch TodayPageCategory
        api_response = api_instance.patch_system_today_page_categories_by_id(id, client_id, patch_operation)
        print("The response of TodayPageCategoriesApi->patch_system_today_page_categories_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TodayPageCategoriesApi->patch_system_today_page_categories_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| todayPageCategoryId | 
 **client_id** | **str**|  | 
 **patch_operation** | [**List[PatchOperation]**](PatchOperation.md)| List of PatchOperation | 

### Return type

[**TodayPageCategory**](TodayPageCategory.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | TodayPageCategory |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_system_today_page_categories**
> TodayPageCategory post_system_today_page_categories(client_id, today_page_category)

Post TodayPageCategory

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.today_page_category import TodayPageCategory
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
    api_instance = connectwise_psa.TodayPageCategoriesApi(api_client)
    client_id = 'client_id_example' # str | 
    today_page_category = connectwise_psa.TodayPageCategory() # TodayPageCategory | todayPageCategory

    try:
        # Post TodayPageCategory
        api_response = api_instance.post_system_today_page_categories(client_id, today_page_category)
        print("The response of TodayPageCategoriesApi->post_system_today_page_categories:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TodayPageCategoriesApi->post_system_today_page_categories: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**|  | 
 **today_page_category** | [**TodayPageCategory**](TodayPageCategory.md)| todayPageCategory | 

### Return type

[**TodayPageCategory**](TodayPageCategory.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | TodayPageCategory |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_system_today_page_categories_by_id**
> TodayPageCategory put_system_today_page_categories_by_id(id, client_id, today_page_category)

Put TodayPageCategory

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.today_page_category import TodayPageCategory
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
    api_instance = connectwise_psa.TodayPageCategoriesApi(api_client)
    id = 56 # int | todayPageCategoryId
    client_id = 'client_id_example' # str | 
    today_page_category = connectwise_psa.TodayPageCategory() # TodayPageCategory | todayPageCategory

    try:
        # Put TodayPageCategory
        api_response = api_instance.put_system_today_page_categories_by_id(id, client_id, today_page_category)
        print("The response of TodayPageCategoriesApi->put_system_today_page_categories_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TodayPageCategoriesApi->put_system_today_page_categories_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| todayPageCategoryId | 
 **client_id** | **str**|  | 
 **today_page_category** | [**TodayPageCategory**](TodayPageCategory.md)| todayPageCategory | 

### Return type

[**TodayPageCategory**](TodayPageCategory.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | TodayPageCategory |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

