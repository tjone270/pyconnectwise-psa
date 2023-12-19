# PricingDetail


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**category** | [**ProductCategoryReference**](ProductCategoryReference.md) |  | [optional] 
**end_date** | **datetime** |  | [optional] 
**id** | **int** |  | [optional] 
**no_end_date** | **bool** |  | [optional] 
**product** | [**CatalogItemReference**](CatalogItemReference.md) |  | [optional] 
**start_date** | **datetime** |  | 
**sub_category** | [**ProductSubCategoryReference**](ProductSubCategoryReference.md) |  | [optional] 

## Example

```python
from connectwise_psa.models.pricing_detail import PricingDetail

# TODO update the JSON string below
json = "{}"
# create an instance of PricingDetail from a JSON string
pricing_detail_instance = PricingDetail.from_json(json)
# print the JSON string representation of the object
print PricingDetail.to_json()

# convert the object into a dict
pricing_detail_dict = pricing_detail_instance.to_dict()
# create an instance of PricingDetail from a dict
pricing_detail_form_dict = pricing_detail.from_dict(pricing_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


