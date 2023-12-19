# AdjustmentDetail


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**adjustment** | [**AdjustmentReference**](AdjustmentReference.md) |  | [optional] 
**catalog_item** | [**CatalogItemReference**](CatalogItemReference.md) |  | [optional] 
**description** | **str** |  Max length: 50; | [optional] 
**id** | **int** |  | [optional] 
**quantity_adjusted** | **int** |  | 
**quantity_on_hand** | **float** |  | [optional] 
**serial_number** | **str** |  Max length: 1000; | [optional] 
**unit_cost** | **float** |  | [optional] 
**warehouse** | [**WarehouseReference**](WarehouseReference.md) |  | [optional] 
**warehouse_bin** | [**WarehouseBinReference**](WarehouseBinReference.md) |  | [optional] 

## Example

```python
from connectwise_psa.models.adjustment_detail import AdjustmentDetail

# TODO update the JSON string below
json = "{}"
# create an instance of AdjustmentDetail from a JSON string
adjustment_detail_instance = AdjustmentDetail.from_json(json)
# print the JSON string representation of the object
print AdjustmentDetail.to_json()

# convert the object into a dict
adjustment_detail_dict = adjustment_detail_instance.to_dict()
# create an instance of AdjustmentDetail from a dict
adjustment_detail_form_dict = adjustment_detail.from_dict(adjustment_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


