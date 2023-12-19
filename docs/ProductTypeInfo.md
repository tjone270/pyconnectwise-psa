# ProductTypeInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**inactive_flag** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.product_type_info import ProductTypeInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ProductTypeInfo from a JSON string
product_type_info_instance = ProductTypeInfo.from_json(json)
# print the JSON string representation of the object
print ProductTypeInfo.to_json()

# convert the object into a dict
product_type_info_dict = product_type_info_instance.to_dict()
# create an instance of ProductTypeInfo from a dict
product_type_info_form_dict = product_type_info.from_dict(product_type_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


