# AdjustmentType


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**audit_trail_flag** | **bool** |  | [optional] 
**created_by** | **str** |  | [optional] 
**date_created** | **datetime** |  | [optional] 
**id** | **int** |  | [optional] 
**identifier** | **str** |  Max length: 50; | 
**name** | **str** |  Max length: 100; | [optional] 

## Example

```python
from connectwise_psa.models.adjustment_type import AdjustmentType

# TODO update the JSON string below
json = "{}"
# create an instance of AdjustmentType from a JSON string
adjustment_type_instance = AdjustmentType.from_json(json)
# print the JSON string representation of the object
print AdjustmentType.to_json()

# convert the object into a dict
adjustment_type_dict = adjustment_type_instance.to_dict()
# create an instance of AdjustmentType from a dict
adjustment_type_form_dict = adjustment_type.from_dict(adjustment_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


