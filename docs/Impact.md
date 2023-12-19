# Impact


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**default_flag** | **bool** |  | [optional] 
**description** | **str** |  Max length: 200; | 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.impact import Impact

# TODO update the JSON string below
json = "{}"
# create an instance of Impact from a JSON string
impact_instance = Impact.from_json(json)
# print the JSON string representation of the object
print Impact.to_json()

# convert the object into a dict
impact_dict = impact_instance.to_dict()
# create an instance of Impact from a dict
impact_form_dict = impact.from_dict(impact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


