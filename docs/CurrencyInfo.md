# CurrencyInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.currency_info import CurrencyInfo

# TODO update the JSON string below
json = "{}"
# create an instance of CurrencyInfo from a JSON string
currency_info_instance = CurrencyInfo.from_json(json)
# print the JSON string representation of the object
print CurrencyInfo.to_json()

# convert the object into a dict
currency_info_dict = currency_info_instance.to_dict()
# create an instance of CurrencyInfo from a dict
currency_info_form_dict = currency_info.from_dict(currency_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


