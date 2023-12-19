# ProjectNote


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**flagged** | **bool** |  | [optional] 
**id** | **int** |  | [optional] 
**project_id** | **int** |  | [optional] 
**text** | **str** |  | 
**type** | [**NoteTypeReference**](NoteTypeReference.md) |  | [optional] 

## Example

```python
from connectwise_psa.models.project_note import ProjectNote

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectNote from a JSON string
project_note_instance = ProjectNote.from_json(json)
# print the JSON string representation of the object
print ProjectNote.to_json()

# convert the object into a dict
project_note_dict = project_note_instance.to_dict()
# create an instance of ProjectNote from a dict
project_note_form_dict = project_note.from_dict(project_note_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


