# connectwise_psa.OpportunitiesApi

All URIs are relative to *https://aus-api.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_sales_opportunities_by_id**](OpportunitiesApi.md#delete_sales_opportunities_by_id) | **DELETE** /sales/opportunities/{id} | Delete ConnectWise.Apis.v3_0.v2015_3.Sales.Opportunity.Opportunity
[**get_sales_opportunities**](OpportunitiesApi.md#get_sales_opportunities) | **GET** /sales/opportunities | Get List of ConnectWise.Apis.v3_0.v2015_3.Sales.Opportunity.Opportunity
[**get_sales_opportunities_by_id**](OpportunitiesApi.md#get_sales_opportunities_by_id) | **GET** /sales/opportunities/{id} | Get ConnectWise.Apis.v3_0.v2015_3.Sales.Opportunity.Opportunity
[**get_sales_opportunities_count**](OpportunitiesApi.md#get_sales_opportunities_count) | **GET** /sales/opportunities/count | Get Count of ConnectWise.Apis.v3_0.v2015_3.Sales.Opportunity.Opportunity
[**get_sales_opportunities_default**](OpportunitiesApi.md#get_sales_opportunities_default) | **GET** /sales/opportunities/default | Get ConnectWise.Apis.v3_0.v2015_3.Sales.Opportunity.Opportunity
[**patch_sales_opportunities_by_id**](OpportunitiesApi.md#patch_sales_opportunities_by_id) | **PATCH** /sales/opportunities/{id} | Patch ConnectWise.Apis.v3_0.v2015_3.Sales.Opportunity.Opportunity
[**post_sales_opportunities**](OpportunitiesApi.md#post_sales_opportunities) | **POST** /sales/opportunities | Post ConnectWise.Apis.v3_0.v2015_3.Sales.Opportunity.Opportunity
[**post_sales_opportunities_by_id_convert_to_agreement**](OpportunitiesApi.md#post_sales_opportunities_by_id_convert_to_agreement) | **POST** /sales/opportunities/{id}/convertToAgreement | Post ApiAgreement
[**post_sales_opportunities_by_id_convert_to_project**](OpportunitiesApi.md#post_sales_opportunities_by_id_convert_to_project) | **POST** /sales/opportunities/{id}/convertToProject | Post ApiProject
[**post_sales_opportunities_by_id_convert_to_sales_order**](OpportunitiesApi.md#post_sales_opportunities_by_id_convert_to_sales_order) | **POST** /sales/opportunities/{id}/convertToSalesOrder | Post ApiSalesOrder
[**post_sales_opportunities_by_id_convert_to_service_ticket**](OpportunitiesApi.md#post_sales_opportunities_by_id_convert_to_service_ticket) | **POST** /sales/opportunities/{id}/convertToServiceTicket | Post ApiTicket
[**put_sales_opportunities_by_id**](OpportunitiesApi.md#put_sales_opportunities_by_id) | **PUT** /sales/opportunities/{id} | Put ConnectWise.Apis.v3_0.v2015_3.Sales.Opportunity.Opportunity


# **delete_sales_opportunities_by_id**
> delete_sales_opportunities_by_id(id, client_id)

Delete ConnectWise.Apis.v3_0.v2015_3.Sales.Opportunity.Opportunity

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
    api_instance = connectwise_psa.OpportunitiesApi(api_client)
    id = 56 # int | opportunityId
    client_id = 'client_id_example' # str | 

    try:
        # Delete ConnectWise.Apis.v3_0.v2015_3.Sales.Opportunity.Opportunity
        api_instance.delete_sales_opportunities_by_id(id, client_id)
    except Exception as e:
        print("Exception when calling OpportunitiesApi->delete_sales_opportunities_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| opportunityId | 
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

# **get_sales_opportunities**
> List[Opportunity] get_sales_opportunities(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of ConnectWise.Apis.v3_0.v2015_3.Sales.Opportunity.Opportunity

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.opportunity import Opportunity
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
    api_instance = connectwise_psa.OpportunitiesApi(api_client)
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
        # Get List of ConnectWise.Apis.v3_0.v2015_3.Sales.Opportunity.Opportunity
        api_response = api_instance.get_sales_opportunities(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of OpportunitiesApi->get_sales_opportunities:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpportunitiesApi->get_sales_opportunities: %s\n" % e)
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

[**List[Opportunity]**](Opportunity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of ConnectWise.Apis.v3_0.v2015_3.Sales.Opportunity.Opportunity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sales_opportunities_by_id**
> Opportunity get_sales_opportunities_by_id(id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get ConnectWise.Apis.v3_0.v2015_3.Sales.Opportunity.Opportunity

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.opportunity import Opportunity
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
    api_instance = connectwise_psa.OpportunitiesApi(api_client)
    id = 56 # int | opportunityId
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
        # Get ConnectWise.Apis.v3_0.v2015_3.Sales.Opportunity.Opportunity
        api_response = api_instance.get_sales_opportunities_by_id(id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of OpportunitiesApi->get_sales_opportunities_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpportunitiesApi->get_sales_opportunities_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| opportunityId | 
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

[**Opportunity**](Opportunity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ConnectWise.Apis.v3_0.v2015_3.Sales.Opportunity.Opportunity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sales_opportunities_count**
> Count get_sales_opportunities_count(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Count of ConnectWise.Apis.v3_0.v2015_3.Sales.Opportunity.Opportunity

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
    api_instance = connectwise_psa.OpportunitiesApi(api_client)
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
        # Get Count of ConnectWise.Apis.v3_0.v2015_3.Sales.Opportunity.Opportunity
        api_response = api_instance.get_sales_opportunities_count(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of OpportunitiesApi->get_sales_opportunities_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpportunitiesApi->get_sales_opportunities_count: %s\n" % e)
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

# **get_sales_opportunities_default**
> Opportunity get_sales_opportunities_default(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get ConnectWise.Apis.v3_0.v2015_3.Sales.Opportunity.Opportunity

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.opportunity import Opportunity
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
    api_instance = connectwise_psa.OpportunitiesApi(api_client)
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
        # Get ConnectWise.Apis.v3_0.v2015_3.Sales.Opportunity.Opportunity
        api_response = api_instance.get_sales_opportunities_default(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of OpportunitiesApi->get_sales_opportunities_default:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpportunitiesApi->get_sales_opportunities_default: %s\n" % e)
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

[**Opportunity**](Opportunity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ConnectWise.Apis.v3_0.v2015_3.Sales.Opportunity.Opportunity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_sales_opportunities_by_id**
> Opportunity patch_sales_opportunities_by_id(id, client_id, patch_operation)

Patch ConnectWise.Apis.v3_0.v2015_3.Sales.Opportunity.Opportunity

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.opportunity import Opportunity
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
    api_instance = connectwise_psa.OpportunitiesApi(api_client)
    id = 56 # int | opportunityId
    client_id = 'client_id_example' # str | 
    patch_operation = [connectwise_psa.PatchOperation()] # List[PatchOperation] | List of PatchOperation

    try:
        # Patch ConnectWise.Apis.v3_0.v2015_3.Sales.Opportunity.Opportunity
        api_response = api_instance.patch_sales_opportunities_by_id(id, client_id, patch_operation)
        print("The response of OpportunitiesApi->patch_sales_opportunities_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpportunitiesApi->patch_sales_opportunities_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| opportunityId | 
 **client_id** | **str**|  | 
 **patch_operation** | [**List[PatchOperation]**](PatchOperation.md)| List of PatchOperation | 

### Return type

[**Opportunity**](Opportunity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ConnectWise.Apis.v3_0.v2015_3.Sales.Opportunity.Opportunity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_sales_opportunities**
> Opportunity post_sales_opportunities(client_id, opportunity)

Post ConnectWise.Apis.v3_0.v2015_3.Sales.Opportunity.Opportunity

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.opportunity import Opportunity
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
    api_instance = connectwise_psa.OpportunitiesApi(api_client)
    client_id = 'client_id_example' # str | 
    opportunity = connectwise_psa.Opportunity() # Opportunity | opportunity

    try:
        # Post ConnectWise.Apis.v3_0.v2015_3.Sales.Opportunity.Opportunity
        api_response = api_instance.post_sales_opportunities(client_id, opportunity)
        print("The response of OpportunitiesApi->post_sales_opportunities:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpportunitiesApi->post_sales_opportunities: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**|  | 
 **opportunity** | [**Opportunity**](Opportunity.md)| opportunity | 

### Return type

[**Opportunity**](Opportunity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | ConnectWise.Apis.v3_0.v2015_3.Sales.Opportunity.Opportunity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_sales_opportunities_by_id_convert_to_agreement**
> Agreement post_sales_opportunities_by_id_convert_to_agreement(id, client_id, opportunity_to_agreement_conversion)

Post ApiAgreement

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.agreement import Agreement
from connectwise_psa.models.opportunity_to_agreement_conversion import OpportunityToAgreementConversion
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
    api_instance = connectwise_psa.OpportunitiesApi(api_client)
    id = 56 # int | opportunityId
    client_id = 'client_id_example' # str | 
    opportunity_to_agreement_conversion = connectwise_psa.OpportunityToAgreementConversion() # OpportunityToAgreementConversion | conversion

    try:
        # Post ApiAgreement
        api_response = api_instance.post_sales_opportunities_by_id_convert_to_agreement(id, client_id, opportunity_to_agreement_conversion)
        print("The response of OpportunitiesApi->post_sales_opportunities_by_id_convert_to_agreement:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpportunitiesApi->post_sales_opportunities_by_id_convert_to_agreement: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| opportunityId | 
 **client_id** | **str**|  | 
 **opportunity_to_agreement_conversion** | [**OpportunityToAgreementConversion**](OpportunityToAgreementConversion.md)| conversion | 

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
**201** | ApiAgreement |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_sales_opportunities_by_id_convert_to_project**
> Project post_sales_opportunities_by_id_convert_to_project(id, client_id, opportunity_to_project_conversion)

Post ApiProject

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.opportunity_to_project_conversion import OpportunityToProjectConversion
from connectwise_psa.models.project import Project
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
    api_instance = connectwise_psa.OpportunitiesApi(api_client)
    id = 56 # int | opportunityId
    client_id = 'client_id_example' # str | 
    opportunity_to_project_conversion = connectwise_psa.OpportunityToProjectConversion() # OpportunityToProjectConversion | conversion

    try:
        # Post ApiProject
        api_response = api_instance.post_sales_opportunities_by_id_convert_to_project(id, client_id, opportunity_to_project_conversion)
        print("The response of OpportunitiesApi->post_sales_opportunities_by_id_convert_to_project:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpportunitiesApi->post_sales_opportunities_by_id_convert_to_project: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| opportunityId | 
 **client_id** | **str**|  | 
 **opportunity_to_project_conversion** | [**OpportunityToProjectConversion**](OpportunityToProjectConversion.md)| conversion | 

### Return type

[**Project**](Project.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | ApiProject |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_sales_opportunities_by_id_convert_to_sales_order**
> Order post_sales_opportunities_by_id_convert_to_sales_order(id, client_id, opportunity_to_sales_order_conversion)

Post ApiSalesOrder

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.opportunity_to_sales_order_conversion import OpportunityToSalesOrderConversion
from connectwise_psa.models.order import Order
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
    api_instance = connectwise_psa.OpportunitiesApi(api_client)
    id = 56 # int | opportunityId
    client_id = 'client_id_example' # str | 
    opportunity_to_sales_order_conversion = connectwise_psa.OpportunityToSalesOrderConversion() # OpportunityToSalesOrderConversion | conversion

    try:
        # Post ApiSalesOrder
        api_response = api_instance.post_sales_opportunities_by_id_convert_to_sales_order(id, client_id, opportunity_to_sales_order_conversion)
        print("The response of OpportunitiesApi->post_sales_opportunities_by_id_convert_to_sales_order:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpportunitiesApi->post_sales_opportunities_by_id_convert_to_sales_order: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| opportunityId | 
 **client_id** | **str**|  | 
 **opportunity_to_sales_order_conversion** | [**OpportunityToSalesOrderConversion**](OpportunityToSalesOrderConversion.md)| conversion | 

### Return type

[**Order**](Order.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | ApiSalesOrder |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_sales_opportunities_by_id_convert_to_service_ticket**
> Ticket post_sales_opportunities_by_id_convert_to_service_ticket(id, client_id, opportunity_to_service_ticket_conversion)

Post ApiTicket

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.opportunity_to_service_ticket_conversion import OpportunityToServiceTicketConversion
from connectwise_psa.models.ticket import Ticket
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
    api_instance = connectwise_psa.OpportunitiesApi(api_client)
    id = 56 # int | opportunityId
    client_id = 'client_id_example' # str | 
    opportunity_to_service_ticket_conversion = connectwise_psa.OpportunityToServiceTicketConversion() # OpportunityToServiceTicketConversion | conversion

    try:
        # Post ApiTicket
        api_response = api_instance.post_sales_opportunities_by_id_convert_to_service_ticket(id, client_id, opportunity_to_service_ticket_conversion)
        print("The response of OpportunitiesApi->post_sales_opportunities_by_id_convert_to_service_ticket:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpportunitiesApi->post_sales_opportunities_by_id_convert_to_service_ticket: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| opportunityId | 
 **client_id** | **str**|  | 
 **opportunity_to_service_ticket_conversion** | [**OpportunityToServiceTicketConversion**](OpportunityToServiceTicketConversion.md)| conversion | 

### Return type

[**Ticket**](Ticket.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | ApiTicket |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_sales_opportunities_by_id**
> Opportunity put_sales_opportunities_by_id(id, client_id, opportunity)

Put ConnectWise.Apis.v3_0.v2015_3.Sales.Opportunity.Opportunity

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.opportunity import Opportunity
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
    api_instance = connectwise_psa.OpportunitiesApi(api_client)
    id = 56 # int | opportunityId
    client_id = 'client_id_example' # str | 
    opportunity = connectwise_psa.Opportunity() # Opportunity | opportunity

    try:
        # Put ConnectWise.Apis.v3_0.v2015_3.Sales.Opportunity.Opportunity
        api_response = api_instance.put_sales_opportunities_by_id(id, client_id, opportunity)
        print("The response of OpportunitiesApi->put_sales_opportunities_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpportunitiesApi->put_sales_opportunities_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| opportunityId | 
 **client_id** | **str**|  | 
 **opportunity** | [**Opportunity**](Opportunity.md)| opportunity | 

### Return type

[**Opportunity**](Opportunity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ConnectWise.Apis.v3_0.v2015_3.Sales.Opportunity.Opportunity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

