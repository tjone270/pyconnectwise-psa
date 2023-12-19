# NoteTypeReference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.note_type_reference import NoteTypeReference

# TODO update the JSON string below
json = "{}"
# create an instance of NoteTypeReference from a JSON string
note_type_reference_instance = NoteTypeReference.from_json(json)
# print the JSON string representation of the object
print NoteTypeReference.to_json()

# convert the object into a dict
note_type_reference_dict = note_type_reference_instance.to_dict()
# create an instance of NoteTypeReference from a dict
note_type_reference_form_dict = note_type_reference.from_dict(note_type_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


