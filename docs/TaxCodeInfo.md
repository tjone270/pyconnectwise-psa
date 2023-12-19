# TaxCodeInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**cancel_date** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**effective_date** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**identifier** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.tax_code_info import TaxCodeInfo

# TODO update the JSON string below
json = "{}"
# create an instance of TaxCodeInfo from a JSON string
tax_code_info_instance = TaxCodeInfo.from_json(json)
# print the JSON string representation of the object
print TaxCodeInfo.to_json()

# convert the object into a dict
tax_code_info_dict = tax_code_info_instance.to_dict()
# create an instance of TaxCodeInfo from a dict
tax_code_info_form_dict = tax_code_info.from_dict(tax_code_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


