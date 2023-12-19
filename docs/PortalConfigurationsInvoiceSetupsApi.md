# connectwise_psa.PortalConfigurationsInvoiceSetupsApi

All URIs are relative to *https://api-aus.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_company_portal_configurations_by_parent_id_invoice_setups**](PortalConfigurationsInvoiceSetupsApi.md#get_company_portal_configurations_by_parent_id_invoice_setups) | **GET** /company/portalConfigurations/{parentId}/invoiceSetups | Get List of PortalConfigurationInvoiceSetup
[**get_company_portal_configurations_by_parent_id_invoice_setups_by_id**](PortalConfigurationsInvoiceSetupsApi.md#get_company_portal_configurations_by_parent_id_invoice_setups_by_id) | **GET** /company/portalConfigurations/{parentId}/invoiceSetups/{id} | Get PortalConfigurationInvoiceSetup
[**get_company_portal_configurations_by_parent_id_invoice_setups_count**](PortalConfigurationsInvoiceSetupsApi.md#get_company_portal_configurations_by_parent_id_invoice_setups_count) | **GET** /company/portalConfigurations/{parentId}/invoiceSetups/count | Get Count of PortalConfigurationInvoiceSetup
[**patch_company_portal_configurations_by_parent_id_invoice_setups_by_id**](PortalConfigurationsInvoiceSetupsApi.md#patch_company_portal_configurations_by_parent_id_invoice_setups_by_id) | **PATCH** /company/portalConfigurations/{parentId}/invoiceSetups/{id} | Patch PortalConfigurationInvoiceSetup
[**post_company_portal_configurations_by_parent_id_invoice_setups_by_id_test_transaction**](PortalConfigurationsInvoiceSetupsApi.md#post_company_portal_configurations_by_parent_id_invoice_setups_by_id_test_transaction) | **POST** /company/portalConfigurations/{parentId}/invoiceSetups/{id}/testTransaction | Post SuccessResponse
[**put_company_portal_configurations_by_parent_id_invoice_setups_by_id**](PortalConfigurationsInvoiceSetupsApi.md#put_company_portal_configurations_by_parent_id_invoice_setups_by_id) | **PUT** /company/portalConfigurations/{parentId}/invoiceSetups/{id} | Put PortalConfigurationInvoiceSetup


# **get_company_portal_configurations_by_parent_id_invoice_setups**
> List[PortalConfigurationInvoiceSetup] get_company_portal_configurations_by_parent_id_invoice_setups(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of PortalConfigurationInvoiceSetup

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.portal_configuration_invoice_setup import PortalConfigurationInvoiceSetup
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
    api_instance = connectwise_psa.PortalConfigurationsInvoiceSetupsApi(api_client)
    parent_id = 56 # int | portalConfigurationId
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
        # Get List of PortalConfigurationInvoiceSetup
        api_response = api_instance.get_company_portal_configurations_by_parent_id_invoice_setups(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of PortalConfigurationsInvoiceSetupsApi->get_company_portal_configurations_by_parent_id_invoice_setups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortalConfigurationsInvoiceSetupsApi->get_company_portal_configurations_by_parent_id_invoice_setups: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| portalConfigurationId | 
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

[**List[PortalConfigurationInvoiceSetup]**](PortalConfigurationInvoiceSetup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of PortalConfigurationInvoiceSetup |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_company_portal_configurations_by_parent_id_invoice_setups_by_id**
> PortalConfigurationInvoiceSetup get_company_portal_configurations_by_parent_id_invoice_setups_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get PortalConfigurationInvoiceSetup

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.portal_configuration_invoice_setup import PortalConfigurationInvoiceSetup
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
    api_instance = connectwise_psa.PortalConfigurationsInvoiceSetupsApi(api_client)
    id = 56 # int | invoiceSetupId
    parent_id = 56 # int | portalConfigurationId
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
        # Get PortalConfigurationInvoiceSetup
        api_response = api_instance.get_company_portal_configurations_by_parent_id_invoice_setups_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of PortalConfigurationsInvoiceSetupsApi->get_company_portal_configurations_by_parent_id_invoice_setups_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortalConfigurationsInvoiceSetupsApi->get_company_portal_configurations_by_parent_id_invoice_setups_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| invoiceSetupId | 
 **parent_id** | **int**| portalConfigurationId | 
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

[**PortalConfigurationInvoiceSetup**](PortalConfigurationInvoiceSetup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | PortalConfigurationInvoiceSetup |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_company_portal_configurations_by_parent_id_invoice_setups_count**
> Count get_company_portal_configurations_by_parent_id_invoice_setups_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Count of PortalConfigurationInvoiceSetup

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
    api_instance = connectwise_psa.PortalConfigurationsInvoiceSetupsApi(api_client)
    parent_id = 56 # int | portalConfigurationId
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
        # Get Count of PortalConfigurationInvoiceSetup
        api_response = api_instance.get_company_portal_configurations_by_parent_id_invoice_setups_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of PortalConfigurationsInvoiceSetupsApi->get_company_portal_configurations_by_parent_id_invoice_setups_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortalConfigurationsInvoiceSetupsApi->get_company_portal_configurations_by_parent_id_invoice_setups_count: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| portalConfigurationId | 
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

# **patch_company_portal_configurations_by_parent_id_invoice_setups_by_id**
> PortalConfigurationInvoiceSetup patch_company_portal_configurations_by_parent_id_invoice_setups_by_id(id, parent_id, client_id, patch_operation)

Patch PortalConfigurationInvoiceSetup

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.patch_operation import PatchOperation
from connectwise_psa.models.portal_configuration_invoice_setup import PortalConfigurationInvoiceSetup
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
    api_instance = connectwise_psa.PortalConfigurationsInvoiceSetupsApi(api_client)
    id = 56 # int | invoiceSetupId
    parent_id = 56 # int | portalConfigurationId
    client_id = 'client_id_example' # str | 
    patch_operation = [connectwise_psa.PatchOperation()] # List[PatchOperation] | List of PatchOperation

    try:
        # Patch PortalConfigurationInvoiceSetup
        api_response = api_instance.patch_company_portal_configurations_by_parent_id_invoice_setups_by_id(id, parent_id, client_id, patch_operation)
        print("The response of PortalConfigurationsInvoiceSetupsApi->patch_company_portal_configurations_by_parent_id_invoice_setups_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortalConfigurationsInvoiceSetupsApi->patch_company_portal_configurations_by_parent_id_invoice_setups_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| invoiceSetupId | 
 **parent_id** | **int**| portalConfigurationId | 
 **client_id** | **str**|  | 
 **patch_operation** | [**List[PatchOperation]**](PatchOperation.md)| List of PatchOperation | 

### Return type

[**PortalConfigurationInvoiceSetup**](PortalConfigurationInvoiceSetup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | PortalConfigurationInvoiceSetup |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_company_portal_configurations_by_parent_id_invoice_setups_by_id_test_transaction**
> SuccessResponse post_company_portal_configurations_by_parent_id_invoice_setups_by_id_test_transaction(id, parent_id, client_id, portal_configuration_invoice_setup)

Post SuccessResponse

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.portal_configuration_invoice_setup import PortalConfigurationInvoiceSetup
from connectwise_psa.models.success_response import SuccessResponse
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
    api_instance = connectwise_psa.PortalConfigurationsInvoiceSetupsApi(api_client)
    id = 56 # int | invoiceSetupId
    parent_id = 56 # int | portalConfigurationId
    client_id = 'client_id_example' # str | 
    portal_configuration_invoice_setup = connectwise_psa.PortalConfigurationInvoiceSetup() # PortalConfigurationInvoiceSetup | portalConfigurationInvoiceSetup

    try:
        # Post SuccessResponse
        api_response = api_instance.post_company_portal_configurations_by_parent_id_invoice_setups_by_id_test_transaction(id, parent_id, client_id, portal_configuration_invoice_setup)
        print("The response of PortalConfigurationsInvoiceSetupsApi->post_company_portal_configurations_by_parent_id_invoice_setups_by_id_test_transaction:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortalConfigurationsInvoiceSetupsApi->post_company_portal_configurations_by_parent_id_invoice_setups_by_id_test_transaction: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| invoiceSetupId | 
 **parent_id** | **int**| portalConfigurationId | 
 **client_id** | **str**|  | 
 **portal_configuration_invoice_setup** | [**PortalConfigurationInvoiceSetup**](PortalConfigurationInvoiceSetup.md)| portalConfigurationInvoiceSetup | 

### Return type

[**SuccessResponse**](SuccessResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | SuccessResponse |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_company_portal_configurations_by_parent_id_invoice_setups_by_id**
> PortalConfigurationInvoiceSetup put_company_portal_configurations_by_parent_id_invoice_setups_by_id(id, parent_id, client_id, portal_configuration_invoice_setup)

Put PortalConfigurationInvoiceSetup

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.portal_configuration_invoice_setup import PortalConfigurationInvoiceSetup
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
    api_instance = connectwise_psa.PortalConfigurationsInvoiceSetupsApi(api_client)
    id = 56 # int | invoiceSetupId
    parent_id = 56 # int | portalConfigurationId
    client_id = 'client_id_example' # str | 
    portal_configuration_invoice_setup = connectwise_psa.PortalConfigurationInvoiceSetup() # PortalConfigurationInvoiceSetup | portalConfigurationInvoiceSetup

    try:
        # Put PortalConfigurationInvoiceSetup
        api_response = api_instance.put_company_portal_configurations_by_parent_id_invoice_setups_by_id(id, parent_id, client_id, portal_configuration_invoice_setup)
        print("The response of PortalConfigurationsInvoiceSetupsApi->put_company_portal_configurations_by_parent_id_invoice_setups_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortalConfigurationsInvoiceSetupsApi->put_company_portal_configurations_by_parent_id_invoice_setups_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| invoiceSetupId | 
 **parent_id** | **int**| portalConfigurationId | 
 **client_id** | **str**|  | 
 **portal_configuration_invoice_setup** | [**PortalConfigurationInvoiceSetup**](PortalConfigurationInvoiceSetup.md)| portalConfigurationInvoiceSetup | 

### Return type

[**PortalConfigurationInvoiceSetup**](PortalConfigurationInvoiceSetup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | PortalConfigurationInvoiceSetup |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

