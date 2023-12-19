# BoardExcludedMember


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**board_id** | **int** |  | [optional] 
**id** | **int** |  | [optional] 
**member_id** | **int** |  | [optional] 

## Example

```python
from connectwise_psa.models.board_excluded_member import BoardExcludedMember

# TODO update the JSON string below
json = "{}"
# create an instance of BoardExcludedMember from a JSON string
board_excluded_member_instance = BoardExcludedMember.from_json(json)
# print the JSON string representation of the object
print BoardExcludedMember.to_json()

# convert the object into a dict
board_excluded_member_dict = board_excluded_member_instance.to_dict()
# create an instance of BoardExcludedMember from a dict
board_excluded_member_form_dict = board_excluded_member.from_dict(board_excluded_member_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


