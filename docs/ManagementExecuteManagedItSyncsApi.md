# connectwise_psa.ManagementExecuteManagedItSyncsApi

All URIs are relative to *https://aus-api.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**post_company_management_by_id_execute_managed_it_sync**](ManagementExecuteManagedItSyncsApi.md#post_company_management_by_id_execute_managed_it_sync) | **POST** /company/management/{id}/executeManagedItSync | Post SuccessResponse


# **post_company_management_by_id_execute_managed_it_sync**
> SuccessResponse post_company_management_by_id_execute_managed_it_sync(id, client_id)

Post SuccessResponse

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.success_response import SuccessResponse
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
    api_instance = connectwise_psa.ManagementExecuteManagedItSyncsApi(api_client)
    id = 56 # int | managementId
    client_id = 'client_id_example' # str | 

    try:
        # Post SuccessResponse
        api_response = api_instance.post_company_management_by_id_execute_managed_it_sync(id, client_id)
        print("The response of ManagementExecuteManagedItSyncsApi->post_company_management_by_id_execute_managed_it_sync:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagementExecuteManagedItSyncsApi->post_company_management_by_id_execute_managed_it_sync: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| managementId | 
 **client_id** | **str**|  | 

### Return type

[**SuccessResponse**](SuccessResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | SuccessResponse |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

