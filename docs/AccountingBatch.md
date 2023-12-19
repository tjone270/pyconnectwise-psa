# AccountingBatch


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**batch_identifier** | **str** |  | [optional] 
**closed_flag** | **bool** |  | [optional] 
**export_expenses_flag** | **bool** |  | [optional] 
**export_invoices_flag** | **bool** |  | [optional] 
**export_products_flag** | **bool** |  | [optional] 
**id** | **int** |  | [optional] 

## Example

```python
from connectwise_psa.models.accounting_batch import AccountingBatch

# TODO update the JSON string below
json = "{}"
# create an instance of AccountingBatch from a JSON string
accounting_batch_instance = AccountingBatch.from_json(json)
# print the JSON string representation of the object
print AccountingBatch.to_json()

# convert the object into a dict
accounting_batch_dict = accounting_batch_instance.to_dict()
# create an instance of AccountingBatch from a dict
accounting_batch_form_dict = accounting_batch.from_dict(accounting_batch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


