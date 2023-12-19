# connectwise_psa.TimeAccrualDetailsApi

All URIs are relative to *https://api-aus.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_time_accruals_by_parent_id_details_by_id**](TimeAccrualDetailsApi.md#delete_time_accruals_by_parent_id_details_by_id) | **DELETE** /time/accruals/{parentId}/details/{id} | Delete TimeAccrualDetail
[**get_time_accruals_by_parent_id_details**](TimeAccrualDetailsApi.md#get_time_accruals_by_parent_id_details) | **GET** /time/accruals/{parentId}/details | Get List of TimeAccrualDetail
[**get_time_accruals_by_parent_id_details_by_id**](TimeAccrualDetailsApi.md#get_time_accruals_by_parent_id_details_by_id) | **GET** /time/accruals/{parentId}/details/{id} | Get TimeAccrualDetail
[**get_time_accruals_by_parent_id_details_count**](TimeAccrualDetailsApi.md#get_time_accruals_by_parent_id_details_count) | **GET** /time/accruals/{parentId}/details/count | Get Count of TimeAccrualDetail
[**patch_time_accruals_by_parent_id_details_by_id**](TimeAccrualDetailsApi.md#patch_time_accruals_by_parent_id_details_by_id) | **PATCH** /time/accruals/{parentId}/details/{id} | Patch TimeAccrualDetail
[**post_time_accruals_by_parent_id_details**](TimeAccrualDetailsApi.md#post_time_accruals_by_parent_id_details) | **POST** /time/accruals/{parentId}/details/ | Post TimeAccrualDetail
[**put_time_accruals_by_parent_id_details_by_id**](TimeAccrualDetailsApi.md#put_time_accruals_by_parent_id_details_by_id) | **PUT** /time/accruals/{parentId}/details/{id} | Put TimeAccrualDetail


# **delete_time_accruals_by_parent_id_details_by_id**
> delete_time_accruals_by_parent_id_details_by_id(id, parent_id, client_id)

Delete TimeAccrualDetail

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
    api_instance = connectwise_psa.TimeAccrualDetailsApi(api_client)
    id = 56 # int | detailId
    parent_id = 56 # int | accrualId
    client_id = 'client_id_example' # str | 

    try:
        # Delete TimeAccrualDetail
        api_instance.delete_time_accruals_by_parent_id_details_by_id(id, parent_id, client_id)
    except Exception as e:
        print("Exception when calling TimeAccrualDetailsApi->delete_time_accruals_by_parent_id_details_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| detailId | 
 **parent_id** | **int**| accrualId | 
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

# **get_time_accruals_by_parent_id_details**
> List[TimeAccrualDetail] get_time_accruals_by_parent_id_details(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of TimeAccrualDetail

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.time_accrual_detail import TimeAccrualDetail
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
    api_instance = connectwise_psa.TimeAccrualDetailsApi(api_client)
    parent_id = 56 # int | accrualId
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
        # Get List of TimeAccrualDetail
        api_response = api_instance.get_time_accruals_by_parent_id_details(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of TimeAccrualDetailsApi->get_time_accruals_by_parent_id_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TimeAccrualDetailsApi->get_time_accruals_by_parent_id_details: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| accrualId | 
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

[**List[TimeAccrualDetail]**](TimeAccrualDetail.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of TimeAccrualDetail |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_time_accruals_by_parent_id_details_by_id**
> TimeAccrualDetail get_time_accruals_by_parent_id_details_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get TimeAccrualDetail

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.time_accrual_detail import TimeAccrualDetail
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
    api_instance = connectwise_psa.TimeAccrualDetailsApi(api_client)
    id = 56 # int | detailId
    parent_id = 56 # int | accrualId
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
        # Get TimeAccrualDetail
        api_response = api_instance.get_time_accruals_by_parent_id_details_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of TimeAccrualDetailsApi->get_time_accruals_by_parent_id_details_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TimeAccrualDetailsApi->get_time_accruals_by_parent_id_details_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| detailId | 
 **parent_id** | **int**| accrualId | 
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

[**TimeAccrualDetail**](TimeAccrualDetail.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | TimeAccrualDetail |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_time_accruals_by_parent_id_details_count**
> Count get_time_accruals_by_parent_id_details_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Count of TimeAccrualDetail

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
    api_instance = connectwise_psa.TimeAccrualDetailsApi(api_client)
    parent_id = 56 # int | accrualId
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
        # Get Count of TimeAccrualDetail
        api_response = api_instance.get_time_accruals_by_parent_id_details_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of TimeAccrualDetailsApi->get_time_accruals_by_parent_id_details_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TimeAccrualDetailsApi->get_time_accruals_by_parent_id_details_count: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| accrualId | 
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

# **patch_time_accruals_by_parent_id_details_by_id**
> TimeAccrualDetail patch_time_accruals_by_parent_id_details_by_id(id, parent_id, client_id, patch_operation)

Patch TimeAccrualDetail

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.patch_operation import PatchOperation
from connectwise_psa.models.time_accrual_detail import TimeAccrualDetail
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
    api_instance = connectwise_psa.TimeAccrualDetailsApi(api_client)
    id = 56 # int | detailId
    parent_id = 56 # int | accrualId
    client_id = 'client_id_example' # str | 
    patch_operation = [connectwise_psa.PatchOperation()] # List[PatchOperation] | List of PatchOperation

    try:
        # Patch TimeAccrualDetail
        api_response = api_instance.patch_time_accruals_by_parent_id_details_by_id(id, parent_id, client_id, patch_operation)
        print("The response of TimeAccrualDetailsApi->patch_time_accruals_by_parent_id_details_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TimeAccrualDetailsApi->patch_time_accruals_by_parent_id_details_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| detailId | 
 **parent_id** | **int**| accrualId | 
 **client_id** | **str**|  | 
 **patch_operation** | [**List[PatchOperation]**](PatchOperation.md)| List of PatchOperation | 

### Return type

[**TimeAccrualDetail**](TimeAccrualDetail.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | TimeAccrualDetail |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_time_accruals_by_parent_id_details**
> TimeAccrualDetail post_time_accruals_by_parent_id_details(parent_id, client_id, time_accrual_detail)

Post TimeAccrualDetail

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.time_accrual_detail import TimeAccrualDetail
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
    api_instance = connectwise_psa.TimeAccrualDetailsApi(api_client)
    parent_id = 56 # int | accrualId
    client_id = 'client_id_example' # str | 
    time_accrual_detail = connectwise_psa.TimeAccrualDetail() # TimeAccrualDetail | timeAccrualDetail

    try:
        # Post TimeAccrualDetail
        api_response = api_instance.post_time_accruals_by_parent_id_details(parent_id, client_id, time_accrual_detail)
        print("The response of TimeAccrualDetailsApi->post_time_accruals_by_parent_id_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TimeAccrualDetailsApi->post_time_accruals_by_parent_id_details: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| accrualId | 
 **client_id** | **str**|  | 
 **time_accrual_detail** | [**TimeAccrualDetail**](TimeAccrualDetail.md)| timeAccrualDetail | 

### Return type

[**TimeAccrualDetail**](TimeAccrualDetail.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | TimeAccrualDetail |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_time_accruals_by_parent_id_details_by_id**
> TimeAccrualDetail put_time_accruals_by_parent_id_details_by_id(id, parent_id, client_id, time_accrual_detail)

Put TimeAccrualDetail

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.time_accrual_detail import TimeAccrualDetail
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
    api_instance = connectwise_psa.TimeAccrualDetailsApi(api_client)
    id = 56 # int | detailId
    parent_id = 56 # int | accrualId
    client_id = 'client_id_example' # str | 
    time_accrual_detail = connectwise_psa.TimeAccrualDetail() # TimeAccrualDetail | timeAccrualDetail

    try:
        # Put TimeAccrualDetail
        api_response = api_instance.put_time_accruals_by_parent_id_details_by_id(id, parent_id, client_id, time_accrual_detail)
        print("The response of TimeAccrualDetailsApi->put_time_accruals_by_parent_id_details_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TimeAccrualDetailsApi->put_time_accruals_by_parent_id_details_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| detailId | 
 **parent_id** | **int**| accrualId | 
 **client_id** | **str**|  | 
 **time_accrual_detail** | [**TimeAccrualDetail**](TimeAccrualDetail.md)| timeAccrualDetail | 

### Return type

[**TimeAccrualDetail**](TimeAccrualDetail.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | TimeAccrualDetail |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

