# BoardTypeSubTypeItemAssociation


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**board** | [**BoardReference**](BoardReference.md) |  | [optional] 
**id** | **int** |  | [optional] 
**item** | [**ServiceItemReference**](ServiceItemReference.md) |  | [optional] 
**sub_type** | [**ServiceSubTypeReference**](ServiceSubTypeReference.md) |  | [optional] 
**type** | [**ServiceTypeReference**](ServiceTypeReference.md) |  | [optional] 

## Example

```python
from connectwise_psa.models.board_type_sub_type_item_association import BoardTypeSubTypeItemAssociation

# TODO update the JSON string below
json = "{}"
# create an instance of BoardTypeSubTypeItemAssociation from a JSON string
board_type_sub_type_item_association_instance = BoardTypeSubTypeItemAssociation.from_json(json)
# print the JSON string representation of the object
print BoardTypeSubTypeItemAssociation.to_json()

# convert the object into a dict
board_type_sub_type_item_association_dict = board_type_sub_type_item_association_instance.to_dict()
# create an instance of BoardTypeSubTypeItemAssociation from a dict
board_type_sub_type_item_association_form_dict = board_type_sub_type_item_association.from_dict(board_type_sub_type_item_association_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


