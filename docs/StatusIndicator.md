# StatusIndicator


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**color** | **str** |  | [optional] 
**icon** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**identifier** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.status_indicator import StatusIndicator

# TODO update the JSON string below
json = "{}"
# create an instance of StatusIndicator from a JSON string
status_indicator_instance = StatusIndicator.from_json(json)
# print the JSON string representation of the object
print StatusIndicator.to_json()

# convert the object into a dict
status_indicator_dict = status_indicator_instance.to_dict()
# create an instance of StatusIndicator from a dict
status_indicator_form_dict = status_indicator.from_dict(status_indicator_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


