# BoardStatusInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**closed_flag** | **bool** |  | [optional] 
**default_flag** | **bool** |  | [optional] 
**id** | **int** |  | [optional] 
**inactive_flag** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**sort_order** | **int** |  | [optional] 

## Example

```python
from connectwise_psa.models.board_status_info import BoardStatusInfo

# TODO update the JSON string below
json = "{}"
# create an instance of BoardStatusInfo from a JSON string
board_status_info_instance = BoardStatusInfo.from_json(json)
# print the JSON string representation of the object
print BoardStatusInfo.to_json()

# convert the object into a dict
board_status_info_dict = board_status_info_instance.to_dict()
# create an instance of BoardStatusInfo from a dict
board_status_info_form_dict = board_status_info.from_dict(board_status_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


