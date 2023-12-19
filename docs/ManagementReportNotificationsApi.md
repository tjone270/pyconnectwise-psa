# connectwise_psa.ManagementReportNotificationsApi

All URIs are relative to *https://api-aus.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_company_companies_by_parent_id_management_report_notifications_by_id**](ManagementReportNotificationsApi.md#delete_company_companies_by_parent_id_management_report_notifications_by_id) | **DELETE** /company/companies/{parentId}/managementReportNotifications/{id} | Delete ManagementReportNotification
[**delete_company_management_by_parent_id_management_report_notifications_by_id**](ManagementReportNotificationsApi.md#delete_company_management_by_parent_id_management_report_notifications_by_id) | **DELETE** /company/management/{parentId}/managementReportNotifications/{id} | Delete ManagementReportNotification
[**get_company_companies_by_parent_id_management_report_notifications**](ManagementReportNotificationsApi.md#get_company_companies_by_parent_id_management_report_notifications) | **GET** /company/companies/{parentId}/managementReportNotifications | Get List of ManagementReportNotification
[**get_company_companies_by_parent_id_management_report_notifications_by_id**](ManagementReportNotificationsApi.md#get_company_companies_by_parent_id_management_report_notifications_by_id) | **GET** /company/companies/{parentId}/managementReportNotifications/{id} | Get ManagementReportNotification
[**get_company_companies_by_parent_id_management_report_notifications_count**](ManagementReportNotificationsApi.md#get_company_companies_by_parent_id_management_report_notifications_count) | **GET** /company/companies/{parentId}/managementReportNotifications/count | Get Count of ManagementReportNotification
[**get_company_management_by_parent_id_management_report_notifications**](ManagementReportNotificationsApi.md#get_company_management_by_parent_id_management_report_notifications) | **GET** /company/management/{parentId}/managementReportNotifications | Get List of ManagementReportNotification
[**get_company_management_by_parent_id_management_report_notifications_by_id**](ManagementReportNotificationsApi.md#get_company_management_by_parent_id_management_report_notifications_by_id) | **GET** /company/management/{parentId}/managementReportNotifications/{id} | Get ManagementReportNotification
[**get_company_management_by_parent_id_management_report_notifications_count**](ManagementReportNotificationsApi.md#get_company_management_by_parent_id_management_report_notifications_count) | **GET** /company/management/{parentId}/managementReportNotifications/count | Get Count of ManagementReportNotification
[**patch_company_companies_by_parent_id_management_report_notifications_by_id**](ManagementReportNotificationsApi.md#patch_company_companies_by_parent_id_management_report_notifications_by_id) | **PATCH** /company/companies/{parentId}/managementReportNotifications/{id} | Patch ManagementReportNotification
[**patch_company_management_by_parent_id_management_report_notifications_by_id**](ManagementReportNotificationsApi.md#patch_company_management_by_parent_id_management_report_notifications_by_id) | **PATCH** /company/management/{parentId}/managementReportNotifications/{id} | Patch ManagementReportNotification
[**post_company_companies_by_parent_id_management_report_notifications**](ManagementReportNotificationsApi.md#post_company_companies_by_parent_id_management_report_notifications) | **POST** /company/companies/{parentId}/managementReportNotifications | Post ManagementReportNotification
[**post_company_management_by_parent_id_management_report_notifications**](ManagementReportNotificationsApi.md#post_company_management_by_parent_id_management_report_notifications) | **POST** /company/management/{parentId}/managementReportNotifications | Post ManagementReportNotification
[**put_company_companies_by_parent_id_management_report_notifications_by_id**](ManagementReportNotificationsApi.md#put_company_companies_by_parent_id_management_report_notifications_by_id) | **PUT** /company/companies/{parentId}/managementReportNotifications/{id} | Put ManagementReportNotification
[**put_company_management_by_parent_id_management_report_notifications_by_id**](ManagementReportNotificationsApi.md#put_company_management_by_parent_id_management_report_notifications_by_id) | **PUT** /company/management/{parentId}/managementReportNotifications/{id} | Put ManagementReportNotification


# **delete_company_companies_by_parent_id_management_report_notifications_by_id**
> delete_company_companies_by_parent_id_management_report_notifications_by_id(id, parent_id, client_id)

Delete ManagementReportNotification

### Example

```python
import time
import os
import connectwise_psa
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
    api_instance = connectwise_psa.ManagementReportNotificationsApi(api_client)
    id = 56 # int | managementReportNotificationId
    parent_id = 56 # int | companyId
    client_id = 'client_id_example' # str | 

    try:
        # Delete ManagementReportNotification
        api_instance.delete_company_companies_by_parent_id_management_report_notifications_by_id(id, parent_id, client_id)
    except Exception as e:
        print("Exception when calling ManagementReportNotificationsApi->delete_company_companies_by_parent_id_management_report_notifications_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| managementReportNotificationId | 
 **parent_id** | **int**| companyId | 
 **client_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_company_management_by_parent_id_management_report_notifications_by_id**
> delete_company_management_by_parent_id_management_report_notifications_by_id(id, parent_id, client_id)

Delete ManagementReportNotification

### Example

```python
import time
import os
import connectwise_psa
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
    api_instance = connectwise_psa.ManagementReportNotificationsApi(api_client)
    id = 56 # int | managementReportNotificationId
    parent_id = 56 # int | managementId
    client_id = 'client_id_example' # str | 

    try:
        # Delete ManagementReportNotification
        api_instance.delete_company_management_by_parent_id_management_report_notifications_by_id(id, parent_id, client_id)
    except Exception as e:
        print("Exception when calling ManagementReportNotificationsApi->delete_company_management_by_parent_id_management_report_notifications_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| managementReportNotificationId | 
 **parent_id** | **int**| managementId | 
 **client_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_company_companies_by_parent_id_management_report_notifications**
> List[ManagementReportNotification] get_company_companies_by_parent_id_management_report_notifications(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of ManagementReportNotification

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.management_report_notification import ManagementReportNotification
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
    api_instance = connectwise_psa.ManagementReportNotificationsApi(api_client)
    parent_id = 56 # int | companyId
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
        # Get List of ManagementReportNotification
        api_response = api_instance.get_company_companies_by_parent_id_management_report_notifications(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of ManagementReportNotificationsApi->get_company_companies_by_parent_id_management_report_notifications:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagementReportNotificationsApi->get_company_companies_by_parent_id_management_report_notifications: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| companyId | 
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

[**List[ManagementReportNotification]**](ManagementReportNotification.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of ManagementReportNotification |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_company_companies_by_parent_id_management_report_notifications_by_id**
> ManagementReportNotification get_company_companies_by_parent_id_management_report_notifications_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get ManagementReportNotification

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.management_report_notification import ManagementReportNotification
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
    api_instance = connectwise_psa.ManagementReportNotificationsApi(api_client)
    id = 56 # int | managementReportNotificationId
    parent_id = 56 # int | companyId
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
        # Get ManagementReportNotification
        api_response = api_instance.get_company_companies_by_parent_id_management_report_notifications_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of ManagementReportNotificationsApi->get_company_companies_by_parent_id_management_report_notifications_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagementReportNotificationsApi->get_company_companies_by_parent_id_management_report_notifications_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| managementReportNotificationId | 
 **parent_id** | **int**| companyId | 
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

[**ManagementReportNotification**](ManagementReportNotification.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ManagementReportNotification |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_company_companies_by_parent_id_management_report_notifications_count**
> Count get_company_companies_by_parent_id_management_report_notifications_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Count of ManagementReportNotification

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
    api_instance = connectwise_psa.ManagementReportNotificationsApi(api_client)
    parent_id = 56 # int | companyId
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
        # Get Count of ManagementReportNotification
        api_response = api_instance.get_company_companies_by_parent_id_management_report_notifications_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of ManagementReportNotificationsApi->get_company_companies_by_parent_id_management_report_notifications_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagementReportNotificationsApi->get_company_companies_by_parent_id_management_report_notifications_count: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| companyId | 
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

# **get_company_management_by_parent_id_management_report_notifications**
> List[ManagementReportNotification] get_company_management_by_parent_id_management_report_notifications(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of ManagementReportNotification

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.management_report_notification import ManagementReportNotification
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
    api_instance = connectwise_psa.ManagementReportNotificationsApi(api_client)
    parent_id = 56 # int | managementId
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
        # Get List of ManagementReportNotification
        api_response = api_instance.get_company_management_by_parent_id_management_report_notifications(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of ManagementReportNotificationsApi->get_company_management_by_parent_id_management_report_notifications:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagementReportNotificationsApi->get_company_management_by_parent_id_management_report_notifications: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| managementId | 
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

[**List[ManagementReportNotification]**](ManagementReportNotification.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of ManagementReportNotification |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_company_management_by_parent_id_management_report_notifications_by_id**
> ManagementReportNotification get_company_management_by_parent_id_management_report_notifications_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get ManagementReportNotification

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.management_report_notification import ManagementReportNotification
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
    api_instance = connectwise_psa.ManagementReportNotificationsApi(api_client)
    id = 56 # int | managementReportNotificationId
    parent_id = 56 # int | managementId
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
        # Get ManagementReportNotification
        api_response = api_instance.get_company_management_by_parent_id_management_report_notifications_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of ManagementReportNotificationsApi->get_company_management_by_parent_id_management_report_notifications_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagementReportNotificationsApi->get_company_management_by_parent_id_management_report_notifications_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| managementReportNotificationId | 
 **parent_id** | **int**| managementId | 
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

[**ManagementReportNotification**](ManagementReportNotification.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ManagementReportNotification |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_company_management_by_parent_id_management_report_notifications_count**
> Count get_company_management_by_parent_id_management_report_notifications_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Count of ManagementReportNotification

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
    api_instance = connectwise_psa.ManagementReportNotificationsApi(api_client)
    parent_id = 56 # int | managementId
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
        # Get Count of ManagementReportNotification
        api_response = api_instance.get_company_management_by_parent_id_management_report_notifications_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of ManagementReportNotificationsApi->get_company_management_by_parent_id_management_report_notifications_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagementReportNotificationsApi->get_company_management_by_parent_id_management_report_notifications_count: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| managementId | 
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

# **patch_company_companies_by_parent_id_management_report_notifications_by_id**
> ManagementReportNotification patch_company_companies_by_parent_id_management_report_notifications_by_id(id, parent_id, client_id, patch_operation)

Patch ManagementReportNotification

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.management_report_notification import ManagementReportNotification
from connectwise_psa.models.patch_operation import PatchOperation
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
    api_instance = connectwise_psa.ManagementReportNotificationsApi(api_client)
    id = 56 # int | managementReportNotificationId
    parent_id = 56 # int | companyId
    client_id = 'client_id_example' # str | 
    patch_operation = [connectwise_psa.PatchOperation()] # List[PatchOperation] | List of PatchOperation

    try:
        # Patch ManagementReportNotification
        api_response = api_instance.patch_company_companies_by_parent_id_management_report_notifications_by_id(id, parent_id, client_id, patch_operation)
        print("The response of ManagementReportNotificationsApi->patch_company_companies_by_parent_id_management_report_notifications_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagementReportNotificationsApi->patch_company_companies_by_parent_id_management_report_notifications_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| managementReportNotificationId | 
 **parent_id** | **int**| companyId | 
 **client_id** | **str**|  | 
 **patch_operation** | [**List[PatchOperation]**](PatchOperation.md)| List of PatchOperation | 

### Return type

[**ManagementReportNotification**](ManagementReportNotification.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ManagementReportNotification |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_company_management_by_parent_id_management_report_notifications_by_id**
> ManagementReportNotification patch_company_management_by_parent_id_management_report_notifications_by_id(id, parent_id, client_id, patch_operation)

Patch ManagementReportNotification

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.management_report_notification import ManagementReportNotification
from connectwise_psa.models.patch_operation import PatchOperation
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
    api_instance = connectwise_psa.ManagementReportNotificationsApi(api_client)
    id = 56 # int | managementReportNotificationId
    parent_id = 56 # int | managementId
    client_id = 'client_id_example' # str | 
    patch_operation = [connectwise_psa.PatchOperation()] # List[PatchOperation] | List of PatchOperation

    try:
        # Patch ManagementReportNotification
        api_response = api_instance.patch_company_management_by_parent_id_management_report_notifications_by_id(id, parent_id, client_id, patch_operation)
        print("The response of ManagementReportNotificationsApi->patch_company_management_by_parent_id_management_report_notifications_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagementReportNotificationsApi->patch_company_management_by_parent_id_management_report_notifications_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| managementReportNotificationId | 
 **parent_id** | **int**| managementId | 
 **client_id** | **str**|  | 
 **patch_operation** | [**List[PatchOperation]**](PatchOperation.md)| List of PatchOperation | 

### Return type

[**ManagementReportNotification**](ManagementReportNotification.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ManagementReportNotification |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_company_companies_by_parent_id_management_report_notifications**
> ManagementReportNotification post_company_companies_by_parent_id_management_report_notifications(parent_id, client_id, management_report_notification)

Post ManagementReportNotification

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.management_report_notification import ManagementReportNotification
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
    api_instance = connectwise_psa.ManagementReportNotificationsApi(api_client)
    parent_id = 56 # int | companyId
    client_id = 'client_id_example' # str | 
    management_report_notification = connectwise_psa.ManagementReportNotification() # ManagementReportNotification | managementReportNotification

    try:
        # Post ManagementReportNotification
        api_response = api_instance.post_company_companies_by_parent_id_management_report_notifications(parent_id, client_id, management_report_notification)
        print("The response of ManagementReportNotificationsApi->post_company_companies_by_parent_id_management_report_notifications:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagementReportNotificationsApi->post_company_companies_by_parent_id_management_report_notifications: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| companyId | 
 **client_id** | **str**|  | 
 **management_report_notification** | [**ManagementReportNotification**](ManagementReportNotification.md)| managementReportNotification | 

### Return type

[**ManagementReportNotification**](ManagementReportNotification.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | ManagementReportNotification |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_company_management_by_parent_id_management_report_notifications**
> ManagementReportNotification post_company_management_by_parent_id_management_report_notifications(parent_id, client_id, management_report_notification)

Post ManagementReportNotification

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.management_report_notification import ManagementReportNotification
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
    api_instance = connectwise_psa.ManagementReportNotificationsApi(api_client)
    parent_id = 56 # int | managementId
    client_id = 'client_id_example' # str | 
    management_report_notification = connectwise_psa.ManagementReportNotification() # ManagementReportNotification | managementReportNotification

    try:
        # Post ManagementReportNotification
        api_response = api_instance.post_company_management_by_parent_id_management_report_notifications(parent_id, client_id, management_report_notification)
        print("The response of ManagementReportNotificationsApi->post_company_management_by_parent_id_management_report_notifications:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagementReportNotificationsApi->post_company_management_by_parent_id_management_report_notifications: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| managementId | 
 **client_id** | **str**|  | 
 **management_report_notification** | [**ManagementReportNotification**](ManagementReportNotification.md)| managementReportNotification | 

### Return type

[**ManagementReportNotification**](ManagementReportNotification.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | ManagementReportNotification |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_company_companies_by_parent_id_management_report_notifications_by_id**
> ManagementReportNotification put_company_companies_by_parent_id_management_report_notifications_by_id(id, parent_id, client_id, management_report_notification)

Put ManagementReportNotification

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.management_report_notification import ManagementReportNotification
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
    api_instance = connectwise_psa.ManagementReportNotificationsApi(api_client)
    id = 56 # int | managementReportNotificationId
    parent_id = 56 # int | companyId
    client_id = 'client_id_example' # str | 
    management_report_notification = connectwise_psa.ManagementReportNotification() # ManagementReportNotification | managementReportNotification

    try:
        # Put ManagementReportNotification
        api_response = api_instance.put_company_companies_by_parent_id_management_report_notifications_by_id(id, parent_id, client_id, management_report_notification)
        print("The response of ManagementReportNotificationsApi->put_company_companies_by_parent_id_management_report_notifications_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagementReportNotificationsApi->put_company_companies_by_parent_id_management_report_notifications_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| managementReportNotificationId | 
 **parent_id** | **int**| companyId | 
 **client_id** | **str**|  | 
 **management_report_notification** | [**ManagementReportNotification**](ManagementReportNotification.md)| managementReportNotification | 

### Return type

[**ManagementReportNotification**](ManagementReportNotification.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ManagementReportNotification |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_company_management_by_parent_id_management_report_notifications_by_id**
> ManagementReportNotification put_company_management_by_parent_id_management_report_notifications_by_id(id, parent_id, client_id, management_report_notification)

Put ManagementReportNotification

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.management_report_notification import ManagementReportNotification
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
    api_instance = connectwise_psa.ManagementReportNotificationsApi(api_client)
    id = 56 # int | managementReportNotificationId
    parent_id = 56 # int | managementId
    client_id = 'client_id_example' # str | 
    management_report_notification = connectwise_psa.ManagementReportNotification() # ManagementReportNotification | managementReportNotification

    try:
        # Put ManagementReportNotification
        api_response = api_instance.put_company_management_by_parent_id_management_report_notifications_by_id(id, parent_id, client_id, management_report_notification)
        print("The response of ManagementReportNotificationsApi->put_company_management_by_parent_id_management_report_notifications_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagementReportNotificationsApi->put_company_management_by_parent_id_management_report_notifications_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| managementReportNotificationId | 
 **parent_id** | **int**| managementId | 
 **client_id** | **str**|  | 
 **management_report_notification** | [**ManagementReportNotification**](ManagementReportNotification.md)| managementReportNotification | 

### Return type

[**ManagementReportNotification**](ManagementReportNotification.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ManagementReportNotification |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

