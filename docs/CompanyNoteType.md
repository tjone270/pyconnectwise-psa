# CompanyNoteType


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**default_flag** | **bool** |  | [optional] 
**id** | **int** |  | [optional] 
**identifier** | **str** |  Max length: 15; | [optional] 
**import_flag** | **bool** |  | [optional] 
**name** | **str** |  Max length: 50; | 

## Example

```python
from connectwise_psa.models.company_note_type import CompanyNoteType

# TODO update the JSON string below
json = "{}"
# create an instance of CompanyNoteType from a JSON string
company_note_type_instance = CompanyNoteType.from_json(json)
# print the JSON string representation of the object
print CompanyNoteType.to_json()

# convert the object into a dict
company_note_type_dict = company_note_type_instance.to_dict()
# create an instance of CompanyNoteType from a dict
company_note_type_form_dict = company_note_type.from_dict(company_note_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


