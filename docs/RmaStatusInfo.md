# RmaStatusInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**sort_order** | **int** |  | [optional] 

## Example

```python
from connectwise_psa.models.rma_status_info import RmaStatusInfo

# TODO update the JSON string below
json = "{}"
# create an instance of RmaStatusInfo from a JSON string
rma_status_info_instance = RmaStatusInfo.from_json(json)
# print the JSON string representation of the object
print RmaStatusInfo.to_json()

# convert the object into a dict
rma_status_info_dict = rma_status_info_instance.to_dict()
# create an instance of RmaStatusInfo from a dict
rma_status_info_form_dict = rma_status_info.from_dict(rma_status_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


