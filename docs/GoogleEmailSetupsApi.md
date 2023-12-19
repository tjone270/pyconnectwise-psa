# connectwise_psa.GoogleEmailSetupsApi

All URIs are relative to *https://api-aus.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_system_googleemailsetup_by_id**](GoogleEmailSetupsApi.md#delete_system_googleemailsetup_by_id) | **DELETE** /system/googleemailsetup/{id} | Delete GoogleEmailSetups
[**get_system_googleemailsetup**](GoogleEmailSetupsApi.md#get_system_googleemailsetup) | **GET** /system/googleemailsetup/ | Get List of GoogleEmailSetups
[**get_system_googleemailsetup_by_id**](GoogleEmailSetupsApi.md#get_system_googleemailsetup_by_id) | **GET** /system/googleemailsetup/{id} | Get GoogleEmailSetups
[**get_system_googleemailsetup_count**](GoogleEmailSetupsApi.md#get_system_googleemailsetup_count) | **GET** /system/googleemailsetup/count | Get Count of GoogleEmailSetups
[**patch_system_googleemailsetup_by_id**](GoogleEmailSetupsApi.md#patch_system_googleemailsetup_by_id) | **PATCH** /system/googleemailsetup/{id} | Patch GoogleEmailSetups
[**post_system_googleemailsetup**](GoogleEmailSetupsApi.md#post_system_googleemailsetup) | **POST** /system/googleemailsetup/ | Post GoogleEmailSetups
[**post_system_googleemailsetup_by_id_test_connection**](GoogleEmailSetupsApi.md#post_system_googleemailsetup_by_id_test_connection) | **POST** /system/googleemailsetup/{id}/testConnection | Post SuccessResponse
[**put_system_googleemailsetup_by_id**](GoogleEmailSetupsApi.md#put_system_googleemailsetup_by_id) | **PUT** /system/googleemailsetup/{id} | Put GoogleEmailSetups


# **delete_system_googleemailsetup_by_id**
> delete_system_googleemailsetup_by_id(id, client_id)

Delete GoogleEmailSetups

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
    api_instance = connectwise_psa.GoogleEmailSetupsApi(api_client)
    id = 56 # int | GoogleEmailSetupId
    client_id = 'client_id_example' # str | 

    try:
        # Delete GoogleEmailSetups
        api_instance.delete_system_googleemailsetup_by_id(id, client_id)
    except Exception as e:
        print("Exception when calling GoogleEmailSetupsApi->delete_system_googleemailsetup_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| GoogleEmailSetupId | 
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

# **get_system_googleemailsetup**
> List[GoogleEmailSetup] get_system_googleemailsetup(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of GoogleEmailSetups

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.google_email_setup import GoogleEmailSetup
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
    api_instance = connectwise_psa.GoogleEmailSetupsApi(api_client)
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
        # Get List of GoogleEmailSetups
        api_response = api_instance.get_system_googleemailsetup(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of GoogleEmailSetupsApi->get_system_googleemailsetup:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GoogleEmailSetupsApi->get_system_googleemailsetup: %s\n" % e)
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

[**List[GoogleEmailSetup]**](GoogleEmailSetup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of googleEmailSetupses |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_system_googleemailsetup_by_id**
> GoogleEmailSetup get_system_googleemailsetup_by_id(id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get GoogleEmailSetups

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.google_email_setup import GoogleEmailSetup
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
    api_instance = connectwise_psa.GoogleEmailSetupsApi(api_client)
    id = 56 # int | GoogleEmailSetupId
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
        # Get GoogleEmailSetups
        api_response = api_instance.get_system_googleemailsetup_by_id(id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of GoogleEmailSetupsApi->get_system_googleemailsetup_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GoogleEmailSetupsApi->get_system_googleemailsetup_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| GoogleEmailSetupId | 
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

[**GoogleEmailSetup**](GoogleEmailSetup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | GoogleEmailSetup |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_system_googleemailsetup_count**
> Count get_system_googleemailsetup_count(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Count of GoogleEmailSetups

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
    api_instance = connectwise_psa.GoogleEmailSetupsApi(api_client)
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
        # Get Count of GoogleEmailSetups
        api_response = api_instance.get_system_googleemailsetup_count(client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of GoogleEmailSetupsApi->get_system_googleemailsetup_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GoogleEmailSetupsApi->get_system_googleemailsetup_count: %s\n" % e)
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

# **patch_system_googleemailsetup_by_id**
> GoogleEmailSetup patch_system_googleemailsetup_by_id(id, client_id, patch_operation)

Patch GoogleEmailSetups

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.google_email_setup import GoogleEmailSetup
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
    api_instance = connectwise_psa.GoogleEmailSetupsApi(api_client)
    id = 56 # int | GoogleEmailSetupId
    client_id = 'client_id_example' # str | 
    patch_operation = [connectwise_psa.PatchOperation()] # List[PatchOperation] | List of PatchOperation

    try:
        # Patch GoogleEmailSetups
        api_response = api_instance.patch_system_googleemailsetup_by_id(id, client_id, patch_operation)
        print("The response of GoogleEmailSetupsApi->patch_system_googleemailsetup_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GoogleEmailSetupsApi->patch_system_googleemailsetup_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| GoogleEmailSetupId | 
 **client_id** | **str**|  | 
 **patch_operation** | [**List[PatchOperation]**](PatchOperation.md)| List of PatchOperation | 

### Return type

[**GoogleEmailSetup**](GoogleEmailSetup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | GoogleEmailSetup |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_system_googleemailsetup**
> GoogleEmailSetup post_system_googleemailsetup(client_id, google_email_setup)

Post GoogleEmailSetups

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.google_email_setup import GoogleEmailSetup
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
    api_instance = connectwise_psa.GoogleEmailSetupsApi(api_client)
    client_id = 'client_id_example' # str | 
    google_email_setup = connectwise_psa.GoogleEmailSetup() # GoogleEmailSetup | GoogleEmailSetup

    try:
        # Post GoogleEmailSetups
        api_response = api_instance.post_system_googleemailsetup(client_id, google_email_setup)
        print("The response of GoogleEmailSetupsApi->post_system_googleemailsetup:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GoogleEmailSetupsApi->post_system_googleemailsetup: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**|  | 
 **google_email_setup** | [**GoogleEmailSetup**](GoogleEmailSetup.md)| GoogleEmailSetup | 

### Return type

[**GoogleEmailSetup**](GoogleEmailSetup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | GoogleEmailSetup |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_system_googleemailsetup_by_id_test_connection**
> SuccessResponse post_system_googleemailsetup_by_id_test_connection(id, client_id)

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
    api_instance = connectwise_psa.GoogleEmailSetupsApi(api_client)
    id = 56 # int | emailSetupId
    client_id = 'client_id_example' # str | 

    try:
        # Post SuccessResponse
        api_response = api_instance.post_system_googleemailsetup_by_id_test_connection(id, client_id)
        print("The response of GoogleEmailSetupsApi->post_system_googleemailsetup_by_id_test_connection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GoogleEmailSetupsApi->post_system_googleemailsetup_by_id_test_connection: %s\n" % e)
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

# **put_system_googleemailsetup_by_id**
> GoogleEmailSetup put_system_googleemailsetup_by_id(id, client_id, google_email_setup)

Put GoogleEmailSetups

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.google_email_setup import GoogleEmailSetup
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
    api_instance = connectwise_psa.GoogleEmailSetupsApi(api_client)
    id = 56 # int | GoogleEmailSetupId
    client_id = 'client_id_example' # str | 
    google_email_setup = connectwise_psa.GoogleEmailSetup() # GoogleEmailSetup | companyTypeAssociation

    try:
        # Put GoogleEmailSetups
        api_response = api_instance.put_system_googleemailsetup_by_id(id, client_id, google_email_setup)
        print("The response of GoogleEmailSetupsApi->put_system_googleemailsetup_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GoogleEmailSetupsApi->put_system_googleemailsetup_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| GoogleEmailSetupId | 
 **client_id** | **str**|  | 
 **google_email_setup** | [**GoogleEmailSetup**](GoogleEmailSetup.md)| companyTypeAssociation | 

### Return type

[**GoogleEmailSetup**](GoogleEmailSetup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | GoogleEmailSetup |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

