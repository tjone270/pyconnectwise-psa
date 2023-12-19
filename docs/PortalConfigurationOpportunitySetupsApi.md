# connectwise_psa.PortalConfigurationOpportunitySetupsApi

All URIs are relative to *https://aus-api.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_company_portal_configurations_by_parent_id_opportunity_setups**](PortalConfigurationOpportunitySetupsApi.md#get_company_portal_configurations_by_parent_id_opportunity_setups) | **GET** /company/portalConfigurations/{parentId}/opportunitySetups | Get List of PortalConfigurationOpportunitySetup
[**get_company_portal_configurations_by_parent_id_opportunity_setups_by_id**](PortalConfigurationOpportunitySetupsApi.md#get_company_portal_configurations_by_parent_id_opportunity_setups_by_id) | **GET** /company/portalConfigurations/{parentId}/opportunitySetups/{id} | Get PortalConfigurationOpportunitySetup
[**patch_company_portal_configurations_by_parent_id_opportunity_setups**](PortalConfigurationOpportunitySetupsApi.md#patch_company_portal_configurations_by_parent_id_opportunity_setups) | **PATCH** /company/portalConfigurations/{parentId}/opportunitySetups | Patch PortalConfigurationOpportunitySetup
[**patch_company_portal_configurations_by_parent_id_opportunity_setups_by_id**](PortalConfigurationOpportunitySetupsApi.md#patch_company_portal_configurations_by_parent_id_opportunity_setups_by_id) | **PATCH** /company/portalConfigurations/{parentId}/opportunitySetups/{id} | Patch PortalConfigurationOpportunitySetup
[**put_company_portal_configurations_by_parent_id_opportunity_setups**](PortalConfigurationOpportunitySetupsApi.md#put_company_portal_configurations_by_parent_id_opportunity_setups) | **PUT** /company/portalConfigurations/{parentId}/opportunitySetups | Put PortalConfigurationOpportunitySetup
[**put_company_portal_configurations_by_parent_id_opportunity_setups_by_id**](PortalConfigurationOpportunitySetupsApi.md#put_company_portal_configurations_by_parent_id_opportunity_setups_by_id) | **PUT** /company/portalConfigurations/{parentId}/opportunitySetups/{id} | Put PortalConfigurationOpportunitySetup


# **get_company_portal_configurations_by_parent_id_opportunity_setups**
> List[PortalConfigurationOpportunitySetup] get_company_portal_configurations_by_parent_id_opportunity_setups(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of PortalConfigurationOpportunitySetup

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.portal_configuration_opportunity_setup import PortalConfigurationOpportunitySetup
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
    api_instance = connectwise_psa.PortalConfigurationOpportunitySetupsApi(api_client)
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
        # Get List of PortalConfigurationOpportunitySetup
        api_response = api_instance.get_company_portal_configurations_by_parent_id_opportunity_setups(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of PortalConfigurationOpportunitySetupsApi->get_company_portal_configurations_by_parent_id_opportunity_setups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortalConfigurationOpportunitySetupsApi->get_company_portal_configurations_by_parent_id_opportunity_setups: %s\n" % e)
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

[**List[PortalConfigurationOpportunitySetup]**](PortalConfigurationOpportunitySetup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of PortalConfigurationOpportunitySetup |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_company_portal_configurations_by_parent_id_opportunity_setups_by_id**
> PortalConfigurationOpportunitySetup get_company_portal_configurations_by_parent_id_opportunity_setups_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get PortalConfigurationOpportunitySetup

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.portal_configuration_opportunity_setup import PortalConfigurationOpportunitySetup
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
    api_instance = connectwise_psa.PortalConfigurationOpportunitySetupsApi(api_client)
    id = 56 # int | opportunitySetupId
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
        # Get PortalConfigurationOpportunitySetup
        api_response = api_instance.get_company_portal_configurations_by_parent_id_opportunity_setups_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of PortalConfigurationOpportunitySetupsApi->get_company_portal_configurations_by_parent_id_opportunity_setups_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortalConfigurationOpportunitySetupsApi->get_company_portal_configurations_by_parent_id_opportunity_setups_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| opportunitySetupId | 
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

[**PortalConfigurationOpportunitySetup**](PortalConfigurationOpportunitySetup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | PortalConfigurationOpportunitySetup |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_company_portal_configurations_by_parent_id_opportunity_setups**
> PortalConfigurationOpportunitySetup patch_company_portal_configurations_by_parent_id_opportunity_setups(parent_id, client_id, patch_operation)

Patch PortalConfigurationOpportunitySetup

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.patch_operation import PatchOperation
from connectwise_psa.models.portal_configuration_opportunity_setup import PortalConfigurationOpportunitySetup
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
    api_instance = connectwise_psa.PortalConfigurationOpportunitySetupsApi(api_client)
    parent_id = 56 # int | portalConfigurationId
    client_id = 'client_id_example' # str | 
    patch_operation = [connectwise_psa.PatchOperation()] # List[PatchOperation] | List of PatchOperation

    try:
        # Patch PortalConfigurationOpportunitySetup
        api_response = api_instance.patch_company_portal_configurations_by_parent_id_opportunity_setups(parent_id, client_id, patch_operation)
        print("The response of PortalConfigurationOpportunitySetupsApi->patch_company_portal_configurations_by_parent_id_opportunity_setups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortalConfigurationOpportunitySetupsApi->patch_company_portal_configurations_by_parent_id_opportunity_setups: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| portalConfigurationId | 
 **client_id** | **str**|  | 
 **patch_operation** | [**List[PatchOperation]**](PatchOperation.md)| List of PatchOperation | 

### Return type

[**PortalConfigurationOpportunitySetup**](PortalConfigurationOpportunitySetup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | PortalConfigurationOpportunitySetup |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_company_portal_configurations_by_parent_id_opportunity_setups_by_id**
> PortalConfigurationOpportunitySetup patch_company_portal_configurations_by_parent_id_opportunity_setups_by_id(id, parent_id, client_id, patch_operation)

Patch PortalConfigurationOpportunitySetup

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.patch_operation import PatchOperation
from connectwise_psa.models.portal_configuration_opportunity_setup import PortalConfigurationOpportunitySetup
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
    api_instance = connectwise_psa.PortalConfigurationOpportunitySetupsApi(api_client)
    id = 56 # int | opportunitySetupId
    parent_id = 56 # int | portalConfigurationId
    client_id = 'client_id_example' # str | 
    patch_operation = [connectwise_psa.PatchOperation()] # List[PatchOperation] | List of PatchOperation

    try:
        # Patch PortalConfigurationOpportunitySetup
        api_response = api_instance.patch_company_portal_configurations_by_parent_id_opportunity_setups_by_id(id, parent_id, client_id, patch_operation)
        print("The response of PortalConfigurationOpportunitySetupsApi->patch_company_portal_configurations_by_parent_id_opportunity_setups_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortalConfigurationOpportunitySetupsApi->patch_company_portal_configurations_by_parent_id_opportunity_setups_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| opportunitySetupId | 
 **parent_id** | **int**| portalConfigurationId | 
 **client_id** | **str**|  | 
 **patch_operation** | [**List[PatchOperation]**](PatchOperation.md)| List of PatchOperation | 

### Return type

[**PortalConfigurationOpportunitySetup**](PortalConfigurationOpportunitySetup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | PortalConfigurationOpportunitySetup |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_company_portal_configurations_by_parent_id_opportunity_setups**
> PortalConfigurationOpportunitySetup put_company_portal_configurations_by_parent_id_opportunity_setups(parent_id, client_id, portal_configuration_opportunity_setup)

Put PortalConfigurationOpportunitySetup

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.portal_configuration_opportunity_setup import PortalConfigurationOpportunitySetup
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
    api_instance = connectwise_psa.PortalConfigurationOpportunitySetupsApi(api_client)
    parent_id = 56 # int | portalConfigurationId
    client_id = 'client_id_example' # str | 
    portal_configuration_opportunity_setup = connectwise_psa.PortalConfigurationOpportunitySetup() # PortalConfigurationOpportunitySetup | opportunitySetup

    try:
        # Put PortalConfigurationOpportunitySetup
        api_response = api_instance.put_company_portal_configurations_by_parent_id_opportunity_setups(parent_id, client_id, portal_configuration_opportunity_setup)
        print("The response of PortalConfigurationOpportunitySetupsApi->put_company_portal_configurations_by_parent_id_opportunity_setups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortalConfigurationOpportunitySetupsApi->put_company_portal_configurations_by_parent_id_opportunity_setups: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| portalConfigurationId | 
 **client_id** | **str**|  | 
 **portal_configuration_opportunity_setup** | [**PortalConfigurationOpportunitySetup**](PortalConfigurationOpportunitySetup.md)| opportunitySetup | 

### Return type

[**PortalConfigurationOpportunitySetup**](PortalConfigurationOpportunitySetup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | PortalConfigurationOpportunitySetup |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_company_portal_configurations_by_parent_id_opportunity_setups_by_id**
> PortalConfigurationOpportunitySetup put_company_portal_configurations_by_parent_id_opportunity_setups_by_id(id, parent_id, client_id, portal_configuration_opportunity_setup)

Put PortalConfigurationOpportunitySetup

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.portal_configuration_opportunity_setup import PortalConfigurationOpportunitySetup
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
    api_instance = connectwise_psa.PortalConfigurationOpportunitySetupsApi(api_client)
    id = 56 # int | opportunitySetupId
    parent_id = 56 # int | portalConfigurationId
    client_id = 'client_id_example' # str | 
    portal_configuration_opportunity_setup = connectwise_psa.PortalConfigurationOpportunitySetup() # PortalConfigurationOpportunitySetup | opportunitySetup

    try:
        # Put PortalConfigurationOpportunitySetup
        api_response = api_instance.put_company_portal_configurations_by_parent_id_opportunity_setups_by_id(id, parent_id, client_id, portal_configuration_opportunity_setup)
        print("The response of PortalConfigurationOpportunitySetupsApi->put_company_portal_configurations_by_parent_id_opportunity_setups_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortalConfigurationOpportunitySetupsApi->put_company_portal_configurations_by_parent_id_opportunity_setups_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| opportunitySetupId | 
 **parent_id** | **int**| portalConfigurationId | 
 **client_id** | **str**|  | 
 **portal_configuration_opportunity_setup** | [**PortalConfigurationOpportunitySetup**](PortalConfigurationOpportunitySetup.md)| opportunitySetup | 

### Return type

[**PortalConfigurationOpportunitySetup**](PortalConfigurationOpportunitySetup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | PortalConfigurationOpportunitySetup |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

