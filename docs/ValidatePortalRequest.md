# ValidatePortalRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | 
**password** | **str** |  | 

## Example

```python
from connectwise_psa.models.validate_portal_request import ValidatePortalRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ValidatePortalRequest from a JSON string
validate_portal_request_instance = ValidatePortalRequest.from_json(json)
# print the JSON string representation of the object
print ValidatePortalRequest.to_json()

# convert the object into a dict
validate_portal_request_dict = validate_portal_request_instance.to_dict()
# create an instance of ValidatePortalRequest from a dict
validate_portal_request_form_dict = validate_portal_request.from_dict(validate_portal_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


