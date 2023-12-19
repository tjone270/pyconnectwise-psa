# MinimumStockByWarehouse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**minimum_stock** | **int** |  | 
**warehouse** | [**WarehouseReference**](WarehouseReference.md) |  | 

## Example

```python
from connectwise_psa.models.minimum_stock_by_warehouse import MinimumStockByWarehouse

# TODO update the JSON string below
json = "{}"
# create an instance of MinimumStockByWarehouse from a JSON string
minimum_stock_by_warehouse_instance = MinimumStockByWarehouse.from_json(json)
# print the JSON string representation of the object
print MinimumStockByWarehouse.to_json()

# convert the object into a dict
minimum_stock_by_warehouse_dict = minimum_stock_by_warehouse_instance.to_dict()
# create an instance of MinimumStockByWarehouse from a dict
minimum_stock_by_warehouse_form_dict = minimum_stock_by_warehouse.from_dict(minimum_stock_by_warehouse_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


