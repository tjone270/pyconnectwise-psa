# CompanyTypeReference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.company_type_reference import CompanyTypeReference

# TODO update the JSON string below
json = "{}"
# create an instance of CompanyTypeReference from a JSON string
company_type_reference_instance = CompanyTypeReference.from_json(json)
# print the JSON string representation of the object
print CompanyTypeReference.to_json()

# convert the object into a dict
company_type_reference_dict = company_type_reference_instance.to_dict()
# create an instance of CompanyTypeReference from a dict
company_type_reference_form_dict = company_type_reference.from_dict(company_type_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


