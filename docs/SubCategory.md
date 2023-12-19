# SubCategory


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**category** | [**ProductCategoryReference**](ProductCategoryReference.md) |  | 
**default_flag** | **bool** |  | [optional] 
**id** | **int** |  | [optional] 
**inactive_flag** | **bool** |  | [optional] 
**integration_xref** | **str** |  Max length: 50; | [optional] 
**name** | **str** |  Max length: 50; | 

## Example

```python
from connectwise_psa.models.sub_category import SubCategory

# TODO update the JSON string below
json = "{}"
# create an instance of SubCategory from a JSON string
sub_category_instance = SubCategory.from_json(json)
# print the JSON string representation of the object
print SubCategory.to_json()

# convert the object into a dict
sub_category_dict = sub_category_instance.to_dict()
# create an instance of SubCategory from a dict
sub_category_form_dict = sub_category.from_dict(sub_category_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


