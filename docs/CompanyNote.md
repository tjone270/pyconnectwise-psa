# CompanyNote


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**company** | [**CompanyReference**](CompanyReference.md) |  | [optional] 
**entered_by** | **str** |  | [optional] 
**flagged** | **bool** |  | [optional] 
**id** | **int** |  | [optional] 
**text** | **str** |  | 
**type** | [**NoteTypeReference**](NoteTypeReference.md) |  | [optional] 

## Example

```python
from connectwise_psa.models.company_note import CompanyNote

# TODO update the JSON string below
json = "{}"
# create an instance of CompanyNote from a JSON string
company_note_instance = CompanyNote.from_json(json)
# print the JSON string representation of the object
print CompanyNote.to_json()

# convert the object into a dict
company_note_dict = company_note_instance.to_dict()
# create an instance of CompanyNote from a dict
company_note_form_dict = company_note.from_dict(company_note_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


