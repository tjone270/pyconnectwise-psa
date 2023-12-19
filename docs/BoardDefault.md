# BoardDefault


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**agreement_id** | **int** |  | [optional] 
**board** | [**BoardReference**](BoardReference.md) |  | [optional] 
**default_flag** | **bool** |  | [optional] 
**id** | **int** |  | [optional] 
**service_type** | [**ServiceTypeReference**](ServiceTypeReference.md) |  | [optional] 

## Example

```python
from connectwise_psa.models.board_default import BoardDefault

# TODO update the JSON string below
json = "{}"
# create an instance of BoardDefault from a JSON string
board_default_instance = BoardDefault.from_json(json)
# print the JSON string representation of the object
print BoardDefault.to_json()

# convert the object into a dict
board_default_dict = board_default_instance.to_dict()
# create an instance of BoardDefault from a dict
board_default_form_dict = board_default.from_dict(board_default_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


