# ContactContactTypeAssociationContactTypeAssociation


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**contact** | [**ContactReference**](ContactReference.md) |  | [optional] 
**id** | **int** |  | [optional] 
**type** | [**ContactTypeReference**](ContactTypeReference.md) |  | [optional] 

## Example

```python
from connectwise_psa.models.contact_contact_type_association_contact_type_association import ContactContactTypeAssociationContactTypeAssociation

# TODO update the JSON string below
json = "{}"
# create an instance of ContactContactTypeAssociationContactTypeAssociation from a JSON string
contact_contact_type_association_contact_type_association_instance = ContactContactTypeAssociationContactTypeAssociation.from_json(json)
# print the JSON string representation of the object
print ContactContactTypeAssociationContactTypeAssociation.to_json()

# convert the object into a dict
contact_contact_type_association_contact_type_association_dict = contact_contact_type_association_contact_type_association_instance.to_dict()
# create an instance of ContactContactTypeAssociationContactTypeAssociation from a dict
contact_contact_type_association_contact_type_association_form_dict = contact_contact_type_association_contact_type_association.from_dict(contact_contact_type_association_contact_type_association_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


