# InvoiceInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**agreement_billing_info** | [**List[AgreementBillingInfo]**](AgreementBillingInfo.md) |  | [optional] 
**billing_setup** | [**BillingSetup**](BillingSetup.md) |  | [optional] 
**bundled_components_info** | [**List[ProductComponent]**](ProductComponent.md) |  | [optional] 
**expenses** | [**List[ExpenseEntry]**](ExpenseEntry.md) |  | [optional] 
**id** | **int** |  | [optional] 
**invoice** | [**Invoice**](Invoice.md) |  | [optional] 
**invoice_template** | [**InvoiceTemplate**](InvoiceTemplate.md) |  | [optional] 
**logo** | [**DocumentInfo**](DocumentInfo.md) |  | [optional] 
**products** | [**List[ProductItem]**](ProductItem.md) |  | [optional] 
**time_entries** | [**List[TimeEntry]**](TimeEntry.md) |  | [optional] 

## Example

```python
from connectwise_psa.models.invoice_info import InvoiceInfo

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceInfo from a JSON string
invoice_info_instance = InvoiceInfo.from_json(json)
# print the JSON string representation of the object
print InvoiceInfo.to_json()

# convert the object into a dict
invoice_info_dict = invoice_info_instance.to_dict()
# create an instance of InvoiceInfo from a dict
invoice_info_form_dict = invoice_info.from_dict(invoice_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


