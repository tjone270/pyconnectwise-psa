# StatusIndicatorReference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**identifier** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.status_indicator_reference import StatusIndicatorReference

# TODO update the JSON string below
json = "{}"
# create an instance of StatusIndicatorReference from a JSON string
status_indicator_reference_instance = StatusIndicatorReference.from_json(json)
# print the JSON string representation of the object
print StatusIndicatorReference.to_json()

# convert the object into a dict
status_indicator_reference_dict = status_indicator_reference_instance.to_dict()
# create an instance of StatusIndicatorReference from a dict
status_indicator_reference_form_dict = status_indicator_reference.from_dict(status_indicator_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


