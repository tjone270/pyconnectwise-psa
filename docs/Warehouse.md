# Warehouse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**company** | [**CompanyReference**](CompanyReference.md) |  | [optional] 
**contact** | [**ContactReference**](ContactReference.md) |  | [optional] 
**currency** | [**CurrencyReference**](CurrencyReference.md) |  | [optional] 
**department** | [**SystemDepartmentReference**](SystemDepartmentReference.md) |  | [optional] 
**id** | **int** |  | [optional] 
**inactive_flag** | **bool** |  | [optional] 
**location** | [**SystemLocationReference**](SystemLocationReference.md) |  | [optional] 
**location_default_flag** | **bool** |  | [optional] 
**location_xref** | **str** |  Max length: 10; | [optional] 
**locked_flag** | **bool** |  | [optional] 
**manager** | [**MemberReference**](MemberReference.md) |  | [optional] 
**name** | **str** |  Max length: 50; | 
**overall_default_flag** | **bool** |  | [optional] 
**site** | [**SiteReference**](SiteReference.md) |  | [optional] 

## Example

```python
from connectwise_psa.models.warehouse import Warehouse

# TODO update the JSON string below
json = "{}"
# create an instance of Warehouse from a JSON string
warehouse_instance = Warehouse.from_json(json)
# print the JSON string representation of the object
print Warehouse.to_json()

# convert the object into a dict
warehouse_dict = warehouse_instance.to_dict()
# create an instance of Warehouse from a dict
warehouse_form_dict = warehouse.from_dict(warehouse_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


