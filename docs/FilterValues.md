# FilterValues


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**childconditions** | **str** |  | [optional] 
**conditions** | **str** |  | [optional] 
**customfieldconditions** | **str** |  | [optional] 
**order_by** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.filter_values import FilterValues

# TODO update the JSON string below
json = "{}"
# create an instance of FilterValues from a JSON string
filter_values_instance = FilterValues.from_json(json)
# print the JSON string representation of the object
print FilterValues.to_json()

# convert the object into a dict
filter_values_dict = filter_values_instance.to_dict()
# create an instance of FilterValues from a dict
filter_values_form_dict = filter_values.from_dict(filter_values_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


