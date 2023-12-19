# connectwise_psa.AgreementWorkRolesApi

All URIs are relative to *https://aus-api.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_finance_agreements_by_parent_id_workroles_by_id**](AgreementWorkRolesApi.md#delete_finance_agreements_by_parent_id_workroles_by_id) | **DELETE** /finance/agreements/{parentId}/workroles/{id} | Delete AgreementWorkRole
[**get_finance_agreements_by_parent_id_workroles**](AgreementWorkRolesApi.md#get_finance_agreements_by_parent_id_workroles) | **GET** /finance/agreements/{parentId}/workroles | Get List of AgreementWorkRole
[**get_finance_agreements_by_parent_id_workroles_by_id**](AgreementWorkRolesApi.md#get_finance_agreements_by_parent_id_workroles_by_id) | **GET** /finance/agreements/{parentId}/workroles/{id} | Get AgreementWorkRole
[**get_finance_agreements_by_parent_id_workroles_count**](AgreementWorkRolesApi.md#get_finance_agreements_by_parent_id_workroles_count) | **GET** /finance/agreements/{parentId}/workroles/count | Get Count of AgreementWorkRole
[**patch_finance_agreements_by_parent_id_workroles_by_id**](AgreementWorkRolesApi.md#patch_finance_agreements_by_parent_id_workroles_by_id) | **PATCH** /finance/agreements/{parentId}/workroles/{id} | Patch AgreementWorkRole
[**post_finance_agreements_by_parent_id_workroles**](AgreementWorkRolesApi.md#post_finance_agreements_by_parent_id_workroles) | **POST** /finance/agreements/{parentId}/workroles | Post AgreementWorkRole
[**put_finance_agreements_by_parent_id_workroles_by_id**](AgreementWorkRolesApi.md#put_finance_agreements_by_parent_id_workroles_by_id) | **PUT** /finance/agreements/{parentId}/workroles/{id} | Put AgreementWorkRole


# **delete_finance_agreements_by_parent_id_workroles_by_id**
> delete_finance_agreements_by_parent_id_workroles_by_id(id, parent_id, client_id)

Delete AgreementWorkRole

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
    api_instance = connectwise_psa.AgreementWorkRolesApi(api_client)
    id = 56 # int | workroleId
    parent_id = 56 # int | agreementId
    client_id = 'client_id_example' # str | 

    try:
        # Delete AgreementWorkRole
        api_instance.delete_finance_agreements_by_parent_id_workroles_by_id(id, parent_id, client_id)
    except Exception as e:
        print("Exception when calling AgreementWorkRolesApi->delete_finance_agreements_by_parent_id_workroles_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| workroleId | 
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

# **get_finance_agreements_by_parent_id_workroles**
> List[AgreementWorkRole] get_finance_agreements_by_parent_id_workroles(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of AgreementWorkRole

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.agreement_work_role import AgreementWorkRole
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
    api_instance = connectwise_psa.AgreementWorkRolesApi(api_client)
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
        # Get List of AgreementWorkRole
        api_response = api_instance.get_finance_agreements_by_parent_id_workroles(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of AgreementWorkRolesApi->get_finance_agreements_by_parent_id_workroles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgreementWorkRolesApi->get_finance_agreements_by_parent_id_workroles: %s\n" % e)
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

[**List[AgreementWorkRole]**](AgreementWorkRole.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of AgreementWorkRole |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_finance_agreements_by_parent_id_workroles_by_id**
> AgreementWorkRole get_finance_agreements_by_parent_id_workroles_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get AgreementWorkRole

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.agreement_work_role import AgreementWorkRole
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
    api_instance = connectwise_psa.AgreementWorkRolesApi(api_client)
    id = 56 # int | workroleId
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
        # Get AgreementWorkRole
        api_response = api_instance.get_finance_agreements_by_parent_id_workroles_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of AgreementWorkRolesApi->get_finance_agreements_by_parent_id_workroles_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgreementWorkRolesApi->get_finance_agreements_by_parent_id_workroles_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| workroleId | 
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

[**AgreementWorkRole**](AgreementWorkRole.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | AgreementWorkRole |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_finance_agreements_by_parent_id_workroles_count**
> Count get_finance_agreements_by_parent_id_workroles_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Count of AgreementWorkRole

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
    api_instance = connectwise_psa.AgreementWorkRolesApi(api_client)
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
        # Get Count of AgreementWorkRole
        api_response = api_instance.get_finance_agreements_by_parent_id_workroles_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of AgreementWorkRolesApi->get_finance_agreements_by_parent_id_workroles_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgreementWorkRolesApi->get_finance_agreements_by_parent_id_workroles_count: %s\n" % e)
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

# **patch_finance_agreements_by_parent_id_workroles_by_id**
> AgreementWorkRole patch_finance_agreements_by_parent_id_workroles_by_id(id, parent_id, client_id, patch_operation)

Patch AgreementWorkRole

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.agreement_work_role import AgreementWorkRole
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
    api_instance = connectwise_psa.AgreementWorkRolesApi(api_client)
    id = 56 # int | workroleId
    parent_id = 56 # int | agreementId
    client_id = 'client_id_example' # str | 
    patch_operation = [connectwise_psa.PatchOperation()] # List[PatchOperation] | List of PatchOperation

    try:
        # Patch AgreementWorkRole
        api_response = api_instance.patch_finance_agreements_by_parent_id_workroles_by_id(id, parent_id, client_id, patch_operation)
        print("The response of AgreementWorkRolesApi->patch_finance_agreements_by_parent_id_workroles_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgreementWorkRolesApi->patch_finance_agreements_by_parent_id_workroles_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| workroleId | 
 **parent_id** | **int**| agreementId | 
 **client_id** | **str**|  | 
 **patch_operation** | [**List[PatchOperation]**](PatchOperation.md)| List of PatchOperation | 

### Return type

[**AgreementWorkRole**](AgreementWorkRole.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | AgreementWorkRole |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_finance_agreements_by_parent_id_workroles**
> AgreementWorkRole post_finance_agreements_by_parent_id_workroles(parent_id, client_id, agreement_work_role)

Post AgreementWorkRole

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.agreement_work_role import AgreementWorkRole
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
    api_instance = connectwise_psa.AgreementWorkRolesApi(api_client)
    parent_id = 56 # int | agreementId
    client_id = 'client_id_example' # str | 
    agreement_work_role = connectwise_psa.AgreementWorkRole() # AgreementWorkRole | workRole

    try:
        # Post AgreementWorkRole
        api_response = api_instance.post_finance_agreements_by_parent_id_workroles(parent_id, client_id, agreement_work_role)
        print("The response of AgreementWorkRolesApi->post_finance_agreements_by_parent_id_workroles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgreementWorkRolesApi->post_finance_agreements_by_parent_id_workroles: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| agreementId | 
 **client_id** | **str**|  | 
 **agreement_work_role** | [**AgreementWorkRole**](AgreementWorkRole.md)| workRole | 

### Return type

[**AgreementWorkRole**](AgreementWorkRole.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | AgreementWorkRole |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_finance_agreements_by_parent_id_workroles_by_id**
> AgreementWorkRole put_finance_agreements_by_parent_id_workroles_by_id(id, parent_id, client_id, agreement_work_role)

Put AgreementWorkRole

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.agreement_work_role import AgreementWorkRole
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
    api_instance = connectwise_psa.AgreementWorkRolesApi(api_client)
    id = 56 # int | workroleId
    parent_id = 56 # int | agreementId
    client_id = 'client_id_example' # str | 
    agreement_work_role = connectwise_psa.AgreementWorkRole() # AgreementWorkRole | workRole

    try:
        # Put AgreementWorkRole
        api_response = api_instance.put_finance_agreements_by_parent_id_workroles_by_id(id, parent_id, client_id, agreement_work_role)
        print("The response of AgreementWorkRolesApi->put_finance_agreements_by_parent_id_workroles_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgreementWorkRolesApi->put_finance_agreements_by_parent_id_workroles_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| workroleId | 
 **parent_id** | **int**| agreementId | 
 **client_id** | **str**|  | 
 **agreement_work_role** | [**AgreementWorkRole**](AgreementWorkRole.md)| workRole | 

### Return type

[**AgreementWorkRole**](AgreementWorkRole.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | AgreementWorkRole |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

