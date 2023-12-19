# Activity


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**agreement** | [**AgreementReference**](AgreementReference.md) |  | [optional] 
**assign_to** | [**MemberReference**](MemberReference.md) |  | [optional] 
**assigned_by** | [**MemberReference**](MemberReference.md) |  | [optional] 
**campaign** | [**CampaignReference**](CampaignReference.md) |  | [optional] 
**company** | [**CompanyReference**](CompanyReference.md) |  | [optional] 
**contact** | [**ContactReference**](ContactReference.md) |  | [optional] 
**currency** | [**CurrencyReference**](CurrencyReference.md) |  | [optional] 
**custom_fields** | [**List[CustomFieldValue]**](CustomFieldValue.md) |  | [optional] 
**date_end** | **datetime** |  | [optional] 
**date_start** | **datetime** |  | [optional] 
**email** | **str** |  Max length: 250; | [optional] 
**id** | **int** |  | [optional] 
**mobile_guid** | **str** |  | [optional] 
**name** | **str** |  Max length: 100; | 
**notes** | **str** |  | [optional] 
**notify_flag** | **bool** |  | [optional] 
**opportunity** | [**OpportunityReference**](OpportunityReference.md) |  | [optional] 
**phone_number** | **str** |  Max length: 30; | [optional] 
**reminder** | [**ReminderReference**](ReminderReference.md) |  | [optional] 
**schedule_status** | [**ScheduleStatusReference**](ScheduleStatusReference.md) |  | [optional] 
**status** | [**ActivityStatusReference**](ActivityStatusReference.md) |  | [optional] 
**ticket** | [**TicketReference**](TicketReference.md) |  | [optional] 
**type** | [**ActivityTypeReference**](ActivityTypeReference.md) |  | [optional] 
**where** | [**ServiceLocationReference**](ServiceLocationReference.md) |  | [optional] 

## Example

```python
from connectwise_psa.models.activity import Activity

# TODO update the JSON string below
json = "{}"
# create an instance of Activity from a JSON string
activity_instance = Activity.from_json(json)
# print the JSON string representation of the object
print Activity.to_json()

# convert the object into a dict
activity_dict = activity_instance.to_dict()
# create an instance of Activity from a dict
activity_form_dict = activity.from_dict(activity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


