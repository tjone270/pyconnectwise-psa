# ProjectWorkplan


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**phases** | [**List[ProjectPhase]**](ProjectPhase.md) |  | [optional] 
**project_id** | **int** |  | [optional] 

## Example

```python
from connectwise_psa.models.project_workplan import ProjectWorkplan

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectWorkplan from a JSON string
project_workplan_instance = ProjectWorkplan.from_json(json)
# print the JSON string representation of the object
print ProjectWorkplan.to_json()

# convert the object into a dict
project_workplan_dict = project_workplan_instance.to_dict()
# create an instance of ProjectWorkplan from a dict
project_workplan_form_dict = project_workplan.from_dict(project_workplan_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


