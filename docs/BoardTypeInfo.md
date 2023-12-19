# BoardTypeInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**board** | [**BoardReference**](BoardReference.md) |  | [optional] 
**id** | **int** |  | [optional] 
**inactive_flag** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.board_type_info import BoardTypeInfo

# TODO update the JSON string below
json = "{}"
# create an instance of BoardTypeInfo from a JSON string
board_type_info_instance = BoardTypeInfo.from_json(json)
# print the JSON string representation of the object
print BoardTypeInfo.to_json()

# convert the object into a dict
board_type_info_dict = board_type_info_instance.to_dict()
# create an instance of BoardTypeInfo from a dict
board_type_info_form_dict = board_type_info.from_dict(board_type_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


