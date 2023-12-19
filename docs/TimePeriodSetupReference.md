# TimePeriodSetupReference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 

## Example

```python
from connectwise_psa.models.time_period_setup_reference import TimePeriodSetupReference

# TODO update the JSON string below
json = "{}"
# create an instance of TimePeriodSetupReference from a JSON string
time_period_setup_reference_instance = TimePeriodSetupReference.from_json(json)
# print the JSON string representation of the object
print TimePeriodSetupReference.to_json()

# convert the object into a dict
time_period_setup_reference_dict = time_period_setup_reference_instance.to_dict()
# create an instance of TimePeriodSetupReference from a dict
time_period_setup_reference_form_dict = time_period_setup_reference.from_dict(time_period_setup_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


