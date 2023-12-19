# ActivityStopwatch


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**activity_id** | **int** |  | 
**activity_mobile_guid** | **str** |  | [optional] 
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
**start_time** | **datetime** |  | [optional] 
**status** | **str** |  | 
**total_pause_time** | **int** |  | [optional] 
**work_role** | [**WorkRoleReference**](WorkRoleReference.md) |  | [optional] 
**work_type** | [**WorkTypeReference**](WorkTypeReference.md) |  | [optional] 

## Example

```python
from connectwise_psa.models.activity_stopwatch import ActivityStopwatch

# TODO update the JSON string below
json = "{}"
# create an instance of ActivityStopwatch from a JSON string
activity_stopwatch_instance = ActivityStopwatch.from_json(json)
# print the JSON string representation of the object
print ActivityStopwatch.to_json()

# convert the object into a dict
activity_stopwatch_dict = activity_stopwatch_instance.to_dict()
# create an instance of ActivityStopwatch from a dict
activity_stopwatch_form_dict = activity_stopwatch.from_dict(activity_stopwatch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


