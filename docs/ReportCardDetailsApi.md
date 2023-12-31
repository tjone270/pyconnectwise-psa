# connectwise_psa.ReportCardDetailsApi

All URIs are relative to *https://api-aus.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_system_report_cards_by_parent_id_details_by_id**](ReportCardDetailsApi.md#delete_system_report_cards_by_parent_id_details_by_id) | **DELETE** /system/reportCards/{parentId}/details/{id} | Delete ReportCardDetail
[**get_system_report_cards_by_parent_id_details**](ReportCardDetailsApi.md#get_system_report_cards_by_parent_id_details) | **GET** /system/reportCards/{parentId}/details | Get List of ReportCardDetail
[**get_system_report_cards_by_parent_id_details_by_id**](ReportCardDetailsApi.md#get_system_report_cards_by_parent_id_details_by_id) | **GET** /system/reportCards/{parentId}/details/{id} | Get ReportCardDetail
[**get_system_report_cards_by_parent_id_details_count**](ReportCardDetailsApi.md#get_system_report_cards_by_parent_id_details_count) | **GET** /system/reportCards/{parentId}/details/count | Get Count of ReportCardDetail
[**patch_system_report_cards_by_parent_id_details_by_id**](ReportCardDetailsApi.md#patch_system_report_cards_by_parent_id_details_by_id) | **PATCH** /system/reportCards/{parentId}/details/{id} | Patch ReportCardDetail
[**post_system_report_cards_by_parent_id_details**](ReportCardDetailsApi.md#post_system_report_cards_by_parent_id_details) | **POST** /system/reportCards/{parentId}/details | Post ReportCardDetail
[**put_system_report_cards_by_parent_id_details_by_id**](ReportCardDetailsApi.md#put_system_report_cards_by_parent_id_details_by_id) | **PUT** /system/reportCards/{parentId}/details/{id} | Put ReportCardDetail


# **delete_system_report_cards_by_parent_id_details_by_id**
> delete_system_report_cards_by_parent_id_details_by_id(id, parent_id, client_id)

Delete ReportCardDetail

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
    api_instance = connectwise_psa.ReportCardDetailsApi(api_client)
    id = 56 # int | detailId
    parent_id = 56 # int | reportCardId
    client_id = 'client_id_example' # str | 

    try:
        # Delete ReportCardDetail
        api_instance.delete_system_report_cards_by_parent_id_details_by_id(id, parent_id, client_id)
    except Exception as e:
        print("Exception when calling ReportCardDetailsApi->delete_system_report_cards_by_parent_id_details_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| detailId | 
 **parent_id** | **int**| reportCardId | 
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

# **get_system_report_cards_by_parent_id_details**
> List[ReportCardDetail] get_system_report_cards_by_parent_id_details(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of ReportCardDetail

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.report_card_detail import ReportCardDetail
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
    api_instance = connectwise_psa.ReportCardDetailsApi(api_client)
    parent_id = 56 # int | reportCardId
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
        # Get List of ReportCardDetail
        api_response = api_instance.get_system_report_cards_by_parent_id_details(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of ReportCardDetailsApi->get_system_report_cards_by_parent_id_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportCardDetailsApi->get_system_report_cards_by_parent_id_details: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| reportCardId | 
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

[**List[ReportCardDetail]**](ReportCardDetail.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of ReportCardDetail |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_system_report_cards_by_parent_id_details_by_id**
> ReportCardDetail get_system_report_cards_by_parent_id_details_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get ReportCardDetail

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.report_card_detail import ReportCardDetail
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
    api_instance = connectwise_psa.ReportCardDetailsApi(api_client)
    id = 56 # int | detailId
    parent_id = 56 # int | reportCardId
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
        # Get ReportCardDetail
        api_response = api_instance.get_system_report_cards_by_parent_id_details_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of ReportCardDetailsApi->get_system_report_cards_by_parent_id_details_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportCardDetailsApi->get_system_report_cards_by_parent_id_details_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| detailId | 
 **parent_id** | **int**| reportCardId | 
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

[**ReportCardDetail**](ReportCardDetail.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ReportCardDetail |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_system_report_cards_by_parent_id_details_count**
> Count get_system_report_cards_by_parent_id_details_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Count of ReportCardDetail

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
    api_instance = connectwise_psa.ReportCardDetailsApi(api_client)
    parent_id = 56 # int | reportCardId
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
        # Get Count of ReportCardDetail
        api_response = api_instance.get_system_report_cards_by_parent_id_details_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of ReportCardDetailsApi->get_system_report_cards_by_parent_id_details_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportCardDetailsApi->get_system_report_cards_by_parent_id_details_count: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| reportCardId | 
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

# **patch_system_report_cards_by_parent_id_details_by_id**
> ReportCardDetail patch_system_report_cards_by_parent_id_details_by_id(id, parent_id, client_id, patch_operation)

Patch ReportCardDetail

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.patch_operation import PatchOperation
from connectwise_psa.models.report_card_detail import ReportCardDetail
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
    api_instance = connectwise_psa.ReportCardDetailsApi(api_client)
    id = 56 # int | detailId
    parent_id = 56 # int | reportCardId
    client_id = 'client_id_example' # str | 
    patch_operation = [connectwise_psa.PatchOperation()] # List[PatchOperation] | List of PatchOperation

    try:
        # Patch ReportCardDetail
        api_response = api_instance.patch_system_report_cards_by_parent_id_details_by_id(id, parent_id, client_id, patch_operation)
        print("The response of ReportCardDetailsApi->patch_system_report_cards_by_parent_id_details_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportCardDetailsApi->patch_system_report_cards_by_parent_id_details_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| detailId | 
 **parent_id** | **int**| reportCardId | 
 **client_id** | **str**|  | 
 **patch_operation** | [**List[PatchOperation]**](PatchOperation.md)| List of PatchOperation | 

### Return type

[**ReportCardDetail**](ReportCardDetail.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ReportCardDetail |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_system_report_cards_by_parent_id_details**
> ReportCardDetail post_system_report_cards_by_parent_id_details(parent_id, client_id, report_card_detail)

Post ReportCardDetail

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.report_card_detail import ReportCardDetail
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
    api_instance = connectwise_psa.ReportCardDetailsApi(api_client)
    parent_id = 56 # int | reportCardId
    client_id = 'client_id_example' # str | 
    report_card_detail = connectwise_psa.ReportCardDetail() # ReportCardDetail | reportCardDetail

    try:
        # Post ReportCardDetail
        api_response = api_instance.post_system_report_cards_by_parent_id_details(parent_id, client_id, report_card_detail)
        print("The response of ReportCardDetailsApi->post_system_report_cards_by_parent_id_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportCardDetailsApi->post_system_report_cards_by_parent_id_details: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| reportCardId | 
 **client_id** | **str**|  | 
 **report_card_detail** | [**ReportCardDetail**](ReportCardDetail.md)| reportCardDetail | 

### Return type

[**ReportCardDetail**](ReportCardDetail.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | ReportCardDetail |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_system_report_cards_by_parent_id_details_by_id**
> ReportCardDetail put_system_report_cards_by_parent_id_details_by_id(id, parent_id, client_id, report_card_detail)

Put ReportCardDetail

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.report_card_detail import ReportCardDetail
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
    api_instance = connectwise_psa.ReportCardDetailsApi(api_client)
    id = 56 # int | detailId
    parent_id = 56 # int | reportCardId
    client_id = 'client_id_example' # str | 
    report_card_detail = connectwise_psa.ReportCardDetail() # ReportCardDetail | reportCardDetail

    try:
        # Put ReportCardDetail
        api_response = api_instance.put_system_report_cards_by_parent_id_details_by_id(id, parent_id, client_id, report_card_detail)
        print("The response of ReportCardDetailsApi->put_system_report_cards_by_parent_id_details_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportCardDetailsApi->put_system_report_cards_by_parent_id_details_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| detailId | 
 **parent_id** | **int**| reportCardId | 
 **client_id** | **str**|  | 
 **report_card_detail** | [**ReportCardDetail**](ReportCardDetail.md)| reportCardDetail | 

### Return type

[**ReportCardDetail**](ReportCardDetail.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ReportCardDetail |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

