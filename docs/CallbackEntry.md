# CallbackEntry


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**description** | **str** |  Max length: 100; | [optional] 
**id** | **int** |  | [optional] 
**inactive_flag** | **bool** |  | [optional] 
**is_self_suppressed_flag** | **bool** |  | [optional] 
**is_soap_callback_flag** | **bool** |  | [optional] 
**level** | **str** |  Required Reference | [optional] 
**member_id** | **int** |  | [optional] 
**object_id** | **int** |  Required Reference | [optional] 
**payload_version** | **str** |  | [optional] 
**type** | **str** |  Required Reference | [optional] 
**url** | **str** |  Required Reference | [optional] 

## Example

```python
from connectwise_psa.models.callback_entry import CallbackEntry

# TODO update the JSON string below
json = "{}"
# create an instance of CallbackEntry from a JSON string
callback_entry_instance = CallbackEntry.from_json(json)
# print the JSON string representation of the object
print CallbackEntry.to_json()

# convert the object into a dict
callback_entry_dict = callback_entry_instance.to_dict()
# create an instance of CallbackEntry from a dict
callback_entry_form_dict = callback_entry.from_dict(callback_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


