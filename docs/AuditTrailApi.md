# connectwise_psa.AuditTrailApi

All URIs are relative to *https://api-aus.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_system_audittrail**](AuditTrailApi.md#get_system_audittrail) | **GET** /system/audittrail | Get List of AuditTrailEntry
[**get_system_audittrail_count**](AuditTrailApi.md#get_system_audittrail_count) | **GET** /system/audittrail/count | Get Count of AuditTrailEntry


# **get_system_audittrail**
> List[AuditTrailEntry] get_system_audittrail(client_id, type=type, id=id, device_identifier=device_identifier, xref_rec_id=xref_rec_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of AuditTrailEntry

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.audit_trail_entry import AuditTrailEntry
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
    api_instance = connectwise_psa.AuditTrailApi(api_client)
    client_id = 'client_id_example' # str | 
    type = 'type_example' # str | type (optional)
    id = 56 # int | id (optional)
    device_identifier = 'device_identifier_example' # str | deviceIdentifier (optional)
    xref_rec_id = 56 # int | xrefRecId (optional)
    conditions = 'conditions_example' # str |  (optional)
    child_conditions = 'child_conditions_example' # str |  (optional)
    custom_field_conditions = 'custom_field_conditions_example' # str |  (optional)
    order_by = 'order_by_example' # str |  (optional)
    fields = 'fields_example' # str |  (optional)
    page = 56 # int |  (optional)
    page_size = 56 # int |  (optional)
    page_id = 56 # int |  (optional)

    try:
        # Get List of AuditTrailEntry
        api_response = api_instance.get_system_audittrail(client_id, type=type, id=id, device_identifier=device_identifier, xref_rec_id=xref_rec_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of AuditTrailApi->get_system_audittrail:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuditTrailApi->get_system_audittrail: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**|  | 
 **type** | **str**| type | [optional] 
 **id** | **int**| id | [optional] 
 **device_identifier** | **str**| deviceIdentifier | [optional] 
 **xref_rec_id** | **int**| xrefRecId | [optional] 
 **conditions** | **str**|  | [optional] 
 **child_conditions** | **str**|  | [optional] 
 **custom_field_conditions** | **str**|  | [optional] 
 **order_by** | **str**|  | [optional] 
 **fields** | **str**|  | [optional] 
 **page** | **int**|  | [optional] 
 **page_size** | **int**|  | [optional] 
 **page_id** | **int**|  | [optional] 

### Return type

[**List[AuditTrailEntry]**](AuditTrailEntry.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of AuditTrailEntry |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_system_audittrail_count**
> Count get_system_audittrail_count(client_id, type=type, id=id, device_identifier=device_identifier, xref_rec_id=xref_rec_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Count of AuditTrailEntry

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.count import Count
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
    api_instance = connectwise_psa.AuditTrailApi(api_client)
    client_id = 'client_id_example' # str | 
    type = 'type_example' # str | type (optional)
    id = 56 # int | id (optional)
    device_identifier = 'device_identifier_example' # str | deviceIdentifier (optional)
    xref_rec_id = 56 # int | xrefRecId (optional)
    conditions = 'conditions_example' # str |  (optional)
    child_conditions = 'child_conditions_example' # str |  (optional)
    custom_field_conditions = 'custom_field_conditions_example' # str |  (optional)
    order_by = 'order_by_example' # str |  (optional)
    fields = 'fields_example' # str |  (optional)
    page = 56 # int |  (optional)
    page_size = 56 # int |  (optional)
    page_id = 56 # int |  (optional)

    try:
        # Get Count of AuditTrailEntry
        api_response = api_instance.get_system_audittrail_count(client_id, type=type, id=id, device_identifier=device_identifier, xref_rec_id=xref_rec_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of AuditTrailApi->get_system_audittrail_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuditTrailApi->get_system_audittrail_count: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**|  | 
 **type** | **str**| type | [optional] 
 **id** | **int**| id | [optional] 
 **device_identifier** | **str**| deviceIdentifier | [optional] 
 **xref_rec_id** | **int**| xrefRecId | [optional] 
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

