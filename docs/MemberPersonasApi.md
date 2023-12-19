# connectwise_psa.MemberPersonasApi

All URIs are relative to *https://api-aus.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_system_members_by_parent_id_personas_by_id**](MemberPersonasApi.md#delete_system_members_by_parent_id_personas_by_id) | **DELETE** /system/members/{parentId}/personas/{id} | Delete MemberPersona
[**get_system_members_by_parent_id_personas**](MemberPersonasApi.md#get_system_members_by_parent_id_personas) | **GET** /system/members/{parentId}/personas | Get List of MemberPersona
[**get_system_members_by_parent_id_personas_by_id**](MemberPersonasApi.md#get_system_members_by_parent_id_personas_by_id) | **GET** /system/members/{parentId}/personas/{id} | Get MemberPersona
[**get_system_members_by_parent_id_personas_count**](MemberPersonasApi.md#get_system_members_by_parent_id_personas_count) | **GET** /system/members/{parentId}/personas/count | Get Count of MemberPersona
[**patch_system_members_by_parent_id_personas_by_id**](MemberPersonasApi.md#patch_system_members_by_parent_id_personas_by_id) | **PATCH** /system/members/{parentId}/personas/{id} | Patch MemberPersona
[**post_system_members_by_parent_id_personas**](MemberPersonasApi.md#post_system_members_by_parent_id_personas) | **POST** /system/members/{parentId}/personas | Post MemberPersona
[**put_system_members_by_parent_id_personas_by_id**](MemberPersonasApi.md#put_system_members_by_parent_id_personas_by_id) | **PUT** /system/members/{parentId}/personas/{id} | Put MemberPersona


# **delete_system_members_by_parent_id_personas_by_id**
> delete_system_members_by_parent_id_personas_by_id(id, parent_id, client_id)

Delete MemberPersona

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
    api_instance = connectwise_psa.MemberPersonasApi(api_client)
    id = 56 # int | personaId
    parent_id = 56 # int | memberId
    client_id = 'client_id_example' # str | 

    try:
        # Delete MemberPersona
        api_instance.delete_system_members_by_parent_id_personas_by_id(id, parent_id, client_id)
    except Exception as e:
        print("Exception when calling MemberPersonasApi->delete_system_members_by_parent_id_personas_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| personaId | 
 **parent_id** | **int**| memberId | 
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

# **get_system_members_by_parent_id_personas**
> List[MemberPersona] get_system_members_by_parent_id_personas(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of MemberPersona

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.member_persona import MemberPersona
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
    api_instance = connectwise_psa.MemberPersonasApi(api_client)
    parent_id = 56 # int | memberId
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
        # Get List of MemberPersona
        api_response = api_instance.get_system_members_by_parent_id_personas(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of MemberPersonasApi->get_system_members_by_parent_id_personas:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MemberPersonasApi->get_system_members_by_parent_id_personas: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| memberId | 
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

[**List[MemberPersona]**](MemberPersona.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of MemberPersona |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_system_members_by_parent_id_personas_by_id**
> MemberPersona get_system_members_by_parent_id_personas_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get MemberPersona

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.member_persona import MemberPersona
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
    api_instance = connectwise_psa.MemberPersonasApi(api_client)
    id = 56 # int | personaId
    parent_id = 56 # int | memberId
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
        # Get MemberPersona
        api_response = api_instance.get_system_members_by_parent_id_personas_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of MemberPersonasApi->get_system_members_by_parent_id_personas_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MemberPersonasApi->get_system_members_by_parent_id_personas_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| personaId | 
 **parent_id** | **int**| memberId | 
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

[**MemberPersona**](MemberPersona.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | MemberPersona |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_system_members_by_parent_id_personas_count**
> Count get_system_members_by_parent_id_personas_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Count of MemberPersona

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
    api_instance = connectwise_psa.MemberPersonasApi(api_client)
    parent_id = 56 # int | memberId
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
        # Get Count of MemberPersona
        api_response = api_instance.get_system_members_by_parent_id_personas_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of MemberPersonasApi->get_system_members_by_parent_id_personas_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MemberPersonasApi->get_system_members_by_parent_id_personas_count: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| memberId | 
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

# **patch_system_members_by_parent_id_personas_by_id**
> MemberPersona patch_system_members_by_parent_id_personas_by_id(id, parent_id, client_id, patch_operation)

Patch MemberPersona

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.member_persona import MemberPersona
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
    api_instance = connectwise_psa.MemberPersonasApi(api_client)
    id = 56 # int | personaId
    parent_id = 56 # int | memberId
    client_id = 'client_id_example' # str | 
    patch_operation = [connectwise_psa.PatchOperation()] # List[PatchOperation] | List of PatchOperation

    try:
        # Patch MemberPersona
        api_response = api_instance.patch_system_members_by_parent_id_personas_by_id(id, parent_id, client_id, patch_operation)
        print("The response of MemberPersonasApi->patch_system_members_by_parent_id_personas_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MemberPersonasApi->patch_system_members_by_parent_id_personas_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| personaId | 
 **parent_id** | **int**| memberId | 
 **client_id** | **str**|  | 
 **patch_operation** | [**List[PatchOperation]**](PatchOperation.md)| List of PatchOperation | 

### Return type

[**MemberPersona**](MemberPersona.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | MemberPersona |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_system_members_by_parent_id_personas**
> MemberPersona post_system_members_by_parent_id_personas(parent_id, client_id, member_persona)

Post MemberPersona

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.member_persona import MemberPersona
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
    api_instance = connectwise_psa.MemberPersonasApi(api_client)
    parent_id = 56 # int | memberId
    client_id = 'client_id_example' # str | 
    member_persona = connectwise_psa.MemberPersona() # MemberPersona | memberPersona

    try:
        # Post MemberPersona
        api_response = api_instance.post_system_members_by_parent_id_personas(parent_id, client_id, member_persona)
        print("The response of MemberPersonasApi->post_system_members_by_parent_id_personas:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MemberPersonasApi->post_system_members_by_parent_id_personas: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| memberId | 
 **client_id** | **str**|  | 
 **member_persona** | [**MemberPersona**](MemberPersona.md)| memberPersona | 

### Return type

[**MemberPersona**](MemberPersona.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | MemberPersona |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_system_members_by_parent_id_personas_by_id**
> MemberPersona put_system_members_by_parent_id_personas_by_id(id, parent_id, client_id, member_persona)

Put MemberPersona

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.member_persona import MemberPersona
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
    api_instance = connectwise_psa.MemberPersonasApi(api_client)
    id = 56 # int | personaId
    parent_id = 56 # int | memberId
    client_id = 'client_id_example' # str | 
    member_persona = connectwise_psa.MemberPersona() # MemberPersona | memberPersona

    try:
        # Put MemberPersona
        api_response = api_instance.put_system_members_by_parent_id_personas_by_id(id, parent_id, client_id, member_persona)
        print("The response of MemberPersonasApi->put_system_members_by_parent_id_personas_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MemberPersonasApi->put_system_members_by_parent_id_personas_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| personaId | 
 **parent_id** | **int**| memberId | 
 **client_id** | **str**|  | 
 **member_persona** | [**MemberPersona**](MemberPersona.md)| memberPersona | 

### Return type

[**MemberPersona**](MemberPersona.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | MemberPersona |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

