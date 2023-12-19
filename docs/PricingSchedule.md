# PricingSchedule


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**companies** | **List[int]** |  | [optional] 
**currency** | [**CurrencyReference**](CurrencyReference.md) |  | [optional] 
**default_flag** | **bool** |  | [optional] 
**id** | **int** |  | [optional] 
**inactive_flag** | **bool** |  | [optional] 
**name** | **str** |  Max length: 30; | 
**remove_all_companies_flag** | **bool** |  | [optional] 
**set_all_companies_flag** | **bool** |  | [optional] 

## Example

```python
from connectwise_psa.models.pricing_schedule import PricingSchedule

# TODO update the JSON string below
json = "{}"
# create an instance of PricingSchedule from a JSON string
pricing_schedule_instance = PricingSchedule.from_json(json)
# print the JSON string representation of the object
print PricingSchedule.to_json()

# convert the object into a dict
pricing_schedule_dict = pricing_schedule_instance.to_dict()
# create an instance of PricingSchedule from a dict
pricing_schedule_form_dict = pricing_schedule.from_dict(pricing_schedule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


