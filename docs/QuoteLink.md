# QuoteLink


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**all_locations_flag** | **bool** |  | [optional] 
**id** | **int** |  | [optional] 
**link** | **str** |  Max length: 2000; | 
**location** | [**SystemLocationReference**](SystemLocationReference.md) |  | [optional] 
**new_window_flag** | **bool** |  | [optional] 

## Example

```python
from connectwise_psa.models.quote_link import QuoteLink

# TODO update the JSON string below
json = "{}"
# create an instance of QuoteLink from a JSON string
quote_link_instance = QuoteLink.from_json(json)
# print the JSON string representation of the object
print QuoteLink.to_json()

# convert the object into a dict
quote_link_dict = quote_link_instance.to_dict()
# create an instance of QuoteLink from a dict
quote_link_form_dict = quote_link.from_dict(quote_link_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


