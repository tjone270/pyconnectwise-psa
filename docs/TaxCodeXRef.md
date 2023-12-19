# TaxCodeXRef


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**default_flag** | **bool** |  | [optional] 
**description** | **str** |  Max length: 50; | 
**id** | **int** |  | [optional] 
**level_five** | **str** |  | [optional] 
**level_four** | **str** |  | [optional] 
**level_one** | **str** |  | [optional] 
**level_six** | **str** |  | [optional] 
**level_three** | **str** |  | [optional] 
**level_two** | **str** |  | [optional] 
**tax_code** | [**TaxCodeReference**](TaxCodeReference.md) |  | [optional] 
**taxable_levels** | **List[int]** |  | [optional] 

## Example

```python
from connectwise_psa.models.tax_code_x_ref import TaxCodeXRef

# TODO update the JSON string below
json = "{}"
# create an instance of TaxCodeXRef from a JSON string
tax_code_x_ref_instance = TaxCodeXRef.from_json(json)
# print the JSON string representation of the object
print TaxCodeXRef.to_json()

# convert the object into a dict
tax_code_x_ref_dict = tax_code_x_ref_instance.to_dict()
# create an instance of TaxCodeXRef from a dict
tax_code_x_ref_form_dict = tax_code_x_ref.from_dict(tax_code_x_ref_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


