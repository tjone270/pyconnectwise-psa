# PhaseStatusReference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.phase_status_reference import PhaseStatusReference

# TODO update the JSON string below
json = "{}"
# create an instance of PhaseStatusReference from a JSON string
phase_status_reference_instance = PhaseStatusReference.from_json(json)
# print the JSON string representation of the object
print PhaseStatusReference.to_json()

# convert the object into a dict
phase_status_reference_dict = phase_status_reference_instance.to_dict()
# create an instance of PhaseStatusReference from a dict
phase_status_reference_form_dict = phase_status_reference.from_dict(phase_status_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


