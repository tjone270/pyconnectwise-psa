# ProcurementAdjustment


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**adjustment_details** | [**List[AdjustmentDetail]**](AdjustmentDetail.md) |  | [optional] 
**closed_by** | **str** |  | [optional] 
**closed_date** | **datetime** |  | [optional] 
**closed_flag** | **bool** |  | [optional] 
**id** | **int** |  | [optional] 
**identifier** | **str** |  Max length: 50; | 
**notes** | **str** |  | [optional] 
**reason** | **str** |  Max length: 100; | [optional] 
**type** | [**AdjustmentTypeReference**](AdjustmentTypeReference.md) |  | [optional] 

## Example

```python
from connectwise_psa.models.procurement_adjustment import ProcurementAdjustment

# TODO update the JSON string below
json = "{}"
# create an instance of ProcurementAdjustment from a JSON string
procurement_adjustment_instance = ProcurementAdjustment.from_json(json)
# print the JSON string representation of the object
print ProcurementAdjustment.to_json()

# convert the object into a dict
procurement_adjustment_dict = procurement_adjustment_instance.to_dict()
# create an instance of ProcurementAdjustment from a dict
procurement_adjustment_form_dict = procurement_adjustment.from_dict(procurement_adjustment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


