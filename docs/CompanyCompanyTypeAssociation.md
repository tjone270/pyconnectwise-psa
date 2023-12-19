# CompanyCompanyTypeAssociation


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**company** | [**CompanyReference**](CompanyReference.md) |  | [optional] 
**id** | **int** |  | [optional] 
**type** | [**CompanyTypeReference**](CompanyTypeReference.md) |  | [optional] 

## Example

```python
from connectwise_psa.models.company_company_type_association import CompanyCompanyTypeAssociation

# TODO update the JSON string below
json = "{}"
# create an instance of CompanyCompanyTypeAssociation from a JSON string
company_company_type_association_instance = CompanyCompanyTypeAssociation.from_json(json)
# print the JSON string representation of the object
print CompanyCompanyTypeAssociation.to_json()

# convert the object into a dict
company_company_type_association_dict = company_company_type_association_instance.to_dict()
# create an instance of CompanyCompanyTypeAssociation from a dict
company_company_type_association_form_dict = company_company_type_association.from_dict(company_company_type_association_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


