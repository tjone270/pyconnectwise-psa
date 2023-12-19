# PortalSecurityLevel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**caption** | **str** |  Max length: 50; | [optional] 
**caption_identifier** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**is_default_flag** | **bool** |  | [optional] 

## Example

```python
from connectwise_psa.models.portal_security_level import PortalSecurityLevel

# TODO update the JSON string below
json = "{}"
# create an instance of PortalSecurityLevel from a JSON string
portal_security_level_instance = PortalSecurityLevel.from_json(json)
# print the JSON string representation of the object
print PortalSecurityLevel.to_json()

# convert the object into a dict
portal_security_level_dict = portal_security_level_instance.to_dict()
# create an instance of PortalSecurityLevel from a dict
portal_security_level_form_dict = portal_security_level.from_dict(portal_security_level_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


