# CorporateStructureInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**base_currency** | [**CurrencyReference**](CurrencyReference.md) |  | [optional] 
**group_caption** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**location_caption** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.corporate_structure_info import CorporateStructureInfo

# TODO update the JSON string below
json = "{}"
# create an instance of CorporateStructureInfo from a JSON string
corporate_structure_info_instance = CorporateStructureInfo.from_json(json)
# print the JSON string representation of the object
print CorporateStructureInfo.to_json()

# convert the object into a dict
corporate_structure_info_dict = corporate_structure_info_instance.to_dict()
# create an instance of CorporateStructureInfo from a dict
corporate_structure_info_form_dict = corporate_structure_info.from_dict(corporate_structure_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


