# CompanyNoteTypeInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**default_flag** | **bool** |  | [optional] 
**id** | **int** |  | [optional] 
**identifier** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.company_note_type_info import CompanyNoteTypeInfo

# TODO update the JSON string below
json = "{}"
# create an instance of CompanyNoteTypeInfo from a JSON string
company_note_type_info_instance = CompanyNoteTypeInfo.from_json(json)
# print the JSON string representation of the object
print CompanyNoteTypeInfo.to_json()

# convert the object into a dict
company_note_type_info_dict = company_note_type_info_instance.to_dict()
# create an instance of CompanyNoteTypeInfo from a dict
company_note_type_info_form_dict = company_note_type_info.from_dict(company_note_type_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


