# BoardType


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**board** | [**BoardReference**](BoardReference.md) |  | [optional] 
**category** | **str** |  | [optional] 
**default_flag** | **bool** |  | [optional] 
**department** | [**SystemDepartmentReference**](SystemDepartmentReference.md) |  | [optional] 
**id** | **int** |  | [optional] 
**inactive_flag** | **bool** |  | [optional] 
**integration_xref** | **str** |  Max length: 50; | [optional] 
**location** | [**SystemLocationReference**](SystemLocationReference.md) |  | [optional] 
**name** | **str** |  Max length: 50; | 
**request_for_change_flag** | **bool** |  | [optional] 
**skill** | [**SkillReference**](SkillReference.md) |  | [optional] 
**skill_category** | [**SkillCategoryReference**](SkillCategoryReference.md) |  | [optional] 

## Example

```python
from connectwise_psa.models.board_type import BoardType

# TODO update the JSON string below
json = "{}"
# create an instance of BoardType from a JSON string
board_type_instance = BoardType.from_json(json)
# print the JSON string representation of the object
print BoardType.to_json()

# convert the object into a dict
board_type_dict = board_type_instance.to_dict()
# create an instance of BoardType from a dict
board_type_form_dict = board_type.from_dict(board_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


