# CompanyGroup


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**all_contacts_flag** | **bool** |  | [optional] 
**company** | [**CompanyReference**](CompanyReference.md) |  | [optional] 
**contact_ids** | **List[int]** |  | [optional] 
**default_contact_flag** | **bool** |  | [optional] 
**group** | [**GroupReference**](GroupReference.md) |  | [optional] 
**id** | **int** |  Required On Updates; | [optional] 
**remove_all_contacts_flag** | **bool** |  | [optional] 
**unsubscribe_flag** | **bool** |  | [optional] 

## Example

```python
from connectwise_psa.models.company_group import CompanyGroup

# TODO update the JSON string below
json = "{}"
# create an instance of CompanyGroup from a JSON string
company_group_instance = CompanyGroup.from_json(json)
# print the JSON string representation of the object
print CompanyGroup.to_json()

# convert the object into a dict
company_group_dict = company_group_instance.to_dict()
# create an instance of CompanyGroup from a dict
company_group_form_dict = company_group.from_dict(company_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


