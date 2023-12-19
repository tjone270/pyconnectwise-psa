# connectwise_psa.PortalConfigurationPasswordEmailSetupsApi

All URIs are relative to *https://aus-api.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_company_portal_configurations_by_parent_id_password_email_setups**](PortalConfigurationPasswordEmailSetupsApi.md#get_company_portal_configurations_by_parent_id_password_email_setups) | **GET** /company/portalConfigurations/{parentId}/passwordEmailSetups | Get List of PortalConfigurationPasswordEmailSetup
[**get_company_portal_configurations_by_parent_id_password_email_setups_by_id**](PortalConfigurationPasswordEmailSetupsApi.md#get_company_portal_configurations_by_parent_id_password_email_setups_by_id) | **GET** /company/portalConfigurations/{parentId}/passwordEmailSetups/{id} | Get PortalConfigurationPasswordEmailSetup
[**patch_company_portal_configurations_by_parent_id_password_email_setups_by_id**](PortalConfigurationPasswordEmailSetupsApi.md#patch_company_portal_configurations_by_parent_id_password_email_setups_by_id) | **PATCH** /company/portalConfigurations/{parentId}/passwordEmailSetups/{id} | Patch PortalConfigurationPasswordEmailSetup
[**put_company_portal_configurations_by_parent_id_password_email_setups_by_id**](PortalConfigurationPasswordEmailSetupsApi.md#put_company_portal_configurations_by_parent_id_password_email_setups_by_id) | **PUT** /company/portalConfigurations/{parentId}/passwordEmailSetups/{id} | Put PortalConfigurationPasswordEmailSetup


# **get_company_portal_configurations_by_parent_id_password_email_setups**
> List[PortalConfigurationPasswordEmailSetup] get_company_portal_configurations_by_parent_id_password_email_setups(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of PortalConfigurationPasswordEmailSetup

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.portal_configuration_password_email_setup import PortalConfigurationPasswordEmailSetup
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
    api_instance = connectwise_psa.PortalConfigurationPasswordEmailSetupsApi(api_client)
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
        # Get List of PortalConfigurationPasswordEmailSetup
        api_response = api_instance.get_company_portal_configurations_by_parent_id_password_email_setups(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of PortalConfigurationPasswordEmailSetupsApi->get_company_portal_configurations_by_parent_id_password_email_setups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortalConfigurationPasswordEmailSetupsApi->get_company_portal_configurations_by_parent_id_password_email_setups: %s\n" % e)
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

[**List[PortalConfigurationPasswordEmailSetup]**](PortalConfigurationPasswordEmailSetup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of PortalConfigurationPasswordEmailSetup |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_company_portal_configurations_by_parent_id_password_email_setups_by_id**
> PortalConfigurationPasswordEmailSetup get_company_portal_configurations_by_parent_id_password_email_setups_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get PortalConfigurationPasswordEmailSetup

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.portal_configuration_password_email_setup import PortalConfigurationPasswordEmailSetup
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
    api_instance = connectwise_psa.PortalConfigurationPasswordEmailSetupsApi(api_client)
    id = 56 # int | passwordEmailSetupId
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
        # Get PortalConfigurationPasswordEmailSetup
        api_response = api_instance.get_company_portal_configurations_by_parent_id_password_email_setups_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of PortalConfigurationPasswordEmailSetupsApi->get_company_portal_configurations_by_parent_id_password_email_setups_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortalConfigurationPasswordEmailSetupsApi->get_company_portal_configurations_by_parent_id_password_email_setups_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| passwordEmailSetupId | 
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

[**PortalConfigurationPasswordEmailSetup**](PortalConfigurationPasswordEmailSetup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | PortalConfigurationPasswordEmailSetup |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_company_portal_configurations_by_parent_id_password_email_setups_by_id**
> PortalConfigurationPasswordEmailSetup patch_company_portal_configurations_by_parent_id_password_email_setups_by_id(id, parent_id, client_id, patch_operation)

Patch PortalConfigurationPasswordEmailSetup

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.patch_operation import PatchOperation
from connectwise_psa.models.portal_configuration_password_email_setup import PortalConfigurationPasswordEmailSetup
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
    api_instance = connectwise_psa.PortalConfigurationPasswordEmailSetupsApi(api_client)
    id = 56 # int | passwordEmailSetupId
    parent_id = 56 # int | portalConfigurationId
    client_id = 'client_id_example' # str | 
    patch_operation = [connectwise_psa.PatchOperation()] # List[PatchOperation] | List of PatchOperation

    try:
        # Patch PortalConfigurationPasswordEmailSetup
        api_response = api_instance.patch_company_portal_configurations_by_parent_id_password_email_setups_by_id(id, parent_id, client_id, patch_operation)
        print("The response of PortalConfigurationPasswordEmailSetupsApi->patch_company_portal_configurations_by_parent_id_password_email_setups_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortalConfigurationPasswordEmailSetupsApi->patch_company_portal_configurations_by_parent_id_password_email_setups_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| passwordEmailSetupId | 
 **parent_id** | **int**| portalConfigurationId | 
 **client_id** | **str**|  | 
 **patch_operation** | [**List[PatchOperation]**](PatchOperation.md)| List of PatchOperation | 

### Return type

[**PortalConfigurationPasswordEmailSetup**](PortalConfigurationPasswordEmailSetup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | PortalConfigurationPasswordEmailSetup |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_company_portal_configurations_by_parent_id_password_email_setups_by_id**
> PortalConfigurationPasswordEmailSetup put_company_portal_configurations_by_parent_id_password_email_setups_by_id(id, parent_id, client_id, portal_configuration_password_email_setup)

Put PortalConfigurationPasswordEmailSetup

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.portal_configuration_password_email_setup import PortalConfigurationPasswordEmailSetup
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
    api_instance = connectwise_psa.PortalConfigurationPasswordEmailSetupsApi(api_client)
    id = 56 # int | passwordEmailSetupId
    parent_id = 56 # int | portalConfigurationId
    client_id = 'client_id_example' # str | 
    portal_configuration_password_email_setup = connectwise_psa.PortalConfigurationPasswordEmailSetup() # PortalConfigurationPasswordEmailSetup | passwordEmailSetup

    try:
        # Put PortalConfigurationPasswordEmailSetup
        api_response = api_instance.put_company_portal_configurations_by_parent_id_password_email_setups_by_id(id, parent_id, client_id, portal_configuration_password_email_setup)
        print("The response of PortalConfigurationPasswordEmailSetupsApi->put_company_portal_configurations_by_parent_id_password_email_setups_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortalConfigurationPasswordEmailSetupsApi->put_company_portal_configurations_by_parent_id_password_email_setups_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| passwordEmailSetupId | 
 **parent_id** | **int**| portalConfigurationId | 
 **client_id** | **str**|  | 
 **portal_configuration_password_email_setup** | [**PortalConfigurationPasswordEmailSetup**](PortalConfigurationPasswordEmailSetup.md)| passwordEmailSetup | 

### Return type

[**PortalConfigurationPasswordEmailSetup**](PortalConfigurationPasswordEmailSetup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | PortalConfigurationPasswordEmailSetup |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

