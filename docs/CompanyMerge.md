# CompanyMerge


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_number** | **str** |  | [optional] 
**activities** | **str** |  | [optional] 
**billing_address** | **str** |  | [optional] 
**billing_contact** | **str** |  | [optional] 
**billing_terms** | **str** |  | [optional] 
**contacts** | **str** |  | [optional] 
**date_acquired** | **str** |  | [optional] 
**documents** | **str** |  | [optional] 
**fax** | **str** |  | [optional] 
**identifier** | **str** |  | [optional] 
**market** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**notes** | **str** |  | [optional] 
**number_of_employees** | **str** |  | [optional] 
**opportunities** | **str** |  | [optional] 
**phone** | **str** |  | [optional] 
**primary_address** | **str** |  | [optional] 
**primary_contact** | **str** |  | [optional] 
**projects** | **str** |  | [optional] 
**revenue** | **str** |  | [optional] 
**revenue_year** | **str** |  | [optional] 
**services** | **str** |  | [optional] 
**sic_code** | **str** |  | [optional] 
**sites** | **str** |  | [optional] 
**source_list** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**tax_code** | **str** |  | [optional] 
**territory** | **str** |  | [optional] 
**time_zone** | **str** |  | [optional] 
**to_company_id** | **int** |  | 
**type** | **str** |  | [optional] 
**user_defined_field1** | **str** |  | [optional] 
**user_defined_field10** | **str** |  | [optional] 
**user_defined_field2** | **str** |  | [optional] 
**user_defined_field3** | **str** |  | [optional] 
**user_defined_field4** | **str** |  | [optional] 
**user_defined_field5** | **str** |  | [optional] 
**user_defined_field6** | **str** |  | [optional] 
**user_defined_field7** | **str** |  | [optional] 
**user_defined_field8** | **str** |  | [optional] 
**user_defined_field9** | **str** |  | [optional] 
**website** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.company_merge import CompanyMerge

# TODO update the JSON string below
json = "{}"
# create an instance of CompanyMerge from a JSON string
company_merge_instance = CompanyMerge.from_json(json)
# print the JSON string representation of the object
print CompanyMerge.to_json()

# convert the object into a dict
company_merge_dict = company_merge_instance.to_dict()
# create an instance of CompanyMerge from a dict
company_merge_form_dict = company_merge.from_dict(company_merge_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


