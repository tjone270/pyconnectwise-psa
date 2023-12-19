# CorporateStructure


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**base_currency** | [**CurrencyReference**](CurrencyReference.md) |  | 
**chief_operating_officer** | [**MemberReference**](MemberReference.md) |  | [optional] 
**controller** | [**MemberReference**](MemberReference.md) |  | [optional] 
**dispatcher** | [**MemberReference**](MemberReference.md) |  | [optional] 
**duty_manager** | [**MemberReference**](MemberReference.md) |  | [optional] 
**fiscal_year_start** | **str** |  | 
**group_caption** | **str** |  Max length: 50; | 
**id** | **int** |  | [optional] 
**level1_name** | **str** |  Max length: 20; | [optional] 
**level2_name** | **str** |  Max length: 20; | [optional] 
**level3_name** | **str** |  Max length: 20; | [optional] 
**level4_name** | **str** |  Max length: 20; | [optional] 
**level5_name** | **str** |  Max length: 20; | [optional] 
**level_count** | **str** |  | [optional] 
**location_caption** | **str** |  Max length: 50; | 
**president** | [**MemberReference**](MemberReference.md) |  | [optional] 
**service_manager** | [**MemberReference**](MemberReference.md) |  | [optional] 

## Example

```python
from connectwise_psa.models.corporate_structure import CorporateStructure

# TODO update the JSON string below
json = "{}"
# create an instance of CorporateStructure from a JSON string
corporate_structure_instance = CorporateStructure.from_json(json)
# print the JSON string representation of the object
print CorporateStructure.to_json()

# convert the object into a dict
corporate_structure_dict = corporate_structure_instance.to_dict()
# create an instance of CorporateStructure from a dict
corporate_structure_form_dict = corporate_structure.from_dict(corporate_structure_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


