# PricingBreak


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**amount** | **float** |  | [optional] 
**detail_id** | **int** |  | [optional] 
**id** | **int** |  | [optional] 
**price_method** | **str** |  | 
**quantity_end** | **float** |  | [optional] 
**quantity_start** | **float** |  | 
**unlimited** | **bool** |  | [optional] 

## Example

```python
from connectwise_psa.models.pricing_break import PricingBreak

# TODO update the JSON string below
json = "{}"
# create an instance of PricingBreak from a JSON string
pricing_break_instance = PricingBreak.from_json(json)
# print the JSON string representation of the object
print PricingBreak.to_json()

# convert the object into a dict
pricing_break_dict = pricing_break_instance.to_dict()
# create an instance of PricingBreak from a dict
pricing_break_form_dict = pricing_break.from_dict(pricing_break_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


