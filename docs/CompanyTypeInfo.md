# CompanyTypeInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**is_vendor** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.company_type_info import CompanyTypeInfo

# TODO update the JSON string below
json = "{}"
# create an instance of CompanyTypeInfo from a JSON string
company_type_info_instance = CompanyTypeInfo.from_json(json)
# print the JSON string representation of the object
print CompanyTypeInfo.to_json()

# convert the object into a dict
company_type_info_dict = company_type_info_instance.to_dict()
# create an instance of CompanyTypeInfo from a dict
company_type_info_form_dict = company_type_info.from_dict(company_type_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


