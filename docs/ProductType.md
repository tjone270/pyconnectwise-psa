# ProductType


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**default_flag** | **bool** |  | [optional] 
**id** | **int** |  | [optional] 
**inactive_flag** | **bool** |  | [optional] 
**name** | **str** |  Max length: 50; | 
**type_xref** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.product_type import ProductType

# TODO update the JSON string below
json = "{}"
# create an instance of ProductType from a JSON string
product_type_instance = ProductType.from_json(json)
# print the JSON string representation of the object
print ProductType.to_json()

# convert the object into a dict
product_type_dict = product_type_instance.to_dict()
# create an instance of ProductType from a dict
product_type_form_dict = product_type.from_dict(product_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


