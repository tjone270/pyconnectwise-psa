# PhaseStatus


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**board_association_ids** | **List[int]** |  | [optional] 
**closed_flag** | **bool** |  | [optional] 
**collapsed_flag** | **bool** |  | [optional] 
**custom_status_indicator_name** | **str** | Required when statusIndicator is Custom. Max length: 30; | [optional] 
**default_flag** | **bool** |  | [optional] 
**id** | **int** |  | [optional] 
**inactive_flag** | **bool** |  | [optional] 
**name** | **str** |  Max length: 30; | 
**status_indicator** | [**StatusIndicatorReference**](StatusIndicatorReference.md) |  | [optional] 

## Example

```python
from connectwise_psa.models.phase_status import PhaseStatus

# TODO update the JSON string below
json = "{}"
# create an instance of PhaseStatus from a JSON string
phase_status_instance = PhaseStatus.from_json(json)
# print the JSON string representation of the object
print PhaseStatus.to_json()

# convert the object into a dict
phase_status_dict = phase_status_instance.to_dict()
# create an instance of PhaseStatus from a dict
phase_status_form_dict = phase_status.from_dict(phase_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


