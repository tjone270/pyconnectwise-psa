# CatalogItem


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**billable_option** | **str** |  | [optional] 
**calculated_cost** | **float** |  | [optional] 
**calculated_cost_flag** | **bool** |  | [optional] 
**calculated_price** | **float** |  | [optional] 
**calculated_price_flag** | **bool** |  | [optional] 
**category** | [**ProductCategoryReference**](ProductCategoryReference.md) |  | [optional] 
**cost** | **float** |  | [optional] 
**custom_fields** | [**List[CustomFieldValue]**](CustomFieldValue.md) |  | [optional] 
**customer_description** | **str** |  Max length: 6000; | 
**date_entered** | **str** |  | [optional] 
**description** | **str** |  Max length: 60; | 
**drop_ship_flag** | **bool** |  | [optional] 
**entity_type** | [**EntityTypeReference**](EntityTypeReference.md) |  | [optional] 
**id** | **int** |  | [optional] 
**identifier** | **str** |  Max length: 60; | 
**inactive_flag** | **bool** |  | [optional] 
**integration_x_ref** | **str** |  Max length: 50; | [optional] 
**manufacturer** | [**ManufacturerReference**](ManufacturerReference.md) |  | [optional] 
**manufacturer_part_number** | **str** |  Max length: 50; | [optional] 
**min_stock_level** | **int** |  | [optional] 
**notes** | **str** |  | [optional] 
**phase_product_flag** | **bool** |  | [optional] 
**price** | **float** |  | [optional] 
**price_attribute** | **str** |  | [optional] 
**product_class** | **str** | Defaults to Non-Inventory. | [optional] 
**recurring_bill_cycle** | [**BillingCycleReference**](BillingCycleReference.md) |  | [optional] 
**recurring_cost** | **float** |  | [optional] 
**recurring_cycle_type** | **str** |  | [optional] 
**recurring_flag** | **bool** |  | [optional] 
**recurring_one_time_flag** | **bool** |  | [optional] 
**recurring_revenue** | **float** |  | [optional] 
**serialized_cost_flag** | **bool** |  | [optional] 
**serialized_flag** | **bool** |  | [optional] 
**sla** | [**SLAReference**](SLAReference.md) |  | [optional] 
**special_order_flag** | **bool** |  | [optional] 
**subcategory** | [**ProductSubCategoryReference**](ProductSubCategoryReference.md) |  | [optional] 
**taxable_flag** | **bool** |  | [optional] 
**type** | [**ProductTypeReference**](ProductTypeReference.md) |  | [optional] 
**unit_of_measure** | [**UnitOfMeasureReference**](UnitOfMeasureReference.md) |  | [optional] 
**vendor** | [**CompanyReference**](CompanyReference.md) |  | [optional] 
**vendor_sku** | **str** |  Max length: 50; | [optional] 

## Example

```python
from connectwise_psa.models.catalog_item import CatalogItem

# TODO update the JSON string below
json = "{}"
# create an instance of CatalogItem from a JSON string
catalog_item_instance = CatalogItem.from_json(json)
# print the JSON string representation of the object
print CatalogItem.to_json()

# convert the object into a dict
catalog_item_dict = catalog_item_instance.to_dict()
# create an instance of CatalogItem from a dict
catalog_item_form_dict = catalog_item.from_dict(catalog_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


