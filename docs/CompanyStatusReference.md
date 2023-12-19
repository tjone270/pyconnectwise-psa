# CompanyStatusReference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.company_status_reference import CompanyStatusReference

# TODO update the JSON string below
json = "{}"
# create an instance of CompanyStatusReference from a JSON string
company_status_reference_instance = CompanyStatusReference.from_json(json)
# print the JSON string representation of the object
print CompanyStatusReference.to_json()

# convert the object into a dict
company_status_reference_dict = company_status_reference_instance.to_dict()
# create an instance of CompanyStatusReference from a dict
company_status_reference_form_dict = company_status_reference.from_dict(company_status_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


