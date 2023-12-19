# InOutBoard


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**additional_info** | **str** |  Max length: 100; | [optional] 
**date_back** | **datetime** |  | 
**id** | **int** |  | [optional] 
**in_out_type** | [**InOutTypeReference**](InOutTypeReference.md) |  | [optional] 
**member** | [**MemberReference**](MemberReference.md) |  | [optional] 

## Example

```python
from connectwise_psa.models.in_out_board import InOutBoard

# TODO update the JSON string below
json = "{}"
# create an instance of InOutBoard from a JSON string
in_out_board_instance = InOutBoard.from_json(json)
# print the JSON string representation of the object
print InOutBoard.to_json()

# convert the object into a dict
in_out_board_dict = in_out_board_instance.to_dict()
# create an instance of InOutBoard from a dict
in_out_board_form_dict = in_out_board.from_dict(in_out_board_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


