# ErrorResponseMessage


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**errors** | [**List[ValidationError]**](ValidationError.md) |  | [optional] 
**message** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.error_response_message import ErrorResponseMessage

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorResponseMessage from a JSON string
error_response_message_instance = ErrorResponseMessage.from_json(json)
# print the JSON string representation of the object
print ErrorResponseMessage.to_json()

# convert the object into a dict
error_response_message_dict = error_response_message_instance.to_dict()
# create an instance of ErrorResponseMessage from a dict
error_response_message_form_dict = error_response_message.from_dict(error_response_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


