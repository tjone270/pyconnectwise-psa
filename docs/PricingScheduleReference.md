# PricingScheduleReference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.pricing_schedule_reference import PricingScheduleReference

# TODO update the JSON string below
json = "{}"
# create an instance of PricingScheduleReference from a JSON string
pricing_schedule_reference_instance = PricingScheduleReference.from_json(json)
# print the JSON string representation of the object
print PricingScheduleReference.to_json()

# convert the object into a dict
pricing_schedule_reference_dict = pricing_schedule_reference_instance.to_dict()
# create an instance of PricingScheduleReference from a dict
pricing_schedule_reference_form_dict = pricing_schedule_reference.from_dict(pricing_schedule_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


