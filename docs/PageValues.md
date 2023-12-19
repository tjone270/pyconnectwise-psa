# PageValues


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** |  | [optional] 
**page_id** | **int** |  | [optional] 
**page_size** | **int** |  | [optional] 

## Example

```python
from connectwise_psa.models.page_values import PageValues

# TODO update the JSON string below
json = "{}"
# create an instance of PageValues from a JSON string
page_values_instance = PageValues.from_json(json)
# print the JSON string representation of the object
print PageValues.to_json()

# convert the object into a dict
page_values_dict = page_values_instance.to_dict()
# create an instance of PageValues from a dict
page_values_form_dict = page_values.from_dict(page_values_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


