# WarehouseBinReference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.warehouse_bin_reference import WarehouseBinReference

# TODO update the JSON string below
json = "{}"
# create an instance of WarehouseBinReference from a JSON string
warehouse_bin_reference_instance = WarehouseBinReference.from_json(json)
# print the JSON string representation of the object
print WarehouseBinReference.to_json()

# convert the object into a dict
warehouse_bin_reference_dict = warehouse_bin_reference_instance.to_dict()
# create an instance of WarehouseBinReference from a dict
warehouse_bin_reference_form_dict = warehouse_bin_reference.from_dict(warehouse_bin_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


