# ScheduleStopwatch


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**agreement** | [**AgreementReference**](AgreementReference.md) |  | [optional] 
**billable_option** | **str** |  | [optional] 
**business_unit_id** | **int** |  | [optional] 
**date_entered** | **datetime** |  | [optional] 
**end_time** | **datetime** |  | [optional] 
**id** | **int** |  | [optional] 
**internal_notes** | **str** |  | [optional] 
**location_id** | **int** |  | [optional] 
**member** | [**MemberReference**](MemberReference.md) |  | [optional] 
**mobile_guid** | **str** |  | [optional] 
**notes** | **str** |  Max length: 4000; | [optional] 
**schedule_id** | **int** |  | 
**schedule_mobile_guid** | **str** |  | [optional] 
**start_time** | **datetime** |  | [optional] 
**status** | **str** |  | 
**total_pause_time** | **int** |  | [optional] 
**work_role** | [**WorkRoleReference**](WorkRoleReference.md) |  | [optional] 
**work_type** | [**WorkTypeReference**](WorkTypeReference.md) |  | [optional] 

## Example

```python
from connectwise_psa.models.schedule_stopwatch import ScheduleStopwatch

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduleStopwatch from a JSON string
schedule_stopwatch_instance = ScheduleStopwatch.from_json(json)
# print the JSON string representation of the object
print ScheduleStopwatch.to_json()

# convert the object into a dict
schedule_stopwatch_dict = schedule_stopwatch_instance.to_dict()
# create an instance of ScheduleStopwatch from a dict
schedule_stopwatch_form_dict = schedule_stopwatch.from_dict(schedule_stopwatch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


