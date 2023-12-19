# connectwise_psa.CompanyPickerItemsApi

All URIs are relative to *https://api-aus.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_company_company_picker_items_by_id**](CompanyPickerItemsApi.md#delete_company_company_picker_items_by_id) | **DELETE** /company/companyPickerItems/{id} | Delete CompanyPickerItem
[**get_company_company_picker_items**](CompanyPickerItemsApi.md#get_company_company_picker_items) | **GET** /company/companyPickerItems | Get List of CompanyPickerItem
[**get_company_company_picker_items_by_id**](CompanyPickerItemsApi.md#get_company_company_picker_items_by_id) | **GET** /company/companyPickerItems/{id} | Get CompanyPickerItem
[**get_company_company_picker_items_count**](CompanyPickerItemsApi.md#get_company_company_picker_items_count) | **GET** /company/companyPickerItems/count | Get Count of CompanyPickerItem
[**post_company_company_picker_items**](CompanyPickerItemsApi.md#post_company_company_picker_items) | **POST** /company/companyPickerItems | Post CompanyPickerItem
[**post_company_company_picker_items_clear**](CompanyPickerItemsApi.md#post_company_company_picker_items_clear) | **POST** /company/companyPickerItems/clear | Post ClearPickerRequest


# **delete_company_company_picker_items_by_id**
> delete_company_company_picker_items_by_id(id, client_id)

Delete CompanyPickerItem

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
    api_instance = connectwise_psa.CompanyPickerItemsApi(api_client)
    id = 56 # int | companyPickerItemId
    client_id = 'client_id_example' # str | 

    try:
        # Delete CompanyPickerItem
        api_instance.delete_company_company_picker_items_by_id(id, client_id)
    except Exception as e:
        print("Exception when calling CompanyPickerItemsApi->delete_company_company_picker_items_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| companyPickerItemId | 
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

# **get_company_company_picker_items**
> List[CompanyPickerItem] get_company_company_picker_items(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of CompanyPickerItem

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.company_picker_item import CompanyPickerItem
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
    api_instance = connectwise_psa.CompanyPickerItemsApi(api_client)
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
        # Get List of CompanyPickerItem
        api_response = api_instance.get_company_company_picker_items(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of CompanyPickerItemsApi->get_company_company_picker_items:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompanyPickerItemsApi->get_company_company_picker_items: %s\n" % e)
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

[**List[CompanyPickerItem]**](CompanyPickerItem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of CompanyPickerItem |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_company_company_picker_items_by_id**
> CompanyPickerItem get_company_company_picker_items_by_id(id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get CompanyPickerItem

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.company_picker_item import CompanyPickerItem
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
    api_instance = connectwise_psa.CompanyPickerItemsApi(api_client)
    id = 56 # int | companyPickerItemId
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
        # Get CompanyPickerItem
        api_response = api_instance.get_company_company_picker_items_by_id(id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of CompanyPickerItemsApi->get_company_company_picker_items_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompanyPickerItemsApi->get_company_company_picker_items_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| companyPickerItemId | 
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

[**CompanyPickerItem**](CompanyPickerItem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | CompanyPickerItem |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_company_company_picker_items_count**
> Count get_company_company_picker_items_count(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Count of CompanyPickerItem

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
    api_instance = connectwise_psa.CompanyPickerItemsApi(api_client)
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
        # Get Count of CompanyPickerItem
        api_response = api_instance.get_company_company_picker_items_count(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of CompanyPickerItemsApi->get_company_company_picker_items_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompanyPickerItemsApi->get_company_company_picker_items_count: %s\n" % e)
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

# **post_company_company_picker_items**
> CompanyPickerItem post_company_company_picker_items(client_id, company_picker_item)

Post CompanyPickerItem

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.company_picker_item import CompanyPickerItem
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
    api_instance = connectwise_psa.CompanyPickerItemsApi(api_client)
    client_id = 'client_id_example' # str | 
    company_picker_item = connectwise_psa.CompanyPickerItem() # CompanyPickerItem | companyPickerItem

    try:
        # Post CompanyPickerItem
        api_response = api_instance.post_company_company_picker_items(client_id, company_picker_item)
        print("The response of CompanyPickerItemsApi->post_company_company_picker_items:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompanyPickerItemsApi->post_company_company_picker_items: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**|  | 
 **company_picker_item** | [**CompanyPickerItem**](CompanyPickerItem.md)| companyPickerItem | 

### Return type

[**CompanyPickerItem**](CompanyPickerItem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | CompanyPickerItem |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_company_company_picker_items_clear**
> ClearPickerRequest post_company_company_picker_items_clear(client_id, clear_picker_request)

Post ClearPickerRequest

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.clear_picker_request import ClearPickerRequest
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
    api_instance = connectwise_psa.CompanyPickerItemsApi(api_client)
    client_id = 'client_id_example' # str | 
    clear_picker_request = connectwise_psa.ClearPickerRequest() # ClearPickerRequest | clearPickerRequest

    try:
        # Post ClearPickerRequest
        api_response = api_instance.post_company_company_picker_items_clear(client_id, clear_picker_request)
        print("The response of CompanyPickerItemsApi->post_company_company_picker_items_clear:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompanyPickerItemsApi->post_company_company_picker_items_clear: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**|  | 
 **clear_picker_request** | [**ClearPickerRequest**](.md)| clearPickerRequest | 

### Return type

[**ClearPickerRequest**](ClearPickerRequest.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | ClearPickerRequest |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

