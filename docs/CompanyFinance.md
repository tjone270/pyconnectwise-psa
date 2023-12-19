# CompanyFinance


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**bill_complete_pm_flag** | **bool** |  | [optional] 
**bill_complete_sr_flag** | **bool** |  | [optional] 
**bill_override_flag** | **bool** |  | [optional] 
**bill_restrict_pm_flag** | **bool** |  | [optional] 
**bill_sr_flag** | **bool** |  | [optional] 
**bill_unapproved_pm_flag** | **bool** |  | [optional] 
**bill_unapproved_sr_flag** | **bool** |  | [optional] 
**company** | [**CompanyReference**](CompanyReference.md) |  | [optional] 
**custom_fields** | [**List[CustomFieldValue]**](CustomFieldValue.md) |  | [optional] 
**email_template** | [**EmailTemplateReference**](EmailTemplateReference.md) |  | [optional] 
**id** | **int** |  | [optional] 

## Example

```python
from connectwise_psa.models.company_finance import CompanyFinance

# TODO update the JSON string below
json = "{}"
# create an instance of CompanyFinance from a JSON string
company_finance_instance = CompanyFinance.from_json(json)
# print the JSON string representation of the object
print CompanyFinance.to_json()

# convert the object into a dict
company_finance_dict = company_finance_instance.to_dict()
# create an instance of CompanyFinance from a dict
company_finance_form_dict = company_finance.from_dict(company_finance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


