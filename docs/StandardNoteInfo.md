# StandardNoteInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**board** | [**BoardReference**](BoardReference.md) |  | [optional] 
**contents** | **str** |  | [optional] 
**department** | [**SystemDepartmentReference**](SystemDepartmentReference.md) |  | [optional] 
**id** | **int** |  | [optional] 
**location** | [**SystemLocationReference**](SystemLocationReference.md) |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.standard_note_info import StandardNoteInfo

# TODO update the JSON string below
json = "{}"
# create an instance of StandardNoteInfo from a JSON string
standard_note_info_instance = StandardNoteInfo.from_json(json)
# print the JSON string representation of the object
print StandardNoteInfo.to_json()

# convert the object into a dict
standard_note_info_dict = standard_note_info_instance.to_dict()
# create an instance of StandardNoteInfo from a dict
standard_note_info_form_dict = standard_note_info.from_dict(standard_note_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


