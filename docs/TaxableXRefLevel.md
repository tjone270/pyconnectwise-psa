# TaxableXRefLevel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**tax_code_level** | [**TaxCodeLevelReference**](TaxCodeLevelReference.md) |  | [optional] 

## Example

```python
from connectwise_psa.models.taxable_x_ref_level import TaxableXRefLevel

# TODO update the JSON string below
json = "{}"
# create an instance of TaxableXRefLevel from a JSON string
taxable_x_ref_level_instance = TaxableXRefLevel.from_json(json)
# print the JSON string representation of the object
print TaxableXRefLevel.to_json()

# convert the object into a dict
taxable_x_ref_level_dict = taxable_x_ref_level_instance.to_dict()
# create an instance of TaxableXRefLevel from a dict
taxable_x_ref_level_form_dict = taxable_x_ref_level.from_dict(taxable_x_ref_level_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


