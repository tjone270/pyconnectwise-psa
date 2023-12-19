# AccountingPackage


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**identifier** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.accounting_package import AccountingPackage

# TODO update the JSON string below
json = "{}"
# create an instance of AccountingPackage from a JSON string
accounting_package_instance = AccountingPackage.from_json(json)
# print the JSON string representation of the object
print AccountingPackage.to_json()

# convert the object into a dict
accounting_package_dict = accounting_package_instance.to_dict()
# create an instance of AccountingPackage from a dict
accounting_package_form_dict = accounting_package.from_dict(accounting_package_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


