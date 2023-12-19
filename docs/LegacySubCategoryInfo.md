# LegacySubCategoryInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**inactive_flag** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.legacy_sub_category_info import LegacySubCategoryInfo

# TODO update the JSON string below
json = "{}"
# create an instance of LegacySubCategoryInfo from a JSON string
legacy_sub_category_info_instance = LegacySubCategoryInfo.from_json(json)
# print the JSON string representation of the object
print LegacySubCategoryInfo.to_json()

# convert the object into a dict
legacy_sub_category_info_dict = legacy_sub_category_info_instance.to_dict()
# create an instance of LegacySubCategoryInfo from a dict
legacy_sub_category_info_form_dict = legacy_sub_category_info.from_dict(legacy_sub_category_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


