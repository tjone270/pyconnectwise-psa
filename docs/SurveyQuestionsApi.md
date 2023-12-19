# connectwise_psa.SurveyQuestionsApi

All URIs are relative to *https://api-aus.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_system_surveys_by_parent_id_questions_by_id**](SurveyQuestionsApi.md#delete_system_surveys_by_parent_id_questions_by_id) | **DELETE** /system/surveys/{parentId}/questions/{id} | Delete SurveyQuestion
[**get_system_surveys_by_parent_id_questions**](SurveyQuestionsApi.md#get_system_surveys_by_parent_id_questions) | **GET** /system/surveys/{parentId}/questions | Get List of SurveyQuestion
[**get_system_surveys_by_parent_id_questions_by_id**](SurveyQuestionsApi.md#get_system_surveys_by_parent_id_questions_by_id) | **GET** /system/surveys/{parentId}/questions/{id} | Get SurveyQuestion
[**get_system_surveys_by_parent_id_questions_count**](SurveyQuestionsApi.md#get_system_surveys_by_parent_id_questions_count) | **GET** /system/surveys/{parentId}/questions/count | Get Count of SurveyQuestion
[**patch_system_surveys_by_parent_id_questions_by_id**](SurveyQuestionsApi.md#patch_system_surveys_by_parent_id_questions_by_id) | **PATCH** /system/surveys/{parentId}/questions/{id} | Patch SurveyQuestion
[**post_system_surveys_by_parent_id_questions**](SurveyQuestionsApi.md#post_system_surveys_by_parent_id_questions) | **POST** /system/surveys/{parentId}/questions | Post SurveyQuestion
[**put_system_surveys_by_parent_id_questions_by_id**](SurveyQuestionsApi.md#put_system_surveys_by_parent_id_questions_by_id) | **PUT** /system/surveys/{parentId}/questions/{id} | Put SurveyQuestion


# **delete_system_surveys_by_parent_id_questions_by_id**
> delete_system_surveys_by_parent_id_questions_by_id(id, parent_id, client_id)

Delete SurveyQuestion

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
    api_instance = connectwise_psa.SurveyQuestionsApi(api_client)
    id = 56 # int | questionId
    parent_id = 56 # int | surveyId
    client_id = 'client_id_example' # str | 

    try:
        # Delete SurveyQuestion
        api_instance.delete_system_surveys_by_parent_id_questions_by_id(id, parent_id, client_id)
    except Exception as e:
        print("Exception when calling SurveyQuestionsApi->delete_system_surveys_by_parent_id_questions_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| questionId | 
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

# **get_system_surveys_by_parent_id_questions**
> List[SurveyQuestion] get_system_surveys_by_parent_id_questions(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of SurveyQuestion

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.survey_question import SurveyQuestion
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
    api_instance = connectwise_psa.SurveyQuestionsApi(api_client)
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
        # Get List of SurveyQuestion
        api_response = api_instance.get_system_surveys_by_parent_id_questions(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of SurveyQuestionsApi->get_system_surveys_by_parent_id_questions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SurveyQuestionsApi->get_system_surveys_by_parent_id_questions: %s\n" % e)
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

[**List[SurveyQuestion]**](SurveyQuestion.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of SurveyQuestion |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_system_surveys_by_parent_id_questions_by_id**
> SurveyQuestion get_system_surveys_by_parent_id_questions_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get SurveyQuestion

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.survey_question import SurveyQuestion
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
    api_instance = connectwise_psa.SurveyQuestionsApi(api_client)
    id = 56 # int | questionId
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
        # Get SurveyQuestion
        api_response = api_instance.get_system_surveys_by_parent_id_questions_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of SurveyQuestionsApi->get_system_surveys_by_parent_id_questions_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SurveyQuestionsApi->get_system_surveys_by_parent_id_questions_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| questionId | 
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

[**SurveyQuestion**](SurveyQuestion.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | SurveyQuestion |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_system_surveys_by_parent_id_questions_count**
> Count get_system_surveys_by_parent_id_questions_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Count of SurveyQuestion

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
    api_instance = connectwise_psa.SurveyQuestionsApi(api_client)
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
        # Get Count of SurveyQuestion
        api_response = api_instance.get_system_surveys_by_parent_id_questions_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of SurveyQuestionsApi->get_system_surveys_by_parent_id_questions_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SurveyQuestionsApi->get_system_surveys_by_parent_id_questions_count: %s\n" % e)
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

# **patch_system_surveys_by_parent_id_questions_by_id**
> SurveyQuestion patch_system_surveys_by_parent_id_questions_by_id(id, parent_id, client_id, patch_operation)

Patch SurveyQuestion

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.patch_operation import PatchOperation
from connectwise_psa.models.survey_question import SurveyQuestion
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
    api_instance = connectwise_psa.SurveyQuestionsApi(api_client)
    id = 56 # int | questionId
    parent_id = 56 # int | surveyId
    client_id = 'client_id_example' # str | 
    patch_operation = [connectwise_psa.PatchOperation()] # List[PatchOperation] | List of PatchOperation

    try:
        # Patch SurveyQuestion
        api_response = api_instance.patch_system_surveys_by_parent_id_questions_by_id(id, parent_id, client_id, patch_operation)
        print("The response of SurveyQuestionsApi->patch_system_surveys_by_parent_id_questions_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SurveyQuestionsApi->patch_system_surveys_by_parent_id_questions_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| questionId | 
 **parent_id** | **int**| surveyId | 
 **client_id** | **str**|  | 
 **patch_operation** | [**List[PatchOperation]**](PatchOperation.md)| List of PatchOperation | 

### Return type

[**SurveyQuestion**](SurveyQuestion.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | SurveyQuestion |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_system_surveys_by_parent_id_questions**
> SurveyQuestion post_system_surveys_by_parent_id_questions(parent_id, client_id, survey_question)

Post SurveyQuestion

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.survey_question import SurveyQuestion
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
    api_instance = connectwise_psa.SurveyQuestionsApi(api_client)
    parent_id = 56 # int | surveyId
    client_id = 'client_id_example' # str | 
    survey_question = connectwise_psa.SurveyQuestion() # SurveyQuestion | surveyQuestion

    try:
        # Post SurveyQuestion
        api_response = api_instance.post_system_surveys_by_parent_id_questions(parent_id, client_id, survey_question)
        print("The response of SurveyQuestionsApi->post_system_surveys_by_parent_id_questions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SurveyQuestionsApi->post_system_surveys_by_parent_id_questions: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| surveyId | 
 **client_id** | **str**|  | 
 **survey_question** | [**SurveyQuestion**](SurveyQuestion.md)| surveyQuestion | 

### Return type

[**SurveyQuestion**](SurveyQuestion.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | SurveyQuestion |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_system_surveys_by_parent_id_questions_by_id**
> SurveyQuestion put_system_surveys_by_parent_id_questions_by_id(id, parent_id, client_id, survey_question)

Put SurveyQuestion

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.survey_question import SurveyQuestion
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
    api_instance = connectwise_psa.SurveyQuestionsApi(api_client)
    id = 56 # int | questionId
    parent_id = 56 # int | surveyId
    client_id = 'client_id_example' # str | 
    survey_question = connectwise_psa.SurveyQuestion() # SurveyQuestion | surveyQuestion

    try:
        # Put SurveyQuestion
        api_response = api_instance.put_system_surveys_by_parent_id_questions_by_id(id, parent_id, client_id, survey_question)
        print("The response of SurveyQuestionsApi->put_system_surveys_by_parent_id_questions_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SurveyQuestionsApi->put_system_surveys_by_parent_id_questions_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| questionId | 
 **parent_id** | **int**| surveyId | 
 **client_id** | **str**|  | 
 **survey_question** | [**SurveyQuestion**](SurveyQuestion.md)| surveyQuestion | 

### Return type

[**SurveyQuestion**](SurveyQuestion.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | SurveyQuestion |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

