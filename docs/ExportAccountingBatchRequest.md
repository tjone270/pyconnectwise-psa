# ExportAccountingBatchRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**batch_identifier** | **str** |  Max length: 50; | [optional] 
**excluded_expense_ids** | **List[int]** |  | [optional] 
**excluded_invoice_ids** | **List[int]** |  | [optional] 
**excluded_product_ids** | **List[str]** |  | [optional] 
**export_expenses_flag** | **bool** | Batch export must include invoices, expenses, or products (procurement). | [optional] 
**export_invoices_flag** | **bool** | Batch export must include invoices, expenses, or products (procurement). | [optional] 
**export_payments_flag** | **bool** | Batch export must include invoices, expenses, or products (procurement). | [optional] 
**export_products_flag** | **bool** | Batch export must include invoices, expenses, or products (procurement). | [optional] 
**gl_interface_identifier** | **str** |  | [optional] 
**included_expense_ids** | **List[int]** |  | [optional] 
**included_invoice_ids** | **List[int]** |  | [optional] 
**included_payment_ids** | **List[int]** |  | [optional] 
**included_product_ids** | **List[str]** |  | [optional] 
**location_id** | **int** |  | [optional] 
**summarize_invoices** | **str** |  | [optional] 
**thru_date** | **datetime** |  | [optional] 

## Example

```python
from connectwise_psa.models.export_accounting_batch_request import ExportAccountingBatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ExportAccountingBatchRequest from a JSON string
export_accounting_batch_request_instance = ExportAccountingBatchRequest.from_json(json)
# print the JSON string representation of the object
print ExportAccountingBatchRequest.to_json()

# convert the object into a dict
export_accounting_batch_request_dict = export_accounting_batch_request_instance.to_dict()
# create an instance of ExportAccountingBatchRequest from a dict
export_accounting_batch_request_form_dict = export_accounting_batch_request.from_dict(export_accounting_batch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


