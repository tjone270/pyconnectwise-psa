# ProjectPhaseReference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.project_phase_reference import ProjectPhaseReference

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectPhaseReference from a JSON string
project_phase_reference_instance = ProjectPhaseReference.from_json(json)
# print the JSON string representation of the object
print ProjectPhaseReference.to_json()

# convert the object into a dict
project_phase_reference_dict = project_phase_reference_instance.to_dict()
# create an instance of ProjectPhaseReference from a dict
project_phase_reference_form_dict = project_phase_reference.from_dict(project_phase_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


