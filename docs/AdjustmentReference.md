# AdjustmentReference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.adjustment_reference import AdjustmentReference

# TODO update the JSON string below
json = "{}"
# create an instance of AdjustmentReference from a JSON string
adjustment_reference_instance = AdjustmentReference.from_json(json)
# print the JSON string representation of the object
print AdjustmentReference.to_json()

# convert the object into a dict
adjustment_reference_dict = adjustment_reference_instance.to_dict()
# create an instance of AdjustmentReference from a dict
adjustment_reference_form_dict = adjustment_reference.from_dict(adjustment_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


