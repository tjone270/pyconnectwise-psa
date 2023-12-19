# MenuEntryLocation


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**location** | [**SystemLocationReference**](SystemLocationReference.md) |  | [optional] 
**menu_entry** | [**SystemMenuEntryReference**](SystemMenuEntryReference.md) |  | [optional] 

## Example

```python
from connectwise_psa.models.menu_entry_location import MenuEntryLocation

# TODO update the JSON string below
json = "{}"
# create an instance of MenuEntryLocation from a JSON string
menu_entry_location_instance = MenuEntryLocation.from_json(json)
# print the JSON string representation of the object
print MenuEntryLocation.to_json()

# convert the object into a dict
menu_entry_location_dict = menu_entry_location_instance.to_dict()
# create an instance of MenuEntryLocation from a dict
menu_entry_location_form_dict = menu_entry_location.from_dict(menu_entry_location_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


