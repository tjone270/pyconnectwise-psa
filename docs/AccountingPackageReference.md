# AccountingPackageReference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**identifier** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.accounting_package_reference import AccountingPackageReference

# TODO update the JSON string below
json = "{}"
# create an instance of AccountingPackageReference from a JSON string
accounting_package_reference_instance = AccountingPackageReference.from_json(json)
# print the JSON string representation of the object
print AccountingPackageReference.to_json()

# convert the object into a dict
accounting_package_reference_dict = accounting_package_reference_instance.to_dict()
# create an instance of AccountingPackageReference from a dict
accounting_package_reference_form_dict = accounting_package_reference.from_dict(accounting_package_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


