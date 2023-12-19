# CompanyCustomNote


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**company** | [**CompanyReference**](CompanyReference.md) |  | [optional] 
**custom_note** | **str** |  Max length: 1500; | 
**id** | **int** |  | [optional] 
**status** | [**CompanyStatusReference**](CompanyStatusReference.md) |  | [optional] 

## Example

```python
from connectwise_psa.models.company_custom_note import CompanyCustomNote

# TODO update the JSON string below
json = "{}"
# create an instance of CompanyCustomNote from a JSON string
company_custom_note_instance = CompanyCustomNote.from_json(json)
# print the JSON string representation of the object
print CompanyCustomNote.to_json()

# convert the object into a dict
company_custom_note_dict = company_custom_note_instance.to_dict()
# create an instance of CompanyCustomNote from a dict
company_custom_note_form_dict = company_custom_note.from_dict(company_custom_note_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


