# connectwise_psa.MyMemberCertificationsApi

All URIs are relative to *https://aus-api.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_system_members_by_parent_id_mycertifications_by_id**](MyMemberCertificationsApi.md#delete_system_members_by_parent_id_mycertifications_by_id) | **DELETE** /system/members/{parentId}/mycertifications/{id} | Delete MemberCertification
[**get_system_members_by_parent_id_mycertifications**](MyMemberCertificationsApi.md#get_system_members_by_parent_id_mycertifications) | **GET** /system/members/{parentId}/mycertifications | Get List of MemberCertification
[**get_system_members_by_parent_id_mycertifications_by_id**](MyMemberCertificationsApi.md#get_system_members_by_parent_id_mycertifications_by_id) | **GET** /system/members/{parentId}/mycertifications/{id} | Get MemberCertification
[**get_system_members_by_parent_id_mycertifications_count**](MyMemberCertificationsApi.md#get_system_members_by_parent_id_mycertifications_count) | **GET** /system/members/{parentId}/mycertifications/count | Get Count of MemberCertification
[**patch_system_members_by_parent_id_mycertifications_by_id**](MyMemberCertificationsApi.md#patch_system_members_by_parent_id_mycertifications_by_id) | **PATCH** /system/members/{parentId}/mycertifications/{id} | Patch MemberCertification
[**post_system_members_by_parent_id_mycertifications**](MyMemberCertificationsApi.md#post_system_members_by_parent_id_mycertifications) | **POST** /system/members/{parentId}/mycertifications | Post MemberCertification
[**put_system_members_by_parent_id_mycertifications_by_id**](MyMemberCertificationsApi.md#put_system_members_by_parent_id_mycertifications_by_id) | **PUT** /system/members/{parentId}/mycertifications/{id} | Put MemberCertification


# **delete_system_members_by_parent_id_mycertifications_by_id**
> delete_system_members_by_parent_id_mycertifications_by_id(id, parent_id, client_id)

Delete MemberCertification

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
    api_instance = connectwise_psa.MyMemberCertificationsApi(api_client)
    id = 56 # int | mycertificationId
    parent_id = 56 # int | memberId
    client_id = 'client_id_example' # str | 

    try:
        # Delete MemberCertification
        api_instance.delete_system_members_by_parent_id_mycertifications_by_id(id, parent_id, client_id)
    except Exception as e:
        print("Exception when calling MyMemberCertificationsApi->delete_system_members_by_parent_id_mycertifications_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| mycertificationId | 
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

# **get_system_members_by_parent_id_mycertifications**
> List[MemberCertification] get_system_members_by_parent_id_mycertifications(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of MemberCertification

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.member_certification import MemberCertification
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
    api_instance = connectwise_psa.MyMemberCertificationsApi(api_client)
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
        # Get List of MemberCertification
        api_response = api_instance.get_system_members_by_parent_id_mycertifications(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of MyMemberCertificationsApi->get_system_members_by_parent_id_mycertifications:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MyMemberCertificationsApi->get_system_members_by_parent_id_mycertifications: %s\n" % e)
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

[**List[MemberCertification]**](MemberCertification.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of MemberCertification |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_system_members_by_parent_id_mycertifications_by_id**
> MemberCertification get_system_members_by_parent_id_mycertifications_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get MemberCertification

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.member_certification import MemberCertification
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
    api_instance = connectwise_psa.MyMemberCertificationsApi(api_client)
    id = 56 # int | mycertificationId
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
        # Get MemberCertification
        api_response = api_instance.get_system_members_by_parent_id_mycertifications_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of MyMemberCertificationsApi->get_system_members_by_parent_id_mycertifications_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MyMemberCertificationsApi->get_system_members_by_parent_id_mycertifications_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| mycertificationId | 
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

[**MemberCertification**](MemberCertification.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | MemberCertification |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_system_members_by_parent_id_mycertifications_count**
> Count get_system_members_by_parent_id_mycertifications_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Count of MemberCertification

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
    api_instance = connectwise_psa.MyMemberCertificationsApi(api_client)
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
        # Get Count of MemberCertification
        api_response = api_instance.get_system_members_by_parent_id_mycertifications_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of MyMemberCertificationsApi->get_system_members_by_parent_id_mycertifications_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MyMemberCertificationsApi->get_system_members_by_parent_id_mycertifications_count: %s\n" % e)
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

# **patch_system_members_by_parent_id_mycertifications_by_id**
> MemberCertification patch_system_members_by_parent_id_mycertifications_by_id(id, parent_id, client_id, patch_operation)

Patch MemberCertification

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.member_certification import MemberCertification
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
    api_instance = connectwise_psa.MyMemberCertificationsApi(api_client)
    id = 56 # int | mycertificationId
    parent_id = 56 # int | memberId
    client_id = 'client_id_example' # str | 
    patch_operation = [connectwise_psa.PatchOperation()] # List[PatchOperation] | List of PatchOperation

    try:
        # Patch MemberCertification
        api_response = api_instance.patch_system_members_by_parent_id_mycertifications_by_id(id, parent_id, client_id, patch_operation)
        print("The response of MyMemberCertificationsApi->patch_system_members_by_parent_id_mycertifications_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MyMemberCertificationsApi->patch_system_members_by_parent_id_mycertifications_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| mycertificationId | 
 **parent_id** | **int**| memberId | 
 **client_id** | **str**|  | 
 **patch_operation** | [**List[PatchOperation]**](PatchOperation.md)| List of PatchOperation | 

### Return type

[**MemberCertification**](MemberCertification.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | MemberCertification |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_system_members_by_parent_id_mycertifications**
> MemberCertification post_system_members_by_parent_id_mycertifications(parent_id, client_id, member_certification)

Post MemberCertification

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.member_certification import MemberCertification
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
    api_instance = connectwise_psa.MyMemberCertificationsApi(api_client)
    parent_id = 56 # int | memberId
    client_id = 'client_id_example' # str | 
    member_certification = connectwise_psa.MemberCertification() # MemberCertification | memberCertification

    try:
        # Post MemberCertification
        api_response = api_instance.post_system_members_by_parent_id_mycertifications(parent_id, client_id, member_certification)
        print("The response of MyMemberCertificationsApi->post_system_members_by_parent_id_mycertifications:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MyMemberCertificationsApi->post_system_members_by_parent_id_mycertifications: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| memberId | 
 **client_id** | **str**|  | 
 **member_certification** | [**MemberCertification**](MemberCertification.md)| memberCertification | 

### Return type

[**MemberCertification**](MemberCertification.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | MemberCertification |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_system_members_by_parent_id_mycertifications_by_id**
> MemberCertification put_system_members_by_parent_id_mycertifications_by_id(id, parent_id, client_id, member_certification)

Put MemberCertification

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.member_certification import MemberCertification
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
    api_instance = connectwise_psa.MyMemberCertificationsApi(api_client)
    id = 56 # int | mycertificationId
    parent_id = 56 # int | memberId
    client_id = 'client_id_example' # str | 
    member_certification = connectwise_psa.MemberCertification() # MemberCertification | memberCertification

    try:
        # Put MemberCertification
        api_response = api_instance.put_system_members_by_parent_id_mycertifications_by_id(id, parent_id, client_id, member_certification)
        print("The response of MyMemberCertificationsApi->put_system_members_by_parent_id_mycertifications_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MyMemberCertificationsApi->put_system_members_by_parent_id_mycertifications_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| mycertificationId | 
 **parent_id** | **int**| memberId | 
 **client_id** | **str**|  | 
 **member_certification** | [**MemberCertification**](MemberCertification.md)| memberCertification | 

### Return type

[**MemberCertification**](MemberCertification.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | MemberCertification |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

