# AccountingPackageSetup


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accounting_package** | [**AccountingPackageReference**](AccountingPackageReference.md) |  | [optional] 
**direct_transfer_flag** | **bool** |  | [optional] 
**enable_tax_groups_flag** | **bool** |  | [optional] 
**expense_format** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**include_cogs_drop_ship_flag** | **bool** |  | [optional] 
**include_cogs_entries_flag** | **bool** |  | [optional] 
**include_expenses_flag** | **bool** |  | [optional] 
**include_invoices_flag** | **bool** |  | [optional] 
**include_items_flag** | **bool** |  | [optional] 
**include_sales_tax_flag** | **bool** |  | [optional] 
**inventory_soh_flag** | **bool** |  | [optional] 
**invoice_format** | **str** |  | [optional] 
**send_component_amount_flag** | **bool** |  | [optional] 
**send_uom_flag** | **bool** |  | [optional] 
**suppress_memo_flag** | **bool** |  | [optional] 
**sync_payment_info_flag** | **bool** |  | [optional] 
**sync_wise_pay_payment_info_flag** | **bool** |  | [optional] 
**transfer_expenses_as_bill_flag** | **bool** |  | [optional] 
**wise_pay_lab_flag** | **bool** |  | [optional] 
**zero_dollar_tax_amounts_flag** | **bool** |  | [optional] 

## Example

```python
from connectwise_psa.models.accounting_package_setup import AccountingPackageSetup

# TODO update the JSON string below
json = "{}"
# create an instance of AccountingPackageSetup from a JSON string
accounting_package_setup_instance = AccountingPackageSetup.from_json(json)
# print the JSON string representation of the object
print AccountingPackageSetup.to_json()

# convert the object into a dict
accounting_package_setup_dict = accounting_package_setup_instance.to_dict()
# create an instance of AccountingPackageSetup from a dict
accounting_package_setup_form_dict = accounting_package_setup.from_dict(accounting_package_setup_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


