# connectwise_psa.CompanyNoteTypesApi

All URIs are relative to *https://api-aus.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_company_note_types_by_id**](CompanyNoteTypesApi.md#delete_company_note_types_by_id) | **DELETE** /company/noteTypes/{id} | Delete CompanyNoteType
[**get_company_note_types**](CompanyNoteTypesApi.md#get_company_note_types) | **GET** /company/noteTypes | Get List of CompanyNoteType
[**get_company_note_types_by_id**](CompanyNoteTypesApi.md#get_company_note_types_by_id) | **GET** /company/noteTypes/{id} | Get CompanyNoteType
[**get_company_note_types_count**](CompanyNoteTypesApi.md#get_company_note_types_count) | **GET** /company/noteTypes/count | Get Count of CompanyNoteType
[**patch_company_note_types_by_id**](CompanyNoteTypesApi.md#patch_company_note_types_by_id) | **PATCH** /company/noteTypes/{id} | Patch CompanyNoteType
[**post_company_note_types**](CompanyNoteTypesApi.md#post_company_note_types) | **POST** /company/noteTypes | Post CompanyNoteType
[**put_company_note_types_by_id**](CompanyNoteTypesApi.md#put_company_note_types_by_id) | **PUT** /company/noteTypes/{id} | Put CompanyNoteType


# **delete_company_note_types_by_id**
> delete_company_note_types_by_id(id, client_id)

Delete CompanyNoteType

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
    api_instance = connectwise_psa.CompanyNoteTypesApi(api_client)
    id = 56 # int | noteTypeId
    client_id = 'client_id_example' # str | 

    try:
        # Delete CompanyNoteType
        api_instance.delete_company_note_types_by_id(id, client_id)
    except Exception as e:
        print("Exception when calling CompanyNoteTypesApi->delete_company_note_types_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| noteTypeId | 
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

# **get_company_note_types**
> List[CompanyNoteType] get_company_note_types(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of CompanyNoteType

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.company_note_type import CompanyNoteType
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
    api_instance = connectwise_psa.CompanyNoteTypesApi(api_client)
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
        # Get List of CompanyNoteType
        api_response = api_instance.get_company_note_types(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of CompanyNoteTypesApi->get_company_note_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompanyNoteTypesApi->get_company_note_types: %s\n" % e)
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

[**List[CompanyNoteType]**](CompanyNoteType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of CompanyNoteType |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_company_note_types_by_id**
> CompanyNoteType get_company_note_types_by_id(id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get CompanyNoteType

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.company_note_type import CompanyNoteType
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
    api_instance = connectwise_psa.CompanyNoteTypesApi(api_client)
    id = 56 # int | noteTypeId
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
        # Get CompanyNoteType
        api_response = api_instance.get_company_note_types_by_id(id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of CompanyNoteTypesApi->get_company_note_types_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompanyNoteTypesApi->get_company_note_types_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| noteTypeId | 
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

[**CompanyNoteType**](CompanyNoteType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | CompanyNoteType |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_company_note_types_count**
> Count get_company_note_types_count(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Count of CompanyNoteType

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
    api_instance = connectwise_psa.CompanyNoteTypesApi(api_client)
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
        # Get Count of CompanyNoteType
        api_response = api_instance.get_company_note_types_count(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of CompanyNoteTypesApi->get_company_note_types_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompanyNoteTypesApi->get_company_note_types_count: %s\n" % e)
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

# **patch_company_note_types_by_id**
> CompanyNoteType patch_company_note_types_by_id(id, client_id, patch_operation)

Patch CompanyNoteType

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.company_note_type import CompanyNoteType
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
    api_instance = connectwise_psa.CompanyNoteTypesApi(api_client)
    id = 56 # int | noteTypeId
    client_id = 'client_id_example' # str | 
    patch_operation = [connectwise_psa.PatchOperation()] # List[PatchOperation] | List of PatchOperation

    try:
        # Patch CompanyNoteType
        api_response = api_instance.patch_company_note_types_by_id(id, client_id, patch_operation)
        print("The response of CompanyNoteTypesApi->patch_company_note_types_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompanyNoteTypesApi->patch_company_note_types_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| noteTypeId | 
 **client_id** | **str**|  | 
 **patch_operation** | [**List[PatchOperation]**](PatchOperation.md)| List of PatchOperation | 

### Return type

[**CompanyNoteType**](CompanyNoteType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | CompanyNoteType |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_company_note_types**
> CompanyNoteType post_company_note_types(client_id, company_note_type)

Post CompanyNoteType

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.company_note_type import CompanyNoteType
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
    api_instance = connectwise_psa.CompanyNoteTypesApi(api_client)
    client_id = 'client_id_example' # str | 
    company_note_type = connectwise_psa.CompanyNoteType() # CompanyNoteType | noteType

    try:
        # Post CompanyNoteType
        api_response = api_instance.post_company_note_types(client_id, company_note_type)
        print("The response of CompanyNoteTypesApi->post_company_note_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompanyNoteTypesApi->post_company_note_types: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**|  | 
 **company_note_type** | [**CompanyNoteType**](CompanyNoteType.md)| noteType | 

### Return type

[**CompanyNoteType**](CompanyNoteType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | CompanyNoteType |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_company_note_types_by_id**
> CompanyNoteType put_company_note_types_by_id(id, client_id, company_note_type)

Put CompanyNoteType

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.company_note_type import CompanyNoteType
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
    api_instance = connectwise_psa.CompanyNoteTypesApi(api_client)
    id = 56 # int | noteTypeId
    client_id = 'client_id_example' # str | 
    company_note_type = connectwise_psa.CompanyNoteType() # CompanyNoteType | noteType

    try:
        # Put CompanyNoteType
        api_response = api_instance.put_company_note_types_by_id(id, client_id, company_note_type)
        print("The response of CompanyNoteTypesApi->put_company_note_types_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompanyNoteTypesApi->put_company_note_types_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| noteTypeId | 
 **client_id** | **str**|  | 
 **company_note_type** | [**CompanyNoteType**](CompanyNoteType.md)| noteType | 

### Return type

[**CompanyNoteType**](CompanyNoteType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | CompanyNoteType |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

