# ProcurementSetting


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**auto_approve_purchase_order_flag** | **bool** |  | [optional] 
**auto_close_purchase_order_flag** | **bool** |  | [optional] 
**auto_close_purchase_order_item_flag** | **bool** |  | [optional] 
**costing_method** | **str** |  | 
**default_product_taxable_flag** | **bool** |  | [optional] 
**disable_auto_pick_flag** | **bool** |  | [optional] 
**disable_cost_updates_flag** | **bool** |  | [optional] 
**disable_negative_inventory_flag** | **bool** |  | [optional] 
**eori_number** | **str** |  Max length: 50; | [optional] 
**id** | **int** |  | [optional] 
**num_decimal_places** | **int** |  | [optional] 
**prefix_suffix_type** | **str** |  | [optional] 
**purchase_order_prefix** | **str** |  Max length: 5; | [optional] 
**purchase_order_suffix** | **str** |  Max length: 5; | [optional] 
**starting_purchase_order_num** | **int** |  | 
**tax_freight_flag** | **bool** |  | [optional] 
**tax_purchase_order_flag** | **bool** |  | [optional] 
**use_vendor_tax_code_flag** | **bool** |  | [optional] 

## Example

```python
from connectwise_psa.models.procurement_setting import ProcurementSetting

# TODO update the JSON string below
json = "{}"
# create an instance of ProcurementSetting from a JSON string
procurement_setting_instance = ProcurementSetting.from_json(json)
# print the JSON string representation of the object
print ProcurementSetting.to_json()

# convert the object into a dict
procurement_setting_dict = procurement_setting_instance.to_dict()
# create an instance of ProcurementSetting from a dict
procurement_setting_form_dict = procurement_setting.from_dict(procurement_setting_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


