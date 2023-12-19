# ProductDetach


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**remove_from_invoice** | **bool** |  | [optional] 
**remove_from_opportunity** | **bool** |  | [optional] 
**remove_from_project** | **bool** |  | [optional] 
**remove_from_sales_order** | **bool** |  | [optional] 
**remove_from_ticket** | **bool** |  | [optional] 

## Example

```python
from connectwise_psa.models.product_detach import ProductDetach

# TODO update the JSON string below
json = "{}"
# create an instance of ProductDetach from a JSON string
product_detach_instance = ProductDetach.from_json(json)
# print the JSON string representation of the object
print ProductDetach.to_json()

# convert the object into a dict
product_detach_dict = product_detach_instance.to_dict()
# create an instance of ProductDetach from a dict
product_detach_form_dict = product_detach.from_dict(product_detach_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


