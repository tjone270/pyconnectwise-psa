# ManagementReportNotification


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**company** | [**CompanyReference**](CompanyReference.md) |  | [optional] 
**email** | **str** |  Max length: 50; | [optional] 
**global_flag** | **bool** |  | [optional] 
**id** | **int** |  | [optional] 
**member** | [**MemberReference**](MemberReference.md) |  | [optional] 
**notify_who** | [**NotificationRecipientReference**](NotificationRecipientReference.md) |  | [optional] 

## Example

```python
from connectwise_psa.models.management_report_notification import ManagementReportNotification

# TODO update the JSON string below
json = "{}"
# create an instance of ManagementReportNotification from a JSON string
management_report_notification_instance = ManagementReportNotification.from_json(json)
# print the JSON string representation of the object
print ManagementReportNotification.to_json()

# convert the object into a dict
management_report_notification_dict = management_report_notification_instance.to_dict()
# create an instance of ManagementReportNotification from a dict
management_report_notification_form_dict = management_report_notification.from_dict(management_report_notification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


