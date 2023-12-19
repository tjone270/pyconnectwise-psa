# connectwise_psa.AgreementAdjustmentsApi

All URIs are relative to *https://api-aus.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_finance_agreements_by_parent_id_adjustments_by_id**](AgreementAdjustmentsApi.md#delete_finance_agreements_by_parent_id_adjustments_by_id) | **DELETE** /finance/agreements/{parentId}/adjustments/{id} | Delete Adjustment
[**get_finance_agreements_by_parent_id_adjustments**](AgreementAdjustmentsApi.md#get_finance_agreements_by_parent_id_adjustments) | **GET** /finance/agreements/{parentId}/adjustments | Get List of Adjustment
[**get_finance_agreements_by_parent_id_adjustments_by_id**](AgreementAdjustmentsApi.md#get_finance_agreements_by_parent_id_adjustments_by_id) | **GET** /finance/agreements/{parentId}/adjustments/{id} | Get Adjustment
[**get_finance_agreements_by_parent_id_adjustments_count**](AgreementAdjustmentsApi.md#get_finance_agreements_by_parent_id_adjustments_count) | **GET** /finance/agreements/{parentId}/adjustments/count | Get Count of Adjustment
[**patch_finance_agreements_by_parent_id_adjustments_by_id**](AgreementAdjustmentsApi.md#patch_finance_agreements_by_parent_id_adjustments_by_id) | **PATCH** /finance/agreements/{parentId}/adjustments/{id} | Patch Adjustment
[**post_finance_agreements_by_parent_id_adjustments**](AgreementAdjustmentsApi.md#post_finance_agreements_by_parent_id_adjustments) | **POST** /finance/agreements/{parentId}/adjustments | Post Adjustment
[**put_finance_agreements_by_parent_id_adjustments_by_id**](AgreementAdjustmentsApi.md#put_finance_agreements_by_parent_id_adjustments_by_id) | **PUT** /finance/agreements/{parentId}/adjustments/{id} | Put Adjustment


# **delete_finance_agreements_by_parent_id_adjustments_by_id**
> delete_finance_agreements_by_parent_id_adjustments_by_id(id, parent_id, client_id)

Delete Adjustment

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
    api_instance = connectwise_psa.AgreementAdjustmentsApi(api_client)
    id = 56 # int | adjustmentId
    parent_id = 56 # int | agreementId
    client_id = 'client_id_example' # str | 

    try:
        # Delete Adjustment
        api_instance.delete_finance_agreements_by_parent_id_adjustments_by_id(id, parent_id, client_id)
    except Exception as e:
        print("Exception when calling AgreementAdjustmentsApi->delete_finance_agreements_by_parent_id_adjustments_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| adjustmentId | 
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

# **get_finance_agreements_by_parent_id_adjustments**
> List[AgreementAdjustment] get_finance_agreements_by_parent_id_adjustments(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of Adjustment

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.agreement_adjustment import AgreementAdjustment
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
    api_instance = connectwise_psa.AgreementAdjustmentsApi(api_client)
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
        # Get List of Adjustment
        api_response = api_instance.get_finance_agreements_by_parent_id_adjustments(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of AgreementAdjustmentsApi->get_finance_agreements_by_parent_id_adjustments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgreementAdjustmentsApi->get_finance_agreements_by_parent_id_adjustments: %s\n" % e)
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

[**List[AgreementAdjustment]**](AgreementAdjustment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of Adjustment |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_finance_agreements_by_parent_id_adjustments_by_id**
> AgreementAdjustment get_finance_agreements_by_parent_id_adjustments_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Adjustment

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.agreement_adjustment import AgreementAdjustment
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
    api_instance = connectwise_psa.AgreementAdjustmentsApi(api_client)
    id = 56 # int | adjustmentId
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
        # Get Adjustment
        api_response = api_instance.get_finance_agreements_by_parent_id_adjustments_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of AgreementAdjustmentsApi->get_finance_agreements_by_parent_id_adjustments_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgreementAdjustmentsApi->get_finance_agreements_by_parent_id_adjustments_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| adjustmentId | 
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

[**AgreementAdjustment**](AgreementAdjustment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Adjustment |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_finance_agreements_by_parent_id_adjustments_count**
> Count get_finance_agreements_by_parent_id_adjustments_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Count of Adjustment

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
    api_instance = connectwise_psa.AgreementAdjustmentsApi(api_client)
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
        # Get Count of Adjustment
        api_response = api_instance.get_finance_agreements_by_parent_id_adjustments_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of AgreementAdjustmentsApi->get_finance_agreements_by_parent_id_adjustments_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgreementAdjustmentsApi->get_finance_agreements_by_parent_id_adjustments_count: %s\n" % e)
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

# **patch_finance_agreements_by_parent_id_adjustments_by_id**
> AgreementAdjustment patch_finance_agreements_by_parent_id_adjustments_by_id(id, parent_id, client_id, patch_operation)

Patch Adjustment

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.agreement_adjustment import AgreementAdjustment
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
    api_instance = connectwise_psa.AgreementAdjustmentsApi(api_client)
    id = 56 # int | adjustmentId
    parent_id = 56 # int | agreementId
    client_id = 'client_id_example' # str | 
    patch_operation = [connectwise_psa.PatchOperation()] # List[PatchOperation] | List of PatchOperation

    try:
        # Patch Adjustment
        api_response = api_instance.patch_finance_agreements_by_parent_id_adjustments_by_id(id, parent_id, client_id, patch_operation)
        print("The response of AgreementAdjustmentsApi->patch_finance_agreements_by_parent_id_adjustments_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgreementAdjustmentsApi->patch_finance_agreements_by_parent_id_adjustments_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| adjustmentId | 
 **parent_id** | **int**| agreementId | 
 **client_id** | **str**|  | 
 **patch_operation** | [**List[PatchOperation]**](PatchOperation.md)| List of PatchOperation | 

### Return type

[**AgreementAdjustment**](AgreementAdjustment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Adjustment |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_finance_agreements_by_parent_id_adjustments**
> AgreementAdjustment post_finance_agreements_by_parent_id_adjustments(parent_id, client_id, agreement_adjustment)

Post Adjustment

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.agreement_adjustment import AgreementAdjustment
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
    api_instance = connectwise_psa.AgreementAdjustmentsApi(api_client)
    parent_id = 56 # int | agreementId
    client_id = 'client_id_example' # str | 
    agreement_adjustment = connectwise_psa.AgreementAdjustment() # AgreementAdjustment | adjustment

    try:
        # Post Adjustment
        api_response = api_instance.post_finance_agreements_by_parent_id_adjustments(parent_id, client_id, agreement_adjustment)
        print("The response of AgreementAdjustmentsApi->post_finance_agreements_by_parent_id_adjustments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgreementAdjustmentsApi->post_finance_agreements_by_parent_id_adjustments: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| agreementId | 
 **client_id** | **str**|  | 
 **agreement_adjustment** | [**AgreementAdjustment**](AgreementAdjustment.md)| adjustment | 

### Return type

[**AgreementAdjustment**](AgreementAdjustment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Adjustment |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_finance_agreements_by_parent_id_adjustments_by_id**
> AgreementAdjustment put_finance_agreements_by_parent_id_adjustments_by_id(id, parent_id, client_id, agreement_adjustment)

Put Adjustment

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.agreement_adjustment import AgreementAdjustment
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
    api_instance = connectwise_psa.AgreementAdjustmentsApi(api_client)
    id = 56 # int | adjustmentId
    parent_id = 56 # int | agreementId
    client_id = 'client_id_example' # str | 
    agreement_adjustment = connectwise_psa.AgreementAdjustment() # AgreementAdjustment | adjustment

    try:
        # Put Adjustment
        api_response = api_instance.put_finance_agreements_by_parent_id_adjustments_by_id(id, parent_id, client_id, agreement_adjustment)
        print("The response of AgreementAdjustmentsApi->put_finance_agreements_by_parent_id_adjustments_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgreementAdjustmentsApi->put_finance_agreements_by_parent_id_adjustments_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| adjustmentId | 
 **parent_id** | **int**| agreementId | 
 **client_id** | **str**|  | 
 **agreement_adjustment** | [**AgreementAdjustment**](AgreementAdjustment.md)| adjustment | 

### Return type

[**AgreementAdjustment**](AgreementAdjustment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Adjustment |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

