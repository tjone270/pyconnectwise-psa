# M365Tenant


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.m365_tenant import M365Tenant

# TODO update the JSON string below
json = "{}"
# create an instance of M365Tenant from a JSON string
m365_tenant_instance = M365Tenant.from_json(json)
# print the JSON string representation of the object
print M365Tenant.to_json()

# convert the object into a dict
m365_tenant_dict = m365_tenant_instance.to_dict()
# create an instance of M365Tenant from a dict
m365_tenant_form_dict = m365_tenant.from_dict(m365_tenant_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


