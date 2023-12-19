# PurchasingDemand


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**products** | [**List[ProductDemand]**](ProductDemand.md) |  | [optional] 
**purchase_order** | [**PurchaseOrder**](PurchaseOrder.md) |  | [optional] 
**vendor** | [**CompanyReference**](CompanyReference.md) |  | [optional] 
**warehouse** | [**WarehouseReference**](WarehouseReference.md) |  | [optional] 

## Example

```python
from connectwise_psa.models.purchasing_demand import PurchasingDemand

# TODO update the JSON string below
json = "{}"
# create an instance of PurchasingDemand from a JSON string
purchasing_demand_instance = PurchasingDemand.from_json(json)
# print the JSON string representation of the object
print PurchasingDemand.to_json()

# convert the object into a dict
purchasing_demand_dict = purchasing_demand_instance.to_dict()
# create an instance of PurchasingDemand from a dict
purchasing_demand_form_dict = purchasing_demand.from_dict(purchasing_demand_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


