# AgreementType


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**add_all_work_role_exclusions** | **bool** |  | [optional] 
**add_all_work_type_exclusions** | **bool** |  | [optional] 
**allow_overruns_flag** | **bool** |  | [optional] 
**application_cycle** | **str** |  | [optional] 
**application_limit** | **float** |  | [optional] 
**application_units** | **str** |  | [optional] 
**application_unlimited_flag** | **bool** |  | [optional] 
**auto_invoice_flag** | **bool** |  | [optional] 
**bill_amount** | **float** |  | [optional] 
**bill_expenses** | **str** |  | 
**bill_one_time_flag** | **bool** |  | [optional] 
**bill_products** | **str** |  | 
**bill_time** | **str** |  | 
**billable_expense_invoice_flag** | **bool** |  | [optional] 
**billable_product_invoice_flag** | **bool** |  | [optional] 
**billable_time_invoice_flag** | **bool** |  | [optional] 
**billing_cycle** | [**BillingCycleReference**](BillingCycleReference.md) |  | [optional] 
**billing_terms** | [**BillingTermsReference**](BillingTermsReference.md) |  | [optional] 
**bottom_comment_flag** | **bool** |  | [optional] 
**carry_over_unused_flag** | **bool** |  | [optional] 
**charge_to_firm_flag** | **bool** |  | [optional] 
**comp_hourly_rate** | **float** |  | [optional] 
**comp_limit_amount** | **float** |  | [optional] 
**copy_work_roles_flag** | **bool** |  | [optional] 
**copy_work_types_flag** | **bool** |  | [optional] 
**cover_agreement_expense_flag** | **bool** |  | [optional] 
**cover_agreement_product_flag** | **bool** |  | [optional] 
**cover_agreement_time_flag** | **bool** |  | [optional] 
**cover_sales_tax_flag** | **bool** |  | [optional] 
**default_flag** | **bool** |  | [optional] 
**department** | [**SystemDepartmentReference**](SystemDepartmentReference.md) |  | [optional] 
**email_template** | [**EmailTemplateReference**](EmailTemplateReference.md) |  | [optional] 
**employee_comp_not_exceed** | **str** |  | 
**employee_comp_rate** | **str** |  | 
**exclusion_work_role_ids** | **List[int]** |  | [optional] 
**exclusion_work_type_ids** | **List[int]** |  | [optional] 
**expire_when_zero** | **bool** |  | [optional] 
**expired_days** | **int** |  | [optional] 
**id** | **int** |  | [optional] 
**inactive_flag** | **bool** |  | [optional] 
**integration_x_ref** | **str** |  Max length: 50; | [optional] 
**invoice_description** | **str** |  Max length: 4000; | [optional] 
**invoice_pre_suffix** | **str** |  Max length: 5; | [optional] 
**invoice_prorated_additions_flag** | **bool** |  | [optional] 
**invoice_template** | [**InvoiceTemplateReference**](InvoiceTemplateReference.md) |  | [optional] 
**invoicing_cycle** | **str** |  | 
**limit** | **int** |  | [optional] 
**location** | [**SystemLocationReference**](SystemLocationReference.md) |  | [optional] 
**name** | **str** |  Max length: 50; | 
**one_time_flag** | **bool** |  | [optional] 
**pre_payment_flag** | **bool** |  | [optional] 
**prefix_suffix_option** | **str** |  | [optional] 
**project_type** | [**ProjectTypeReference**](ProjectTypeReference.md) |  | [optional] 
**prorate_flag** | **bool** |  | [optional] 
**remove_all_work_role_exclusions** | **bool** |  | [optional] 
**remove_all_work_type_exclusions** | **bool** |  | [optional] 
**restrict_department_flag** | **bool** |  | [optional] 
**restrict_down_payment_flag** | **bool** |  | [optional] 
**restrict_location_flag** | **bool** |  | [optional] 
**sla** | [**SLAReference**](SLAReference.md) |  | [optional] 
**taxable_flag** | **bool** |  | [optional] 
**top_comment_flag** | **bool** |  | [optional] 
**work_role** | [**WorkRoleReference**](WorkRoleReference.md) |  | [optional] 
**work_type** | [**WorkTypeReference**](WorkTypeReference.md) |  | [optional] 

## Example

```python
from connectwise_psa.models.agreement_type import AgreementType

# TODO update the JSON string below
json = "{}"
# create an instance of AgreementType from a JSON string
agreement_type_instance = AgreementType.from_json(json)
# print the JSON string representation of the object
print AgreementType.to_json()

# convert the object into a dict
agreement_type_dict = agreement_type_instance.to_dict()
# create an instance of AgreementType from a dict
agreement_type_form_dict = agreement_type.from_dict(agreement_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


