# SetupScreen


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**category** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**module_description** | **str** |  | [optional] 
**module_identifier** | **str** |  | [optional] 
**module_name** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.setup_screen import SetupScreen

# TODO update the JSON string below
json = "{}"
# create an instance of SetupScreen from a JSON string
setup_screen_instance = SetupScreen.from_json(json)
# print the JSON string representation of the object
print SetupScreen.to_json()

# convert the object into a dict
setup_screen_dict = setup_screen_instance.to_dict()
# create an instance of SetupScreen from a dict
setup_screen_form_dict = setup_screen.from_dict(setup_screen_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


