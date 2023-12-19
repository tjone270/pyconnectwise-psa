# TimeEntryReference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 

## Example

```python
from connectwise_psa.models.time_entry_reference import TimeEntryReference

# TODO update the JSON string below
json = "{}"
# create an instance of TimeEntryReference from a JSON string
time_entry_reference_instance = TimeEntryReference.from_json(json)
# print the JSON string representation of the object
print TimeEntryReference.to_json()

# convert the object into a dict
time_entry_reference_dict = time_entry_reference_instance.to_dict()
# create an instance of TimeEntryReference from a dict
time_entry_reference_form_dict = time_entry_reference.from_dict(time_entry_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


