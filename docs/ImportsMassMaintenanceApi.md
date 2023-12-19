# connectwise_psa.ImportsMassMaintenanceApi

All URIs are relative to *https://api-aus.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**post_system_import_mass_maintenance_by_id**](ImportsMassMaintenanceApi.md#post_system_import_mass_maintenance_by_id) | **POST** /system/importMassMaintenance/{id} | Post ImportMassMaintenance


# **post_system_import_mass_maintenance_by_id**
> ImportMassMaintenance post_system_import_mass_maintenance_by_id(id, client_id)

Post ImportMassMaintenance

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.import_mass_maintenance import ImportMassMaintenance
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
    api_instance = connectwise_psa.ImportsMassMaintenanceApi(api_client)
    id = 56 # int | importMassMaintenanceId
    client_id = 'client_id_example' # str | 

    try:
        # Post ImportMassMaintenance
        api_response = api_instance.post_system_import_mass_maintenance_by_id(id, client_id)
        print("The response of ImportsMassMaintenanceApi->post_system_import_mass_maintenance_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImportsMassMaintenanceApi->post_system_import_mass_maintenance_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| importMassMaintenanceId | 
 **client_id** | **str**|  | 

### Return type

[**ImportMassMaintenance**](ImportMassMaintenance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ImportMassMaintenance |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

