# OpportunityContact


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**company** | [**CompanyReference**](CompanyReference.md) |  | [optional] 
**contact** | [**ContactReference**](ContactReference.md) |  | [optional] 
**email_address** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**notes** | **str** |  | [optional] 
**opportunity_id** | **int** |  | [optional] 
**phone_number** | **str** |  | [optional] 
**referral_flag** | **bool** |  | [optional] 
**role** | [**OpportunitySalesRoleReference**](OpportunitySalesRoleReference.md) |  | [optional] 

## Example

```python
from connectwise_psa.models.opportunity_contact import OpportunityContact

# TODO update the JSON string below
json = "{}"
# create an instance of OpportunityContact from a JSON string
opportunity_contact_instance = OpportunityContact.from_json(json)
# print the JSON string representation of the object
print OpportunityContact.to_json()

# convert the object into a dict
opportunity_contact_dict = opportunity_contact_instance.to_dict()
# create an instance of OpportunityContact from a dict
opportunity_contact_form_dict = opportunity_contact.from_dict(opportunity_contact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


