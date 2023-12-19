# RmaAction


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**default_flag** | **bool** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  Max length: 50; | 

## Example

```python
from connectwise_psa.models.rma_action import RmaAction

# TODO update the JSON string below
json = "{}"
# create an instance of RmaAction from a JSON string
rma_action_instance = RmaAction.from_json(json)
# print the JSON string representation of the object
print RmaAction.to_json()

# convert the object into a dict
rma_action_dict = rma_action_instance.to_dict()
# create an instance of RmaAction from a dict
rma_action_form_dict = rma_action.from_dict(rma_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


