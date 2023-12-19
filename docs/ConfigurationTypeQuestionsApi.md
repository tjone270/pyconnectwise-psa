# connectwise_psa.ConfigurationTypeQuestionsApi

All URIs are relative to *https://api-aus.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_company_configurations_types_by_parent_id_questions_by_id**](ConfigurationTypeQuestionsApi.md#delete_company_configurations_types_by_parent_id_questions_by_id) | **DELETE** /company/configurations/types/{parentId}/questions/{id} | Delete ConfigurationTypeQuestion
[**get_company_configurations_types_by_parent_id_questions**](ConfigurationTypeQuestionsApi.md#get_company_configurations_types_by_parent_id_questions) | **GET** /company/configurations/types/{parentId}/questions | Get List of ConfigurationTypeQuestion
[**get_company_configurations_types_by_parent_id_questions_by_id**](ConfigurationTypeQuestionsApi.md#get_company_configurations_types_by_parent_id_questions_by_id) | **GET** /company/configurations/types/{parentId}/questions/{id} | Get ConfigurationTypeQuestion
[**get_company_configurations_types_by_parent_id_questions_count**](ConfigurationTypeQuestionsApi.md#get_company_configurations_types_by_parent_id_questions_count) | **GET** /company/configurations/types/{parentId}/questions/count | Get Count of ConfigurationTypeQuestion
[**patch_company_configurations_types_by_parent_id_questions_by_id**](ConfigurationTypeQuestionsApi.md#patch_company_configurations_types_by_parent_id_questions_by_id) | **PATCH** /company/configurations/types/{parentId}/questions/{id} | Patch ConfigurationTypeQuestion
[**post_company_configurations_types_by_parent_id_questions**](ConfigurationTypeQuestionsApi.md#post_company_configurations_types_by_parent_id_questions) | **POST** /company/configurations/types/{parentId}/questions | Post ConfigurationTypeQuestion
[**put_company_configurations_types_by_parent_id_questions_by_id**](ConfigurationTypeQuestionsApi.md#put_company_configurations_types_by_parent_id_questions_by_id) | **PUT** /company/configurations/types/{parentId}/questions/{id} | Put ConfigurationTypeQuestion


# **delete_company_configurations_types_by_parent_id_questions_by_id**
> delete_company_configurations_types_by_parent_id_questions_by_id(id, parent_id, client_id)

Delete ConfigurationTypeQuestion

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
    api_instance = connectwise_psa.ConfigurationTypeQuestionsApi(api_client)
    id = 56 # int | questionId
    parent_id = 56 # int | typeId
    client_id = 'client_id_example' # str | 

    try:
        # Delete ConfigurationTypeQuestion
        api_instance.delete_company_configurations_types_by_parent_id_questions_by_id(id, parent_id, client_id)
    except Exception as e:
        print("Exception when calling ConfigurationTypeQuestionsApi->delete_company_configurations_types_by_parent_id_questions_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| questionId | 
 **parent_id** | **int**| typeId | 
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

# **get_company_configurations_types_by_parent_id_questions**
> List[ConfigurationTypeQuestion] get_company_configurations_types_by_parent_id_questions(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of ConfigurationTypeQuestion

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.configuration_type_question import ConfigurationTypeQuestion
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
    api_instance = connectwise_psa.ConfigurationTypeQuestionsApi(api_client)
    parent_id = 56 # int | typeId
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
        # Get List of ConfigurationTypeQuestion
        api_response = api_instance.get_company_configurations_types_by_parent_id_questions(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of ConfigurationTypeQuestionsApi->get_company_configurations_types_by_parent_id_questions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationTypeQuestionsApi->get_company_configurations_types_by_parent_id_questions: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| typeId | 
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

[**List[ConfigurationTypeQuestion]**](ConfigurationTypeQuestion.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of ConfigurationTypeQuestion |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_company_configurations_types_by_parent_id_questions_by_id**
> ConfigurationTypeQuestion get_company_configurations_types_by_parent_id_questions_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get ConfigurationTypeQuestion

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.configuration_type_question import ConfigurationTypeQuestion
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
    api_instance = connectwise_psa.ConfigurationTypeQuestionsApi(api_client)
    id = 56 # int | questionId
    parent_id = 56 # int | typeId
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
        # Get ConfigurationTypeQuestion
        api_response = api_instance.get_company_configurations_types_by_parent_id_questions_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of ConfigurationTypeQuestionsApi->get_company_configurations_types_by_parent_id_questions_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationTypeQuestionsApi->get_company_configurations_types_by_parent_id_questions_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| questionId | 
 **parent_id** | **int**| typeId | 
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

[**ConfigurationTypeQuestion**](ConfigurationTypeQuestion.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ConfigurationTypeQuestion |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_company_configurations_types_by_parent_id_questions_count**
> Count get_company_configurations_types_by_parent_id_questions_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Count of ConfigurationTypeQuestion

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
    api_instance = connectwise_psa.ConfigurationTypeQuestionsApi(api_client)
    parent_id = 56 # int | typeId
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
        # Get Count of ConfigurationTypeQuestion
        api_response = api_instance.get_company_configurations_types_by_parent_id_questions_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of ConfigurationTypeQuestionsApi->get_company_configurations_types_by_parent_id_questions_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationTypeQuestionsApi->get_company_configurations_types_by_parent_id_questions_count: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| typeId | 
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

# **patch_company_configurations_types_by_parent_id_questions_by_id**
> ConfigurationTypeQuestion patch_company_configurations_types_by_parent_id_questions_by_id(id, parent_id, client_id, patch_operation)

Patch ConfigurationTypeQuestion

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.configuration_type_question import ConfigurationTypeQuestion
from connectwise_psa.models.patch_operation import PatchOperation
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
    api_instance = connectwise_psa.ConfigurationTypeQuestionsApi(api_client)
    id = 56 # int | questionId
    parent_id = 56 # int | typeId
    client_id = 'client_id_example' # str | 
    patch_operation = [connectwise_psa.PatchOperation()] # List[PatchOperation] | List of PatchOperation

    try:
        # Patch ConfigurationTypeQuestion
        api_response = api_instance.patch_company_configurations_types_by_parent_id_questions_by_id(id, parent_id, client_id, patch_operation)
        print("The response of ConfigurationTypeQuestionsApi->patch_company_configurations_types_by_parent_id_questions_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationTypeQuestionsApi->patch_company_configurations_types_by_parent_id_questions_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| questionId | 
 **parent_id** | **int**| typeId | 
 **client_id** | **str**|  | 
 **patch_operation** | [**List[PatchOperation]**](PatchOperation.md)| List of PatchOperation | 

### Return type

[**ConfigurationTypeQuestion**](ConfigurationTypeQuestion.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ConfigurationTypeQuestion |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_company_configurations_types_by_parent_id_questions**
> ConfigurationTypeQuestion post_company_configurations_types_by_parent_id_questions(parent_id, client_id, configuration_type_question)

Post ConfigurationTypeQuestion

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.configuration_type_question import ConfigurationTypeQuestion
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
    api_instance = connectwise_psa.ConfigurationTypeQuestionsApi(api_client)
    parent_id = 56 # int | typeId
    client_id = 'client_id_example' # str | 
    configuration_type_question = connectwise_psa.ConfigurationTypeQuestion() # ConfigurationTypeQuestion | configurationTypeQuestion

    try:
        # Post ConfigurationTypeQuestion
        api_response = api_instance.post_company_configurations_types_by_parent_id_questions(parent_id, client_id, configuration_type_question)
        print("The response of ConfigurationTypeQuestionsApi->post_company_configurations_types_by_parent_id_questions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationTypeQuestionsApi->post_company_configurations_types_by_parent_id_questions: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| typeId | 
 **client_id** | **str**|  | 
 **configuration_type_question** | [**ConfigurationTypeQuestion**](ConfigurationTypeQuestion.md)| configurationTypeQuestion | 

### Return type

[**ConfigurationTypeQuestion**](ConfigurationTypeQuestion.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | ConfigurationTypeQuestion |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_company_configurations_types_by_parent_id_questions_by_id**
> ConfigurationTypeQuestion put_company_configurations_types_by_parent_id_questions_by_id(id, parent_id, client_id, configuration_type_question)

Put ConfigurationTypeQuestion

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.configuration_type_question import ConfigurationTypeQuestion
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
    api_instance = connectwise_psa.ConfigurationTypeQuestionsApi(api_client)
    id = 56 # int | questionId
    parent_id = 56 # int | typeId
    client_id = 'client_id_example' # str | 
    configuration_type_question = connectwise_psa.ConfigurationTypeQuestion() # ConfigurationTypeQuestion | configurationTypeQuestion

    try:
        # Put ConfigurationTypeQuestion
        api_response = api_instance.put_company_configurations_types_by_parent_id_questions_by_id(id, parent_id, client_id, configuration_type_question)
        print("The response of ConfigurationTypeQuestionsApi->put_company_configurations_types_by_parent_id_questions_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationTypeQuestionsApi->put_company_configurations_types_by_parent_id_questions_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| questionId | 
 **parent_id** | **int**| typeId | 
 **client_id** | **str**|  | 
 **configuration_type_question** | [**ConfigurationTypeQuestion**](ConfigurationTypeQuestion.md)| configurationTypeQuestion | 

### Return type

[**ConfigurationTypeQuestion**](ConfigurationTypeQuestion.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ConfigurationTypeQuestion |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

