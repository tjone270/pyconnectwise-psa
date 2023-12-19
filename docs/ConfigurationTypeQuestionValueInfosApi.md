# connectwise_psa.ConfigurationTypeQuestionValueInfosApi

All URIs are relative to *https://api-aus.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_configurations_types_by_grandparent_id_questions_by_parent_id_values_by_id_info**](ConfigurationTypeQuestionValueInfosApi.md#get_configurations_types_by_grandparent_id_questions_by_parent_id_values_by_id_info) | **GET** /configurations/types/{grandparentId}/questions/{parentId}/values/{id}/info | Get ConfigurationTypeQuestionValueInfo
[**get_configurations_types_by_grandparent_id_questions_by_parent_id_values_info**](ConfigurationTypeQuestionValueInfosApi.md#get_configurations_types_by_grandparent_id_questions_by_parent_id_values_info) | **GET** /configurations/types/{grandparentId}/questions/{parentId}/values/info | Get ConfigurationTypeQuestionValueInfo
[**get_configurations_types_by_grandparent_id_questions_by_parent_id_values_info_count**](ConfigurationTypeQuestionValueInfosApi.md#get_configurations_types_by_grandparent_id_questions_by_parent_id_values_info_count) | **GET** /configurations/types/{grandparentId}/questions/{parentId}/values/info/count | Get Count of ConfigurationTypeQuestionValueInfos


# **get_configurations_types_by_grandparent_id_questions_by_parent_id_values_by_id_info**
> ConfigurationTypeQuestionInfo get_configurations_types_by_grandparent_id_questions_by_parent_id_values_by_id_info(grandparent_id, parent_id, id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get ConfigurationTypeQuestionValueInfo

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.configuration_type_question_info import ConfigurationTypeQuestionInfo
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
    api_instance = connectwise_psa.ConfigurationTypeQuestionValueInfosApi(api_client)
    grandparent_id = 56 # int | ConfigurationTypeQuestionInfo
    parent_id = 56 # int | ConfigurationTypeQuestionInfo
    id = 56 # int | ConfigurationTypeQuestionInfo
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
        # Get ConfigurationTypeQuestionValueInfo
        api_response = api_instance.get_configurations_types_by_grandparent_id_questions_by_parent_id_values_by_id_info(grandparent_id, parent_id, id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of ConfigurationTypeQuestionValueInfosApi->get_configurations_types_by_grandparent_id_questions_by_parent_id_values_by_id_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationTypeQuestionValueInfosApi->get_configurations_types_by_grandparent_id_questions_by_parent_id_values_by_id_info: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **grandparent_id** | **int**| ConfigurationTypeQuestionInfo | 
 **parent_id** | **int**| ConfigurationTypeQuestionInfo | 
 **id** | **int**| ConfigurationTypeQuestionInfo | 
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

[**ConfigurationTypeQuestionInfo**](ConfigurationTypeQuestionInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ConfigurationTypeQuestionInfo |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_configurations_types_by_grandparent_id_questions_by_parent_id_values_info**
> List[ConfigurationTypeQuestionValueInfo] get_configurations_types_by_grandparent_id_questions_by_parent_id_values_info(grandparent_id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get ConfigurationTypeQuestionValueInfo

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.configuration_type_question_value_info import ConfigurationTypeQuestionValueInfo
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
    api_instance = connectwise_psa.ConfigurationTypeQuestionValueInfosApi(api_client)
    grandparent_id = 56 # int | ConfigurationTypeQuestionValueInfo
    parent_id = 56 # int | ConfigurationTypeQuestionValueInfo
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
        # Get ConfigurationTypeQuestionValueInfo
        api_response = api_instance.get_configurations_types_by_grandparent_id_questions_by_parent_id_values_info(grandparent_id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of ConfigurationTypeQuestionValueInfosApi->get_configurations_types_by_grandparent_id_questions_by_parent_id_values_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationTypeQuestionValueInfosApi->get_configurations_types_by_grandparent_id_questions_by_parent_id_values_info: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **grandparent_id** | **int**| ConfigurationTypeQuestionValueInfo | 
 **parent_id** | **int**| ConfigurationTypeQuestionValueInfo | 
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

[**List[ConfigurationTypeQuestionValueInfo]**](ConfigurationTypeQuestionValueInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of ConfigurationTypeQuestionInfos |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_configurations_types_by_grandparent_id_questions_by_parent_id_values_info_count**
> Count get_configurations_types_by_grandparent_id_questions_by_parent_id_values_info_count(grandparent_id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Count of ConfigurationTypeQuestionValueInfos

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
    api_instance = connectwise_psa.ConfigurationTypeQuestionValueInfosApi(api_client)
    grandparent_id = 56 # int | ConfigurationTypeQuestionValueInfo
    parent_id = 56 # int | ConfigurationTypeQuestionValueInfo
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
        # Get Count of ConfigurationTypeQuestionValueInfos
        api_response = api_instance.get_configurations_types_by_grandparent_id_questions_by_parent_id_values_info_count(grandparent_id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of ConfigurationTypeQuestionValueInfosApi->get_configurations_types_by_grandparent_id_questions_by_parent_id_values_info_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationTypeQuestionValueInfosApi->get_configurations_types_by_grandparent_id_questions_by_parent_id_values_info_count: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **grandparent_id** | **int**| ConfigurationTypeQuestionValueInfo | 
 **parent_id** | **int**| ConfigurationTypeQuestionValueInfo | 
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

