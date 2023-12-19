# BoardCopy


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  Max length: 50; | 

## Example

```python
from connectwise_psa.models.board_copy import BoardCopy

# TODO update the JSON string below
json = "{}"
# create an instance of BoardCopy from a JSON string
board_copy_instance = BoardCopy.from_json(json)
# print the JSON string representation of the object
print BoardCopy.to_json()

# convert the object into a dict
board_copy_dict = board_copy_instance.to_dict()
# create an instance of BoardCopy from a dict
board_copy_form_dict = board_copy.from_dict(board_copy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


