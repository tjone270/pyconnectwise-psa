# connectwise_psa.MyCompanyDocumentSetupApi

All URIs are relative to *https://aus-api.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_system_mycompany_documents**](MyCompanyDocumentSetupApi.md#get_system_mycompany_documents) | **GET** /system/mycompany/documents | Get List of DocumentSetup
[**get_system_mycompany_documents_by_id**](MyCompanyDocumentSetupApi.md#get_system_mycompany_documents_by_id) | **GET** /system/mycompany/documents/{id} | Get DocumentSetup
[**patch_system_mycompany_documents_by_id**](MyCompanyDocumentSetupApi.md#patch_system_mycompany_documents_by_id) | **PATCH** /system/mycompany/documents/{id} | Patch DocumentSetup
[**put_system_mycompany_documents_by_id**](MyCompanyDocumentSetupApi.md#put_system_mycompany_documents_by_id) | **PUT** /system/mycompany/documents/{id} | Put DocumentSetup


# **get_system_mycompany_documents**
> List[DocumentSetup] get_system_mycompany_documents(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of DocumentSetup

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.document_setup import DocumentSetup
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
    api_instance = connectwise_psa.MyCompanyDocumentSetupApi(api_client)
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
        # Get List of DocumentSetup
        api_response = api_instance.get_system_mycompany_documents(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of MyCompanyDocumentSetupApi->get_system_mycompany_documents:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MyCompanyDocumentSetupApi->get_system_mycompany_documents: %s\n" % e)
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

[**List[DocumentSetup]**](DocumentSetup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of DocumentSetup |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_system_mycompany_documents_by_id**
> DocumentSetup get_system_mycompany_documents_by_id(id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get DocumentSetup

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.document_setup import DocumentSetup
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
    api_instance = connectwise_psa.MyCompanyDocumentSetupApi(api_client)
    id = 56 # int | documentId
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
        # Get DocumentSetup
        api_response = api_instance.get_system_mycompany_documents_by_id(id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of MyCompanyDocumentSetupApi->get_system_mycompany_documents_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MyCompanyDocumentSetupApi->get_system_mycompany_documents_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| documentId | 
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

[**DocumentSetup**](DocumentSetup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | DocumentSetup |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_system_mycompany_documents_by_id**
> DocumentSetup patch_system_mycompany_documents_by_id(id, client_id, patch_operation)

Patch DocumentSetup

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.document_setup import DocumentSetup
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
    api_instance = connectwise_psa.MyCompanyDocumentSetupApi(api_client)
    id = 56 # int | documentId
    client_id = 'client_id_example' # str | 
    patch_operation = [connectwise_psa.PatchOperation()] # List[PatchOperation] | List of PatchOperation

    try:
        # Patch DocumentSetup
        api_response = api_instance.patch_system_mycompany_documents_by_id(id, client_id, patch_operation)
        print("The response of MyCompanyDocumentSetupApi->patch_system_mycompany_documents_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MyCompanyDocumentSetupApi->patch_system_mycompany_documents_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| documentId | 
 **client_id** | **str**|  | 
 **patch_operation** | [**List[PatchOperation]**](PatchOperation.md)| List of PatchOperation | 

### Return type

[**DocumentSetup**](DocumentSetup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | DocumentSetup |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_system_mycompany_documents_by_id**
> DocumentSetup put_system_mycompany_documents_by_id(id, client_id, document_setup)

Put DocumentSetup

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.document_setup import DocumentSetup
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
    api_instance = connectwise_psa.MyCompanyDocumentSetupApi(api_client)
    id = 56 # int | documentId
    client_id = 'client_id_example' # str | 
    document_setup = connectwise_psa.DocumentSetup() # DocumentSetup | document

    try:
        # Put DocumentSetup
        api_response = api_instance.put_system_mycompany_documents_by_id(id, client_id, document_setup)
        print("The response of MyCompanyDocumentSetupApi->put_system_mycompany_documents_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MyCompanyDocumentSetupApi->put_system_mycompany_documents_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| documentId | 
 **client_id** | **str**|  | 
 **document_setup** | [**DocumentSetup**](DocumentSetup.md)| document | 

### Return type

[**DocumentSetup**](DocumentSetup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | DocumentSetup |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

