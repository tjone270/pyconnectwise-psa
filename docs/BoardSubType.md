# BoardSubType


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**add_all_types_flag** | **bool** |  | [optional] 
**board** | [**BoardReference**](BoardReference.md) |  | [optional] 
**id** | **int** |  | [optional] 
**inactive_flag** | **bool** |  | [optional] 
**name** | **str** |  Max length: 50; | 
**remove_all_types_flag** | **bool** |  | [optional] 
**type_association_ids** | **List[int]** |  | [optional] 

## Example

```python
from connectwise_psa.models.board_sub_type import BoardSubType

# TODO update the JSON string below
json = "{}"
# create an instance of BoardSubType from a JSON string
board_sub_type_instance = BoardSubType.from_json(json)
# print the JSON string representation of the object
print BoardSubType.to_json()

# convert the object into a dict
board_sub_type_dict = board_sub_type_instance.to_dict()
# create an instance of BoardSubType from a dict
board_sub_type_form_dict = board_sub_type.from_dict(board_sub_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


