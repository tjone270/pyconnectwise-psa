# Category


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**add_all_locations** | **bool** |  | [optional] 
**default_flag** | **bool** |  | [optional] 
**id** | **int** |  | [optional] 
**inactive_flag** | **bool** |  | [optional] 
**integration_xref** | **str** |  Max length: 50; | [optional] 
**location_ids** | **List[int]** |  | [optional] 
**name** | **str** |  Max length: 50; | 
**price_level_xref** | **str** |  Max length: 10; | [optional] 
**remove_all_locations** | **bool** |  | [optional] 

## Example

```python
from connectwise_psa.models.category import Category

# TODO update the JSON string below
json = "{}"
# create an instance of Category from a JSON string
category_instance = Category.from_json(json)
# print the JSON string representation of the object
print Category.to_json()

# convert the object into a dict
category_dict = category_instance.to_dict()
# create an instance of Category from a dict
category_form_dict = category.from_dict(category_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


