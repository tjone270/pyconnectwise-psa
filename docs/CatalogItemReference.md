# CatalogItemReference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**identifier** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.catalog_item_reference import CatalogItemReference

# TODO update the JSON string below
json = "{}"
# create an instance of CatalogItemReference from a JSON string
catalog_item_reference_instance = CatalogItemReference.from_json(json)
# print the JSON string representation of the object
print CatalogItemReference.to_json()

# convert the object into a dict
catalog_item_reference_dict = catalog_item_reference_instance.to_dict()
# create an instance of CatalogItemReference from a dict
catalog_item_reference_form_dict = catalog_item_reference.from_dict(catalog_item_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


