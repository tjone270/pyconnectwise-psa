# AdjustmentDetailReference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.adjustment_detail_reference import AdjustmentDetailReference

# TODO update the JSON string below
json = "{}"
# create an instance of AdjustmentDetailReference from a JSON string
adjustment_detail_reference_instance = AdjustmentDetailReference.from_json(json)
# print the JSON string representation of the object
print AdjustmentDetailReference.to_json()

# convert the object into a dict
adjustment_detail_reference_dict = adjustment_detail_reference_instance.to_dict()
# create an instance of AdjustmentDetailReference from a dict
adjustment_detail_reference_form_dict = adjustment_detail_reference.from_dict(adjustment_detail_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


