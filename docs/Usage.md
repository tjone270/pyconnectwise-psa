# Usage


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**description** | **str** |  | [optional] 
**hyperlink** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**type** | **str** |  | [optional] 
**type_key** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.usage import Usage

# TODO update the JSON string below
json = "{}"
# create an instance of Usage from a JSON string
usage_instance = Usage.from_json(json)
# print the JSON string representation of the object
print Usage.to_json()

# convert the object into a dict
usage_dict = usage_instance.to_dict()
# create an instance of Usage from a dict
usage_form_dict = usage.from_dict(usage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


