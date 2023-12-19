# ProductCategoryReference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.product_category_reference import ProductCategoryReference

# TODO update the JSON string below
json = "{}"
# create an instance of ProductCategoryReference from a JSON string
product_category_reference_instance = ProductCategoryReference.from_json(json)
# print the JSON string representation of the object
print ProductCategoryReference.to_json()

# convert the object into a dict
product_category_reference_dict = product_category_reference_instance.to_dict()
# create an instance of ProductCategoryReference from a dict
product_category_reference_form_dict = product_category_reference.from_dict(product_category_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


