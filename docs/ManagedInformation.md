# ManagedInformation


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**child_configurations_matching_on** | **str** |  | [optional] 
**inactivate_configurations_matching_on** | **str** |  | [optional] 
**inactive_configuration_status_id** | **int** |  | [optional] 
**level** | **str** |  | [optional] 
**managed_identifier** | **str** |  | [optional] 
**management_solution_name** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.managed_information import ManagedInformation

# TODO update the JSON string below
json = "{}"
# create an instance of ManagedInformation from a JSON string
managed_information_instance = ManagedInformation.from_json(json)
# print the JSON string representation of the object
print ManagedInformation.to_json()

# convert the object into a dict
managed_information_dict = managed_information_instance.to_dict()
# create an instance of ManagedInformation from a dict
managed_information_form_dict = managed_information.from_dict(managed_information_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


