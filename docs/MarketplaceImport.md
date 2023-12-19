# MarketplaceImport


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**marketplace_import_type** | **str** |  | [optional] 
**marketplace_object** | **List[object]** |  | [optional] 
**required_fields** | **List[str]** |  | [optional] 

## Example

```python
from connectwise_psa.models.marketplace_import import MarketplaceImport

# TODO update the JSON string below
json = "{}"
# create an instance of MarketplaceImport from a JSON string
marketplace_import_instance = MarketplaceImport.from_json(json)
# print the JSON string representation of the object
print MarketplaceImport.to_json()

# convert the object into a dict
marketplace_import_dict = marketplace_import_instance.to_dict()
# create an instance of MarketplaceImport from a dict
marketplace_import_form_dict = marketplace_import.from_dict(marketplace_import_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


