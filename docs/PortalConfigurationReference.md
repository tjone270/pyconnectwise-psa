# PortalConfigurationReference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.portal_configuration_reference import PortalConfigurationReference

# TODO update the JSON string below
json = "{}"
# create an instance of PortalConfigurationReference from a JSON string
portal_configuration_reference_instance = PortalConfigurationReference.from_json(json)
# print the JSON string representation of the object
print PortalConfigurationReference.to_json()

# convert the object into a dict
portal_configuration_reference_dict = portal_configuration_reference_instance.to_dict()
# create an instance of PortalConfigurationReference from a dict
portal_configuration_reference_form_dict = portal_configuration_reference.from_dict(portal_configuration_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


