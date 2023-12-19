# ProductSubCategoryReference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.product_sub_category_reference import ProductSubCategoryReference

# TODO update the JSON string below
json = "{}"
# create an instance of ProductSubCategoryReference from a JSON string
product_sub_category_reference_instance = ProductSubCategoryReference.from_json(json)
# print the JSON string representation of the object
print ProductSubCategoryReference.to_json()

# convert the object into a dict
product_sub_category_reference_dict = product_sub_category_reference_instance.to_dict()
# create an instance of ProductSubCategoryReference from a dict
product_sub_category_reference_form_dict = product_sub_category_reference.from_dict(product_sub_category_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


