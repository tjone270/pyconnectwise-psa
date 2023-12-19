# PortalSecurity


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** |  | [optional] 
**identifier** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.portal_security import PortalSecurity

# TODO update the JSON string below
json = "{}"
# create an instance of PortalSecurity from a JSON string
portal_security_instance = PortalSecurity.from_json(json)
# print the JSON string representation of the object
print PortalSecurity.to_json()

# convert the object into a dict
portal_security_dict = portal_security_instance.to_dict()
# create an instance of PortalSecurity from a dict
portal_security_form_dict = portal_security.from_dict(portal_security_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


