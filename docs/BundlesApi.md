# connectwise_psa.BundlesApi

All URIs are relative to *https://api-aus.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**post_system_bundles**](BundlesApi.md#post_system_bundles) | **POST** /system/bundles | Post BundleResultsCollection
[**post_system_bundles_count**](BundlesApi.md#post_system_bundles_count) | **POST** /system/bundles/count | Post BundleResultsCollection


# **post_system_bundles**
> BundleResultsCollection post_system_bundles(client_id, bundle_requests_collection)

Post BundleResultsCollection

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.bundle_requests_collection import BundleRequestsCollection
from connectwise_psa.models.bundle_results_collection import BundleResultsCollection
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
    api_instance = connectwise_psa.BundlesApi(api_client)
    client_id = 'client_id_example' # str | 
    bundle_requests_collection = connectwise_psa.BundleRequestsCollection() # BundleRequestsCollection | requests

    try:
        # Post BundleResultsCollection
        api_response = api_instance.post_system_bundles(client_id, bundle_requests_collection)
        print("The response of BundlesApi->post_system_bundles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BundlesApi->post_system_bundles: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**|  | 
 **bundle_requests_collection** | [**BundleRequestsCollection**](BundleRequestsCollection.md)| requests | 

### Return type

[**BundleResultsCollection**](BundleResultsCollection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | BundleResultsCollection |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_system_bundles_count**
> BundleResultsCollection post_system_bundles_count(client_id, bundle_requests_collection)

Post BundleResultsCollection

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.bundle_requests_collection import BundleRequestsCollection
from connectwise_psa.models.bundle_results_collection import BundleResultsCollection
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
    api_instance = connectwise_psa.BundlesApi(api_client)
    client_id = 'client_id_example' # str | 
    bundle_requests_collection = connectwise_psa.BundleRequestsCollection() # BundleRequestsCollection | requests

    try:
        # Post BundleResultsCollection
        api_response = api_instance.post_system_bundles_count(client_id, bundle_requests_collection)
        print("The response of BundlesApi->post_system_bundles_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BundlesApi->post_system_bundles_count: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**|  | 
 **bundle_requests_collection** | [**BundleRequestsCollection**](BundleRequestsCollection.md)| requests | 

### Return type

[**BundleResultsCollection**](BundleResultsCollection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | BundleResultsCollection |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

