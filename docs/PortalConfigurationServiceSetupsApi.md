# connectwise_psa.PortalConfigurationServiceSetupsApi

All URIs are relative to *https://aus-api.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_company_portal_configurations_by_parent_id_service_setups**](PortalConfigurationServiceSetupsApi.md#get_company_portal_configurations_by_parent_id_service_setups) | **GET** /company/portalConfigurations/{parentId}/serviceSetups | Get List of PortalConfigurationServiceSetup
[**get_company_portal_configurations_by_parent_id_service_setups_by_id**](PortalConfigurationServiceSetupsApi.md#get_company_portal_configurations_by_parent_id_service_setups_by_id) | **GET** /company/portalConfigurations/{parentId}/serviceSetups/{id} | Get PortalConfigurationServiceSetup
[**get_company_portal_configurations_by_parent_id_service_setups_count**](PortalConfigurationServiceSetupsApi.md#get_company_portal_configurations_by_parent_id_service_setups_count) | **GET** /company/portalConfigurations/{parentId}/serviceSetups/count | Get Count of PortalConfigurationServiceSetup
[**patch_company_portal_configurations_by_parent_id_service_setups_by_id**](PortalConfigurationServiceSetupsApi.md#patch_company_portal_configurations_by_parent_id_service_setups_by_id) | **PATCH** /company/portalConfigurations/{parentId}/serviceSetups/{id} | Patch PortalConfigurationServiceSetup
[**put_company_portal_configurations_by_parent_id_service_setups_by_id**](PortalConfigurationServiceSetupsApi.md#put_company_portal_configurations_by_parent_id_service_setups_by_id) | **PUT** /company/portalConfigurations/{parentId}/serviceSetups/{id} | Put PortalConfigurationServiceSetup


# **get_company_portal_configurations_by_parent_id_service_setups**
> List[PortalConfigurationServiceSetup] get_company_portal_configurations_by_parent_id_service_setups(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of PortalConfigurationServiceSetup

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.portal_configuration_service_setup import PortalConfigurationServiceSetup
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
    api_instance = connectwise_psa.PortalConfigurationServiceSetupsApi(api_client)
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
        # Get List of PortalConfigurationServiceSetup
        api_response = api_instance.get_company_portal_configurations_by_parent_id_service_setups(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of PortalConfigurationServiceSetupsApi->get_company_portal_configurations_by_parent_id_service_setups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortalConfigurationServiceSetupsApi->get_company_portal_configurations_by_parent_id_service_setups: %s\n" % e)
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

[**List[PortalConfigurationServiceSetup]**](PortalConfigurationServiceSetup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of PortalConfigurationServiceSetup |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_company_portal_configurations_by_parent_id_service_setups_by_id**
> PortalConfigurationServiceSetup get_company_portal_configurations_by_parent_id_service_setups_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get PortalConfigurationServiceSetup

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.portal_configuration_service_setup import PortalConfigurationServiceSetup
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
    api_instance = connectwise_psa.PortalConfigurationServiceSetupsApi(api_client)
    id = 56 # int | serviceSetupId
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
        # Get PortalConfigurationServiceSetup
        api_response = api_instance.get_company_portal_configurations_by_parent_id_service_setups_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of PortalConfigurationServiceSetupsApi->get_company_portal_configurations_by_parent_id_service_setups_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortalConfigurationServiceSetupsApi->get_company_portal_configurations_by_parent_id_service_setups_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| serviceSetupId | 
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

[**PortalConfigurationServiceSetup**](PortalConfigurationServiceSetup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | PortalConfigurationServiceSetup |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_company_portal_configurations_by_parent_id_service_setups_count**
> Count get_company_portal_configurations_by_parent_id_service_setups_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Count of PortalConfigurationServiceSetup

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
    api_instance = connectwise_psa.PortalConfigurationServiceSetupsApi(api_client)
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
        # Get Count of PortalConfigurationServiceSetup
        api_response = api_instance.get_company_portal_configurations_by_parent_id_service_setups_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of PortalConfigurationServiceSetupsApi->get_company_portal_configurations_by_parent_id_service_setups_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortalConfigurationServiceSetupsApi->get_company_portal_configurations_by_parent_id_service_setups_count: %s\n" % e)
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

# **patch_company_portal_configurations_by_parent_id_service_setups_by_id**
> PortalConfigurationServiceSetup patch_company_portal_configurations_by_parent_id_service_setups_by_id(id, parent_id, client_id, patch_operation)

Patch PortalConfigurationServiceSetup

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.patch_operation import PatchOperation
from connectwise_psa.models.portal_configuration_service_setup import PortalConfigurationServiceSetup
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
    api_instance = connectwise_psa.PortalConfigurationServiceSetupsApi(api_client)
    id = 56 # int | serviceSetupId
    parent_id = 56 # int | portalConfigurationId
    client_id = 'client_id_example' # str | 
    patch_operation = [connectwise_psa.PatchOperation()] # List[PatchOperation] | List of PatchOperation

    try:
        # Patch PortalConfigurationServiceSetup
        api_response = api_instance.patch_company_portal_configurations_by_parent_id_service_setups_by_id(id, parent_id, client_id, patch_operation)
        print("The response of PortalConfigurationServiceSetupsApi->patch_company_portal_configurations_by_parent_id_service_setups_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortalConfigurationServiceSetupsApi->patch_company_portal_configurations_by_parent_id_service_setups_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| serviceSetupId | 
 **parent_id** | **int**| portalConfigurationId | 
 **client_id** | **str**|  | 
 **patch_operation** | [**List[PatchOperation]**](PatchOperation.md)| List of PatchOperation | 

### Return type

[**PortalConfigurationServiceSetup**](PortalConfigurationServiceSetup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | PortalConfigurationServiceSetup |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_company_portal_configurations_by_parent_id_service_setups_by_id**
> PortalConfigurationServiceSetup put_company_portal_configurations_by_parent_id_service_setups_by_id(id, parent_id, client_id, portal_configuration_service_setup)

Put PortalConfigurationServiceSetup

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.portal_configuration_service_setup import PortalConfigurationServiceSetup
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
    api_instance = connectwise_psa.PortalConfigurationServiceSetupsApi(api_client)
    id = 56 # int | serviceSetupId
    parent_id = 56 # int | portalConfigurationId
    client_id = 'client_id_example' # str | 
    portal_configuration_service_setup = connectwise_psa.PortalConfigurationServiceSetup() # PortalConfigurationServiceSetup | portalConfigurationServiceSetup

    try:
        # Put PortalConfigurationServiceSetup
        api_response = api_instance.put_company_portal_configurations_by_parent_id_service_setups_by_id(id, parent_id, client_id, portal_configuration_service_setup)
        print("The response of PortalConfigurationServiceSetupsApi->put_company_portal_configurations_by_parent_id_service_setups_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortalConfigurationServiceSetupsApi->put_company_portal_configurations_by_parent_id_service_setups_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| serviceSetupId | 
 **parent_id** | **int**| portalConfigurationId | 
 **client_id** | **str**|  | 
 **portal_configuration_service_setup** | [**PortalConfigurationServiceSetup**](PortalConfigurationServiceSetup.md)| portalConfigurationServiceSetup | 

### Return type

[**PortalConfigurationServiceSetup**](PortalConfigurationServiceSetup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | PortalConfigurationServiceSetup |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

