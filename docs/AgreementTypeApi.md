# connectwise_psa.AgreementTypeApi

All URIs are relative to *https://aus-api.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**post_finance_agreements_by_id_copy**](AgreementTypeApi.md#post_finance_agreements_by_id_copy) | **POST** /finance/agreements/types{id}/copy | Post AgreementType


# **post_finance_agreements_by_id_copy**
> AgreementType post_finance_agreements_by_id_copy(id, client_id)

Post AgreementType

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.agreement_type import AgreementType
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
    api_instance = connectwise_psa.AgreementTypeApi(api_client)
    id = 56 # int | agreementTypeId
    client_id = 'client_id_example' # str | 

    try:
        # Post AgreementType
        api_response = api_instance.post_finance_agreements_by_id_copy(id, client_id)
        print("The response of AgreementTypeApi->post_finance_agreements_by_id_copy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgreementTypeApi->post_finance_agreements_by_id_copy: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| agreementTypeId | 
 **client_id** | **str**|  | 

### Return type

[**AgreementType**](AgreementType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | AgreementType |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

