# connectwise_psa.MarketplaceImportsApi

All URIs are relative to *https://api-aus.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_system_marketplaceimport_getdefinition_by_id**](MarketplaceImportsApi.md#get_system_marketplaceimport_getdefinition_by_id) | **GET** /system/marketplaceimport/getdefinition/{id} | Get MarketplaceImport
[**post_system_marketplaceimport_import**](MarketplaceImportsApi.md#post_system_marketplaceimport_import) | **POST** /system/marketplaceimport/import | Post MarketplaceImport


# **get_system_marketplaceimport_getdefinition_by_id**
> MarketplaceImport get_system_marketplaceimport_getdefinition_by_id(id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get MarketplaceImport

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.marketplace_import import MarketplaceImport
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
    api_instance = connectwise_psa.MarketplaceImportsApi(api_client)
    id = 56 # int | getdefinitionId
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
        # Get MarketplaceImport
        api_response = api_instance.get_system_marketplaceimport_getdefinition_by_id(id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of MarketplaceImportsApi->get_system_marketplaceimport_getdefinition_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketplaceImportsApi->get_system_marketplaceimport_getdefinition_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| getdefinitionId | 
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

[**MarketplaceImport**](MarketplaceImport.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | MarketplaceImport |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_system_marketplaceimport_import**
> MarketplaceImport post_system_marketplaceimport_import(client_id, marketplace_import)

Post MarketplaceImport

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.marketplace_import import MarketplaceImport
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
    api_instance = connectwise_psa.MarketplaceImportsApi(api_client)
    client_id = 'client_id_example' # str | 
    marketplace_import = connectwise_psa.MarketplaceImport() # MarketplaceImport | marketplaceImport

    try:
        # Post MarketplaceImport
        api_response = api_instance.post_system_marketplaceimport_import(client_id, marketplace_import)
        print("The response of MarketplaceImportsApi->post_system_marketplaceimport_import:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketplaceImportsApi->post_system_marketplaceimport_import: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**|  | 
 **marketplace_import** | [**MarketplaceImport**](MarketplaceImport.md)| marketplaceImport | 

### Return type

[**MarketplaceImport**](MarketplaceImport.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | MarketplaceImport |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

