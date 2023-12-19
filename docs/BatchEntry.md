# BatchEntry


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**account_number** | **str** |  | [optional] 
**account_type** | **str** |  | [optional] 
**adjustment_detail** | [**AdjustmentDetailReference**](AdjustmentDetailReference.md) |  | [optional] 
**cost** | **float** |  | [optional] 
**cost_of_goods_sold_account_number** | **str** |  | [optional] 
**credit** | **float** |  | [optional] 
**debit** | **float** |  | [optional] 
**expense** | [**ExpenseDetailReference**](ExpenseDetailReference.md) |  | [optional] 
**id** | **int** |  | [optional] 
**invoice** | [**InvoiceReference**](InvoiceReference.md) |  | [optional] 
**item** | **str** |  | [optional] 
**line_item** | [**PurchaseOrderLineItemReference**](PurchaseOrderLineItemReference.md) |  | [optional] 
**name** | **str** |  | [optional] 
**purchase_order** | [**PurchaseOrderReference**](PurchaseOrderReference.md) |  | [optional] 
**sales_code** | **str** |  | [optional] 
**transfer** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.batch_entry import BatchEntry

# TODO update the JSON string below
json = "{}"
# create an instance of BatchEntry from a JSON string
batch_entry_instance = BatchEntry.from_json(json)
# print the JSON string representation of the object
print BatchEntry.to_json()

# convert the object into a dict
batch_entry_dict = batch_entry_instance.to_dict()
# create an instance of BatchEntry from a dict
batch_entry_form_dict = batch_entry.from_dict(batch_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


