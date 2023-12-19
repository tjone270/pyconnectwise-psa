# SystemMenuEntryReference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.system_menu_entry_reference import SystemMenuEntryReference

# TODO update the JSON string below
json = "{}"
# create an instance of SystemMenuEntryReference from a JSON string
system_menu_entry_reference_instance = SystemMenuEntryReference.from_json(json)
# print the JSON string representation of the object
print SystemMenuEntryReference.to_json()

# convert the object into a dict
system_menu_entry_reference_dict = system_menu_entry_reference_instance.to_dict()
# create an instance of SystemMenuEntryReference from a dict
system_menu_entry_reference_form_dict = system_menu_entry_reference.from_dict(system_menu_entry_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


