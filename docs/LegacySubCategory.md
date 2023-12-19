# LegacySubCategory


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**inactive_flag** | **bool** |  | [optional] 
**name** | **str** |  Max length: 50; | 

## Example

```python
from connectwise_psa.models.legacy_sub_category import LegacySubCategory

# TODO update the JSON string below
json = "{}"
# create an instance of LegacySubCategory from a JSON string
legacy_sub_category_instance = LegacySubCategory.from_json(json)
# print the JSON string representation of the object
print LegacySubCategory.to_json()

# convert the object into a dict
legacy_sub_category_dict = legacy_sub_category_instance.to_dict()
# create an instance of LegacySubCategory from a dict
legacy_sub_category_form_dict = legacy_sub_category.from_dict(legacy_sub_category_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


