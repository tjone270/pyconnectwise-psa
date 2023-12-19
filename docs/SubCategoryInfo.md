# SubCategoryInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**category** | [**ProductCategoryReference**](ProductCategoryReference.md) |  | [optional] 
**id** | **int** |  | [optional] 
**inactive_flag** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.sub_category_info import SubCategoryInfo

# TODO update the JSON string below
json = "{}"
# create an instance of SubCategoryInfo from a JSON string
sub_category_info_instance = SubCategoryInfo.from_json(json)
# print the JSON string representation of the object
print SubCategoryInfo.to_json()

# convert the object into a dict
sub_category_info_dict = sub_category_info_instance.to_dict()
# create an instance of SubCategoryInfo from a dict
sub_category_info_form_dict = sub_category_info.from_dict(sub_category_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


