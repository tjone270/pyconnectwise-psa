# connectwise_psa.AgreementAdditionsApi

All URIs are relative to *https://api-aus.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_finance_agreements_by_parent_id_additions_by_id**](AgreementAdditionsApi.md#delete_finance_agreements_by_parent_id_additions_by_id) | **DELETE** /finance/agreements/{parentId}/additions/{id} | Delete Addition
[**get_finance_agreements_by_parent_id_additions**](AgreementAdditionsApi.md#get_finance_agreements_by_parent_id_additions) | **GET** /finance/agreements/{parentId}/additions | Get List of Addition
[**get_finance_agreements_by_parent_id_additions_by_id**](AgreementAdditionsApi.md#get_finance_agreements_by_parent_id_additions_by_id) | **GET** /finance/agreements/{parentId}/additions/{id} | Get Addition
[**get_finance_agreements_by_parent_id_additions_count**](AgreementAdditionsApi.md#get_finance_agreements_by_parent_id_additions_count) | **GET** /finance/agreements/{parentId}/additions/count | Get Count of Addition
[**patch_finance_agreements_by_parent_id_additions_by_id**](AgreementAdditionsApi.md#patch_finance_agreements_by_parent_id_additions_by_id) | **PATCH** /finance/agreements/{parentId}/additions/{id} | Patch Addition
[**post_finance_agreements_by_parent_id_additions**](AgreementAdditionsApi.md#post_finance_agreements_by_parent_id_additions) | **POST** /finance/agreements/{parentId}/additions | Post Addition
[**put_finance_agreements_by_parent_id_additions_by_id**](AgreementAdditionsApi.md#put_finance_agreements_by_parent_id_additions_by_id) | **PUT** /finance/agreements/{parentId}/additions/{id} | Put Addition


# **delete_finance_agreements_by_parent_id_additions_by_id**
> delete_finance_agreements_by_parent_id_additions_by_id(id, parent_id, client_id)

Delete Addition

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
    api_instance = connectwise_psa.AgreementAdditionsApi(api_client)
    id = 56 # int | additionId
    parent_id = 56 # int | agreementId
    client_id = 'client_id_example' # str | 

    try:
        # Delete Addition
        api_instance.delete_finance_agreements_by_parent_id_additions_by_id(id, parent_id, client_id)
    except Exception as e:
        print("Exception when calling AgreementAdditionsApi->delete_finance_agreements_by_parent_id_additions_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| additionId | 
 **parent_id** | **int**| agreementId | 
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

# **get_finance_agreements_by_parent_id_additions**
> List[Addition] get_finance_agreements_by_parent_id_additions(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of Addition

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.addition import Addition
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
    api_instance = connectwise_psa.AgreementAdditionsApi(api_client)
    parent_id = 56 # int | agreementId
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
        # Get List of Addition
        api_response = api_instance.get_finance_agreements_by_parent_id_additions(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of AgreementAdditionsApi->get_finance_agreements_by_parent_id_additions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgreementAdditionsApi->get_finance_agreements_by_parent_id_additions: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| agreementId | 
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

[**List[Addition]**](Addition.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of Addition |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_finance_agreements_by_parent_id_additions_by_id**
> Addition get_finance_agreements_by_parent_id_additions_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Addition

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.addition import Addition
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
    api_instance = connectwise_psa.AgreementAdditionsApi(api_client)
    id = 56 # int | additionId
    parent_id = 56 # int | agreementId
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
        # Get Addition
        api_response = api_instance.get_finance_agreements_by_parent_id_additions_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of AgreementAdditionsApi->get_finance_agreements_by_parent_id_additions_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgreementAdditionsApi->get_finance_agreements_by_parent_id_additions_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| additionId | 
 **parent_id** | **int**| agreementId | 
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

[**Addition**](Addition.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Addition |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_finance_agreements_by_parent_id_additions_count**
> Count get_finance_agreements_by_parent_id_additions_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Count of Addition

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
    api_instance = connectwise_psa.AgreementAdditionsApi(api_client)
    parent_id = 56 # int | agreementId
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
        # Get Count of Addition
        api_response = api_instance.get_finance_agreements_by_parent_id_additions_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of AgreementAdditionsApi->get_finance_agreements_by_parent_id_additions_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgreementAdditionsApi->get_finance_agreements_by_parent_id_additions_count: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| agreementId | 
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

# **patch_finance_agreements_by_parent_id_additions_by_id**
> Addition patch_finance_agreements_by_parent_id_additions_by_id(id, parent_id, client_id, patch_operation)

Patch Addition

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.addition import Addition
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
    api_instance = connectwise_psa.AgreementAdditionsApi(api_client)
    id = 56 # int | additionId
    parent_id = 56 # int | agreementId
    client_id = 'client_id_example' # str | 
    patch_operation = [connectwise_psa.PatchOperation()] # List[PatchOperation] | List of PatchOperation

    try:
        # Patch Addition
        api_response = api_instance.patch_finance_agreements_by_parent_id_additions_by_id(id, parent_id, client_id, patch_operation)
        print("The response of AgreementAdditionsApi->patch_finance_agreements_by_parent_id_additions_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgreementAdditionsApi->patch_finance_agreements_by_parent_id_additions_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| additionId | 
 **parent_id** | **int**| agreementId | 
 **client_id** | **str**|  | 
 **patch_operation** | [**List[PatchOperation]**](PatchOperation.md)| List of PatchOperation | 

### Return type

[**Addition**](Addition.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Addition |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_finance_agreements_by_parent_id_additions**
> Addition post_finance_agreements_by_parent_id_additions(parent_id, client_id, addition)

Post Addition

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.addition import Addition
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
    api_instance = connectwise_psa.AgreementAdditionsApi(api_client)
    parent_id = 56 # int | agreementId
    client_id = 'client_id_example' # str | 
    addition = connectwise_psa.Addition() # Addition | addition

    try:
        # Post Addition
        api_response = api_instance.post_finance_agreements_by_parent_id_additions(parent_id, client_id, addition)
        print("The response of AgreementAdditionsApi->post_finance_agreements_by_parent_id_additions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgreementAdditionsApi->post_finance_agreements_by_parent_id_additions: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| agreementId | 
 **client_id** | **str**|  | 
 **addition** | [**Addition**](Addition.md)| addition | 

### Return type

[**Addition**](Addition.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Addition |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_finance_agreements_by_parent_id_additions_by_id**
> Addition put_finance_agreements_by_parent_id_additions_by_id(id, parent_id, client_id, addition)

Put Addition

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.addition import Addition
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
    api_instance = connectwise_psa.AgreementAdditionsApi(api_client)
    id = 56 # int | additionId
    parent_id = 56 # int | agreementId
    client_id = 'client_id_example' # str | 
    addition = connectwise_psa.Addition() # Addition | addition

    try:
        # Put Addition
        api_response = api_instance.put_finance_agreements_by_parent_id_additions_by_id(id, parent_id, client_id, addition)
        print("The response of AgreementAdditionsApi->put_finance_agreements_by_parent_id_additions_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgreementAdditionsApi->put_finance_agreements_by_parent_id_additions_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| additionId | 
 **parent_id** | **int**| agreementId | 
 **client_id** | **str**|  | 
 **addition** | [**Addition**](Addition.md)| addition | 

### Return type

[**Addition**](Addition.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Addition |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

