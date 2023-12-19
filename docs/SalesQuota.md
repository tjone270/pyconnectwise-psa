# SalesQuota


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**april_margin** | **float** |  | [optional] 
**april_revenue** | **float** |  | [optional] 
**august_margin** | **float** |  | [optional] 
**august_revenue** | **float** |  | [optional] 
**category** | [**ProductCategoryReference**](ProductCategoryReference.md) |  | [optional] 
**currency** | [**CurrencyReference**](CurrencyReference.md) |  | [optional] 
**december_margin** | **float** |  | [optional] 
**december_revenue** | **float** |  | [optional] 
**department** | [**SystemDepartmentReference**](SystemDepartmentReference.md) |  | [optional] 
**february_margin** | **float** |  | [optional] 
**february_revenue** | **float** |  | [optional] 
**forecast_year** | **int** |  | [optional] 
**id** | **int** |  | [optional] 
**january_margin** | **float** |  | [optional] 
**january_revenue** | **float** |  | [optional] 
**july_margin** | **float** |  | [optional] 
**july_revenue** | **float** |  | [optional] 
**june_margin** | **float** |  | [optional] 
**june_revenue** | **float** |  | [optional] 
**location** | [**SystemLocationReference**](SystemLocationReference.md) |  | [optional] 
**march_margin** | **float** |  | [optional] 
**march_revenue** | **float** |  | [optional] 
**may_margin** | **float** |  | [optional] 
**may_revenue** | **float** |  | [optional] 
**member** | [**MemberReference**](MemberReference.md) |  | [optional] 
**november_margin** | **float** |  | [optional] 
**november_revenue** | **float** |  | [optional] 
**october_margin** | **float** |  | [optional] 
**october_revenue** | **float** |  | [optional] 
**september_margin** | **float** |  | [optional] 
**september_revenue** | **float** |  | [optional] 
**sub_category** | [**ProductSubCategoryReference**](ProductSubCategoryReference.md) |  | [optional] 

## Example

```python
from connectwise_psa.models.sales_quota import SalesQuota

# TODO update the JSON string below
json = "{}"
# create an instance of SalesQuota from a JSON string
sales_quota_instance = SalesQuota.from_json(json)
# print the JSON string representation of the object
print SalesQuota.to_json()

# convert the object into a dict
sales_quota_dict = sales_quota_instance.to_dict()
# create an instance of SalesQuota from a dict
sales_quota_form_dict = sales_quota.from_dict(sales_quota_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


