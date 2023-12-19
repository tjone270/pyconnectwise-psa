# CatalogPricing


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**catalog_item** | [**CatalogItemReference**](CatalogItemReference.md) |  | [optional] 
**company** | [**CompanyReference**](CompanyReference.md) |  | [optional] 
**var_date** | **str** |  | [optional] 
**location** | [**SystemLocationReference**](SystemLocationReference.md) |  | [optional] 
**price** | **float** |  | [optional] 
**quantity** | **int** |  | [optional] 

## Example

```python
from connectwise_psa.models.catalog_pricing import CatalogPricing

# TODO update the JSON string below
json = "{}"
# create an instance of CatalogPricing from a JSON string
catalog_pricing_instance = CatalogPricing.from_json(json)
# print the JSON string representation of the object
print CatalogPricing.to_json()

# convert the object into a dict
catalog_pricing_dict = catalog_pricing_instance.to_dict()
# create an instance of CatalogPricing from a dict
catalog_pricing_form_dict = catalog_pricing.from_dict(catalog_pricing_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


