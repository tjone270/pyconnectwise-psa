# RmaActionReference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.rma_action_reference import RmaActionReference

# TODO update the JSON string below
json = "{}"
# create an instance of RmaActionReference from a JSON string
rma_action_reference_instance = RmaActionReference.from_json(json)
# print the JSON string representation of the object
print RmaActionReference.to_json()

# convert the object into a dict
rma_action_reference_dict = rma_action_reference_instance.to_dict()
# create an instance of RmaActionReference from a dict
rma_action_reference_form_dict = rma_action_reference.from_dict(rma_action_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


