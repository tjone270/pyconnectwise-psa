# FinanceCurrency


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**currency_code** | [**CurrencyCodeReference**](CurrencyCodeReference.md) |  | [optional] 
**currency_identifier** | **str** |  Max length: 10; | 
**decimal_separator** | **str** |  Max length: 1; | [optional] 
**display_id_flag** | **bool** |  | [optional] 
**display_symbol_flag** | **bool** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  Max length: 50; | 
**negative_parentheses_flag** | **bool** |  | [optional] 
**number_of_decimals** | **int** |  | [optional] 
**report_format** | **str** |  | [optional] 
**right_align** | **bool** |  | [optional] 
**symbol** | **str** |  Max length: 10; | [optional] 
**thousands_separator** | **str** |  Max length: 1; | [optional] 

## Example

```python
from connectwise_psa.models.finance_currency import FinanceCurrency

# TODO update the JSON string below
json = "{}"
# create an instance of FinanceCurrency from a JSON string
finance_currency_instance = FinanceCurrency.from_json(json)
# print the JSON string representation of the object
print FinanceCurrency.to_json()

# convert the object into a dict
finance_currency_dict = finance_currency_instance.to_dict()
# create an instance of FinanceCurrency from a dict
finance_currency_form_dict = finance_currency.from_dict(finance_currency_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


