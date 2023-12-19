# ReminderReference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.reminder_reference import ReminderReference

# TODO update the JSON string below
json = "{}"
# create an instance of ReminderReference from a JSON string
reminder_reference_instance = ReminderReference.from_json(json)
# print the JSON string representation of the object
print ReminderReference.to_json()

# convert the object into a dict
reminder_reference_dict = reminder_reference_instance.to_dict()
# create an instance of ReminderReference from a dict
reminder_reference_form_dict = reminder_reference.from_dict(reminder_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


