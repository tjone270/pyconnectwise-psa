# CatalogItemInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**billable_option** | **str** |  | [optional] 
**cost** | **float** |  | [optional] 
**customer_description** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**drop_ship_flag** | **bool** |  | [optional] 
**id** | **int** |  | [optional] 
**identifier** | **str** |  | [optional] 
**inactive_flag** | **bool** |  | [optional] 
**manufacturer_part_number** | **str** |  | [optional] 
**price** | **float** |  | [optional] 
**product_class** | **str** |  | [optional] 
**serialized_cost_flag** | **bool** |  | [optional] 
**special_order_flag** | **bool** |  | [optional] 
**taxable_flag** | **bool** |  | [optional] 
**vendor_sku** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.catalog_item_info import CatalogItemInfo

# TODO update the JSON string below
json = "{}"
# create an instance of CatalogItemInfo from a JSON string
catalog_item_info_instance = CatalogItemInfo.from_json(json)
# print the JSON string representation of the object
print CatalogItemInfo.to_json()

# convert the object into a dict
catalog_item_info_dict = catalog_item_info_instance.to_dict()
# create an instance of CatalogItemInfo from a dict
catalog_item_info_form_dict = catalog_item_info.from_dict(catalog_item_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


