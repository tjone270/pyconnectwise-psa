# M365Contact


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**assigned_licenses** | **str** |  | [optional] 
**contact_rec_id** | **int** |  | [optional] 
**department** | **str** |  | [optional] 
**directory_roles** | **str** |  | [optional] 
**display_name** | **str** |  | [optional] 
**employee_type** | **str** |  | [optional] 
**groups** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**m365_contact_id** | **str** |  | [optional] 
**manager_id** | **str** |  | [optional] 
**proxy_addresses** | **str** |  | [optional] 
**proxy_addresses_plain** | **str** |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**user_principal_name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.m365_contact import M365Contact

# TODO update the JSON string below
json = "{}"
# create an instance of M365Contact from a JSON string
m365_contact_instance = M365Contact.from_json(json)
# print the JSON string representation of the object
print M365Contact.to_json()

# convert the object into a dict
m365_contact_dict = m365_contact_instance.to_dict()
# create an instance of M365Contact from a dict
m365_contact_form_dict = m365_contact.from_dict(m365_contact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


