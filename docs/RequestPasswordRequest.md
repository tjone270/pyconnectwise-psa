# RequestPasswordRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | 

## Example

```python
from connectwise_psa.models.request_password_request import RequestPasswordRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RequestPasswordRequest from a JSON string
request_password_request_instance = RequestPasswordRequest.from_json(json)
# print the JSON string representation of the object
print RequestPasswordRequest.to_json()

# convert the object into a dict
request_password_request_dict = request_password_request_instance.to_dict()
# create an instance of RequestPasswordRequest from a dict
request_password_request_form_dict = request_password_request.from_dict(request_password_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


