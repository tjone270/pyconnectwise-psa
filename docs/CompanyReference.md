# CompanyReference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**identifier** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.company_reference import CompanyReference

# TODO update the JSON string below
json = "{}"
# create an instance of CompanyReference from a JSON string
company_reference_instance = CompanyReference.from_json(json)
# print the JSON string representation of the object
print CompanyReference.to_json()

# convert the object into a dict
company_reference_dict = company_reference_instance.to_dict()
# create an instance of CompanyReference from a dict
company_reference_form_dict = company_reference.from_dict(company_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


