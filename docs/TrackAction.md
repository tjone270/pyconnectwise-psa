# TrackAction


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**activity_status** | [**ActivityStatusReference**](ActivityStatusReference.md) |  | [optional] 
**activity_type** | [**ActivityTypeReference**](ActivityTypeReference.md) |  | [optional] 
**attached_track** | [**TrackReference**](TrackReference.md) |  | [optional] 
**bcc_contact** | [**ContactReference**](ContactReference.md) |  | [optional] 
**cc_contact** | [**ContactReference**](ContactReference.md) |  | [optional] 
**company_status** | [**CompanyStatusReference**](CompanyStatusReference.md) |  | [optional] 
**days_to_execute** | **int** |  | [optional] 
**email_from** | **str** |  Max length: 250; | [optional] 
**email_recipient** | **str** |  Max length: 250; | [optional] 
**group** | [**GroupReference**](GroupReference.md) |  | [optional] 
**id** | **int** |  | [optional] 
**notes** | **str** |  | [optional] 
**notify_from** | [**NotificationRecipientReference**](NotificationRecipientReference.md) |  | [optional] 
**notify_type** | **str** |  | 
**notify_who** | [**NotificationRecipientReference**](NotificationRecipientReference.md) |  | [optional] 
**service_template** | [**ServiceTemplateReference**](ServiceTemplateReference.md) |  | [optional] 
**specific_member_from** | [**MemberReference**](MemberReference.md) |  | [optional] 
**specific_member_to** | [**MemberReference**](MemberReference.md) |  | [optional] 
**subject** | **str** |  Max length: 100; | [optional] 
**track** | [**TrackReference**](TrackReference.md) |  | [optional] 

## Example

```python
from connectwise_psa.models.track_action import TrackAction

# TODO update the JSON string below
json = "{}"
# create an instance of TrackAction from a JSON string
track_action_instance = TrackAction.from_json(json)
# print the JSON string representation of the object
print TrackAction.to_json()

# convert the object into a dict
track_action_dict = track_action_instance.to_dict()
# create an instance of TrackAction from a dict
track_action_form_dict = track_action.from_dict(track_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


