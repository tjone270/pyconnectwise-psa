# MarketDescription


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  Max length: 50; | 

## Example

```python
from connectwise_psa.models.market_description import MarketDescription

# TODO update the JSON string below
json = "{}"
# create an instance of MarketDescription from a JSON string
market_description_instance = MarketDescription.from_json(json)
# print the JSON string representation of the object
print MarketDescription.to_json()

# convert the object into a dict
market_description_dict = market_description_instance.to_dict()
# create an instance of MarketDescription from a dict
market_description_form_dict = market_description.from_dict(market_description_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


