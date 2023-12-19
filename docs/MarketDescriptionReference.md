# MarketDescriptionReference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.market_description_reference import MarketDescriptionReference

# TODO update the JSON string below
json = "{}"
# create an instance of MarketDescriptionReference from a JSON string
market_description_reference_instance = MarketDescriptionReference.from_json(json)
# print the JSON string representation of the object
print MarketDescriptionReference.to_json()

# convert the object into a dict
market_description_reference_dict = market_description_reference_instance.to_dict()
# create an instance of MarketDescriptionReference from a dict
market_description_reference_form_dict = market_description_reference.from_dict(market_description_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


