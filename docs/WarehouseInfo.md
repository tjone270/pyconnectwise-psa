# WarehouseInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**inactive_flag** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.warehouse_info import WarehouseInfo

# TODO update the JSON string below
json = "{}"
# create an instance of WarehouseInfo from a JSON string
warehouse_info_instance = WarehouseInfo.from_json(json)
# print the JSON string representation of the object
print WarehouseInfo.to_json()

# convert the object into a dict
warehouse_info_dict = warehouse_info_instance.to_dict()
# create an instance of WarehouseInfo from a dict
warehouse_info_form_dict = warehouse_info.from_dict(warehouse_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


