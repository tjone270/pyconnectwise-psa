# CompanyContactTypeAssociation


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**contact** | [**ContactReference**](ContactReference.md) |  | [optional] 
**id** | **int** |  | [optional] 
**type** | [**ContactTypeReference**](ContactTypeReference.md) |  | [optional] 

## Example

```python
from connectwise_psa.models.company_contact_type_association import CompanyContactTypeAssociation

# TODO update the JSON string below
json = "{}"
# create an instance of CompanyContactTypeAssociation from a JSON string
company_contact_type_association_instance = CompanyContactTypeAssociation.from_json(json)
# print the JSON string representation of the object
print CompanyContactTypeAssociation.to_json()

# convert the object into a dict
company_contact_type_association_dict = company_contact_type_association_instance.to_dict()
# create an instance of CompanyContactTypeAssociation from a dict
company_contact_type_association_form_dict = company_contact_type_association.from_dict(company_contact_type_association_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


