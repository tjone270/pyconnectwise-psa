# TimeAccrualReference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.time_accrual_reference import TimeAccrualReference

# TODO update the JSON string below
json = "{}"
# create an instance of TimeAccrualReference from a JSON string
time_accrual_reference_instance = TimeAccrualReference.from_json(json)
# print the JSON string representation of the object
print TimeAccrualReference.to_json()

# convert the object into a dict
time_accrual_reference_dict = time_accrual_reference_instance.to_dict()
# create an instance of TimeAccrualReference from a dict
time_accrual_reference_form_dict = time_accrual_reference.from_dict(time_accrual_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


