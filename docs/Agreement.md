# Agreement


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**agreement_status** | **str** |  | [optional] 
**allow_overruns** | **bool** |  | [optional] 
**application_cycle** | **str** |  | [optional] 
**application_limit** | **float** |  | [optional] 
**application_units** | **str** |  | [optional] 
**application_unlimited_flag** | **bool** |  | [optional] 
**auto_invoice_flag** | **bool** |  | [optional] 
**bill_amount** | **float** |  | [optional] 
**bill_expenses** | **str** |  Required On Updates; | [optional] 
**bill_one_time_flag** | **bool** |  | [optional] 
**bill_products** | **str** |  Required On Updates; | [optional] 
**bill_start_date** | **datetime** |  | [optional] 
**bill_time** | **str** |  Required On Updates; | [optional] 
**bill_to_company** | [**CompanyReference**](CompanyReference.md) |  | [optional] 
**bill_to_contact** | [**ContactReference**](ContactReference.md) |  | [optional] 
**bill_to_site** | [**SiteReference**](SiteReference.md) |  | [optional] 
**billable_expense_invoice** | **bool** |  | [optional] 
**billable_product_invoice** | **bool** |  | [optional] 
**billable_time_invoice** | **bool** |  | [optional] 
**billing_cycle** | [**BillingCycleReference**](BillingCycleReference.md) |  | [optional] 
**billing_terms** | [**BillingTermsReference**](BillingTermsReference.md) |  | [optional] 
**bottom_comment** | **bool** |  | [optional] 
**cancelled_flag** | **bool** |  | [optional] 
**carry_over_unused** | **bool** |  | [optional] 
**charge_to_firm** | **bool** |  | [optional] 
**comp_hourly_rate** | **float** |  | [optional] 
**comp_limit_amount** | **float** |  | [optional] 
**company** | [**CompanyReference**](CompanyReference.md) |  | [optional] 
**company_location** | [**SystemLocationReference**](SystemLocationReference.md) |  | [optional] 
**contact** | [**ContactReference**](ContactReference.md) |  | [optional] 
**cover_agreement_expense** | **bool** |  | [optional] 
**cover_agreement_product** | **bool** |  | [optional] 
**cover_agreement_time** | **bool** |  | [optional] 
**cover_sales_tax** | **bool** |  | [optional] 
**currency** | [**CurrencyReference**](CurrencyReference.md) |  | [optional] 
**custom_fields** | [**List[CustomFieldValue]**](CustomFieldValue.md) |  | [optional] 
**customer_po** | **str** |  Max length: 50; | [optional] 
**date_cancelled** | **datetime** |  | [optional] 
**department** | [**SystemDepartmentReference**](SystemDepartmentReference.md) |  | [optional] 
**employee_comp_not_exceed** | **str** |  | [optional] 
**employee_comp_rate** | **str** |  Required On Updates; | [optional] 
**end_date** | **datetime** |  | [optional] 
**expire_when_zero** | **bool** |  | [optional] 
**expired_days** | **int** |  | [optional] 
**id** | **int** |  | [optional] 
**internal_notes** | **str** |  | [optional] 
**invoice_description** | **str** |  | [optional] 
**invoice_prorated_additions_flag** | **bool** |  | [optional] 
**invoice_template** | [**InvoiceTemplateReference**](InvoiceTemplateReference.md) |  | [optional] 
**invoicing_cycle** | **str** |  Required On Updates; | [optional] 
**limit** | **int** |  | [optional] 
**location** | [**SystemLocationReference**](SystemLocationReference.md) |  | [optional] 
**name** | **str** |  Max length: 100; | 
**next_invoice_date** | **str** |  | [optional] 
**no_ending_date_flag** | **bool** |  | [optional] 
**one_time_flag** | **bool** |  | [optional] 
**opportunity** | [**OpportunityReference**](OpportunityReference.md) |  | [optional] 
**parent_agreement** | [**AgreementReference**](AgreementReference.md) |  | [optional] 
**period_type** | **str** |  | [optional] 
**project_type** | [**ProjectTypeReference**](ProjectTypeReference.md) |  | [optional] 
**prorate_first_bill** | **float** |  | [optional] 
**prorate_flag** | **bool** |  | [optional] 
**reason_cancelled** | **str** |  Max length: 100; | [optional] 
**restrict_department_flag** | **bool** |  | [optional] 
**restrict_down_payment** | **bool** |  | [optional] 
**restrict_location_flag** | **bool** |  | [optional] 
**ship_to_company** | [**CompanyReference**](CompanyReference.md) |  | [optional] 
**ship_to_contact** | [**ContactReference**](ContactReference.md) |  | [optional] 
**ship_to_site** | [**SiteReference**](SiteReference.md) |  | [optional] 
**site** | [**SiteReference**](SiteReference.md) |  | [optional] 
**sla** | [**SLAReference**](SLAReference.md) |  | [optional] 
**start_date** | **datetime** |  | [optional] 
**sub_contract_company** | [**CompanyReference**](CompanyReference.md) |  | [optional] 
**sub_contract_contact** | [**ContactReference**](ContactReference.md) |  | [optional] 
**tax_code** | [**TaxCodeReference**](TaxCodeReference.md) |  | [optional] 
**taxable** | **bool** |  | [optional] 
**top_comment** | **bool** |  | [optional] 
**type** | [**AgreementTypeReference**](AgreementTypeReference.md) |  | [optional] 
**work_order** | **str** |  Max length: 20; | [optional] 
**work_role** | [**WorkRoleReference**](WorkRoleReference.md) |  | [optional] 
**work_type** | [**WorkTypeReference**](WorkTypeReference.md) |  | [optional] 

## Example

```python
from connectwise_psa.models.agreement import Agreement

# TODO update the JSON string below
json = "{}"
# create an instance of Agreement from a JSON string
agreement_instance = Agreement.from_json(json)
# print the JSON string representation of the object
print Agreement.to_json()

# convert the object into a dict
agreement_dict = agreement_instance.to_dict()
# create an instance of Agreement from a dict
agreement_form_dict = agreement.from_dict(agreement_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


