# CatalogComponent


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
**parent_catalog_item** | [**CatalogItemReference**](CatalogItemReference.md) |  | [optional] 
**price** | **float** |  | [optional] 
**quantity** | **float** |  | 
**sequence_number** | **int** |  | [optional] 

## Example

```python
from connectwise_psa.models.catalog_component import CatalogComponent

# TODO update the JSON string below
json = "{}"
# create an instance of CatalogComponent from a JSON string
catalog_component_instance = CatalogComponent.from_json(json)
# print the JSON string representation of the object
print CatalogComponent.to_json()

# convert the object into a dict
catalog_component_dict = catalog_component_instance.to_dict()
# create an instance of CatalogComponent from a dict
catalog_component_form_dict = catalog_component.from_dict(catalog_component_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


