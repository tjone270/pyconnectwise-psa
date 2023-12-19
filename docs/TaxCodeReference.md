# TaxCodeReference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.tax_code_reference import TaxCodeReference

# TODO update the JSON string below
json = "{}"
# create an instance of TaxCodeReference from a JSON string
tax_code_reference_instance = TaxCodeReference.from_json(json)
# print the JSON string representation of the object
print TaxCodeReference.to_json()

# convert the object into a dict
tax_code_reference_dict = tax_code_reference_instance.to_dict()
# create an instance of TaxCodeReference from a dict
tax_code_reference_form_dict = tax_code_reference.from_dict(tax_code_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


