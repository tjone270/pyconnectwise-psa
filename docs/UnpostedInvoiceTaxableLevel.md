# UnpostedInvoiceTaxableLevel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**tax_amount** | **float** |  | [optional] 
**tax_code_xref** | **str** |  | [optional] 
**tax_level** | **int** |  | [optional] 

## Example

```python
from connectwise_psa.models.unposted_invoice_taxable_level import UnpostedInvoiceTaxableLevel

# TODO update the JSON string below
json = "{}"
# create an instance of UnpostedInvoiceTaxableLevel from a JSON string
unposted_invoice_taxable_level_instance = UnpostedInvoiceTaxableLevel.from_json(json)
# print the JSON string representation of the object
print UnpostedInvoiceTaxableLevel.to_json()

# convert the object into a dict
unposted_invoice_taxable_level_dict = unposted_invoice_taxable_level_instance.to_dict()
# create an instance of UnpostedInvoiceTaxableLevel from a dict
unposted_invoice_taxable_level_form_dict = unposted_invoice_taxable_level.from_dict(unposted_invoice_taxable_level_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


