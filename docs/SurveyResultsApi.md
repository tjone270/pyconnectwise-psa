# connectwise_psa.SurveyResultsApi

All URIs are relative to *https://aus-api.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_service_surveys_by_parent_id_results_by_id**](SurveyResultsApi.md#delete_service_surveys_by_parent_id_results_by_id) | **DELETE** /service/surveys/{parentId}/results/{id} | Delete SurveyResult
[**get_service_surveys_by_parent_id_results**](SurveyResultsApi.md#get_service_surveys_by_parent_id_results) | **GET** /service/surveys/{parentId}/results | Get List of SurveyResult
[**get_service_surveys_by_parent_id_results_by_id**](SurveyResultsApi.md#get_service_surveys_by_parent_id_results_by_id) | **GET** /service/surveys/{parentId}/results/{id} | Get SurveyResult
[**get_service_surveys_by_parent_id_results_count**](SurveyResultsApi.md#get_service_surveys_by_parent_id_results_count) | **GET** /service/surveys/{parentId}/results/count | Get Count of SurveyResult
[**patch_service_surveys_by_parent_id_results_by_id**](SurveyResultsApi.md#patch_service_surveys_by_parent_id_results_by_id) | **PATCH** /service/surveys/{parentId}/results/{id} | Patch SurveyResult
[**post_service_surveys_by_parent_id_results**](SurveyResultsApi.md#post_service_surveys_by_parent_id_results) | **POST** /service/surveys/{parentId}/results | Post SurveyResult
[**put_service_surveys_by_parent_id_results_by_id**](SurveyResultsApi.md#put_service_surveys_by_parent_id_results_by_id) | **PUT** /service/surveys/{parentId}/results/{id} | Put SurveyResult


# **delete_service_surveys_by_parent_id_results_by_id**
> delete_service_surveys_by_parent_id_results_by_id(id, parent_id, client_id)

Delete SurveyResult

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
    api_instance = connectwise_psa.SurveyResultsApi(api_client)
    id = 56 # int | resultId
    parent_id = 56 # int | surveyId
    client_id = 'client_id_example' # str | 

    try:
        # Delete SurveyResult
        api_instance.delete_service_surveys_by_parent_id_results_by_id(id, parent_id, client_id)
    except Exception as e:
        print("Exception when calling SurveyResultsApi->delete_service_surveys_by_parent_id_results_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| resultId | 
 **parent_id** | **int**| surveyId | 
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

# **get_service_surveys_by_parent_id_results**
> List[SurveyResult] get_service_surveys_by_parent_id_results(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of SurveyResult

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.survey_result import SurveyResult
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
    api_instance = connectwise_psa.SurveyResultsApi(api_client)
    parent_id = 56 # int | surveyId
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
        # Get List of SurveyResult
        api_response = api_instance.get_service_surveys_by_parent_id_results(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of SurveyResultsApi->get_service_surveys_by_parent_id_results:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SurveyResultsApi->get_service_surveys_by_parent_id_results: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| surveyId | 
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

[**List[SurveyResult]**](SurveyResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of SurveyResult |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_service_surveys_by_parent_id_results_by_id**
> SurveyResult get_service_surveys_by_parent_id_results_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get SurveyResult

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.survey_result import SurveyResult
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
    api_instance = connectwise_psa.SurveyResultsApi(api_client)
    id = 56 # int | resultId
    parent_id = 56 # int | surveyId
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
        # Get SurveyResult
        api_response = api_instance.get_service_surveys_by_parent_id_results_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of SurveyResultsApi->get_service_surveys_by_parent_id_results_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SurveyResultsApi->get_service_surveys_by_parent_id_results_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| resultId | 
 **parent_id** | **int**| surveyId | 
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

[**SurveyResult**](SurveyResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | SurveyResult |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_service_surveys_by_parent_id_results_count**
> Count get_service_surveys_by_parent_id_results_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Count of SurveyResult

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
    api_instance = connectwise_psa.SurveyResultsApi(api_client)
    parent_id = 56 # int | surveyId
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
        # Get Count of SurveyResult
        api_response = api_instance.get_service_surveys_by_parent_id_results_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of SurveyResultsApi->get_service_surveys_by_parent_id_results_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SurveyResultsApi->get_service_surveys_by_parent_id_results_count: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| surveyId | 
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

# **patch_service_surveys_by_parent_id_results_by_id**
> SurveyResult patch_service_surveys_by_parent_id_results_by_id(id, parent_id, client_id, patch_operation)

Patch SurveyResult

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.patch_operation import PatchOperation
from connectwise_psa.models.survey_result import SurveyResult
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
    api_instance = connectwise_psa.SurveyResultsApi(api_client)
    id = 56 # int | resultId
    parent_id = 56 # int | surveyId
    client_id = 'client_id_example' # str | 
    patch_operation = [connectwise_psa.PatchOperation()] # List[PatchOperation] | List of PatchOperation

    try:
        # Patch SurveyResult
        api_response = api_instance.patch_service_surveys_by_parent_id_results_by_id(id, parent_id, client_id, patch_operation)
        print("The response of SurveyResultsApi->patch_service_surveys_by_parent_id_results_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SurveyResultsApi->patch_service_surveys_by_parent_id_results_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| resultId | 
 **parent_id** | **int**| surveyId | 
 **client_id** | **str**|  | 
 **patch_operation** | [**List[PatchOperation]**](PatchOperation.md)| List of PatchOperation | 

### Return type

[**SurveyResult**](SurveyResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | SurveyResult |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_service_surveys_by_parent_id_results**
> SurveyResult post_service_surveys_by_parent_id_results(parent_id, client_id, survey_result)

Post SurveyResult

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.survey_result import SurveyResult
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
    api_instance = connectwise_psa.SurveyResultsApi(api_client)
    parent_id = 56 # int | surveyId
    client_id = 'client_id_example' # str | 
    survey_result = connectwise_psa.SurveyResult() # SurveyResult | surveyResult

    try:
        # Post SurveyResult
        api_response = api_instance.post_service_surveys_by_parent_id_results(parent_id, client_id, survey_result)
        print("The response of SurveyResultsApi->post_service_surveys_by_parent_id_results:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SurveyResultsApi->post_service_surveys_by_parent_id_results: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| surveyId | 
 **client_id** | **str**|  | 
 **survey_result** | [**SurveyResult**](SurveyResult.md)| surveyResult | 

### Return type

[**SurveyResult**](SurveyResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | SurveyResult |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_service_surveys_by_parent_id_results_by_id**
> SurveyResult put_service_surveys_by_parent_id_results_by_id(id, parent_id, client_id, survey_result)

Put SurveyResult

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.survey_result import SurveyResult
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
    api_instance = connectwise_psa.SurveyResultsApi(api_client)
    id = 56 # int | resultId
    parent_id = 56 # int | surveyId
    client_id = 'client_id_example' # str | 
    survey_result = connectwise_psa.SurveyResult() # SurveyResult | surveyResult

    try:
        # Put SurveyResult
        api_response = api_instance.put_service_surveys_by_parent_id_results_by_id(id, parent_id, client_id, survey_result)
        print("The response of SurveyResultsApi->put_service_surveys_by_parent_id_results_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SurveyResultsApi->put_service_surveys_by_parent_id_results_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| resultId | 
 **parent_id** | **int**| surveyId | 
 **client_id** | **str**|  | 
 **survey_result** | [**SurveyResult**](SurveyResult.md)| surveyResult | 

### Return type

[**SurveyResult**](SurveyResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | SurveyResult |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

