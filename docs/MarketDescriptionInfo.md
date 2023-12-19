# MarketDescriptionInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.market_description_info import MarketDescriptionInfo

# TODO update the JSON string below
json = "{}"
# create an instance of MarketDescriptionInfo from a JSON string
market_description_info_instance = MarketDescriptionInfo.from_json(json)
# print the JSON string representation of the object
print MarketDescriptionInfo.to_json()

# convert the object into a dict
market_description_info_dict = market_description_info_instance.to_dict()
# create an instance of MarketDescriptionInfo from a dict
market_description_info_form_dict = market_description_info.from_dict(market_description_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


