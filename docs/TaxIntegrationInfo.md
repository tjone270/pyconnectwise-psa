# TaxIntegrationInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**enabled_flag** | **bool** |  | [optional] 
**id** | **int** |  | [optional] 
**tax_integration_type** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.tax_integration_info import TaxIntegrationInfo

# TODO update the JSON string below
json = "{}"
# create an instance of TaxIntegrationInfo from a JSON string
tax_integration_info_instance = TaxIntegrationInfo.from_json(json)
# print the JSON string representation of the object
print TaxIntegrationInfo.to_json()

# convert the object into a dict
tax_integration_info_dict = tax_integration_info_instance.to_dict()
# create an instance of TaxIntegrationInfo from a dict
tax_integration_info_form_dict = tax_integration_info.from_dict(tax_integration_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


