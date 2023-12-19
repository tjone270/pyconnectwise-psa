# CorporateStructureLevel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.corporate_structure_level import CorporateStructureLevel

# TODO update the JSON string below
json = "{}"
# create an instance of CorporateStructureLevel from a JSON string
corporate_structure_level_instance = CorporateStructureLevel.from_json(json)
# print the JSON string representation of the object
print CorporateStructureLevel.to_json()

# convert the object into a dict
corporate_structure_level_dict = corporate_structure_level_instance.to_dict()
# create an instance of CorporateStructureLevel from a dict
corporate_structure_level_form_dict = corporate_structure_level.from_dict(corporate_structure_level_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


