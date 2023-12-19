# TaxCode


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**add_all_expense_types** | **bool** |  | [optional] 
**add_all_product_types** | **bool** |  | [optional] 
**add_all_work_roles** | **bool** |  | [optional] 
**canada_calculate_gst_flag** | **bool** |  | [optional] 
**cancel_date** | **datetime** |  | [optional] 
**country** | [**CountryReference**](CountryReference.md) |  | [optional] 
**default_flag** | **bool** |  | [optional] 
**description** | **str** |  Max length: 50; | 
**display_on_invoice_flag** | **bool** |  | [optional] 
**effective_date** | **datetime** |  | 
**expense_type_ids** | **List[int]** | Array of expense type exemptions for the tax code. | [optional] 
**id** | **int** |  | [optional] 
**identifier** | **str** |  Max length: 8; | 
**invoice_caption** | **str** |  Max length: 25; | 
**level_five_agency_xref** | **str** |  Max length: 100; | [optional] 
**level_five_apply_single_unit_flag** | **bool** |  | [optional] 
**level_five_apply_single_unit_max** | **float** |  | [optional] 
**level_five_apply_single_unit_min** | **float** |  | [optional] 
**level_five_caption** | **str** |  Max length: 25; | [optional] 
**level_five_expenses_flag** | **bool** |  | [optional] 
**level_five_products_flag** | **bool** |  | [optional] 
**level_five_rate** | **float** |  | [optional] 
**level_five_rate_type** | **str** |  | [optional] 
**level_five_services_flag** | **bool** |  | [optional] 
**level_five_tax_code_xref** | **str** |  Max length: 50; | [optional] 
**level_five_taxable_max** | **float** |  | [optional] 
**level_four_agency_xref** | **str** |  Max length: 100; | [optional] 
**level_four_apply_single_unit_flag** | **bool** |  | [optional] 
**level_four_apply_single_unit_max** | **float** |  | [optional] 
**level_four_apply_single_unit_min** | **float** |  | [optional] 
**level_four_caption** | **str** |  Max length: 25; | [optional] 
**level_four_expenses_flag** | **bool** |  | [optional] 
**level_four_products_flag** | **bool** |  | [optional] 
**level_four_rate** | **float** |  | [optional] 
**level_four_rate_type** | **str** |  | [optional] 
**level_four_services_flag** | **bool** |  | [optional] 
**level_four_tax_code_xref** | **str** |  Max length: 50; | [optional] 
**level_four_taxable_max** | **float** |  | [optional] 
**level_one_agency_xref** | **str** |  Max length: 100; | [optional] 
**level_one_apply_single_unit_flag** | **bool** |  | [optional] 
**level_one_apply_single_unit_max** | **float** |  | [optional] 
**level_one_apply_single_unit_min** | **float** |  | [optional] 
**level_one_caption** | **str** |  Max length: 25; | [optional] 
**level_one_expenses_flag** | **bool** |  | [optional] 
**level_one_products_flag** | **bool** |  | [optional] 
**level_one_rate** | **float** |  | [optional] 
**level_one_rate_type** | **str** |  | [optional] 
**level_one_services_flag** | **bool** |  | [optional] 
**level_one_tax_code_xref** | **str** |  Max length: 50; | [optional] 
**level_one_taxable_max** | **float** |  | [optional] 
**level_six_agency_xref** | **str** |  Max length: 100; | [optional] 
**level_six_apply_single_unit_flag** | **bool** |  | [optional] 
**level_six_apply_single_unit_max** | **float** |  | [optional] 
**level_six_apply_single_unit_min** | **float** |  | [optional] 
**level_six_caption** | **str** |  Max length: 25; | [optional] 
**level_six_expenses_flag** | **bool** |  | [optional] 
**level_six_products_flag** | **bool** |  | [optional] 
**level_six_rate** | **float** |  | [optional] 
**level_six_rate_type** | **str** |  | [optional] 
**level_six_services_flag** | **bool** |  | [optional] 
**level_six_tax_code_xref** | **str** |  Max length: 50; | [optional] 
**level_six_taxable_max** | **float** |  | [optional] 
**level_three_agency_xref** | **str** |  Max length: 100; | [optional] 
**level_three_apply_single_unit_flag** | **bool** |  | [optional] 
**level_three_apply_single_unit_max** | **float** |  | [optional] 
**level_three_apply_single_unit_min** | **float** |  | [optional] 
**level_three_caption** | **str** |  Max length: 25; | [optional] 
**level_three_expenses_flag** | **bool** |  | [optional] 
**level_three_products_flag** | **bool** |  | [optional] 
**level_three_rate** | **float** |  | [optional] 
**level_three_rate_type** | **str** |  | [optional] 
**level_three_services_flag** | **bool** |  | [optional] 
**level_three_tax_code_xref** | **str** |  Max length: 50; | [optional] 
**level_three_taxable_max** | **float** |  | [optional] 
**level_two_agency_xref** | **str** |  Max length: 100; | [optional] 
**level_two_apply_single_unit_flag** | **bool** |  | [optional] 
**level_two_apply_single_unit_max** | **float** |  | [optional] 
**level_two_apply_single_unit_min** | **float** |  | [optional] 
**level_two_caption** | **str** |  Max length: 25; | [optional] 
**level_two_expenses_flag** | **bool** |  | [optional] 
**level_two_products_flag** | **bool** |  | [optional] 
**level_two_rate** | **float** |  | [optional] 
**level_two_rate_type** | **str** |  | [optional] 
**level_two_services_flag** | **bool** |  | [optional] 
**level_two_tax_code_xref** | **str** |  Max length: 50; | [optional] 
**level_two_taxable_max** | **float** |  | [optional] 
**product_type_ids** | **List[int]** | Array of product type exemptions for the tax code. | [optional] 
**remove_all_expense_types** | **bool** |  | [optional] 
**remove_all_product_types** | **bool** |  | [optional] 
**remove_all_work_roles** | **bool** |  | [optional] 
**work_role_ids** | **List[int]** | Array of work role exemptions for the tax code. | [optional] 

## Example

```python
from connectwise_psa.models.tax_code import TaxCode

# TODO update the JSON string below
json = "{}"
# create an instance of TaxCode from a JSON string
tax_code_instance = TaxCode.from_json(json)
# print the JSON string representation of the object
print TaxCode.to_json()

# convert the object into a dict
tax_code_dict = tax_code_instance.to_dict()
# create an instance of TaxCode from a dict
tax_code_form_dict = tax_code.from_dict(tax_code_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


