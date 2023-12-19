# connectwise_psa.AgreementWorkTypeExclusionsApi

All URIs are relative to *https://aus-api.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_finance_agreements_by_parent_id_work_type_exclusions_by_id**](AgreementWorkTypeExclusionsApi.md#delete_finance_agreements_by_parent_id_work_type_exclusions_by_id) | **DELETE** /finance/agreements/{parentId}/workTypeExclusions/{id} | Delete AgreementWorkTypeExclusion
[**get_finance_agreements_by_parent_id_work_type_exclusions**](AgreementWorkTypeExclusionsApi.md#get_finance_agreements_by_parent_id_work_type_exclusions) | **GET** /finance/agreements/{parentId}/workTypeExclusions | Get List of AgreementWorkTypeExclusion
[**get_finance_agreements_by_parent_id_work_type_exclusions_count**](AgreementWorkTypeExclusionsApi.md#get_finance_agreements_by_parent_id_work_type_exclusions_count) | **GET** /finance/agreements/{parentId}/workTypeExclusions/count | Get Count of AgreementWorkTypeExclusion
[**post_finance_agreements_by_parent_id_work_type_exclusions**](AgreementWorkTypeExclusionsApi.md#post_finance_agreements_by_parent_id_work_type_exclusions) | **POST** /finance/agreements/{parentId}/workTypeExclusions | Post AgreementWorkTypeExclusion


# **delete_finance_agreements_by_parent_id_work_type_exclusions_by_id**
> delete_finance_agreements_by_parent_id_work_type_exclusions_by_id(id, parent_id, client_id)

Delete AgreementWorkTypeExclusion

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
    api_instance = connectwise_psa.AgreementWorkTypeExclusionsApi(api_client)
    id = 56 # int | workTypeExclusionId
    parent_id = 56 # int | agreementId
    client_id = 'client_id_example' # str | 

    try:
        # Delete AgreementWorkTypeExclusion
        api_instance.delete_finance_agreements_by_parent_id_work_type_exclusions_by_id(id, parent_id, client_id)
    except Exception as e:
        print("Exception when calling AgreementWorkTypeExclusionsApi->delete_finance_agreements_by_parent_id_work_type_exclusions_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| workTypeExclusionId | 
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

# **get_finance_agreements_by_parent_id_work_type_exclusions**
> List[AgreementWorkTypeExclusion] get_finance_agreements_by_parent_id_work_type_exclusions(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of AgreementWorkTypeExclusion

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.agreement_work_type_exclusion import AgreementWorkTypeExclusion
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
    api_instance = connectwise_psa.AgreementWorkTypeExclusionsApi(api_client)
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
        # Get List of AgreementWorkTypeExclusion
        api_response = api_instance.get_finance_agreements_by_parent_id_work_type_exclusions(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of AgreementWorkTypeExclusionsApi->get_finance_agreements_by_parent_id_work_type_exclusions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgreementWorkTypeExclusionsApi->get_finance_agreements_by_parent_id_work_type_exclusions: %s\n" % e)
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

[**List[AgreementWorkTypeExclusion]**](AgreementWorkTypeExclusion.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of AgreementWorkTypeExclusion |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_finance_agreements_by_parent_id_work_type_exclusions_count**
> Count get_finance_agreements_by_parent_id_work_type_exclusions_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Count of AgreementWorkTypeExclusion

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
    api_instance = connectwise_psa.AgreementWorkTypeExclusionsApi(api_client)
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
        # Get Count of AgreementWorkTypeExclusion
        api_response = api_instance.get_finance_agreements_by_parent_id_work_type_exclusions_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of AgreementWorkTypeExclusionsApi->get_finance_agreements_by_parent_id_work_type_exclusions_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgreementWorkTypeExclusionsApi->get_finance_agreements_by_parent_id_work_type_exclusions_count: %s\n" % e)
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

# **post_finance_agreements_by_parent_id_work_type_exclusions**
> AgreementWorkTypeExclusion post_finance_agreements_by_parent_id_work_type_exclusions(parent_id, client_id, agreement_work_type_exclusion)

Post AgreementWorkTypeExclusion

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.agreement_work_type_exclusion import AgreementWorkTypeExclusion
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
    api_instance = connectwise_psa.AgreementWorkTypeExclusionsApi(api_client)
    parent_id = 56 # int | agreementId
    client_id = 'client_id_example' # str | 
    agreement_work_type_exclusion = connectwise_psa.AgreementWorkTypeExclusion() # AgreementWorkTypeExclusion | workTypeExclusion

    try:
        # Post AgreementWorkTypeExclusion
        api_response = api_instance.post_finance_agreements_by_parent_id_work_type_exclusions(parent_id, client_id, agreement_work_type_exclusion)
        print("The response of AgreementWorkTypeExclusionsApi->post_finance_agreements_by_parent_id_work_type_exclusions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgreementWorkTypeExclusionsApi->post_finance_agreements_by_parent_id_work_type_exclusions: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| agreementId | 
 **client_id** | **str**|  | 
 **agreement_work_type_exclusion** | [**AgreementWorkTypeExclusion**](AgreementWorkTypeExclusion.md)| workTypeExclusion | 

### Return type

[**AgreementWorkTypeExclusion**](AgreementWorkTypeExclusion.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | AgreementWorkTypeExclusion |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

