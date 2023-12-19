# connectwise_psa.ConfigurationTypeQuestionValuesApi

All URIs are relative to *https://aus-api.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_company_configurations_types_by_grandparent_id_questions_by_parent_id_values_by_id**](ConfigurationTypeQuestionValuesApi.md#delete_company_configurations_types_by_grandparent_id_questions_by_parent_id_values_by_id) | **DELETE** /company/configurations/types/{grandparentId}/questions/{parentId}/values/{id} | Delete ConfigurationTypeQuestionValue
[**get_company_configurations_types_by_grandparent_id_questions_by_parent_id_values**](ConfigurationTypeQuestionValuesApi.md#get_company_configurations_types_by_grandparent_id_questions_by_parent_id_values) | **GET** /company/configurations/types/{grandparentId}/questions/{parentId}/values | Get List of ConfigurationTypeQuestionValue
[**get_company_configurations_types_by_grandparent_id_questions_by_parent_id_values_by_id**](ConfigurationTypeQuestionValuesApi.md#get_company_configurations_types_by_grandparent_id_questions_by_parent_id_values_by_id) | **GET** /company/configurations/types/{grandparentId}/questions/{parentId}/values/{id} | Get ConfigurationTypeQuestionValue
[**get_company_configurations_types_by_grandparent_id_questions_by_parent_id_values_by_id_usages**](ConfigurationTypeQuestionValuesApi.md#get_company_configurations_types_by_grandparent_id_questions_by_parent_id_values_by_id_usages) | **GET** /company/configurations/types/{grandparentId}/questions/{parentId}/values/{id}/usages | Get List of Usage
[**get_company_configurations_types_by_grandparent_id_questions_by_parent_id_values_by_id_usages_list**](ConfigurationTypeQuestionValuesApi.md#get_company_configurations_types_by_grandparent_id_questions_by_parent_id_values_by_id_usages_list) | **GET** /company/configurations/types/{grandparentId}/questions/{parentId}/values/{id}/usages/list | Get List of Usage
[**get_company_configurations_types_by_grandparent_id_questions_by_parent_id_values_count**](ConfigurationTypeQuestionValuesApi.md#get_company_configurations_types_by_grandparent_id_questions_by_parent_id_values_count) | **GET** /company/configurations/types/{grandparentId}/questions/{parentId}/values/count | Get Count of ConfigurationTypeQuestionValue
[**patch_company_configurations_types_by_grandparent_id_questions_by_parent_id_values_by_id**](ConfigurationTypeQuestionValuesApi.md#patch_company_configurations_types_by_grandparent_id_questions_by_parent_id_values_by_id) | **PATCH** /company/configurations/types/{grandparentId}/questions/{parentId}/values/{id} | Patch ConfigurationTypeQuestionValue
[**post_company_configurations_types_by_grandparent_id_questions_by_parent_id_values**](ConfigurationTypeQuestionValuesApi.md#post_company_configurations_types_by_grandparent_id_questions_by_parent_id_values) | **POST** /company/configurations/types/{grandparentId}/questions/{parentId}/values | Post ConfigurationTypeQuestionValue
[**put_company_configurations_types_by_grandparent_id_questions_by_parent_id_values_by_id**](ConfigurationTypeQuestionValuesApi.md#put_company_configurations_types_by_grandparent_id_questions_by_parent_id_values_by_id) | **PUT** /company/configurations/types/{grandparentId}/questions/{parentId}/values/{id} | Put ConfigurationTypeQuestionValue


# **delete_company_configurations_types_by_grandparent_id_questions_by_parent_id_values_by_id**
> delete_company_configurations_types_by_grandparent_id_questions_by_parent_id_values_by_id(id, parent_id, grandparent_id, client_id)

Delete ConfigurationTypeQuestionValue

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
    api_instance = connectwise_psa.ConfigurationTypeQuestionValuesApi(api_client)
    id = 56 # int | valueId
    parent_id = 56 # int | questionId
    grandparent_id = 56 # int | typeId
    client_id = 'client_id_example' # str | 

    try:
        # Delete ConfigurationTypeQuestionValue
        api_instance.delete_company_configurations_types_by_grandparent_id_questions_by_parent_id_values_by_id(id, parent_id, grandparent_id, client_id)
    except Exception as e:
        print("Exception when calling ConfigurationTypeQuestionValuesApi->delete_company_configurations_types_by_grandparent_id_questions_by_parent_id_values_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| valueId | 
 **parent_id** | **int**| questionId | 
 **grandparent_id** | **int**| typeId | 
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

# **get_company_configurations_types_by_grandparent_id_questions_by_parent_id_values**
> List[ConfigurationTypeQuestionValue] get_company_configurations_types_by_grandparent_id_questions_by_parent_id_values(parent_id, grandparent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of ConfigurationTypeQuestionValue

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.configuration_type_question_value import ConfigurationTypeQuestionValue
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
    api_instance = connectwise_psa.ConfigurationTypeQuestionValuesApi(api_client)
    parent_id = 56 # int | questionId
    grandparent_id = 56 # int | typeId
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
        # Get List of ConfigurationTypeQuestionValue
        api_response = api_instance.get_company_configurations_types_by_grandparent_id_questions_by_parent_id_values(parent_id, grandparent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of ConfigurationTypeQuestionValuesApi->get_company_configurations_types_by_grandparent_id_questions_by_parent_id_values:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationTypeQuestionValuesApi->get_company_configurations_types_by_grandparent_id_questions_by_parent_id_values: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| questionId | 
 **grandparent_id** | **int**| typeId | 
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

[**List[ConfigurationTypeQuestionValue]**](ConfigurationTypeQuestionValue.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of ConfigurationTypeQuestionValue |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_company_configurations_types_by_grandparent_id_questions_by_parent_id_values_by_id**
> ConfigurationTypeQuestionValue get_company_configurations_types_by_grandparent_id_questions_by_parent_id_values_by_id(id, parent_id, grandparent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get ConfigurationTypeQuestionValue

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.configuration_type_question_value import ConfigurationTypeQuestionValue
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
    api_instance = connectwise_psa.ConfigurationTypeQuestionValuesApi(api_client)
    id = 56 # int | valueId
    parent_id = 56 # int | questionId
    grandparent_id = 56 # int | typeId
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
        # Get ConfigurationTypeQuestionValue
        api_response = api_instance.get_company_configurations_types_by_grandparent_id_questions_by_parent_id_values_by_id(id, parent_id, grandparent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of ConfigurationTypeQuestionValuesApi->get_company_configurations_types_by_grandparent_id_questions_by_parent_id_values_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationTypeQuestionValuesApi->get_company_configurations_types_by_grandparent_id_questions_by_parent_id_values_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| valueId | 
 **parent_id** | **int**| questionId | 
 **grandparent_id** | **int**| typeId | 
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

[**ConfigurationTypeQuestionValue**](ConfigurationTypeQuestionValue.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ConfigurationTypeQuestionValue |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_company_configurations_types_by_grandparent_id_questions_by_parent_id_values_by_id_usages**
> List[Usage] get_company_configurations_types_by_grandparent_id_questions_by_parent_id_values_by_id_usages(id, parent_id, grandparent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of Usage

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.usage import Usage
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
    api_instance = connectwise_psa.ConfigurationTypeQuestionValuesApi(api_client)
    id = 56 # int | valueId
    parent_id = 56 # int | questionId
    grandparent_id = 56 # int | typeId
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
        # Get List of Usage
        api_response = api_instance.get_company_configurations_types_by_grandparent_id_questions_by_parent_id_values_by_id_usages(id, parent_id, grandparent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of ConfigurationTypeQuestionValuesApi->get_company_configurations_types_by_grandparent_id_questions_by_parent_id_values_by_id_usages:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationTypeQuestionValuesApi->get_company_configurations_types_by_grandparent_id_questions_by_parent_id_values_by_id_usages: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| valueId | 
 **parent_id** | **int**| questionId | 
 **grandparent_id** | **int**| typeId | 
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

[**List[Usage]**](Usage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of Usage |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_company_configurations_types_by_grandparent_id_questions_by_parent_id_values_by_id_usages_list**
> List[Usage] get_company_configurations_types_by_grandparent_id_questions_by_parent_id_values_by_id_usages_list(id, parent_id, grandparent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of Usage

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.usage import Usage
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
    api_instance = connectwise_psa.ConfigurationTypeQuestionValuesApi(api_client)
    id = 56 # int | valueId
    parent_id = 56 # int | questionId
    grandparent_id = 56 # int | typeId
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
        # Get List of Usage
        api_response = api_instance.get_company_configurations_types_by_grandparent_id_questions_by_parent_id_values_by_id_usages_list(id, parent_id, grandparent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of ConfigurationTypeQuestionValuesApi->get_company_configurations_types_by_grandparent_id_questions_by_parent_id_values_by_id_usages_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationTypeQuestionValuesApi->get_company_configurations_types_by_grandparent_id_questions_by_parent_id_values_by_id_usages_list: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| valueId | 
 **parent_id** | **int**| questionId | 
 **grandparent_id** | **int**| typeId | 
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

[**List[Usage]**](Usage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of Usage |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_company_configurations_types_by_grandparent_id_questions_by_parent_id_values_count**
> Count get_company_configurations_types_by_grandparent_id_questions_by_parent_id_values_count(parent_id, grandparent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Count of ConfigurationTypeQuestionValue

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
    api_instance = connectwise_psa.ConfigurationTypeQuestionValuesApi(api_client)
    parent_id = 56 # int | questionId
    grandparent_id = 56 # int | typeId
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
        # Get Count of ConfigurationTypeQuestionValue
        api_response = api_instance.get_company_configurations_types_by_grandparent_id_questions_by_parent_id_values_count(parent_id, grandparent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of ConfigurationTypeQuestionValuesApi->get_company_configurations_types_by_grandparent_id_questions_by_parent_id_values_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationTypeQuestionValuesApi->get_company_configurations_types_by_grandparent_id_questions_by_parent_id_values_count: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| questionId | 
 **grandparent_id** | **int**| typeId | 
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

# **patch_company_configurations_types_by_grandparent_id_questions_by_parent_id_values_by_id**
> ConfigurationTypeQuestionValue patch_company_configurations_types_by_grandparent_id_questions_by_parent_id_values_by_id(id, parent_id, grandparent_id, client_id, patch_operation)

Patch ConfigurationTypeQuestionValue

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.configuration_type_question_value import ConfigurationTypeQuestionValue
from connectwise_psa.models.patch_operation import PatchOperation
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
    api_instance = connectwise_psa.ConfigurationTypeQuestionValuesApi(api_client)
    id = 56 # int | valueId
    parent_id = 56 # int | questionId
    grandparent_id = 56 # int | typeId
    client_id = 'client_id_example' # str | 
    patch_operation = [connectwise_psa.PatchOperation()] # List[PatchOperation] | List of PatchOperation

    try:
        # Patch ConfigurationTypeQuestionValue
        api_response = api_instance.patch_company_configurations_types_by_grandparent_id_questions_by_parent_id_values_by_id(id, parent_id, grandparent_id, client_id, patch_operation)
        print("The response of ConfigurationTypeQuestionValuesApi->patch_company_configurations_types_by_grandparent_id_questions_by_parent_id_values_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationTypeQuestionValuesApi->patch_company_configurations_types_by_grandparent_id_questions_by_parent_id_values_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| valueId | 
 **parent_id** | **int**| questionId | 
 **grandparent_id** | **int**| typeId | 
 **client_id** | **str**|  | 
 **patch_operation** | [**List[PatchOperation]**](PatchOperation.md)| List of PatchOperation | 

### Return type

[**ConfigurationTypeQuestionValue**](ConfigurationTypeQuestionValue.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ConfigurationTypeQuestionValue |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_company_configurations_types_by_grandparent_id_questions_by_parent_id_values**
> ConfigurationTypeQuestionValue post_company_configurations_types_by_grandparent_id_questions_by_parent_id_values(parent_id, grandparent_id, client_id, configuration_type_question_value)

Post ConfigurationTypeQuestionValue

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.configuration_type_question_value import ConfigurationTypeQuestionValue
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
    api_instance = connectwise_psa.ConfigurationTypeQuestionValuesApi(api_client)
    parent_id = 56 # int | questionId
    grandparent_id = 56 # int | typeId
    client_id = 'client_id_example' # str | 
    configuration_type_question_value = connectwise_psa.ConfigurationTypeQuestionValue() # ConfigurationTypeQuestionValue | configurationTypeQuestionValue

    try:
        # Post ConfigurationTypeQuestionValue
        api_response = api_instance.post_company_configurations_types_by_grandparent_id_questions_by_parent_id_values(parent_id, grandparent_id, client_id, configuration_type_question_value)
        print("The response of ConfigurationTypeQuestionValuesApi->post_company_configurations_types_by_grandparent_id_questions_by_parent_id_values:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationTypeQuestionValuesApi->post_company_configurations_types_by_grandparent_id_questions_by_parent_id_values: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| questionId | 
 **grandparent_id** | **int**| typeId | 
 **client_id** | **str**|  | 
 **configuration_type_question_value** | [**ConfigurationTypeQuestionValue**](ConfigurationTypeQuestionValue.md)| configurationTypeQuestionValue | 

### Return type

[**ConfigurationTypeQuestionValue**](ConfigurationTypeQuestionValue.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | ConfigurationTypeQuestionValue |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_company_configurations_types_by_grandparent_id_questions_by_parent_id_values_by_id**
> ConfigurationTypeQuestionValue put_company_configurations_types_by_grandparent_id_questions_by_parent_id_values_by_id(id, parent_id, grandparent_id, client_id, configuration_type_question_value)

Put ConfigurationTypeQuestionValue

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.configuration_type_question_value import ConfigurationTypeQuestionValue
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
    api_instance = connectwise_psa.ConfigurationTypeQuestionValuesApi(api_client)
    id = 56 # int | valueId
    parent_id = 56 # int | questionId
    grandparent_id = 56 # int | typeId
    client_id = 'client_id_example' # str | 
    configuration_type_question_value = connectwise_psa.ConfigurationTypeQuestionValue() # ConfigurationTypeQuestionValue | configurationTypeQuestionValue

    try:
        # Put ConfigurationTypeQuestionValue
        api_response = api_instance.put_company_configurations_types_by_grandparent_id_questions_by_parent_id_values_by_id(id, parent_id, grandparent_id, client_id, configuration_type_question_value)
        print("The response of ConfigurationTypeQuestionValuesApi->put_company_configurations_types_by_grandparent_id_questions_by_parent_id_values_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigurationTypeQuestionValuesApi->put_company_configurations_types_by_grandparent_id_questions_by_parent_id_values_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| valueId | 
 **parent_id** | **int**| questionId | 
 **grandparent_id** | **int**| typeId | 
 **client_id** | **str**|  | 
 **configuration_type_question_value** | [**ConfigurationTypeQuestionValue**](ConfigurationTypeQuestionValue.md)| configurationTypeQuestionValue | 

### Return type

[**ConfigurationTypeQuestionValue**](ConfigurationTypeQuestionValue.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ConfigurationTypeQuestionValue |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

