# ProductTypeExemption


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**product_type** | [**ProductTypeReference**](ProductTypeReference.md) |  | 
**taxable_levels** | **List[int]** |  | [optional] 

## Example

```python
from connectwise_psa.models.product_type_exemption import ProductTypeExemption

# TODO update the JSON string below
json = "{}"
# create an instance of ProductTypeExemption from a JSON string
product_type_exemption_instance = ProductTypeExemption.from_json(json)
# print the JSON string representation of the object
print ProductTypeExemption.to_json()

# convert the object into a dict
product_type_exemption_dict = product_type_exemption_instance.to_dict()
# create an instance of ProductTypeExemption from a dict
product_type_exemption_form_dict = product_type_exemption.from_dict(product_type_exemption_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


