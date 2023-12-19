# BoardReference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.board_reference import BoardReference

# TODO update the JSON string below
json = "{}"
# create an instance of BoardReference from a JSON string
board_reference_instance = BoardReference.from_json(json)
# print the JSON string representation of the object
print BoardReference.to_json()

# convert the object into a dict
board_reference_dict = board_reference_instance.to_dict()
# create an instance of BoardReference from a dict
board_reference_form_dict = board_reference.from_dict(board_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


