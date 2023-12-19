# CurrencyReference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**currency_code** | **str** |  | [optional] 
**currency_identifier** | **str** |  | [optional] 
**decimal_separator** | **str** |  | [optional] 
**display_id_flag** | **bool** |  | [optional] 
**display_symbol_flag** | **bool** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**negative_parentheses_flag** | **bool** |  | [optional] 
**number_of_decimals** | **int** |  | [optional] 
**right_align** | **bool** |  | [optional] 
**symbol** | **str** |  | [optional] 
**thousands_separator** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.currency_reference import CurrencyReference

# TODO update the JSON string below
json = "{}"
# create an instance of CurrencyReference from a JSON string
currency_reference_instance = CurrencyReference.from_json(json)
# print the JSON string representation of the object
print CurrencyReference.to_json()

# convert the object into a dict
currency_reference_dict = currency_reference_instance.to_dict()
# create an instance of CurrencyReference from a dict
currency_reference_form_dict = currency_reference.from_dict(currency_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


