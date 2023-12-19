# connectwise_psa.MemberSkillsApi

All URIs are relative to *https://aus-api.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_system_members_by_parent_id_skills_by_id**](MemberSkillsApi.md#delete_system_members_by_parent_id_skills_by_id) | **DELETE** /system/members/{parentId}/skills/{id} | Delete MemberSkill
[**delete_system_my_account_by_parent_id_skills_by_id**](MemberSkillsApi.md#delete_system_my_account_by_parent_id_skills_by_id) | **DELETE** /system/myAccount/{parentId}/skills/{id} | Delete MemberSkill
[**get_system_members_by_parent_id_skills**](MemberSkillsApi.md#get_system_members_by_parent_id_skills) | **GET** /system/members/{parentId}/skills | Get List of MemberSkill
[**get_system_members_by_parent_id_skills_by_id**](MemberSkillsApi.md#get_system_members_by_parent_id_skills_by_id) | **GET** /system/members/{parentId}/skills/{id} | Get MemberSkill
[**get_system_members_by_parent_id_skills_count**](MemberSkillsApi.md#get_system_members_by_parent_id_skills_count) | **GET** /system/members/{parentId}/skills/count | Get Count of MemberSkill
[**get_system_my_account_by_parent_id_skills**](MemberSkillsApi.md#get_system_my_account_by_parent_id_skills) | **GET** /system/myAccount/{parentId}/skills | Get List of MemberSkill
[**get_system_my_account_by_parent_id_skills_by_id**](MemberSkillsApi.md#get_system_my_account_by_parent_id_skills_by_id) | **GET** /system/myAccount/{parentId}/skills/{id} | Get MemberSkill
[**get_system_my_account_by_parent_id_skills_count**](MemberSkillsApi.md#get_system_my_account_by_parent_id_skills_count) | **GET** /system/myAccount/{parentId}/skills/count | Get Count of MemberSkill
[**patch_system_members_by_parent_id_skills_by_id**](MemberSkillsApi.md#patch_system_members_by_parent_id_skills_by_id) | **PATCH** /system/members/{parentId}/skills/{id} | Patch MemberSkill
[**patch_system_my_account_by_parent_id_skills_by_id**](MemberSkillsApi.md#patch_system_my_account_by_parent_id_skills_by_id) | **PATCH** /system/myAccount/{parentId}/skills/{id} | Patch MemberSkill
[**post_system_members_by_parent_id_skills**](MemberSkillsApi.md#post_system_members_by_parent_id_skills) | **POST** /system/members/{parentId}/skills | Post MemberSkill
[**post_system_my_account_by_parent_id_skills**](MemberSkillsApi.md#post_system_my_account_by_parent_id_skills) | **POST** /system/myAccount/{parentId}/skills | Post MemberSkill
[**put_system_members_by_parent_id_skills_by_id**](MemberSkillsApi.md#put_system_members_by_parent_id_skills_by_id) | **PUT** /system/members/{parentId}/skills/{id} | Put MemberSkill
[**put_system_my_account_by_parent_id_skills_by_id**](MemberSkillsApi.md#put_system_my_account_by_parent_id_skills_by_id) | **PUT** /system/myAccount/{parentId}/skills/{id} | Put MemberSkill


# **delete_system_members_by_parent_id_skills_by_id**
> delete_system_members_by_parent_id_skills_by_id(id, parent_id, client_id)

Delete MemberSkill

### Example

```python
import time
import os
import connectwise_psa
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
    api_instance = connectwise_psa.MemberSkillsApi(api_client)
    id = 56 # int | skillId
    parent_id = 56 # int | memberId
    client_id = 'client_id_example' # str | 

    try:
        # Delete MemberSkill
        api_instance.delete_system_members_by_parent_id_skills_by_id(id, parent_id, client_id)
    except Exception as e:
        print("Exception when calling MemberSkillsApi->delete_system_members_by_parent_id_skills_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| skillId | 
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

# **delete_system_my_account_by_parent_id_skills_by_id**
> delete_system_my_account_by_parent_id_skills_by_id(id, parent_id, client_id)

Delete MemberSkill

### Example

```python
import time
import os
import connectwise_psa
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
    api_instance = connectwise_psa.MemberSkillsApi(api_client)
    id = 56 # int | skillId
    parent_id = 56 # int | memberId
    client_id = 'client_id_example' # str | 

    try:
        # Delete MemberSkill
        api_instance.delete_system_my_account_by_parent_id_skills_by_id(id, parent_id, client_id)
    except Exception as e:
        print("Exception when calling MemberSkillsApi->delete_system_my_account_by_parent_id_skills_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| skillId | 
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

# **get_system_members_by_parent_id_skills**
> List[MemberSkill] get_system_members_by_parent_id_skills(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of MemberSkill

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.member_skill import MemberSkill
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
    api_instance = connectwise_psa.MemberSkillsApi(api_client)
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
        # Get List of MemberSkill
        api_response = api_instance.get_system_members_by_parent_id_skills(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of MemberSkillsApi->get_system_members_by_parent_id_skills:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MemberSkillsApi->get_system_members_by_parent_id_skills: %s\n" % e)
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

[**List[MemberSkill]**](MemberSkill.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of MemberSkill |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_system_members_by_parent_id_skills_by_id**
> MemberSkill get_system_members_by_parent_id_skills_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get MemberSkill

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.member_skill import MemberSkill
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
    api_instance = connectwise_psa.MemberSkillsApi(api_client)
    id = 56 # int | skillId
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
        # Get MemberSkill
        api_response = api_instance.get_system_members_by_parent_id_skills_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of MemberSkillsApi->get_system_members_by_parent_id_skills_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MemberSkillsApi->get_system_members_by_parent_id_skills_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| skillId | 
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

[**MemberSkill**](MemberSkill.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | MemberSkill |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_system_members_by_parent_id_skills_count**
> Count get_system_members_by_parent_id_skills_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Count of MemberSkill

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.count import Count
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
    api_instance = connectwise_psa.MemberSkillsApi(api_client)
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
        # Get Count of MemberSkill
        api_response = api_instance.get_system_members_by_parent_id_skills_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of MemberSkillsApi->get_system_members_by_parent_id_skills_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MemberSkillsApi->get_system_members_by_parent_id_skills_count: %s\n" % e)
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

# **get_system_my_account_by_parent_id_skills**
> List[MemberSkill] get_system_my_account_by_parent_id_skills(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of MemberSkill

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.member_skill import MemberSkill
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
    api_instance = connectwise_psa.MemberSkillsApi(api_client)
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
        # Get List of MemberSkill
        api_response = api_instance.get_system_my_account_by_parent_id_skills(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of MemberSkillsApi->get_system_my_account_by_parent_id_skills:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MemberSkillsApi->get_system_my_account_by_parent_id_skills: %s\n" % e)
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

[**List[MemberSkill]**](MemberSkill.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of MemberSkill |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_system_my_account_by_parent_id_skills_by_id**
> MemberSkill get_system_my_account_by_parent_id_skills_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get MemberSkill

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.member_skill import MemberSkill
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
    api_instance = connectwise_psa.MemberSkillsApi(api_client)
    id = 56 # int | skillId
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
        # Get MemberSkill
        api_response = api_instance.get_system_my_account_by_parent_id_skills_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of MemberSkillsApi->get_system_my_account_by_parent_id_skills_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MemberSkillsApi->get_system_my_account_by_parent_id_skills_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| skillId | 
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

[**MemberSkill**](MemberSkill.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | MemberSkill |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_system_my_account_by_parent_id_skills_count**
> Count get_system_my_account_by_parent_id_skills_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Count of MemberSkill

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.count import Count
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
    api_instance = connectwise_psa.MemberSkillsApi(api_client)
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
        # Get Count of MemberSkill
        api_response = api_instance.get_system_my_account_by_parent_id_skills_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of MemberSkillsApi->get_system_my_account_by_parent_id_skills_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MemberSkillsApi->get_system_my_account_by_parent_id_skills_count: %s\n" % e)
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

# **patch_system_members_by_parent_id_skills_by_id**
> MemberSkill patch_system_members_by_parent_id_skills_by_id(id, parent_id, client_id, patch_operation)

Patch MemberSkill

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.member_skill import MemberSkill
from connectwise_psa.models.patch_operation import PatchOperation
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
    api_instance = connectwise_psa.MemberSkillsApi(api_client)
    id = 56 # int | skillId
    parent_id = 56 # int | memberId
    client_id = 'client_id_example' # str | 
    patch_operation = [connectwise_psa.PatchOperation()] # List[PatchOperation] | List of PatchOperation

    try:
        # Patch MemberSkill
        api_response = api_instance.patch_system_members_by_parent_id_skills_by_id(id, parent_id, client_id, patch_operation)
        print("The response of MemberSkillsApi->patch_system_members_by_parent_id_skills_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MemberSkillsApi->patch_system_members_by_parent_id_skills_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| skillId | 
 **parent_id** | **int**| memberId | 
 **client_id** | **str**|  | 
 **patch_operation** | [**List[PatchOperation]**](PatchOperation.md)| List of PatchOperation | 

### Return type

[**MemberSkill**](MemberSkill.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | MemberSkill |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_system_my_account_by_parent_id_skills_by_id**
> MemberSkill patch_system_my_account_by_parent_id_skills_by_id(id, parent_id, client_id, patch_operation)

Patch MemberSkill

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.member_skill import MemberSkill
from connectwise_psa.models.patch_operation import PatchOperation
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
    api_instance = connectwise_psa.MemberSkillsApi(api_client)
    id = 56 # int | skillId
    parent_id = 56 # int | memberId
    client_id = 'client_id_example' # str | 
    patch_operation = [connectwise_psa.PatchOperation()] # List[PatchOperation] | List of PatchOperation

    try:
        # Patch MemberSkill
        api_response = api_instance.patch_system_my_account_by_parent_id_skills_by_id(id, parent_id, client_id, patch_operation)
        print("The response of MemberSkillsApi->patch_system_my_account_by_parent_id_skills_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MemberSkillsApi->patch_system_my_account_by_parent_id_skills_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| skillId | 
 **parent_id** | **int**| memberId | 
 **client_id** | **str**|  | 
 **patch_operation** | [**List[PatchOperation]**](PatchOperation.md)| List of PatchOperation | 

### Return type

[**MemberSkill**](MemberSkill.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | MemberSkill |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_system_members_by_parent_id_skills**
> MemberSkill post_system_members_by_parent_id_skills(parent_id, client_id, member_skill)

Post MemberSkill

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.member_skill import MemberSkill
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
    api_instance = connectwise_psa.MemberSkillsApi(api_client)
    parent_id = 56 # int | memberId
    client_id = 'client_id_example' # str | 
    member_skill = connectwise_psa.MemberSkill() # MemberSkill | memberSkill

    try:
        # Post MemberSkill
        api_response = api_instance.post_system_members_by_parent_id_skills(parent_id, client_id, member_skill)
        print("The response of MemberSkillsApi->post_system_members_by_parent_id_skills:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MemberSkillsApi->post_system_members_by_parent_id_skills: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| memberId | 
 **client_id** | **str**|  | 
 **member_skill** | [**MemberSkill**](MemberSkill.md)| memberSkill | 

### Return type

[**MemberSkill**](MemberSkill.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | MemberSkill |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_system_my_account_by_parent_id_skills**
> MemberSkill post_system_my_account_by_parent_id_skills(parent_id, client_id, member_skill)

Post MemberSkill

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.member_skill import MemberSkill
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
    api_instance = connectwise_psa.MemberSkillsApi(api_client)
    parent_id = 56 # int | memberId
    client_id = 'client_id_example' # str | 
    member_skill = connectwise_psa.MemberSkill() # MemberSkill | memberSkill

    try:
        # Post MemberSkill
        api_response = api_instance.post_system_my_account_by_parent_id_skills(parent_id, client_id, member_skill)
        print("The response of MemberSkillsApi->post_system_my_account_by_parent_id_skills:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MemberSkillsApi->post_system_my_account_by_parent_id_skills: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| memberId | 
 **client_id** | **str**|  | 
 **member_skill** | [**MemberSkill**](MemberSkill.md)| memberSkill | 

### Return type

[**MemberSkill**](MemberSkill.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | MemberSkill |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_system_members_by_parent_id_skills_by_id**
> MemberSkill put_system_members_by_parent_id_skills_by_id(id, parent_id, client_id, member_skill)

Put MemberSkill

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.member_skill import MemberSkill
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
    api_instance = connectwise_psa.MemberSkillsApi(api_client)
    id = 56 # int | skillId
    parent_id = 56 # int | memberId
    client_id = 'client_id_example' # str | 
    member_skill = connectwise_psa.MemberSkill() # MemberSkill | memberSkill

    try:
        # Put MemberSkill
        api_response = api_instance.put_system_members_by_parent_id_skills_by_id(id, parent_id, client_id, member_skill)
        print("The response of MemberSkillsApi->put_system_members_by_parent_id_skills_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MemberSkillsApi->put_system_members_by_parent_id_skills_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| skillId | 
 **parent_id** | **int**| memberId | 
 **client_id** | **str**|  | 
 **member_skill** | [**MemberSkill**](MemberSkill.md)| memberSkill | 

### Return type

[**MemberSkill**](MemberSkill.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | MemberSkill |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_system_my_account_by_parent_id_skills_by_id**
> MemberSkill put_system_my_account_by_parent_id_skills_by_id(id, parent_id, client_id, member_skill)

Put MemberSkill

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.member_skill import MemberSkill
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
    api_instance = connectwise_psa.MemberSkillsApi(api_client)
    id = 56 # int | skillId
    parent_id = 56 # int | memberId
    client_id = 'client_id_example' # str | 
    member_skill = connectwise_psa.MemberSkill() # MemberSkill | memberSkill

    try:
        # Put MemberSkill
        api_response = api_instance.put_system_my_account_by_parent_id_skills_by_id(id, parent_id, client_id, member_skill)
        print("The response of MemberSkillsApi->put_system_my_account_by_parent_id_skills_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MemberSkillsApi->put_system_my_account_by_parent_id_skills_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| skillId | 
 **parent_id** | **int**| memberId | 
 **client_id** | **str**|  | 
 **member_skill** | [**MemberSkill**](MemberSkill.md)| memberSkill | 

### Return type

[**MemberSkill**](MemberSkill.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | MemberSkill |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

