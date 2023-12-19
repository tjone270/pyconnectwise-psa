# connectwise_psa.AgreementsApi

All URIs are relative to *https://aus-api.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_finance_agreements_by_id**](AgreementsApi.md#delete_finance_agreements_by_id) | **DELETE** /finance/agreements/{id} | Delete Agreement
[**delete_finance_agreements_by_parent_id_configurations_by_id**](AgreementsApi.md#delete_finance_agreements_by_parent_id_configurations_by_id) | **DELETE** /finance/agreements/{parentId}/configurations/{id} | Delete ConfigurationReference
[**get_finance_agreements**](AgreementsApi.md#get_finance_agreements) | **GET** /finance/agreements | Get List of Agreement
[**get_finance_agreements_by_id**](AgreementsApi.md#get_finance_agreements_by_id) | **GET** /finance/agreements/{id} | Get Agreement
[**get_finance_agreements_by_id_application_parameters_by_pod_id**](AgreementsApi.md#get_finance_agreements_by_id_application_parameters_by_pod_id) | **GET** /finance/agreements/{id}/applicationParameters/{podId} | Get AgreementApplicationParameters
[**get_finance_agreements_by_id_recurring_parameters_by_pod_id**](AgreementsApi.md#get_finance_agreements_by_id_recurring_parameters_by_pod_id) | **GET** /finance/agreements/{id}/recurringParameters/{podId} | Get AgreementRecurringParameters
[**get_finance_agreements_by_parent_id_configurations**](AgreementsApi.md#get_finance_agreements_by_parent_id_configurations) | **GET** /finance/agreements/{parentId}/configurations | Get List of ConfigurationReference
[**get_finance_agreements_by_parent_id_configurations_by_id**](AgreementsApi.md#get_finance_agreements_by_parent_id_configurations_by_id) | **GET** /finance/agreements/{parentId}/configurations/{id} | Get ConfigurationReference
[**get_finance_agreements_by_parent_id_configurations_count**](AgreementsApi.md#get_finance_agreements_by_parent_id_configurations_count) | **GET** /finance/agreements/{parentId}/configurations/count | Get Count of ConfigurationReference
[**get_finance_agreements_count**](AgreementsApi.md#get_finance_agreements_count) | **GET** /finance/agreements/count | Get Count of Agreement
[**patch_finance_agreements_by_id**](AgreementsApi.md#patch_finance_agreements_by_id) | **PATCH** /finance/agreements/{id} | Patch Agreement
[**post_finance_agreements**](AgreementsApi.md#post_finance_agreements) | **POST** /finance/agreements | Post Agreement
[**post_finance_agreements_by_id_invoice**](AgreementsApi.md#post_finance_agreements_by_id_invoice) | **POST** /finance/agreements/{id}/invoice | Post AgreementInvoice
[**post_finance_agreements_by_parent_id_configurations**](AgreementsApi.md#post_finance_agreements_by_parent_id_configurations) | **POST** /finance/agreements/{parentId}/configurations | Post ConfigurationReference
[**post_finance_agreements_by_parent_id_copy**](AgreementsApi.md#post_finance_agreements_by_parent_id_copy) | **POST** /finance/agreements/{parentId}/copy | Post CopyAgreementAction
[**put_finance_agreements_by_id**](AgreementsApi.md#put_finance_agreements_by_id) | **PUT** /finance/agreements/{id} | Put Agreement


# **delete_finance_agreements_by_id**
> delete_finance_agreements_by_id(id, client_id)

Delete Agreement

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
    api_instance = connectwise_psa.AgreementsApi(api_client)
    id = 56 # int | agreementId
    client_id = 'client_id_example' # str | 

    try:
        # Delete Agreement
        api_instance.delete_finance_agreements_by_id(id, client_id)
    except Exception as e:
        print("Exception when calling AgreementsApi->delete_finance_agreements_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| agreementId | 
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

# **delete_finance_agreements_by_parent_id_configurations_by_id**
> delete_finance_agreements_by_parent_id_configurations_by_id(id, parent_id, client_id)

Delete ConfigurationReference

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
    api_instance = connectwise_psa.AgreementsApi(api_client)
    id = 56 # int | configurationId
    parent_id = 56 # int | agreementId
    client_id = 'client_id_example' # str | 

    try:
        # Delete ConfigurationReference
        api_instance.delete_finance_agreements_by_parent_id_configurations_by_id(id, parent_id, client_id)
    except Exception as e:
        print("Exception when calling AgreementsApi->delete_finance_agreements_by_parent_id_configurations_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| configurationId | 
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

# **get_finance_agreements**
> List[Agreement] get_finance_agreements(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of Agreement

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.agreement import Agreement
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
    api_instance = connectwise_psa.AgreementsApi(api_client)
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
        # Get List of Agreement
        api_response = api_instance.get_finance_agreements(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of AgreementsApi->get_finance_agreements:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgreementsApi->get_finance_agreements: %s\n" % e)
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

[**List[Agreement]**](Agreement.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of Agreement |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_finance_agreements_by_id**
> Agreement get_finance_agreements_by_id(id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Agreement

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.agreement import Agreement
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
    api_instance = connectwise_psa.AgreementsApi(api_client)
    id = 56 # int | agreementId
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
        # Get Agreement
        api_response = api_instance.get_finance_agreements_by_id(id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of AgreementsApi->get_finance_agreements_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgreementsApi->get_finance_agreements_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| agreementId | 
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

[**Agreement**](Agreement.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Agreement |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_finance_agreements_by_id_application_parameters_by_pod_id**
> AgreementApplicationParameters get_finance_agreements_by_id_application_parameters_by_pod_id(id, pod_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get AgreementApplicationParameters

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.agreement_application_parameters import AgreementApplicationParameters
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
    api_instance = connectwise_psa.AgreementsApi(api_client)
    id = 56 # int | agreementHeaderId
    pod_id = 'pod_id_example' # str | podId
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
        # Get AgreementApplicationParameters
        api_response = api_instance.get_finance_agreements_by_id_application_parameters_by_pod_id(id, pod_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of AgreementsApi->get_finance_agreements_by_id_application_parameters_by_pod_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgreementsApi->get_finance_agreements_by_id_application_parameters_by_pod_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| agreementHeaderId | 
 **pod_id** | **str**| podId | 
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

[**AgreementApplicationParameters**](AgreementApplicationParameters.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | AgreementApplicationParameters |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_finance_agreements_by_id_recurring_parameters_by_pod_id**
> AgreementRecurringParameters get_finance_agreements_by_id_recurring_parameters_by_pod_id(id, pod_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get AgreementRecurringParameters

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.agreement_recurring_parameters import AgreementRecurringParameters
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
    api_instance = connectwise_psa.AgreementsApi(api_client)
    id = 56 # int | agreementId
    pod_id = 'pod_id_example' # str | podId
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
        # Get AgreementRecurringParameters
        api_response = api_instance.get_finance_agreements_by_id_recurring_parameters_by_pod_id(id, pod_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of AgreementsApi->get_finance_agreements_by_id_recurring_parameters_by_pod_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgreementsApi->get_finance_agreements_by_id_recurring_parameters_by_pod_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| agreementId | 
 **pod_id** | **str**| podId | 
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

[**AgreementRecurringParameters**](AgreementRecurringParameters.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | AgreementRecurringParameters |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_finance_agreements_by_parent_id_configurations**
> List[ConfigurationReference] get_finance_agreements_by_parent_id_configurations(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of ConfigurationReference

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.configuration_reference import ConfigurationReference
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
    api_instance = connectwise_psa.AgreementsApi(api_client)
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
        # Get List of ConfigurationReference
        api_response = api_instance.get_finance_agreements_by_parent_id_configurations(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of AgreementsApi->get_finance_agreements_by_parent_id_configurations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgreementsApi->get_finance_agreements_by_parent_id_configurations: %s\n" % e)
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

[**List[ConfigurationReference]**](ConfigurationReference.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of ConfigurationReference |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_finance_agreements_by_parent_id_configurations_by_id**
> ConfigurationReference get_finance_agreements_by_parent_id_configurations_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get ConfigurationReference

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.configuration_reference import ConfigurationReference
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
    api_instance = connectwise_psa.AgreementsApi(api_client)
    id = 56 # int | configurationId
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
        # Get ConfigurationReference
        api_response = api_instance.get_finance_agreements_by_parent_id_configurations_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of AgreementsApi->get_finance_agreements_by_parent_id_configurations_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgreementsApi->get_finance_agreements_by_parent_id_configurations_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| configurationId | 
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

[**ConfigurationReference**](ConfigurationReference.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ConfigurationReference |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_finance_agreements_by_parent_id_configurations_count**
> Count get_finance_agreements_by_parent_id_configurations_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Count of ConfigurationReference

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
    api_instance = connectwise_psa.AgreementsApi(api_client)
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
        # Get Count of ConfigurationReference
        api_response = api_instance.get_finance_agreements_by_parent_id_configurations_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of AgreementsApi->get_finance_agreements_by_parent_id_configurations_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgreementsApi->get_finance_agreements_by_parent_id_configurations_count: %s\n" % e)
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

# **get_finance_agreements_count**
> Count get_finance_agreements_count(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Count of Agreement

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
    api_instance = connectwise_psa.AgreementsApi(api_client)
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
        # Get Count of Agreement
        api_response = api_instance.get_finance_agreements_count(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of AgreementsApi->get_finance_agreements_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgreementsApi->get_finance_agreements_count: %s\n" % e)
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

# **patch_finance_agreements_by_id**
> Agreement patch_finance_agreements_by_id(id, client_id, patch_operation)

Patch Agreement

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.agreement import Agreement
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
    api_instance = connectwise_psa.AgreementsApi(api_client)
    id = 56 # int | agreementId
    client_id = 'client_id_example' # str | 
    patch_operation = [connectwise_psa.PatchOperation()] # List[PatchOperation] | List of PatchOperation

    try:
        # Patch Agreement
        api_response = api_instance.patch_finance_agreements_by_id(id, client_id, patch_operation)
        print("The response of AgreementsApi->patch_finance_agreements_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgreementsApi->patch_finance_agreements_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| agreementId | 
 **client_id** | **str**|  | 
 **patch_operation** | [**List[PatchOperation]**](PatchOperation.md)| List of PatchOperation | 

### Return type

[**Agreement**](Agreement.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Agreement |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_finance_agreements**
> Agreement post_finance_agreements(client_id, agreement)

Post Agreement

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.agreement import Agreement
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
    api_instance = connectwise_psa.AgreementsApi(api_client)
    client_id = 'client_id_example' # str | 
    agreement = connectwise_psa.Agreement() # Agreement | agreement

    try:
        # Post Agreement
        api_response = api_instance.post_finance_agreements(client_id, agreement)
        print("The response of AgreementsApi->post_finance_agreements:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgreementsApi->post_finance_agreements: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**|  | 
 **agreement** | [**Agreement**](Agreement.md)| agreement | 

### Return type

[**Agreement**](Agreement.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Agreement |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_finance_agreements_by_id_invoice**
> int post_finance_agreements_by_id_invoice(id, client_id)

Post AgreementInvoice

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
    api_instance = connectwise_psa.AgreementsApi(api_client)
    id = 56 # int | id
    client_id = 'client_id_example' # str | 

    try:
        # Post AgreementInvoice
        api_response = api_instance.post_finance_agreements_by_id_invoice(id, client_id)
        print("The response of AgreementsApi->post_finance_agreements_by_id_invoice:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgreementsApi->post_finance_agreements_by_id_invoice: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| id | 
 **client_id** | **str**|  | 

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Agreement |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_finance_agreements_by_parent_id_configurations**
> ConfigurationReference post_finance_agreements_by_parent_id_configurations(parent_id, client_id, configuration_reference)

Post ConfigurationReference

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.configuration_reference import ConfigurationReference
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
    api_instance = connectwise_psa.AgreementsApi(api_client)
    parent_id = 56 # int | agreementId
    client_id = 'client_id_example' # str | 
    configuration_reference = connectwise_psa.ConfigurationReference() # ConfigurationReference | configuration

    try:
        # Post ConfigurationReference
        api_response = api_instance.post_finance_agreements_by_parent_id_configurations(parent_id, client_id, configuration_reference)
        print("The response of AgreementsApi->post_finance_agreements_by_parent_id_configurations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgreementsApi->post_finance_agreements_by_parent_id_configurations: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| agreementId | 
 **client_id** | **str**|  | 
 **configuration_reference** | [**ConfigurationReference**](ConfigurationReference.md)| configuration | 

### Return type

[**ConfigurationReference**](ConfigurationReference.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | ConfigurationReference |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_finance_agreements_by_parent_id_copy**
> Agreement post_finance_agreements_by_parent_id_copy(parent_id, client_id)

Post CopyAgreementAction

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.agreement import Agreement
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
    api_instance = connectwise_psa.AgreementsApi(api_client)
    parent_id = 56 # int | agreementId
    client_id = 'client_id_example' # str | 

    try:
        # Post CopyAgreementAction
        api_response = api_instance.post_finance_agreements_by_parent_id_copy(parent_id, client_id)
        print("The response of AgreementsApi->post_finance_agreements_by_parent_id_copy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgreementsApi->post_finance_agreements_by_parent_id_copy: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| agreementId | 
 **client_id** | **str**|  | 

### Return type

[**Agreement**](Agreement.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | CopyAgreementAction |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_finance_agreements_by_id**
> Agreement put_finance_agreements_by_id(id, client_id, agreement)

Put Agreement

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.agreement import Agreement
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
    api_instance = connectwise_psa.AgreementsApi(api_client)
    id = 56 # int | agreementId
    client_id = 'client_id_example' # str | 
    agreement = connectwise_psa.Agreement() # Agreement | agreement

    try:
        # Put Agreement
        api_response = api_instance.put_finance_agreements_by_id(id, client_id, agreement)
        print("The response of AgreementsApi->put_finance_agreements_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgreementsApi->put_finance_agreements_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| agreementId | 
 **client_id** | **str**|  | 
 **agreement** | [**Agreement**](Agreement.md)| agreement | 

### Return type

[**Agreement**](Agreement.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Agreement |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

