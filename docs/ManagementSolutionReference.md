# ManagementSolutionReference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**setup_name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.management_solution_reference import ManagementSolutionReference

# TODO update the JSON string below
json = "{}"
# create an instance of ManagementSolutionReference from a JSON string
management_solution_reference_instance = ManagementSolutionReference.from_json(json)
# print the JSON string representation of the object
print ManagementSolutionReference.to_json()

# convert the object into a dict
management_solution_reference_dict = management_solution_reference_instance.to_dict()
# create an instance of ManagementSolutionReference from a dict
management_solution_reference_form_dict = management_solution_reference.from_dict(management_solution_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


