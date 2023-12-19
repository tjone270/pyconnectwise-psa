# Contact


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**address_line1** | **str** |  | [optional] 
**address_line2** | **str** |  | [optional] 
**anniversary** | **str** |  | [optional] 
**assistant_contact** | [**ContactReference**](ContactReference.md) |  | [optional] 
**birth_day** | **str** |  | [optional] 
**children** | **str** |  | [optional] 
**children_flag** | **bool** |  | [optional] 
**city** | **str** |  | [optional] 
**communication_items** | [**List[ContactCommunicationItem]**](ContactCommunicationItem.md) |  | [optional] 
**company** | [**CompanyReference**](CompanyReference.md) |  | [optional] 
**company_location** | [**SystemLocationReference**](SystemLocationReference.md) |  | [optional] 
**country** | [**CountryReference**](CountryReference.md) |  | [optional] 
**custom_fields** | [**List[CustomFieldValue]**](CustomFieldValue.md) |  | [optional] 
**default_billing_flag** | **bool** |  | [optional] 
**default_flag** | **bool** |  | [optional] 
**default_merge_contact_id** | **int** |  | [optional] 
**default_phone_extension** | **str** |  | [optional] 
**default_phone_nbr** | **str** |  | [optional] 
**default_phone_type** | **str** |  | [optional] 
**department** | [**ContactDepartmentReference**](ContactDepartmentReference.md) |  | [optional] 
**disable_portal_login_flag** | **bool** |  | [optional] 
**facebook_url** | **str** |  | [optional] 
**first_name** | **str** |  | [optional] 
**gender** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**ignore_duplicates** | **bool** |  | [optional] 
**inactive_flag** | **bool** |  | [optional] 
**integrator_tags** | **List[str]** |  | [optional] 
**last_name** | **str** |  | [optional] 
**linked_in_url** | **str** |  | [optional] 
**manager_contact** | [**ContactReference**](ContactReference.md) |  | [optional] 
**married_flag** | **bool** |  | [optional] 
**mobile_guid** | **str** |  | [optional] 
**nick_name** | **str** |  | [optional] 
**photo** | [**DocumentReference**](DocumentReference.md) |  | [optional] 
**portal_password** | **str** |  | [optional] 
**portal_security_level** | **int** |  | [optional] 
**presence** | **str** |  | [optional] 
**relationship** | [**RelationshipReference**](RelationshipReference.md) |  | [optional] 
**relationship_override** | **str** |  | [optional] 
**school** | **str** |  | [optional] 
**security_identifier** | **str** |  | [optional] 
**significant_other** | **str** |  | [optional] 
**site** | [**SiteReference**](SiteReference.md) |  | [optional] 
**state** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**twitter_url** | **str** |  | [optional] 
**type_ids** | **List[int]** | Gets or sets integrer array of Contact_Type_Recids to be assigned to contact that can be passed in only during new contact creation (post)             To update existing contacts type, use the /company/contactTypeAssociations or /company/contacts/{ID}/typeAssociations endpoints. | [optional] 
**types** | [**List[ContactTypeReference]**](ContactTypeReference.md) |  | [optional] 
**unsubscribe_flag** | **bool** |  | [optional] 
**user_defined_field1** | **str** |  Max length: 50; | [optional] 
**user_defined_field10** | **str** |  Max length: 50; | [optional] 
**user_defined_field2** | **str** |  Max length: 50; | [optional] 
**user_defined_field3** | **str** |  Max length: 50; | [optional] 
**user_defined_field4** | **str** |  Max length: 50; | [optional] 
**user_defined_field5** | **str** |  Max length: 50; | [optional] 
**user_defined_field6** | **str** |  Max length: 50; | [optional] 
**user_defined_field7** | **str** |  Max length: 50; | [optional] 
**user_defined_field8** | **str** |  Max length: 50; | [optional] 
**user_defined_field9** | **str** |  Max length: 50; | [optional] 
**zip** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.contact import Contact

# TODO update the JSON string below
json = "{}"
# create an instance of Contact from a JSON string
contact_instance = Contact.from_json(json)
# print the JSON string representation of the object
print Contact.to_json()

# convert the object into a dict
contact_dict = contact_instance.to_dict()
# create an instance of Contact from a dict
contact_form_dict = contact.from_dict(contact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


