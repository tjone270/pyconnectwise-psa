# MenuEntry


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**add_all_locations** | **bool** |  | [optional] 
**caption** | **str** |  Max length: 50; | 
**client_id** | **str** | Only required if not already set Max length: 36; | [optional] 
**id** | **int** |  | [optional] 
**large_menu_icon_id** | **int** |  | [optional] 
**link** | **str** |  Max length: 2000; | 
**location_ids** | **List[int]** |  | [optional] 
**menu_location** | [**MenuLocationReference**](MenuLocationReference.md) |  | [optional] 
**new_window_flag** | **bool** |  | 
**origin** | **str** |  Max length: 2000; | [optional] 
**remove_all_locations** | **bool** |  | [optional] 
**small_menu_icon_id** | **int** |  | [optional] 

## Example

```python
from connectwise_psa.models.menu_entry import MenuEntry

# TODO update the JSON string below
json = "{}"
# create an instance of MenuEntry from a JSON string
menu_entry_instance = MenuEntry.from_json(json)
# print the JSON string representation of the object
print MenuEntry.to_json()

# convert the object into a dict
menu_entry_dict = menu_entry_instance.to_dict()
# create an instance of MenuEntry from a dict
menu_entry_form_dict = menu_entry.from_dict(menu_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


