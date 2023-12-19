# BoardAutoAssignResource


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**member** | [**MemberReference**](MemberReference.md) |  | [optional] 
**notify_who** | [**NotificationRecipientReference**](NotificationRecipientReference.md) |  | [optional] 

## Example

```python
from connectwise_psa.models.board_auto_assign_resource import BoardAutoAssignResource

# TODO update the JSON string below
json = "{}"
# create an instance of BoardAutoAssignResource from a JSON string
board_auto_assign_resource_instance = BoardAutoAssignResource.from_json(json)
# print the JSON string representation of the object
print BoardAutoAssignResource.to_json()

# convert the object into a dict
board_auto_assign_resource_dict = board_auto_assign_resource_instance.to_dict()
# create an instance of BoardAutoAssignResource from a dict
board_auto_assign_resource_form_dict = board_auto_assign_resource.from_dict(board_auto_assign_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


