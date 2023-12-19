# TaxCodeLevel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**agency_xref** | **str** |  Max length: 100; | [optional] 
**caption** | **str** |  Max length: 25; | [optional] 
**id** | **int** |  | [optional] 
**rate_type** | **str** |  | 
**single_unit_flag** | **bool** |  | [optional] 
**single_unit_maximum** | **float** |  | [optional] 
**single_unit_minimum** | **float** |  | [optional] 
**tax_code_xref** | **str** |  Max length: 50; | [optional] 
**tax_expenses_flag** | **bool** |  | [optional] 
**tax_level** | **int** |  | [optional] 
**tax_products_flag** | **bool** |  | [optional] 
**tax_rate** | **float** |  | 
**tax_services_flag** | **bool** |  | [optional] 
**taxable_max** | **float** |  | [optional] 

## Example

```python
from connectwise_psa.models.tax_code_level import TaxCodeLevel

# TODO update the JSON string below
json = "{}"
# create an instance of TaxCodeLevel from a JSON string
tax_code_level_instance = TaxCodeLevel.from_json(json)
# print the JSON string representation of the object
print TaxCodeLevel.to_json()

# convert the object into a dict
tax_code_level_dict = tax_code_level_instance.to_dict()
# create an instance of TaxCodeLevel from a dict
tax_code_level_form_dict = tax_code_level.from_dict(tax_code_level_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


