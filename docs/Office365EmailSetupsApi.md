# connectwise_psa.Office365EmailSetupsApi

All URIs are relative to *https://api-aus.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_system_office365_email_setups_by_id**](Office365EmailSetupsApi.md#delete_system_office365_email_setups_by_id) | **DELETE** /system/office365/emailSetups/{id} | Delete Office365EmailSetup
[**get_system_office365_email_setups**](Office365EmailSetupsApi.md#get_system_office365_email_setups) | **GET** /system/office365/emailSetups | Get List of Office365EmailSetup
[**get_system_office365_email_setups_by_id**](Office365EmailSetupsApi.md#get_system_office365_email_setups_by_id) | **GET** /system/office365/emailSetups/{id} | Get Office365EmailSetup
[**get_system_office365_email_setups_by_id_get_emails**](Office365EmailSetupsApi.md#get_system_office365_email_setups_by_id_get_emails) | **GET** /system/office365/emailSetups/{id}/getEmails/ | Get List of UserEmails from inbound ticket service
[**get_system_office365_email_setups_count**](Office365EmailSetupsApi.md#get_system_office365_email_setups_count) | **GET** /system/office365/emailSetups/count | Get Count of Office365EmailSetup
[**patch_system_office365_email_setups_by_id**](Office365EmailSetupsApi.md#patch_system_office365_email_setups_by_id) | **PATCH** /system/office365/emailSetups/{id} | Patch Office365EmailSetup
[**post_system_office365_email_setups**](Office365EmailSetupsApi.md#post_system_office365_email_setups) | **POST** /system/office365/emailSetups | Post Office365EmailSetup
[**post_system_office365_email_setups_by_id_authorize**](Office365EmailSetupsApi.md#post_system_office365_email_setups_by_id_authorize) | **POST** /system/office365/emailSetups/{id}/authorize | Post SuccessResponse
[**post_system_office365_email_setups_by_id_test_connection**](Office365EmailSetupsApi.md#post_system_office365_email_setups_by_id_test_connection) | **POST** /system/office365/emailSetups/{id}/testConnection | Post SuccessResponse
[**put_system_office365_email_setups_by_id**](Office365EmailSetupsApi.md#put_system_office365_email_setups_by_id) | **PUT** /system/office365/emailSetups/{id} | Put Office365EmailSetup


# **delete_system_office365_email_setups_by_id**
> delete_system_office365_email_setups_by_id(id, client_id)

Delete Office365EmailSetup

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
    api_instance = connectwise_psa.Office365EmailSetupsApi(api_client)
    id = 56 # int | emailSetupId
    client_id = 'client_id_example' # str | 

    try:
        # Delete Office365EmailSetup
        api_instance.delete_system_office365_email_setups_by_id(id, client_id)
    except Exception as e:
        print("Exception when calling Office365EmailSetupsApi->delete_system_office365_email_setups_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| emailSetupId | 
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

# **get_system_office365_email_setups**
> List[Office365EmailSetup] get_system_office365_email_setups(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of Office365EmailSetup

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.office365_email_setup import Office365EmailSetup
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
    api_instance = connectwise_psa.Office365EmailSetupsApi(api_client)
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
        # Get List of Office365EmailSetup
        api_response = api_instance.get_system_office365_email_setups(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of Office365EmailSetupsApi->get_system_office365_email_setups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Office365EmailSetupsApi->get_system_office365_email_setups: %s\n" % e)
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

[**List[Office365EmailSetup]**](Office365EmailSetup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of Office365EmailSetup |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_system_office365_email_setups_by_id**
> Office365EmailSetup get_system_office365_email_setups_by_id(id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Office365EmailSetup

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.office365_email_setup import Office365EmailSetup
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
    api_instance = connectwise_psa.Office365EmailSetupsApi(api_client)
    id = 56 # int | emailSetupId
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
        # Get Office365EmailSetup
        api_response = api_instance.get_system_office365_email_setups_by_id(id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of Office365EmailSetupsApi->get_system_office365_email_setups_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Office365EmailSetupsApi->get_system_office365_email_setups_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| emailSetupId | 
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

[**Office365EmailSetup**](Office365EmailSetup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Office365EmailSetup |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_system_office365_email_setups_by_id_get_emails**
> List[UserEmail] get_system_office365_email_setups_by_id_get_emails(id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of UserEmails from inbound ticket service

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.user_email import UserEmail
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
    api_instance = connectwise_psa.Office365EmailSetupsApi(api_client)
    id = 56 # int | emailSetupId
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
        # Get List of UserEmails from inbound ticket service
        api_response = api_instance.get_system_office365_email_setups_by_id_get_emails(id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of Office365EmailSetupsApi->get_system_office365_email_setups_by_id_get_emails:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Office365EmailSetupsApi->get_system_office365_email_setups_by_id_get_emails: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| emailSetupId | 
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

[**List[UserEmail]**](UserEmail.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of UserEmail |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_system_office365_email_setups_count**
> Count get_system_office365_email_setups_count(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Count of Office365EmailSetup

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
    api_instance = connectwise_psa.Office365EmailSetupsApi(api_client)
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
        # Get Count of Office365EmailSetup
        api_response = api_instance.get_system_office365_email_setups_count(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of Office365EmailSetupsApi->get_system_office365_email_setups_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Office365EmailSetupsApi->get_system_office365_email_setups_count: %s\n" % e)
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

# **patch_system_office365_email_setups_by_id**
> Office365EmailSetup patch_system_office365_email_setups_by_id(id, client_id, patch_operation)

Patch Office365EmailSetup

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.office365_email_setup import Office365EmailSetup
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
    api_instance = connectwise_psa.Office365EmailSetupsApi(api_client)
    id = 56 # int | emailSetupId
    client_id = 'client_id_example' # str | 
    patch_operation = [connectwise_psa.PatchOperation()] # List[PatchOperation] | List of PatchOperation

    try:
        # Patch Office365EmailSetup
        api_response = api_instance.patch_system_office365_email_setups_by_id(id, client_id, patch_operation)
        print("The response of Office365EmailSetupsApi->patch_system_office365_email_setups_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Office365EmailSetupsApi->patch_system_office365_email_setups_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| emailSetupId | 
 **client_id** | **str**|  | 
 **patch_operation** | [**List[PatchOperation]**](PatchOperation.md)| List of PatchOperation | 

### Return type

[**Office365EmailSetup**](Office365EmailSetup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Office365EmailSetup |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_system_office365_email_setups**
> Office365EmailSetup post_system_office365_email_setups(client_id, office365_email_setup)

Post Office365EmailSetup

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.office365_email_setup import Office365EmailSetup
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
    api_instance = connectwise_psa.Office365EmailSetupsApi(api_client)
    client_id = 'client_id_example' # str | 
    office365_email_setup = connectwise_psa.Office365EmailSetup() # Office365EmailSetup | entity

    try:
        # Post Office365EmailSetup
        api_response = api_instance.post_system_office365_email_setups(client_id, office365_email_setup)
        print("The response of Office365EmailSetupsApi->post_system_office365_email_setups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Office365EmailSetupsApi->post_system_office365_email_setups: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**|  | 
 **office365_email_setup** | [**Office365EmailSetup**](Office365EmailSetup.md)| entity | 

### Return type

[**Office365EmailSetup**](Office365EmailSetup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Office365EmailSetup |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_system_office365_email_setups_by_id_authorize**
> SuccessResponse post_system_office365_email_setups_by_id_authorize(id, client_id)

Post SuccessResponse

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.success_response import SuccessResponse
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
    api_instance = connectwise_psa.Office365EmailSetupsApi(api_client)
    id = 56 # int | emailSetupId
    client_id = 'client_id_example' # str | 

    try:
        # Post SuccessResponse
        api_response = api_instance.post_system_office365_email_setups_by_id_authorize(id, client_id)
        print("The response of Office365EmailSetupsApi->post_system_office365_email_setups_by_id_authorize:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Office365EmailSetupsApi->post_system_office365_email_setups_by_id_authorize: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| emailSetupId | 
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

# **post_system_office365_email_setups_by_id_test_connection**
> SuccessResponse post_system_office365_email_setups_by_id_test_connection(id, client_id)

Post SuccessResponse

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.success_response import SuccessResponse
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
    api_instance = connectwise_psa.Office365EmailSetupsApi(api_client)
    id = 56 # int | emailSetupId
    client_id = 'client_id_example' # str | 

    try:
        # Post SuccessResponse
        api_response = api_instance.post_system_office365_email_setups_by_id_test_connection(id, client_id)
        print("The response of Office365EmailSetupsApi->post_system_office365_email_setups_by_id_test_connection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Office365EmailSetupsApi->post_system_office365_email_setups_by_id_test_connection: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| emailSetupId | 
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

# **put_system_office365_email_setups_by_id**
> Office365EmailSetup put_system_office365_email_setups_by_id(id, client_id, office365_email_setup)

Put Office365EmailSetup

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.office365_email_setup import Office365EmailSetup
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
    api_instance = connectwise_psa.Office365EmailSetupsApi(api_client)
    id = 56 # int | emailSetupId
    client_id = 'client_id_example' # str | 
    office365_email_setup = connectwise_psa.Office365EmailSetup() # Office365EmailSetup | entity

    try:
        # Put Office365EmailSetup
        api_response = api_instance.put_system_office365_email_setups_by_id(id, client_id, office365_email_setup)
        print("The response of Office365EmailSetupsApi->put_system_office365_email_setups_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Office365EmailSetupsApi->put_system_office365_email_setups_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| emailSetupId | 
 **client_id** | **str**|  | 
 **office365_email_setup** | [**Office365EmailSetup**](Office365EmailSetup.md)| entity | 

### Return type

[**Office365EmailSetup**](Office365EmailSetup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Office365EmailSetup |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

