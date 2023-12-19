# CreateAccountingBatchRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**batch_identifier** | **str** |  Max length: 50; | [optional] 
**export_expenses_flag** | **bool** | Batch must export Invoices, Expenses or Products. | [optional] 
**export_invoices_flag** | **bool** | Batch must export Invoices, Expenses or Products. | [optional] 
**export_products_flag** | **bool** | Batch must export Invoices, Expenses or Products. | [optional] 
**gl_interface_identifier** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**processed_record_ids** | **List[int]** | GL Entry RecIDs. | 
**summarize_expenses** | **bool** |  | [optional] 

## Example

```python
from connectwise_psa.models.create_accounting_batch_request import CreateAccountingBatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAccountingBatchRequest from a JSON string
create_accounting_batch_request_instance = CreateAccountingBatchRequest.from_json(json)
# print the JSON string representation of the object
print CreateAccountingBatchRequest.to_json()

# convert the object into a dict
create_accounting_batch_request_dict = create_accounting_batch_request_instance.to_dict()
# create an instance of CreateAccountingBatchRequest from a dict
create_accounting_batch_request_form_dict = create_accounting_batch_request.from_dict(create_accounting_batch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


