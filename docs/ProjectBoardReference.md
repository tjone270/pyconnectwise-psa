# ProjectBoardReference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.project_board_reference import ProjectBoardReference

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectBoardReference from a JSON string
project_board_reference_instance = ProjectBoardReference.from_json(json)
# print the JSON string representation of the object
print ProjectBoardReference.to_json()

# convert the object into a dict
project_board_reference_dict = project_board_reference_instance.to_dict()
# create an instance of ProjectBoardReference from a dict
project_board_reference_form_dict = project_board_reference.from_dict(project_board_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


