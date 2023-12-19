# BoardInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**all_sort** | **str** |  | [optional] 
**closed_loop_all_flag** | **bool** |  | [optional] 
**closed_loop_discussions_flag** | **bool** |  | [optional] 
**closed_loop_internal_analysis_flag** | **bool** |  | [optional] 
**closed_loop_resolution_flag** | **bool** |  | [optional] 
**department** | [**SystemDepartmentReference**](SystemDepartmentReference.md) |  | [optional] 
**id** | **int** |  | [optional] 
**inactive_flag** | **bool** |  | [optional] 
**internal_analysis_sort** | **str** |  | [optional] 
**location** | [**SystemLocationReference**](SystemLocationReference.md) |  | [optional] 
**name** | **str** |  | [optional] 
**problem_sort** | **str** |  | [optional] 
**project_flag** | **bool** |  | [optional] 
**resolution_sort** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.board_info import BoardInfo

# TODO update the JSON string below
json = "{}"
# create an instance of BoardInfo from a JSON string
board_info_instance = BoardInfo.from_json(json)
# print the JSON string representation of the object
print BoardInfo.to_json()

# convert the object into a dict
board_info_dict = board_info_instance.to_dict()
# create an instance of BoardInfo from a dict
board_info_form_dict = board_info.from_dict(board_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


