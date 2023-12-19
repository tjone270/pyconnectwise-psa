# AdjustmentTypeInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.adjustment_type_info import AdjustmentTypeInfo

# TODO update the JSON string below
json = "{}"
# create an instance of AdjustmentTypeInfo from a JSON string
adjustment_type_info_instance = AdjustmentTypeInfo.from_json(json)
# print the JSON string representation of the object
print AdjustmentTypeInfo.to_json()

# convert the object into a dict
adjustment_type_info_dict = adjustment_type_info_instance.to_dict()
# create an instance of AdjustmentTypeInfo from a dict
adjustment_type_info_form_dict = adjustment_type_info.from_dict(adjustment_type_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


