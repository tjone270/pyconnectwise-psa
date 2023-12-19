# CalendarSetupReference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 

## Example

```python
from connectwise_psa.models.calendar_setup_reference import CalendarSetupReference

# TODO update the JSON string below
json = "{}"
# create an instance of CalendarSetupReference from a JSON string
calendar_setup_reference_instance = CalendarSetupReference.from_json(json)
# print the JSON string representation of the object
print CalendarSetupReference.to_json()

# convert the object into a dict
calendar_setup_reference_dict = calendar_setup_reference_instance.to_dict()
# create an instance of CalendarSetupReference from a dict
calendar_setup_reference_form_dict = calendar_setup_reference.from_dict(calendar_setup_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


