# OpportunityNote


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**entered_by** | **str** |  | [optional] 
**flagged** | **bool** |  | [optional] 
**id** | **int** |  | [optional] 
**mobile_guid** | **str** |  | [optional] 
**opportunity_id** | **int** |  | [optional] 
**text** | **str** |  | 
**type** | [**NoteTypeReference**](NoteTypeReference.md) |  | [optional] 

## Example

```python
from connectwise_psa.models.opportunity_note import OpportunityNote

# TODO update the JSON string below
json = "{}"
# create an instance of OpportunityNote from a JSON string
opportunity_note_instance = OpportunityNote.from_json(json)
# print the JSON string representation of the object
print OpportunityNote.to_json()

# convert the object into a dict
opportunity_note_dict = opportunity_note_instance.to_dict()
# create an instance of OpportunityNote from a dict
opportunity_note_form_dict = opportunity_note.from_dict(opportunity_note_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


