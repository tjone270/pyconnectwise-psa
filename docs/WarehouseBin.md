# WarehouseBin


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**company** | [**CompanyReference**](CompanyReference.md) |  | [optional] 
**default_flag** | **bool** |  | [optional] 
**department** | [**SystemDepartmentReference**](SystemDepartmentReference.md) |  | [optional] 
**height** | **float** |  | [optional] 
**id** | **int** |  | [optional] 
**inactive_flag** | **bool** |  | [optional] 
**length** | **float** |  | [optional] 
**location** | [**SystemLocationReference**](SystemLocationReference.md) |  | [optional] 
**manager** | [**MemberReference**](MemberReference.md) |  | [optional] 
**max_quantity** | **float** |  | [optional] 
**min_quantity** | **float** |  | [optional] 
**name** | **str** |  Max length: 50; | 
**overflow_bin** | [**WarehouseBinReference**](WarehouseBinReference.md) |  | [optional] 
**quantity_on_hand** | **int** |  | [optional] 
**transfer_bin** | [**WarehouseBinReference**](WarehouseBinReference.md) |  | [optional] 
**warehouse** | [**WarehouseReference**](WarehouseReference.md) |  | [optional] 
**weight** | **float** |  | [optional] 
**width** | **float** |  | [optional] 

## Example

```python
from connectwise_psa.models.warehouse_bin import WarehouseBin

# TODO update the JSON string below
json = "{}"
# create an instance of WarehouseBin from a JSON string
warehouse_bin_instance = WarehouseBin.from_json(json)
# print the JSON string representation of the object
print WarehouseBin.to_json()

# convert the object into a dict
warehouse_bin_dict = warehouse_bin_instance.to_dict()
# create an instance of WarehouseBin from a dict
warehouse_bin_form_dict = warehouse_bin.from_dict(warehouse_bin_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


