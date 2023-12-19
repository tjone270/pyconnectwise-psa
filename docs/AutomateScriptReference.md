# AutomateScriptReference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.automate_script_reference import AutomateScriptReference

# TODO update the JSON string below
json = "{}"
# create an instance of AutomateScriptReference from a JSON string
automate_script_reference_instance = AutomateScriptReference.from_json(json)
# print the JSON string representation of the object
print AutomateScriptReference.to_json()

# convert the object into a dict
automate_script_reference_dict = automate_script_reference_instance.to_dict()
# create an instance of AutomateScriptReference from a dict
automate_script_reference_form_dict = automate_script_reference.from_dict(automate_script_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


