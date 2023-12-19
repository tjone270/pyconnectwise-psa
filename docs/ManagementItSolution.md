# ManagementItSolution


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**continuum_api_password** | **str** | Gets or sets             this is only required for Continuum solution. Max length: 100; | [optional] 
**continuum_api_username** | **str** | Gets or sets             this is only required for Continuum solution. Max length: 100; | [optional] 
**global_login_flag** | **bool** |  | [optional] 
**global_login_password** | **str** | Gets or sets             this is only required when globalLoginFlag &#x3D; true. Max length: 50; | [optional] 
**global_login_username** | **str** | Gets or sets             this is only required when globalLoginFlag &#x3D; true. Max length: 50; | [optional] 
**id** | **int** |  | [optional] 
**level_api_password** | **str** | Gets or sets             this is only required for Level Platforms solution. Max length: 100; | [optional] 
**level_api_username** | **str** | Gets or sets             this is only required for Level Platforms solution. Max length: 100; | [optional] 
**level_var_domain** | **str** | Gets or sets             this is only required for Level Platforms solution. Max length: 100; | [optional] 
**management_it_solution_type** | **str** |  | 
**management_server_url** | **str** | Gets or sets             this is only required for Level Platforms. Max length: 200; | [optional] 
**management_solution_name** | **str** | Gets or sets             this is only required when managementItSolutionType is Custom. Max length: 30; | [optional] 
**n_able_password** | **str** | Gets or sets             this is only required for N-Able solution. Max length: 50; | [optional] 
**n_able_username** | **str** | Gets or sets             this is only required for N-Able solution. Max length: 50; | [optional] 
**name** | **str** |  Max length: 30; | 
**no_display_flag** | **bool** |  | [optional] 
**override_login_location_flag** | **bool** |  | [optional] 
**override_web_service_location_flag** | **bool** |  | [optional] 
**portal_override_login_url** | **str** | Gets or sets             this is only required for Level Platforms when overrideLoginLocationFlag is true. Max length: 200; | [optional] 
**using_ssl_flag** | **bool** |  | [optional] 
**webservice_override_url** | **str** | Gets or sets             this is only required for Level Platforms when overrideWebServiceLocationFlag is true. Max length: 200; | [optional] 

## Example

```python
from connectwise_psa.models.management_it_solution import ManagementItSolution

# TODO update the JSON string below
json = "{}"
# create an instance of ManagementItSolution from a JSON string
management_it_solution_instance = ManagementItSolution.from_json(json)
# print the JSON string representation of the object
print ManagementItSolution.to_json()

# convert the object into a dict
management_it_solution_dict = management_it_solution_instance.to_dict()
# create an instance of ManagementItSolution from a dict
management_it_solution_form_dict = management_it_solution.from_dict(management_it_solution_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


