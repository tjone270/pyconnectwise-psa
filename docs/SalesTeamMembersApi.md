# connectwise_psa.SalesTeamMembersApi

All URIs are relative to *https://api-aus.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_sales_sales_teams_by_parent_id_members_by_id**](SalesTeamMembersApi.md#delete_sales_sales_teams_by_parent_id_members_by_id) | **DELETE** /sales/salesTeams/{parentId}/members/{id} | Delete SalesTeamMember
[**get_sales_sales_teams_by_parent_id_members**](SalesTeamMembersApi.md#get_sales_sales_teams_by_parent_id_members) | **GET** /sales/salesTeams/{parentId}/members | Get List of SalesTeamMember
[**get_sales_sales_teams_by_parent_id_members_by_id**](SalesTeamMembersApi.md#get_sales_sales_teams_by_parent_id_members_by_id) | **GET** /sales/salesTeams/{parentId}/members/{id} | Get SalesTeamMember
[**get_sales_sales_teams_by_parent_id_members_count**](SalesTeamMembersApi.md#get_sales_sales_teams_by_parent_id_members_count) | **GET** /sales/salesTeams/{parentId}/members/count | Get Count of SalesTeamMember
[**patch_sales_sales_teams_by_parent_id_members_by_id**](SalesTeamMembersApi.md#patch_sales_sales_teams_by_parent_id_members_by_id) | **PATCH** /sales/salesTeams/{parentId}/members/{id} | Patch SalesTeamMember
[**post_sales_sales_teams_by_parent_id_members**](SalesTeamMembersApi.md#post_sales_sales_teams_by_parent_id_members) | **POST** /sales/salesTeams/{parentId}/members | Post SalesTeamMember
[**put_sales_sales_teams_by_parent_id_members_by_id**](SalesTeamMembersApi.md#put_sales_sales_teams_by_parent_id_members_by_id) | **PUT** /sales/salesTeams/{parentId}/members/{id} | Put SalesTeamMember


# **delete_sales_sales_teams_by_parent_id_members_by_id**
> delete_sales_sales_teams_by_parent_id_members_by_id(id, parent_id, client_id)

Delete SalesTeamMember

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
    api_instance = connectwise_psa.SalesTeamMembersApi(api_client)
    id = 56 # int | memberId
    parent_id = 56 # int | salesTeamId
    client_id = 'client_id_example' # str | 

    try:
        # Delete SalesTeamMember
        api_instance.delete_sales_sales_teams_by_parent_id_members_by_id(id, parent_id, client_id)
    except Exception as e:
        print("Exception when calling SalesTeamMembersApi->delete_sales_sales_teams_by_parent_id_members_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| memberId | 
 **parent_id** | **int**| salesTeamId | 
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

# **get_sales_sales_teams_by_parent_id_members**
> List[SalesTeamMember] get_sales_sales_teams_by_parent_id_members(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of SalesTeamMember

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.sales_team_member import SalesTeamMember
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
    api_instance = connectwise_psa.SalesTeamMembersApi(api_client)
    parent_id = 56 # int | salesTeamId
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
        # Get List of SalesTeamMember
        api_response = api_instance.get_sales_sales_teams_by_parent_id_members(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of SalesTeamMembersApi->get_sales_sales_teams_by_parent_id_members:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SalesTeamMembersApi->get_sales_sales_teams_by_parent_id_members: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| salesTeamId | 
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

[**List[SalesTeamMember]**](SalesTeamMember.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of SalesTeamMember |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sales_sales_teams_by_parent_id_members_by_id**
> SalesTeamMember get_sales_sales_teams_by_parent_id_members_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get SalesTeamMember

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.sales_team_member import SalesTeamMember
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
    api_instance = connectwise_psa.SalesTeamMembersApi(api_client)
    id = 56 # int | memberId
    parent_id = 56 # int | salesTeamId
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
        # Get SalesTeamMember
        api_response = api_instance.get_sales_sales_teams_by_parent_id_members_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of SalesTeamMembersApi->get_sales_sales_teams_by_parent_id_members_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SalesTeamMembersApi->get_sales_sales_teams_by_parent_id_members_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| memberId | 
 **parent_id** | **int**| salesTeamId | 
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

[**SalesTeamMember**](SalesTeamMember.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | SalesTeamMember |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sales_sales_teams_by_parent_id_members_count**
> Count get_sales_sales_teams_by_parent_id_members_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Count of SalesTeamMember

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
    api_instance = connectwise_psa.SalesTeamMembersApi(api_client)
    parent_id = 56 # int | salesTeamId
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
        # Get Count of SalesTeamMember
        api_response = api_instance.get_sales_sales_teams_by_parent_id_members_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of SalesTeamMembersApi->get_sales_sales_teams_by_parent_id_members_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SalesTeamMembersApi->get_sales_sales_teams_by_parent_id_members_count: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| salesTeamId | 
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

# **patch_sales_sales_teams_by_parent_id_members_by_id**
> SalesTeamMember patch_sales_sales_teams_by_parent_id_members_by_id(id, parent_id, client_id, patch_operation)

Patch SalesTeamMember

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.patch_operation import PatchOperation
from connectwise_psa.models.sales_team_member import SalesTeamMember
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
    api_instance = connectwise_psa.SalesTeamMembersApi(api_client)
    id = 56 # int | memberId
    parent_id = 56 # int | salesTeamId
    client_id = 'client_id_example' # str | 
    patch_operation = [connectwise_psa.PatchOperation()] # List[PatchOperation] | List of PatchOperation

    try:
        # Patch SalesTeamMember
        api_response = api_instance.patch_sales_sales_teams_by_parent_id_members_by_id(id, parent_id, client_id, patch_operation)
        print("The response of SalesTeamMembersApi->patch_sales_sales_teams_by_parent_id_members_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SalesTeamMembersApi->patch_sales_sales_teams_by_parent_id_members_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| memberId | 
 **parent_id** | **int**| salesTeamId | 
 **client_id** | **str**|  | 
 **patch_operation** | [**List[PatchOperation]**](PatchOperation.md)| List of PatchOperation | 

### Return type

[**SalesTeamMember**](SalesTeamMember.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | SalesTeamMember |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_sales_sales_teams_by_parent_id_members**
> SalesTeamMember post_sales_sales_teams_by_parent_id_members(parent_id, client_id, sales_team_member)

Post SalesTeamMember

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.sales_team_member import SalesTeamMember
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
    api_instance = connectwise_psa.SalesTeamMembersApi(api_client)
    parent_id = 56 # int | salesTeamId
    client_id = 'client_id_example' # str | 
    sales_team_member = connectwise_psa.SalesTeamMember() # SalesTeamMember | salesTeamMember

    try:
        # Post SalesTeamMember
        api_response = api_instance.post_sales_sales_teams_by_parent_id_members(parent_id, client_id, sales_team_member)
        print("The response of SalesTeamMembersApi->post_sales_sales_teams_by_parent_id_members:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SalesTeamMembersApi->post_sales_sales_teams_by_parent_id_members: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| salesTeamId | 
 **client_id** | **str**|  | 
 **sales_team_member** | [**SalesTeamMember**](SalesTeamMember.md)| salesTeamMember | 

### Return type

[**SalesTeamMember**](SalesTeamMember.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | SalesTeamMember |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_sales_sales_teams_by_parent_id_members_by_id**
> SalesTeamMember put_sales_sales_teams_by_parent_id_members_by_id(id, parent_id, client_id, sales_team_member)

Put SalesTeamMember

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.sales_team_member import SalesTeamMember
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
    api_instance = connectwise_psa.SalesTeamMembersApi(api_client)
    id = 56 # int | memberId
    parent_id = 56 # int | salesTeamId
    client_id = 'client_id_example' # str | 
    sales_team_member = connectwise_psa.SalesTeamMember() # SalesTeamMember | salesTeamMember

    try:
        # Put SalesTeamMember
        api_response = api_instance.put_sales_sales_teams_by_parent_id_members_by_id(id, parent_id, client_id, sales_team_member)
        print("The response of SalesTeamMembersApi->put_sales_sales_teams_by_parent_id_members_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SalesTeamMembersApi->put_sales_sales_teams_by_parent_id_members_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| memberId | 
 **parent_id** | **int**| salesTeamId | 
 **client_id** | **str**|  | 
 **sales_team_member** | [**SalesTeamMember**](SalesTeamMember.md)| salesTeamMember | 

### Return type

[**SalesTeamMember**](SalesTeamMember.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | SalesTeamMember |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

