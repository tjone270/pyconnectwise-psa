# connectwise_psa.TeamMembersApi

All URIs are relative to *https://api-aus.myconnectwise.net/v4_6_release/apis/3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**post_service_team_members**](TeamMembersApi.md#post_service_team_members) | **POST** /service/teamMembers | Post TeamMember


# **post_service_team_members**
> TeamMember post_service_team_members(client_id, team_member)

Post TeamMember

### Example

```python
import time
import os
import connectwise_psa
from connectwise_psa.models.team_member import TeamMember
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
    api_instance = connectwise_psa.TeamMembersApi(api_client)
    client_id = 'client_id_example' # str | 
    team_member = connectwise_psa.TeamMember() # TeamMember | teamMember

    try:
        # Post TeamMember
        api_response = api_instance.post_service_team_members(client_id, team_member)
        print("The response of TeamMembersApi->post_service_team_members:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamMembersApi->post_service_team_members: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**|  | 
 **team_member** | [**TeamMember**](TeamMember.md)| teamMember | 

### Return type

[**TeamMember**](TeamMember.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.connectwise.com+json; version=2022.2

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | TeamMember |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

