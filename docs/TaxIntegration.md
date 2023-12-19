# TaxIntegration


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**account_number** | **str** |  Max length: 50; | [optional] 
**accounting_integration_flag** | **bool** |  | [optional] 
**commit_transactions_flag** | **bool** |  | [optional] 
**company_code** | **str** |  Max length: 50; | [optional] 
**enabled_flag** | **bool** |  | [optional] 
**expense_tax_code** | **str** |  Max length: 50; | [optional] 
**freight_tax_code** | **str** |  Max length: 50; | [optional] 
**id** | **int** |  | [optional] 
**invoice_amount_tax_code** | **str** |  Max length: 50; | [optional] 
**license_key** | **str** |  Max length: 50; | [optional] 
**product_tax_code** | **str** |  Max length: 50; | [optional] 
**sales_invoice_flag** | **bool** |  | [optional] 
**service_url** | **str** |  Max length: 250; | [optional] 
**tax_integration_type** | **str** |  | [optional] 
**tax_line_flag** | **bool** |  | [optional] 
**time_tax_code** | **str** |  Max length: 50; | [optional] 

## Example

```python
from connectwise_psa.models.tax_integration import TaxIntegration

# TODO update the JSON string below
json = "{}"
# create an instance of TaxIntegration from a JSON string
tax_integration_instance = TaxIntegration.from_json(json)
# print the JSON string representation of the object
print TaxIntegration.to_json()

# convert the object into a dict
tax_integration_dict = tax_integration_instance.to_dict()
# create an instance of TaxIntegration from a dict
tax_integration_form_dict = tax_integration.from_dict(tax_integration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


