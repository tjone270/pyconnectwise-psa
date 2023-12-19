# OnHandSerialNumber


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**catalog_item** | [**CatalogItemReference**](CatalogItemReference.md) |  | [optional] 
**id** | **int** |  | [optional] 
**serial** | **str** |  | [optional] 
**warehouse** | [**WarehouseReference**](WarehouseReference.md) |  | [optional] 
**warehouse_bin** | [**WarehouseBinReference**](WarehouseBinReference.md) |  | [optional] 

## Example

```python
from connectwise_psa.models.on_hand_serial_number import OnHandSerialNumber

# TODO update the JSON string below
json = "{}"
# create an instance of OnHandSerialNumber from a JSON string
on_hand_serial_number_instance = OnHandSerialNumber.from_json(json)
# print the JSON string representation of the object
print OnHandSerialNumber.to_json()

# convert the object into a dict
on_hand_serial_number_dict = on_hand_serial_number_instance.to_dict()
# create an instance of OnHandSerialNumber from a dict
on_hand_serial_number_form_dict = on_hand_serial_number.from_dict(on_hand_serial_number_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


