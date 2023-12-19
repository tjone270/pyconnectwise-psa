# ValidatePortalResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contact_id** | **int** |  | [optional] 
**success** | **bool** |  | [optional] 

## Example

```python
from connectwise_psa.models.validate_portal_response import ValidatePortalResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ValidatePortalResponse from a JSON string
validate_portal_response_instance = ValidatePortalResponse.from_json(json)
# print the JSON string representation of the object
print ValidatePortalResponse.to_json()

# convert the object into a dict
validate_portal_response_dict = validate_portal_response_instance.to_dict()
# create an instance of ValidatePortalResponse from a dict
validate_portal_response_form_dict = validate_portal_response.from_dict(validate_portal_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


