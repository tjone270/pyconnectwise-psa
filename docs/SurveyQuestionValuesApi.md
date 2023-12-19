# connectwise_psa.SurveyQuestionValuesApi

All URIs are relative to *https://aus-api.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_system_surveys_by_grandparent_id_questions_by_parent_id_values_by_id**](SurveyQuestionValuesApi.md#delete_system_surveys_by_grandparent_id_questions_by_parent_id_values_by_id) | **DELETE** /system/surveys/{grandparentId}/questions/{parentId}/values/{id} | Delete SurveyQuestionValue
[**get_system_surveys_by_grandparent_id_questions_by_parent_id_values**](SurveyQuestionValuesApi.md#get_system_surveys_by_grandparent_id_questions_by_parent_id_values) | **GET** /system/surveys/{grandparentId}/questions/{parentId}/values | Get List of SurveyQuestionValue
[**get_system_surveys_by_grandparent_id_questions_by_parent_id_values_by_id**](SurveyQuestionValuesApi.md#get_system_surveys_by_grandparent_id_questions_by_parent_id_values_by_id) | **GET** /system/surveys/{grandparentId}/questions/{parentId}/values/{id} | Get SurveyQuestionValue
[**patch_system_surveys_by_grandparent_id_questions_by_parent_id_values_by_id**](SurveyQuestionValuesApi.md#patch_system_surveys_by_grandparent_id_questions_by_parent_id_values_by_id) | **PATCH** /system/surveys/{grandparentId}/questions/{parentId}/values/{id} | Patch SurveyQuestionValue
[**post_system_surveys_by_grandparent_id_questions_by_parent_id_values**](SurveyQuestionValuesApi.md#post_system_surveys_by_grandparent_id_questions_by_parent_id_values) | **POST** /system/surveys/{grandparentId}/questions/{parentId}/values | Post SurveyQuestionValue
[**put_system_surveys_by_grandparent_id_questions_by_parent_id_values_by_id**](SurveyQuestionValuesApi.md#put_system_surveys_by_grandparent_id_questions_by_parent_id_values_by_id) | **PUT** /system/surveys/{grandparentId}/questions/{parentId}/values/{id} | Put SurveyQuestionValue


# **delete_system_surveys_by_grandparent_id_questions_by_parent_id_values_by_id**
> delete_system_surveys_by_grandparent_id_questions_by_parent_id_values_by_id(id, parent_id, grandparent_id, client_id)

Delete SurveyQuestionValue

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
    api_instance = connectwise_psa.SurveyQuestionValuesApi(api_client)
    id = 56 # int | valueId
    parent_id = 56 # int | questionId
    grandparent_id = 56 # int | surveyId
    client_id = 'client_id_example' # str | 

    try:
        # Delete SurveyQuestionValue
        api_instance.delete_system_surveys_by_grandparent_id_questions_by_parent_id_values_by_id(id, parent_id, grandparent_id, client_id)
    except Exception as e:
        print("Exception when calling SurveyQuestionValuesApi->delete_system_surveys_by_grandparent_id_questions_by_parent_id_values_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| valueId | 
 **parent_id** | **int**| questionId | 
 **grandparent_id** | **int**| surveyId | 
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

# **get_system_surveys_by_grandparent_id_questions_by_parent_id_values**
> List[SurveyQuestionValue] get_system_surveys_by_grandparent_id_questions_by_parent_id_values(parent_id, grandparent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of SurveyQuestionValue

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.survey_question_value import SurveyQuestionValue
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
    api_instance = connectwise_psa.SurveyQuestionValuesApi(api_client)
    parent_id = 56 # int | questionId
    grandparent_id = 56 # int | surveyId
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
        # Get List of SurveyQuestionValue
        api_response = api_instance.get_system_surveys_by_grandparent_id_questions_by_parent_id_values(parent_id, grandparent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of SurveyQuestionValuesApi->get_system_surveys_by_grandparent_id_questions_by_parent_id_values:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SurveyQuestionValuesApi->get_system_surveys_by_grandparent_id_questions_by_parent_id_values: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| questionId | 
 **grandparent_id** | **int**| surveyId | 
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

[**List[SurveyQuestionValue]**](SurveyQuestionValue.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of SurveyQuestionValue |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_system_surveys_by_grandparent_id_questions_by_parent_id_values_by_id**
> SurveyQuestionValue get_system_surveys_by_grandparent_id_questions_by_parent_id_values_by_id(id, parent_id, grandparent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get SurveyQuestionValue

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.survey_question_value import SurveyQuestionValue
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
    api_instance = connectwise_psa.SurveyQuestionValuesApi(api_client)
    id = 56 # int | valueId
    parent_id = 56 # int | questionId
    grandparent_id = 56 # int | surveyId
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
        # Get SurveyQuestionValue
        api_response = api_instance.get_system_surveys_by_grandparent_id_questions_by_parent_id_values_by_id(id, parent_id, grandparent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of SurveyQuestionValuesApi->get_system_surveys_by_grandparent_id_questions_by_parent_id_values_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SurveyQuestionValuesApi->get_system_surveys_by_grandparent_id_questions_by_parent_id_values_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| valueId | 
 **parent_id** | **int**| questionId | 
 **grandparent_id** | **int**| surveyId | 
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

[**SurveyQuestionValue**](SurveyQuestionValue.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | SurveyQuestionValue |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_system_surveys_by_grandparent_id_questions_by_parent_id_values_by_id**
> SurveyQuestionValue patch_system_surveys_by_grandparent_id_questions_by_parent_id_values_by_id(id, parent_id, grandparent_id, client_id, patch_operation)

Patch SurveyQuestionValue

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.patch_operation import PatchOperation
from connectwise_psa.models.survey_question_value import SurveyQuestionValue
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
    api_instance = connectwise_psa.SurveyQuestionValuesApi(api_client)
    id = 56 # int | valueId
    parent_id = 56 # int | questionId
    grandparent_id = 56 # int | surveyId
    client_id = 'client_id_example' # str | 
    patch_operation = [connectwise_psa.PatchOperation()] # List[PatchOperation] | List of PatchOperation

    try:
        # Patch SurveyQuestionValue
        api_response = api_instance.patch_system_surveys_by_grandparent_id_questions_by_parent_id_values_by_id(id, parent_id, grandparent_id, client_id, patch_operation)
        print("The response of SurveyQuestionValuesApi->patch_system_surveys_by_grandparent_id_questions_by_parent_id_values_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SurveyQuestionValuesApi->patch_system_surveys_by_grandparent_id_questions_by_parent_id_values_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| valueId | 
 **parent_id** | **int**| questionId | 
 **grandparent_id** | **int**| surveyId | 
 **client_id** | **str**|  | 
 **patch_operation** | [**List[PatchOperation]**](PatchOperation.md)| List of PatchOperation | 

### Return type

[**SurveyQuestionValue**](SurveyQuestionValue.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | SurveyQuestionValue |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_system_surveys_by_grandparent_id_questions_by_parent_id_values**
> SurveyQuestionValue post_system_surveys_by_grandparent_id_questions_by_parent_id_values(parent_id, grandparent_id, client_id, survey_question_value)

Post SurveyQuestionValue

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.survey_question_value import SurveyQuestionValue
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
    api_instance = connectwise_psa.SurveyQuestionValuesApi(api_client)
    parent_id = 56 # int | questionId
    grandparent_id = 56 # int | surveyId
    client_id = 'client_id_example' # str | 
    survey_question_value = connectwise_psa.SurveyQuestionValue() # SurveyQuestionValue | surveyQuestionValue

    try:
        # Post SurveyQuestionValue
        api_response = api_instance.post_system_surveys_by_grandparent_id_questions_by_parent_id_values(parent_id, grandparent_id, client_id, survey_question_value)
        print("The response of SurveyQuestionValuesApi->post_system_surveys_by_grandparent_id_questions_by_parent_id_values:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SurveyQuestionValuesApi->post_system_surveys_by_grandparent_id_questions_by_parent_id_values: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| questionId | 
 **grandparent_id** | **int**| surveyId | 
 **client_id** | **str**|  | 
 **survey_question_value** | [**SurveyQuestionValue**](SurveyQuestionValue.md)| surveyQuestionValue | 

### Return type

[**SurveyQuestionValue**](SurveyQuestionValue.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | SurveyQuestionValue |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_system_surveys_by_grandparent_id_questions_by_parent_id_values_by_id**
> SurveyQuestionValue put_system_surveys_by_grandparent_id_questions_by_parent_id_values_by_id(id, parent_id, grandparent_id, client_id, survey_question_value)

Put SurveyQuestionValue

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.survey_question_value import SurveyQuestionValue
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
    api_instance = connectwise_psa.SurveyQuestionValuesApi(api_client)
    id = 56 # int | valueId
    parent_id = 56 # int | questionId
    grandparent_id = 56 # int | surveyId
    client_id = 'client_id_example' # str | 
    survey_question_value = connectwise_psa.SurveyQuestionValue() # SurveyQuestionValue | surveyQuestionValue

    try:
        # Put SurveyQuestionValue
        api_response = api_instance.put_system_surveys_by_grandparent_id_questions_by_parent_id_values_by_id(id, parent_id, grandparent_id, client_id, survey_question_value)
        print("The response of SurveyQuestionValuesApi->put_system_surveys_by_grandparent_id_questions_by_parent_id_values_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SurveyQuestionValuesApi->put_system_surveys_by_grandparent_id_questions_by_parent_id_values_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| valueId | 
 **parent_id** | **int**| questionId | 
 **grandparent_id** | **int**| surveyId | 
 **client_id** | **str**|  | 
 **survey_question_value** | [**SurveyQuestionValue**](SurveyQuestionValue.md)| surveyQuestionValue | 

### Return type

[**SurveyQuestionValue**](SurveyQuestionValue.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | SurveyQuestionValue |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

