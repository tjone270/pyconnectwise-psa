# AdjustmentTypeReference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**identifier** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.adjustment_type_reference import AdjustmentTypeReference

# TODO update the JSON string below
json = "{}"
# create an instance of AdjustmentTypeReference from a JSON string
adjustment_type_reference_instance = AdjustmentTypeReference.from_json(json)
# print the JSON string representation of the object
print AdjustmentTypeReference.to_json()

# convert the object into a dict
adjustment_type_reference_dict = adjustment_type_reference_instance.to_dict()
# create an instance of AdjustmentTypeReference from a dict
adjustment_type_reference_form_dict = adjustment_type_reference.from_dict(adjustment_type_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


