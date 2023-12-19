# ProductComponent


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**catalog_item** | [**CatalogItemReference**](CatalogItemReference.md) |  | [optional] 
**cost** | **float** |  | [optional] 
**hide_description_flag** | **bool** |  | [optional] 
**hide_extended_price_flag** | **bool** |  | [optional] 
**hide_item_identifier_flag** | **bool** |  | [optional] 
**hide_price_flag** | **bool** |  | [optional] 
**hide_quantity_flag** | **bool** |  | [optional] 
**id** | **int** |  | [optional] 
**parent_product_item** | [**ProductItemReference**](ProductItemReference.md) |  | [optional] 
**price** | **float** |  | [optional] 
**product_item** | [**ProductItemReference**](ProductItemReference.md) |  | [optional] 
**quantity** | **float** |  | 
**sequence_number** | **int** |  Required On Updates; | [optional] 
**vendor** | [**CompanyReference**](CompanyReference.md) |  | [optional] 

## Example

```python
from connectwise_psa.models.product_component import ProductComponent

# TODO update the JSON string below
json = "{}"
# create an instance of ProductComponent from a JSON string
product_component_instance = ProductComponent.from_json(json)
# print the JSON string representation of the object
print ProductComponent.to_json()

# convert the object into a dict
product_component_dict = product_component_instance.to_dict()
# create an instance of ProductComponent from a dict
product_component_form_dict = product_component.from_dict(product_component_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


