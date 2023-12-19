# WarehouseReference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**locked_flag** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.warehouse_reference import WarehouseReference

# TODO update the JSON string below
json = "{}"
# create an instance of WarehouseReference from a JSON string
warehouse_reference_instance = WarehouseReference.from_json(json)
# print the JSON string representation of the object
print WarehouseReference.to_json()

# convert the object into a dict
warehouse_reference_dict = warehouse_reference_instance.to_dict()
# create an instance of WarehouseReference from a dict
warehouse_reference_form_dict = warehouse_reference.from_dict(warehouse_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


