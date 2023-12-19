# CorporateStructureLevelReference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.corporate_structure_level_reference import CorporateStructureLevelReference

# TODO update the JSON string below
json = "{}"
# create an instance of CorporateStructureLevelReference from a JSON string
corporate_structure_level_reference_instance = CorporateStructureLevelReference.from_json(json)
# print the JSON string representation of the object
print CorporateStructureLevelReference.to_json()

# convert the object into a dict
corporate_structure_level_reference_dict = corporate_structure_level_reference_instance.to_dict()
# create an instance of CorporateStructureLevelReference from a dict
corporate_structure_level_reference_form_dict = corporate_structure_level_reference.from_dict(corporate_structure_level_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


