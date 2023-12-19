# connectwise_psa.ManagementReportSetupsApi

All URIs are relative to *https://api-aus.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_company_companies_by_parent_id_management_report_setup**](ManagementReportSetupsApi.md#get_company_companies_by_parent_id_management_report_setup) | **GET** /company/companies/{parentId}/managementReportSetup | Get List of ManagementReportSetup
[**patch_company_companies_by_parent_id_management_report_setup_by_id**](ManagementReportSetupsApi.md#patch_company_companies_by_parent_id_management_report_setup_by_id) | **PATCH** /company/companies/{parentId}/managementReportSetup/{id} | Patch ManagementReportSetup
[**post_company_companies_by_parent_id_management_report_setup**](ManagementReportSetupsApi.md#post_company_companies_by_parent_id_management_report_setup) | **POST** /company/companies/{parentId}/managementReportSetup | Post ManagementReportSetup
[**put_company_companies_by_parent_id_management_report_setup_by_id**](ManagementReportSetupsApi.md#put_company_companies_by_parent_id_management_report_setup_by_id) | **PUT** /company/companies/{parentId}/managementReportSetup/{id} | Put ManagementReportSetup


# **get_company_companies_by_parent_id_management_report_setup**
> List[ManagementReportSetup] get_company_companies_by_parent_id_management_report_setup(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of ManagementReportSetup

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.management_report_setup import ManagementReportSetup
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
    api_instance = connectwise_psa.ManagementReportSetupsApi(api_client)
    parent_id = 56 # int | companyId
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
        # Get List of ManagementReportSetup
        api_response = api_instance.get_company_companies_by_parent_id_management_report_setup(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of ManagementReportSetupsApi->get_company_companies_by_parent_id_management_report_setup:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagementReportSetupsApi->get_company_companies_by_parent_id_management_report_setup: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| companyId | 
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

[**List[ManagementReportSetup]**](ManagementReportSetup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of ManagementReportSetup |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_company_companies_by_parent_id_management_report_setup_by_id**
> ManagementReportSetup patch_company_companies_by_parent_id_management_report_setup_by_id(id, parent_id, client_id, patch_operation)

Patch ManagementReportSetup

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.management_report_setup import ManagementReportSetup
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
    api_instance = connectwise_psa.ManagementReportSetupsApi(api_client)
    id = 56 # int | managementReportSetupId
    parent_id = 56 # int | companyId
    client_id = 'client_id_example' # str | 
    patch_operation = [connectwise_psa.PatchOperation()] # List[PatchOperation] | List of PatchOperation

    try:
        # Patch ManagementReportSetup
        api_response = api_instance.patch_company_companies_by_parent_id_management_report_setup_by_id(id, parent_id, client_id, patch_operation)
        print("The response of ManagementReportSetupsApi->patch_company_companies_by_parent_id_management_report_setup_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagementReportSetupsApi->patch_company_companies_by_parent_id_management_report_setup_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| managementReportSetupId | 
 **parent_id** | **int**| companyId | 
 **client_id** | **str**|  | 
 **patch_operation** | [**List[PatchOperation]**](PatchOperation.md)| List of PatchOperation | 

### Return type

[**ManagementReportSetup**](ManagementReportSetup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ManagementReportSetup |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_company_companies_by_parent_id_management_report_setup**
> ManagementReportSetup post_company_companies_by_parent_id_management_report_setup(parent_id, client_id, management_report_setup)

Post ManagementReportSetup

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.management_report_setup import ManagementReportSetup
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
    api_instance = connectwise_psa.ManagementReportSetupsApi(api_client)
    parent_id = 56 # int | companyId
    client_id = 'client_id_example' # str | 
    management_report_setup = connectwise_psa.ManagementReportSetup() # ManagementReportSetup | managementReportSetup

    try:
        # Post ManagementReportSetup
        api_response = api_instance.post_company_companies_by_parent_id_management_report_setup(parent_id, client_id, management_report_setup)
        print("The response of ManagementReportSetupsApi->post_company_companies_by_parent_id_management_report_setup:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagementReportSetupsApi->post_company_companies_by_parent_id_management_report_setup: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| companyId | 
 **client_id** | **str**|  | 
 **management_report_setup** | [**ManagementReportSetup**](ManagementReportSetup.md)| managementReportSetup | 

### Return type

[**ManagementReportSetup**](ManagementReportSetup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | ManagementReportSetup |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_company_companies_by_parent_id_management_report_setup_by_id**
> ManagementReportSetup put_company_companies_by_parent_id_management_report_setup_by_id(id, parent_id, client_id, management_report_setup)

Put ManagementReportSetup

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.management_report_setup import ManagementReportSetup
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
    api_instance = connectwise_psa.ManagementReportSetupsApi(api_client)
    id = 56 # int | managementReportSetupId
    parent_id = 56 # int | companyId
    client_id = 'client_id_example' # str | 
    management_report_setup = connectwise_psa.ManagementReportSetup() # ManagementReportSetup | managementReportSetup

    try:
        # Put ManagementReportSetup
        api_response = api_instance.put_company_companies_by_parent_id_management_report_setup_by_id(id, parent_id, client_id, management_report_setup)
        print("The response of ManagementReportSetupsApi->put_company_companies_by_parent_id_management_report_setup_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagementReportSetupsApi->put_company_companies_by_parent_id_management_report_setup_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| managementReportSetupId | 
 **parent_id** | **int**| companyId | 
 **client_id** | **str**|  | 
 **management_report_setup** | [**ManagementReportSetup**](ManagementReportSetup.md)| managementReportSetup | 

### Return type

[**ManagementReportSetup**](ManagementReportSetup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ManagementReportSetup |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

