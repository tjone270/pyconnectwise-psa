# connectwise_psa.ManagedDevicesIntegrationCrossReferencesApi

All URIs are relative to *https://aus-api.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_company_managed_devices_integrations_by_parent_id_cross_references_by_id**](ManagedDevicesIntegrationCrossReferencesApi.md#delete_company_managed_devices_integrations_by_parent_id_cross_references_by_id) | **DELETE** /company/managedDevicesIntegrations/{parentId}/crossReferences/{id} | Delete ManagedDevicesIntegrationCrossReference
[**get_company_managed_devices_integrations_by_parent_id_cross_references**](ManagedDevicesIntegrationCrossReferencesApi.md#get_company_managed_devices_integrations_by_parent_id_cross_references) | **GET** /company/managedDevicesIntegrations/{parentId}/crossReferences | Get List of ManagedDevicesIntegrationCrossReference
[**get_company_managed_devices_integrations_by_parent_id_cross_references_by_id**](ManagedDevicesIntegrationCrossReferencesApi.md#get_company_managed_devices_integrations_by_parent_id_cross_references_by_id) | **GET** /company/managedDevicesIntegrations/{parentId}/crossReferences/{id} | Get ManagedDevicesIntegrationCrossReference
[**get_company_managed_devices_integrations_by_parent_id_cross_references_count**](ManagedDevicesIntegrationCrossReferencesApi.md#get_company_managed_devices_integrations_by_parent_id_cross_references_count) | **GET** /company/managedDevicesIntegrations/{parentId}/crossReferences/count | Get Count of ManagedDevicesIntegrationCrossReference
[**patch_company_managed_devices_integrations_by_parent_id_cross_references_by_id**](ManagedDevicesIntegrationCrossReferencesApi.md#patch_company_managed_devices_integrations_by_parent_id_cross_references_by_id) | **PATCH** /company/managedDevicesIntegrations/{parentId}/crossReferences/{id} | Patch ManagedDevicesIntegrationCrossReference
[**post_company_managed_devices_integrations_by_parent_id_cross_references**](ManagedDevicesIntegrationCrossReferencesApi.md#post_company_managed_devices_integrations_by_parent_id_cross_references) | **POST** /company/managedDevicesIntegrations/{parentId}/crossReferences | Post ManagedDevicesIntegrationCrossReference
[**put_company_managed_devices_integrations_by_parent_id_cross_references_by_id**](ManagedDevicesIntegrationCrossReferencesApi.md#put_company_managed_devices_integrations_by_parent_id_cross_references_by_id) | **PUT** /company/managedDevicesIntegrations/{parentId}/crossReferences/{id} | Put ManagedDevicesIntegrationCrossReference


# **delete_company_managed_devices_integrations_by_parent_id_cross_references_by_id**
> ManagedDevicesIntegrationCrossReference delete_company_managed_devices_integrations_by_parent_id_cross_references_by_id(id, parent_id, client_id)

Delete ManagedDevicesIntegrationCrossReference

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.managed_devices_integration_cross_reference import ManagedDevicesIntegrationCrossReference
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
    api_instance = connectwise_psa.ManagedDevicesIntegrationCrossReferencesApi(api_client)
    id = 56 # int | crossReferenceId
    parent_id = 56 # int | managedDevicesIntegrationId
    client_id = 'client_id_example' # str | 

    try:
        # Delete ManagedDevicesIntegrationCrossReference
        api_response = api_instance.delete_company_managed_devices_integrations_by_parent_id_cross_references_by_id(id, parent_id, client_id)
        print("The response of ManagedDevicesIntegrationCrossReferencesApi->delete_company_managed_devices_integrations_by_parent_id_cross_references_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagedDevicesIntegrationCrossReferencesApi->delete_company_managed_devices_integrations_by_parent_id_cross_references_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| crossReferenceId | 
 **parent_id** | **int**| managedDevicesIntegrationId | 
 **client_id** | **str**|  | 

### Return type

[**ManagedDevicesIntegrationCrossReference**](ManagedDevicesIntegrationCrossReference.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ManagedDevicesIntegrationCrossReference |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_company_managed_devices_integrations_by_parent_id_cross_references**
> List[ManagedDevicesIntegrationCrossReference] get_company_managed_devices_integrations_by_parent_id_cross_references(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of ManagedDevicesIntegrationCrossReference

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.managed_devices_integration_cross_reference import ManagedDevicesIntegrationCrossReference
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
    api_instance = connectwise_psa.ManagedDevicesIntegrationCrossReferencesApi(api_client)
    parent_id = 56 # int | managedDevicesIntegrationId
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
        # Get List of ManagedDevicesIntegrationCrossReference
        api_response = api_instance.get_company_managed_devices_integrations_by_parent_id_cross_references(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of ManagedDevicesIntegrationCrossReferencesApi->get_company_managed_devices_integrations_by_parent_id_cross_references:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagedDevicesIntegrationCrossReferencesApi->get_company_managed_devices_integrations_by_parent_id_cross_references: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| managedDevicesIntegrationId | 
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

[**List[ManagedDevicesIntegrationCrossReference]**](ManagedDevicesIntegrationCrossReference.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of ManagedDevicesIntegrationCrossReference |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_company_managed_devices_integrations_by_parent_id_cross_references_by_id**
> ManagedDevicesIntegrationCrossReference get_company_managed_devices_integrations_by_parent_id_cross_references_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get ManagedDevicesIntegrationCrossReference

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.managed_devices_integration_cross_reference import ManagedDevicesIntegrationCrossReference
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
    api_instance = connectwise_psa.ManagedDevicesIntegrationCrossReferencesApi(api_client)
    id = 56 # int | crossReferenceId
    parent_id = 56 # int | managedDevicesIntegrationId
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
        # Get ManagedDevicesIntegrationCrossReference
        api_response = api_instance.get_company_managed_devices_integrations_by_parent_id_cross_references_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of ManagedDevicesIntegrationCrossReferencesApi->get_company_managed_devices_integrations_by_parent_id_cross_references_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagedDevicesIntegrationCrossReferencesApi->get_company_managed_devices_integrations_by_parent_id_cross_references_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| crossReferenceId | 
 **parent_id** | **int**| managedDevicesIntegrationId | 
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

[**ManagedDevicesIntegrationCrossReference**](ManagedDevicesIntegrationCrossReference.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ManagedDevicesIntegrationCrossReference |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_company_managed_devices_integrations_by_parent_id_cross_references_count**
> Count get_company_managed_devices_integrations_by_parent_id_cross_references_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Count of ManagedDevicesIntegrationCrossReference

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
    api_instance = connectwise_psa.ManagedDevicesIntegrationCrossReferencesApi(api_client)
    parent_id = 56 # int | managedDevicesIntegrationId
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
        # Get Count of ManagedDevicesIntegrationCrossReference
        api_response = api_instance.get_company_managed_devices_integrations_by_parent_id_cross_references_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of ManagedDevicesIntegrationCrossReferencesApi->get_company_managed_devices_integrations_by_parent_id_cross_references_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagedDevicesIntegrationCrossReferencesApi->get_company_managed_devices_integrations_by_parent_id_cross_references_count: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| managedDevicesIntegrationId | 
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

# **patch_company_managed_devices_integrations_by_parent_id_cross_references_by_id**
> ManagedDevicesIntegrationCrossReference patch_company_managed_devices_integrations_by_parent_id_cross_references_by_id(id, parent_id, client_id, patch_operation)

Patch ManagedDevicesIntegrationCrossReference

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.managed_devices_integration_cross_reference import ManagedDevicesIntegrationCrossReference
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
    api_instance = connectwise_psa.ManagedDevicesIntegrationCrossReferencesApi(api_client)
    id = 56 # int | crossReferenceId
    parent_id = 56 # int | managedDevicesIntegrationId
    client_id = 'client_id_example' # str | 
    patch_operation = [connectwise_psa.PatchOperation()] # List[PatchOperation] | List of PatchOperation

    try:
        # Patch ManagedDevicesIntegrationCrossReference
        api_response = api_instance.patch_company_managed_devices_integrations_by_parent_id_cross_references_by_id(id, parent_id, client_id, patch_operation)
        print("The response of ManagedDevicesIntegrationCrossReferencesApi->patch_company_managed_devices_integrations_by_parent_id_cross_references_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagedDevicesIntegrationCrossReferencesApi->patch_company_managed_devices_integrations_by_parent_id_cross_references_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| crossReferenceId | 
 **parent_id** | **int**| managedDevicesIntegrationId | 
 **client_id** | **str**|  | 
 **patch_operation** | [**List[PatchOperation]**](PatchOperation.md)| List of PatchOperation | 

### Return type

[**ManagedDevicesIntegrationCrossReference**](ManagedDevicesIntegrationCrossReference.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ManagedDevicesIntegrationCrossReference |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_company_managed_devices_integrations_by_parent_id_cross_references**
> ManagedDevicesIntegrationCrossReference post_company_managed_devices_integrations_by_parent_id_cross_references(parent_id, client_id, managed_devices_integration_cross_reference)

Post ManagedDevicesIntegrationCrossReference

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.managed_devices_integration_cross_reference import ManagedDevicesIntegrationCrossReference
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
    api_instance = connectwise_psa.ManagedDevicesIntegrationCrossReferencesApi(api_client)
    parent_id = 56 # int | managedDevicesIntegrationId
    client_id = 'client_id_example' # str | 
    managed_devices_integration_cross_reference = connectwise_psa.ManagedDevicesIntegrationCrossReference() # ManagedDevicesIntegrationCrossReference | crossReference

    try:
        # Post ManagedDevicesIntegrationCrossReference
        api_response = api_instance.post_company_managed_devices_integrations_by_parent_id_cross_references(parent_id, client_id, managed_devices_integration_cross_reference)
        print("The response of ManagedDevicesIntegrationCrossReferencesApi->post_company_managed_devices_integrations_by_parent_id_cross_references:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagedDevicesIntegrationCrossReferencesApi->post_company_managed_devices_integrations_by_parent_id_cross_references: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| managedDevicesIntegrationId | 
 **client_id** | **str**|  | 
 **managed_devices_integration_cross_reference** | [**ManagedDevicesIntegrationCrossReference**](ManagedDevicesIntegrationCrossReference.md)| crossReference | 

### Return type

[**ManagedDevicesIntegrationCrossReference**](ManagedDevicesIntegrationCrossReference.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ManagedDevicesIntegrationCrossReference |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_company_managed_devices_integrations_by_parent_id_cross_references_by_id**
> ManagedDevicesIntegrationCrossReference put_company_managed_devices_integrations_by_parent_id_cross_references_by_id(id, parent_id, client_id, managed_devices_integration_cross_reference)

Put ManagedDevicesIntegrationCrossReference

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.managed_devices_integration_cross_reference import ManagedDevicesIntegrationCrossReference
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
    api_instance = connectwise_psa.ManagedDevicesIntegrationCrossReferencesApi(api_client)
    id = 56 # int | crossReferenceId
    parent_id = 56 # int | managedDevicesIntegrationId
    client_id = 'client_id_example' # str | 
    managed_devices_integration_cross_reference = connectwise_psa.ManagedDevicesIntegrationCrossReference() # ManagedDevicesIntegrationCrossReference | crossReference

    try:
        # Put ManagedDevicesIntegrationCrossReference
        api_response = api_instance.put_company_managed_devices_integrations_by_parent_id_cross_references_by_id(id, parent_id, client_id, managed_devices_integration_cross_reference)
        print("The response of ManagedDevicesIntegrationCrossReferencesApi->put_company_managed_devices_integrations_by_parent_id_cross_references_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagedDevicesIntegrationCrossReferencesApi->put_company_managed_devices_integrations_by_parent_id_cross_references_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| crossReferenceId | 
 **parent_id** | **int**| managedDevicesIntegrationId | 
 **client_id** | **str**|  | 
 **managed_devices_integration_cross_reference** | [**ManagedDevicesIntegrationCrossReference**](ManagedDevicesIntegrationCrossReference.md)| crossReference | 

### Return type

[**ManagedDevicesIntegrationCrossReference**](ManagedDevicesIntegrationCrossReference.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ManagedDevicesIntegrationCrossReference |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

