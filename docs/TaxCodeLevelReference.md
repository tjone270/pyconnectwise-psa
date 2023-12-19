# TaxCodeLevelReference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.tax_code_level_reference import TaxCodeLevelReference

# TODO update the JSON string below
json = "{}"
# create an instance of TaxCodeLevelReference from a JSON string
tax_code_level_reference_instance = TaxCodeLevelReference.from_json(json)
# print the JSON string representation of the object
print TaxCodeLevelReference.to_json()

# convert the object into a dict
tax_code_level_reference_dict = tax_code_level_reference_instance.to_dict()
# create an instance of TaxCodeLevelReference from a dict
tax_code_level_reference_form_dict = tax_code_level_reference.from_dict(tax_code_level_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


