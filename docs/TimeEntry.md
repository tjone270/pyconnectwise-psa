# TimeEntry


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**actual_hours** | **float** |  | [optional] 
**add_to_detail_description_flag** | **bool** |  | [optional] 
**add_to_internal_analysis_flag** | **bool** |  | [optional] 
**add_to_resolution_flag** | **bool** |  | [optional] 
**agreement** | [**AgreementReference**](AgreementReference.md) |  | [optional] 
**agreement_amount** | **float** |  | [optional] 
**agreement_hours** | **float** |  | [optional] 
**billable_option** | **str** |  Required On Updates; | [optional] 
**business_unit_id** | **int** |  | [optional] 
**charge_to_id** | **int** | If chargeToId is not specified, we asume you enter time against the company specified | [optional] 
**charge_to_type** | **str** | If chargeToId is not specified, we asume you enter time against the company specified | [optional] 
**company** | [**CompanyReference**](CompanyReference.md) |  | [optional] 
**custom_fields** | [**List[CustomFieldValue]**](CustomFieldValue.md) |  | [optional] 
**date_entered** | **datetime** |  | [optional] 
**email_cc** | **str** | To update this value use the /service/tickets endpoint automaticEmailCc field | [optional] 
**email_cc_flag** | **bool** | This is an action flag. To update this value use the /service/tickets endpoint automaticEmailCcFlag field | [optional] 
**email_contact_flag** | **bool** | This is an action flag. To update this value use the /service/tickets endpoint automaticEmailContactFlag field | [optional] 
**email_resource_flag** | **bool** | This is an action flag. To update this value use the /service/tickets endpoint automaticEmailResourceFlag field | [optional] 
**entered_by** | **str** |  | [optional] 
**hourly_rate** | **float** | This field may only be Updated, it is defaulted on Create | [optional] 
**hours_billed** | **float** |  | [optional] 
**hours_deduct** | **float** |  | [optional] 
**id** | **int** |  | [optional] 
**internal_notes** | **str** |  | [optional] 
**invoice** | [**InvoiceReference**](InvoiceReference.md) |  | [optional] 
**invoice_hours** | **float** |  | [optional] 
**location_id** | **int** |  | [optional] 
**member** | [**MemberReference**](MemberReference.md) |  | [optional] 
**mobile_guid** | **str** |  | [optional] 
**notes** | **str** |  | [optional] 
**overage_rate** | **float** |  | [optional] 
**phase** | [**ProjectPhaseReference**](ProjectPhaseReference.md) |  | [optional] 
**project** | [**ProjectReference**](ProjectReference.md) |  | [optional] 
**status** | **str** |  | [optional] 
**ticket** | [**TicketReference**](TicketReference.md) |  | [optional] 
**time_end** | **datetime** |  | [optional] 
**time_sheet** | [**TimeSheetReference**](TimeSheetReference.md) |  | [optional] 
**time_start** | **datetime** |  | 
**work_role** | [**WorkRoleReference**](WorkRoleReference.md) |  | [optional] 
**work_type** | [**WorkTypeReference**](WorkTypeReference.md) |  | [optional] 

## Example

```python
from connectwise_psa.models.time_entry import TimeEntry

# TODO update the JSON string below
json = "{}"
# create an instance of TimeEntry from a JSON string
time_entry_instance = TimeEntry.from_json(json)
# print the JSON string representation of the object
print TimeEntry.to_json()

# convert the object into a dict
time_entry_dict = time_entry_instance.to_dict()
# create an instance of TimeEntry from a dict
time_entry_form_dict = time_entry.from_dict(time_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


