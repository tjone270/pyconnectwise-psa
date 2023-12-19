# BoardItemAssociation


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**add_all_sub_types_flag** | **bool** |  | [optional] 
**board** | [**BoardReference**](BoardReference.md) |  | [optional] 
**id** | **int** |  | 
**item** | [**ServiceItemReference**](ServiceItemReference.md) |  | [optional] 
**remove_all_sub_types_flag** | **bool** |  | [optional] 
**sub_type_association_ids** | **List[int]** | If addAllSubTypesFlag and removeAllSubTypesFlag are both false, this field is required. | [optional] 

## Example

```python
from connectwise_psa.models.board_item_association import BoardItemAssociation

# TODO update the JSON string below
json = "{}"
# create an instance of BoardItemAssociation from a JSON string
board_item_association_instance = BoardItemAssociation.from_json(json)
# print the JSON string representation of the object
print BoardItemAssociation.to_json()

# convert the object into a dict
board_item_association_dict = board_item_association_instance.to_dict()
# create an instance of BoardItemAssociation from a dict
board_item_association_form_dict = board_item_association.from_dict(board_item_association_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


