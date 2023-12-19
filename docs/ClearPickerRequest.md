# ClearPickerRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**member** | [**MemberReference**](MemberReference.md) |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.clear_picker_request import ClearPickerRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ClearPickerRequest from a JSON string
clear_picker_request_instance = ClearPickerRequest.from_json(json)
# print the JSON string representation of the object
print ClearPickerRequest.to_json()

# convert the object into a dict
clear_picker_request_dict = clear_picker_request_instance.to_dict()
# create an instance of ClearPickerRequest from a dict
clear_picker_request_form_dict = clear_picker_request.from_dict(clear_picker_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


