# MarketingCompany


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**all_contacts_flag** | **bool** |  | [optional] 
**default_contact_flag** | **bool** |  | [optional] 
**group_id** | **int** |  | [optional] 
**id** | **int** |  | [optional] 
**unsubscribe_flag** | **bool** |  | [optional] 

## Example

```python
from connectwise_psa.models.marketing_company import MarketingCompany

# TODO update the JSON string below
json = "{}"
# create an instance of MarketingCompany from a JSON string
marketing_company_instance = MarketingCompany.from_json(json)
# print the JSON string representation of the object
print MarketingCompany.to_json()

# convert the object into a dict
marketing_company_dict = marketing_company_instance.to_dict()
# create an instance of MarketingCompany from a dict
marketing_company_form_dict = marketing_company.from_dict(marketing_company_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


