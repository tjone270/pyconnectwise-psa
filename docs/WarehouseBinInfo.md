# WarehouseBinInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**default_flag** | **bool** |  | [optional] 
**id** | **int** |  | [optional] 
**inactive_flag** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**warehouse** | [**WarehouseReference**](WarehouseReference.md) |  | [optional] 

## Example

```python
from connectwise_psa.models.warehouse_bin_info import WarehouseBinInfo

# TODO update the JSON string below
json = "{}"
# create an instance of WarehouseBinInfo from a JSON string
warehouse_bin_info_instance = WarehouseBinInfo.from_json(json)
# print the JSON string representation of the object
print WarehouseBinInfo.to_json()

# convert the object into a dict
warehouse_bin_info_dict = warehouse_bin_info_instance.to_dict()
# create an instance of WarehouseBinInfo from a dict
warehouse_bin_info_form_dict = warehouse_bin_info.from_dict(warehouse_bin_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


