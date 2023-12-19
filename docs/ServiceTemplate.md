# ServiceTemplate


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**agreement** | [**AgreementReference**](AgreementReference.md) |  | [optional] 
**assigned_by** | [**MemberReference**](MemberReference.md) |  | [optional] 
**assigned_notify_flag** | **bool** |  | [optional] 
**attach_schedule_to_new_service_flag** | **bool** |  | [optional] 
**bill_complete_flag** | **bool** |  | [optional] 
**bill_service_separately_flag** | **bool** |  | [optional] 
**bill_unapproved_time_and_expenses_flag** | **bool** |  | [optional] 
**billing_amount** | **float** |  | [optional] 
**billing_method** | **str** |  | [optional] 
**board** | [**BoardReference**](BoardReference.md) |  | [optional] 
**company** | [**CompanyReference**](CompanyReference.md) |  | [optional] 
**contact** | [**ContactReference**](ContactReference.md) |  | [optional] 
**department** | [**SystemDepartmentReference**](SystemDepartmentReference.md) |  | [optional] 
**email_cc** | **str** |  | [optional] 
**email_cc_flag** | **bool** |  | [optional] 
**email_contact_flag** | **bool** |  | [optional] 
**email_resource_flag** | **bool** |  | [optional] 
**expense_billable_flag** | **bool** |  | [optional] 
**expense_invoice_flag** | **bool** |  | [optional] 
**hours_budget** | **float** |  | [optional] 
**id** | **int** |  | [optional] 
**impact** | **str** |  | [optional] 
**internal_analysis** | **str** |  | [optional] 
**item** | [**ServiceItemReference**](ServiceItemReference.md) |  | [optional] 
**location** | [**SystemLocationReference**](SystemLocationReference.md) |  | [optional] 
**name** | **str** |  | [optional] 
**override_flag** | **bool** |  | [optional] 
**priority** | [**PriorityReference**](PriorityReference.md) |  | [optional] 
**problem** | **str** |  | [optional] 
**product_invoice_flag** | **bool** |  | [optional] 
**purchase_order_number** | **str** |  | [optional] 
**reference** | **str** |  | [optional] 
**restrict_downpayment_flag** | **bool** |  | [optional] 
**schedule_days_before** | **int** |  | [optional] 
**service_days_before** | **int** |  | [optional] 
**service_location** | [**ServiceLocationReference**](ServiceLocationReference.md) |  | [optional] 
**severity** | **str** |  | [optional] 
**site** | [**SiteReference**](SiteReference.md) |  | [optional] 
**source** | [**ServiceSourceReference**](ServiceSourceReference.md) |  | [optional] 
**status** | [**ServiceStatusReference**](ServiceStatusReference.md) |  | [optional] 
**subtype** | [**ServiceSubTypeReference**](ServiceSubTypeReference.md) |  | [optional] 
**summary** | **str** |  | [optional] 
**team** | [**ServiceTeamReference**](ServiceTeamReference.md) |  | [optional] 
**template_flag** | **bool** |  | [optional] 
**time_billable_flag** | **bool** |  | [optional] 
**time_invoice_flag** | **bool** |  | [optional] 
**type** | [**ServiceTypeReference**](ServiceTypeReference.md) |  | [optional] 

## Example

```python
from connectwise_psa.models.service_template import ServiceTemplate

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceTemplate from a JSON string
service_template_instance = ServiceTemplate.from_json(json)
# print the JSON string representation of the object
print ServiceTemplate.to_json()

# convert the object into a dict
service_template_dict = service_template_instance.to_dict()
# create an instance of ServiceTemplate from a dict
service_template_form_dict = service_template.from_dict(service_template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


