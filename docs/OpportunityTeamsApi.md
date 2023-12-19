# connectwise_psa.OpportunityTeamsApi

All URIs are relative to *https://api-aus.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_sales_opportunities_by_parent_id_team_by_id**](OpportunityTeamsApi.md#delete_sales_opportunities_by_parent_id_team_by_id) | **DELETE** /sales/opportunities/{parentId}/team/{id} | Delete Team
[**get_sales_opportunities_by_parent_id_team**](OpportunityTeamsApi.md#get_sales_opportunities_by_parent_id_team) | **GET** /sales/opportunities/{parentId}/team | Get List of Team
[**get_sales_opportunities_by_parent_id_team_by_id**](OpportunityTeamsApi.md#get_sales_opportunities_by_parent_id_team_by_id) | **GET** /sales/opportunities/{parentId}/team/{id} | Get Team
[**get_sales_opportunities_by_parent_id_team_count**](OpportunityTeamsApi.md#get_sales_opportunities_by_parent_id_team_count) | **GET** /sales/opportunities/{parentId}/team/count | Get Count of Team
[**patch_sales_opportunities_by_parent_id_team_by_id**](OpportunityTeamsApi.md#patch_sales_opportunities_by_parent_id_team_by_id) | **PATCH** /sales/opportunities/{parentId}/team/{id} | Patch Team
[**post_sales_opportunities_by_parent_id_team**](OpportunityTeamsApi.md#post_sales_opportunities_by_parent_id_team) | **POST** /sales/opportunities/{parentId}/team | Post Team
[**put_sales_opportunities_by_parent_id_team_by_id**](OpportunityTeamsApi.md#put_sales_opportunities_by_parent_id_team_by_id) | **PUT** /sales/opportunities/{parentId}/team/{id} | Put Team


# **delete_sales_opportunities_by_parent_id_team_by_id**
> delete_sales_opportunities_by_parent_id_team_by_id(id, parent_id, client_id)

Delete Team

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
    api_instance = connectwise_psa.OpportunityTeamsApi(api_client)
    id = 56 # int | teamId
    parent_id = 56 # int | opportunityId
    client_id = 'client_id_example' # str | 

    try:
        # Delete Team
        api_instance.delete_sales_opportunities_by_parent_id_team_by_id(id, parent_id, client_id)
    except Exception as e:
        print("Exception when calling OpportunityTeamsApi->delete_sales_opportunities_by_parent_id_team_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| teamId | 
 **parent_id** | **int**| opportunityId | 
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

# **get_sales_opportunities_by_parent_id_team**
> List[Team] get_sales_opportunities_by_parent_id_team(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get List of Team

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.team import Team
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
    api_instance = connectwise_psa.OpportunityTeamsApi(api_client)
    parent_id = 56 # int | opportunityId
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
        # Get List of Team
        api_response = api_instance.get_sales_opportunities_by_parent_id_team(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of OpportunityTeamsApi->get_sales_opportunities_by_parent_id_team:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpportunityTeamsApi->get_sales_opportunities_by_parent_id_team: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| opportunityId | 
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

[**List[Team]**](Team.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of Team |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sales_opportunities_by_parent_id_team_by_id**
> Team get_sales_opportunities_by_parent_id_team_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Team

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.team import Team
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
    api_instance = connectwise_psa.OpportunityTeamsApi(api_client)
    id = 56 # int | teamId
    parent_id = 56 # int | opportunityId
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
        # Get Team
        api_response = api_instance.get_sales_opportunities_by_parent_id_team_by_id(id, parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of OpportunityTeamsApi->get_sales_opportunities_by_parent_id_team_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpportunityTeamsApi->get_sales_opportunities_by_parent_id_team_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| teamId | 
 **parent_id** | **int**| opportunityId | 
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

[**Team**](Team.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Team |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sales_opportunities_by_parent_id_team_count**
> Count get_sales_opportunities_by_parent_id_team_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)

Get Count of Team

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
    api_instance = connectwise_psa.OpportunityTeamsApi(api_client)
    parent_id = 56 # int | opportunityId
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
        # Get Count of Team
        api_response = api_instance.get_sales_opportunities_by_parent_id_team_count(parent_id, client_id, conditions=conditions, child_conditions=child_conditions, custom_field_conditions=custom_field_conditions, order_by=order_by, fields=fields, page=page, page_size=page_size, page_id=page_id)
        print("The response of OpportunityTeamsApi->get_sales_opportunities_by_parent_id_team_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpportunityTeamsApi->get_sales_opportunities_by_parent_id_team_count: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| opportunityId | 
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

# **patch_sales_opportunities_by_parent_id_team_by_id**
> Team patch_sales_opportunities_by_parent_id_team_by_id(id, parent_id, client_id, patch_operation)

Patch Team

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.patch_operation import PatchOperation
from connectwise_psa.models.team import Team
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
    api_instance = connectwise_psa.OpportunityTeamsApi(api_client)
    id = 56 # int | teamId
    parent_id = 56 # int | opportunityId
    client_id = 'client_id_example' # str | 
    patch_operation = [connectwise_psa.PatchOperation()] # List[PatchOperation] | List of PatchOperation

    try:
        # Patch Team
        api_response = api_instance.patch_sales_opportunities_by_parent_id_team_by_id(id, parent_id, client_id, patch_operation)
        print("The response of OpportunityTeamsApi->patch_sales_opportunities_by_parent_id_team_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpportunityTeamsApi->patch_sales_opportunities_by_parent_id_team_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| teamId | 
 **parent_id** | **int**| opportunityId | 
 **client_id** | **str**|  | 
 **patch_operation** | [**List[PatchOperation]**](PatchOperation.md)| List of PatchOperation | 

### Return type

[**Team**](Team.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Team |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_sales_opportunities_by_parent_id_team**
> Team post_sales_opportunities_by_parent_id_team(parent_id, client_id, team)

Post Team

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.team import Team
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
    api_instance = connectwise_psa.OpportunityTeamsApi(api_client)
    parent_id = 56 # int | opportunityId
    client_id = 'client_id_example' # str | 
    team = connectwise_psa.Team() # Team | team

    try:
        # Post Team
        api_response = api_instance.post_sales_opportunities_by_parent_id_team(parent_id, client_id, team)
        print("The response of OpportunityTeamsApi->post_sales_opportunities_by_parent_id_team:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpportunityTeamsApi->post_sales_opportunities_by_parent_id_team: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **int**| opportunityId | 
 **client_id** | **str**|  | 
 **team** | [**Team**](Team.md)| team | 

### Return type

[**Team**](Team.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Team |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_sales_opportunities_by_parent_id_team_by_id**
> Team put_sales_opportunities_by_parent_id_team_by_id(id, parent_id, client_id, team)

Put Team

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.team import Team
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
    api_instance = connectwise_psa.OpportunityTeamsApi(api_client)
    id = 56 # int | teamId
    parent_id = 56 # int | opportunityId
    client_id = 'client_id_example' # str | 
    team = connectwise_psa.Team() # Team | team

    try:
        # Put Team
        api_response = api_instance.put_sales_opportunities_by_parent_id_team_by_id(id, parent_id, client_id, team)
        print("The response of OpportunityTeamsApi->put_sales_opportunities_by_parent_id_team_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpportunityTeamsApi->put_sales_opportunities_by_parent_id_team_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| teamId | 
 **parent_id** | **int**| opportunityId | 
 **client_id** | **str**|  | 
 **team** | [**Team**](Team.md)| team | 

### Return type

[**Team**](Team.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Team |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

