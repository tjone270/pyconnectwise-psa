# connectwise_psa.ExpenseReportsApi

All URIs are relative to *https://aus-api.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_expense_reports**](ExpenseReportsApi.md#get_expense_reports) | **GET** /expense/reports | Get List of ExpenseReport
[**get_expense_reports_by_id**](ExpenseReportsApi.md#get_expense_reports_by_id) | **GET** /expense/reports/{id} | Get ExpenseReport
[**get_expense_reports_count**](ExpenseReportsApi.md#get_expense_reports_count) | **GET** /expense/reports/count | Get Count of ExpenseReport
[**post_expense_reports_by_id_approve**](ExpenseReportsApi.md#post_expense_reports_by_id_approve) | **POST** /expense/reports/{id}/approve | Post SuccessResponse
[**post_expense_reports_by_id_reject**](ExpenseReportsApi.md#post_expense_reports_by_id_reject) | **POST** /expense/reports/{id}/reject | Post SuccessResponse
[**post_expense_reports_by_id_reverse**](ExpenseReportsApi.md#post_expense_reports_by_id_reverse) | **POST** /expense/reports/{id}/reverse | Post SuccessResponse
[**post_expense_reports_by_id_submit**](ExpenseReportsApi.md#post_expense_reports_by_id_submit) | **POST** /expense/reports/{id}/submit | Post SuccessResponse


# **get_expense_reports**
> List[ExpenseReport] get_expense_reports(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of ExpenseReport

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.expense_report import ExpenseReport
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
    api_instance = connectwise_psa.ExpenseReportsApi(api_client)
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
        # Get List of ExpenseReport
        api_response = api_instance.get_expense_reports(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of ExpenseReportsApi->get_expense_reports:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExpenseReportsApi->get_expense_reports: %s\n" % e)
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

[**List[ExpenseReport]**](ExpenseReport.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of ExpenseReport |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_expense_reports_by_id**
> ExpenseReport get_expense_reports_by_id(id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get ExpenseReport

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.expense_report import ExpenseReport
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
    api_instance = connectwise_psa.ExpenseReportsApi(api_client)
    id = 56 # int | reportId
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
        # Get ExpenseReport
        api_response = api_instance.get_expense_reports_by_id(id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of ExpenseReportsApi->get_expense_reports_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExpenseReportsApi->get_expense_reports_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| reportId | 
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

[**ExpenseReport**](ExpenseReport.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ExpenseReport |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_expense_reports_count**
> Count get_expense_reports_count(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Count of ExpenseReport

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
    api_instance = connectwise_psa.ExpenseReportsApi(api_client)
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
        # Get Count of ExpenseReport
        api_response = api_instance.get_expense_reports_count(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of ExpenseReportsApi->get_expense_reports_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExpenseReportsApi->get_expense_reports_count: %s\n" % e)
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

# **post_expense_reports_by_id_approve**
> SuccessResponse post_expense_reports_by_id_approve(id, client_id, expense_report_tier_update)

Post SuccessResponse

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.expense_report_tier_update import ExpenseReportTierUpdate
from connectwise_psa.models.success_response import SuccessResponse
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
    api_instance = connectwise_psa.ExpenseReportsApi(api_client)
    id = 56 # int | reportId
    client_id = 'client_id_example' # str | 
    expense_report_tier_update = connectwise_psa.ExpenseReportTierUpdate() # ExpenseReportTierUpdate | reportId

    try:
        # Post SuccessResponse
        api_response = api_instance.post_expense_reports_by_id_approve(id, client_id, expense_report_tier_update)
        print("The response of ExpenseReportsApi->post_expense_reports_by_id_approve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExpenseReportsApi->post_expense_reports_by_id_approve: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| reportId | 
 **client_id** | **str**|  | 
 **expense_report_tier_update** | [**ExpenseReportTierUpdate**](ExpenseReportTierUpdate.md)| reportId | 

### Return type

[**SuccessResponse**](SuccessResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | SuccessResponse |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_expense_reports_by_id_reject**
> SuccessResponse post_expense_reports_by_id_reject(id, client_id)

Post SuccessResponse

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.success_response import SuccessResponse
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
    api_instance = connectwise_psa.ExpenseReportsApi(api_client)
    id = 56 # int | reportId
    client_id = 'client_id_example' # str | 

    try:
        # Post SuccessResponse
        api_response = api_instance.post_expense_reports_by_id_reject(id, client_id)
        print("The response of ExpenseReportsApi->post_expense_reports_by_id_reject:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExpenseReportsApi->post_expense_reports_by_id_reject: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| reportId | 
 **client_id** | **str**|  | 

### Return type

[**SuccessResponse**](SuccessResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | SuccessResponse |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_expense_reports_by_id_reverse**
> SuccessResponse post_expense_reports_by_id_reverse(id, client_id)

Post SuccessResponse

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.success_response import SuccessResponse
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
    api_instance = connectwise_psa.ExpenseReportsApi(api_client)
    id = 56 # int | reportId
    client_id = 'client_id_example' # str | 

    try:
        # Post SuccessResponse
        api_response = api_instance.post_expense_reports_by_id_reverse(id, client_id)
        print("The response of ExpenseReportsApi->post_expense_reports_by_id_reverse:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExpenseReportsApi->post_expense_reports_by_id_reverse: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| reportId | 
 **client_id** | **str**|  | 

### Return type

[**SuccessResponse**](SuccessResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | SuccessResponse |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_expense_reports_by_id_submit**
> SuccessResponse post_expense_reports_by_id_submit(id, client_id)

Post SuccessResponse

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.success_response import SuccessResponse
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
    api_instance = connectwise_psa.ExpenseReportsApi(api_client)
    id = 56 # int | reportId
    client_id = 'client_id_example' # str | 

    try:
        # Post SuccessResponse
        api_response = api_instance.post_expense_reports_by_id_submit(id, client_id)
        print("The response of ExpenseReportsApi->post_expense_reports_by_id_submit:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExpenseReportsApi->post_expense_reports_by_id_submit: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| reportId | 
 **client_id** | **str**|  | 

### Return type

[**SuccessResponse**](SuccessResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | SuccessResponse |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

