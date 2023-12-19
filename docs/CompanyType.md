# CompanyType


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**default_flag** | **bool** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  Max length: 50; | 
**service_alert_flag** | **bool** |  | [optional] 
**service_alert_message** | **str** |  Max length: 150; | [optional] 
**vendor_flag** | **bool** |  | [optional] 

## Example

```python
from connectwise_psa.models.company_type import CompanyType

# TODO update the JSON string below
json = "{}"
# create an instance of CompanyType from a JSON string
company_type_instance = CompanyType.from_json(json)
# print the JSON string representation of the object
print CompanyType.to_json()

# convert the object into a dict
company_type_dict = company_type_instance.to_dict()
# create an instance of CompanyType from a dict
company_type_form_dict = company_type.from_dict(company_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


