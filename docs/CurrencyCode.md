# CurrencyCode


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.currency_code import CurrencyCode

# TODO update the JSON string below
json = "{}"
# create an instance of CurrencyCode from a JSON string
currency_code_instance = CurrencyCode.from_json(json)
# print the JSON string representation of the object
print CurrencyCode.to_json()

# convert the object into a dict
currency_code_dict = currency_code_instance.to_dict()
# create an instance of CurrencyCode from a dict
currency_code_form_dict = currency_code.from_dict(currency_code_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


