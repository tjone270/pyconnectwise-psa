# connectwise_psa.PurchasingDemandsApi

All URIs are relative to *https://aus-api.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**post_procurement_purchasing_demands**](PurchasingDemandsApi.md#post_procurement_purchasing_demands) | **POST** /procurement/purchasingDemands | Post PurchasingDemand


# **post_procurement_purchasing_demands**
> PurchasingDemand post_procurement_purchasing_demands(client_id, purchasing_demand)

Post PurchasingDemand

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.purchasing_demand import PurchasingDemand
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
    api_instance = connectwise_psa.PurchasingDemandsApi(api_client)
    client_id = 'client_id_example' # str | 
    purchasing_demand = connectwise_psa.PurchasingDemand() # PurchasingDemand | purchasingDemand

    try:
        # Post PurchasingDemand
        api_response = api_instance.post_procurement_purchasing_demands(client_id, purchasing_demand)
        print("The response of PurchasingDemandsApi->post_procurement_purchasing_demands:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PurchasingDemandsApi->post_procurement_purchasing_demands: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**|  | 
 **purchasing_demand** | [**PurchasingDemand**](PurchasingDemand.md)| purchasingDemand | 

### Return type

[**PurchasingDemand**](PurchasingDemand.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | PurchasingDemand |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

