# BoardSubTypeInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**inactive_flag** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**type_association_ids** | **List[int]** |  | [optional] 

## Example

```python
from connectwise_psa.models.board_sub_type_info import BoardSubTypeInfo

# TODO update the JSON string below
json = "{}"
# create an instance of BoardSubTypeInfo from a JSON string
board_sub_type_info_instance = BoardSubTypeInfo.from_json(json)
# print the JSON string representation of the object
print BoardSubTypeInfo.to_json()

# convert the object into a dict
board_sub_type_info_dict = board_sub_type_info_instance.to_dict()
# create an instance of BoardSubTypeInfo from a dict
board_sub_type_info_form_dict = board_sub_type_info.from_dict(board_sub_type_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


