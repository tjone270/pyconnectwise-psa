# RmaActionInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.rma_action_info import RmaActionInfo

# TODO update the JSON string below
json = "{}"
# create an instance of RmaActionInfo from a JSON string
rma_action_info_instance = RmaActionInfo.from_json(json)
# print the JSON string representation of the object
print RmaActionInfo.to_json()

# convert the object into a dict
rma_action_info_dict = rma_action_info_instance.to_dict()
# create an instance of RmaActionInfo from a dict
rma_action_info_form_dict = rma_action_info.from_dict(rma_action_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


