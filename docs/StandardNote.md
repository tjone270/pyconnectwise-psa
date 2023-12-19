# StandardNote


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**board** | [**BoardReference**](BoardReference.md) |  | [optional] 
**contents** | **str** |  | 
**department** | [**SystemDepartmentReference**](SystemDepartmentReference.md) |  | [optional] 
**id** | **int** |  | [optional] 
**location** | [**SystemLocationReference**](SystemLocationReference.md) |  | [optional] 
**name** | **str** |  Max length: 50; | 

## Example

```python
from connectwise_psa.models.standard_note import StandardNote

# TODO update the JSON string below
json = "{}"
# create an instance of StandardNote from a JSON string
standard_note_instance = StandardNote.from_json(json)
# print the JSON string representation of the object
print StandardNote.to_json()

# convert the object into a dict
standard_note_dict = standard_note_instance.to_dict()
# create an instance of StandardNote from a dict
standard_note_form_dict = standard_note.from_dict(standard_note_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


